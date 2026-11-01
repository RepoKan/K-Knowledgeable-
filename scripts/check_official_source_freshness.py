#!/usr/bin/env python3
"""Check allowlisted official documentation sources without promoting content.

This tool records response metadata and a bounded response-body digest only.
It never writes fetched documentation into the knowledge base.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "knowledge-supporting/manifests/official-source-catalog-r1.json"
MAX_BODY_BYTES = 2 * 1024 * 1024
TIMEOUT_SECONDS = 20


def check_source(source: dict) -> dict:
    url = source["url"]
    allowed_hosts = set(source["allowed_hosts"])
    requested_host = (urlparse(url).hostname or "").lower()
    if requested_host not in allowed_hosts:
        return {"id": source["id"], "state": "BLOCKED_HOST", "url": url}

    request = Request(
        url,
        headers={
            "User-Agent": "KKS-Official-Source-Freshness/1.0 (+metadata-only)",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.1",
        },
    )
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            final_url = response.geturl()
            final_host = (urlparse(final_url).hostname or "").lower()
            if final_host not in allowed_hosts:
                return {
                    "id": source["id"],
                    "state": "BLOCKED_REDIRECT_HOST",
                    "url": url,
                    "final_url": final_url,
                }
            body = response.read(MAX_BODY_BYTES + 1)
            truncated = len(body) > MAX_BODY_BYTES
            body = body[:MAX_BODY_BYTES]
            return {
                "id": source["id"],
                "title": source["title"],
                "state": "HTTP_OK" if 200 <= response.status < 300 else "HTTP_ERROR",
                "status_code": response.status,
                "url": url,
                "final_url": final_url,
                "content_type": response.headers.get("Content-Type"),
                "etag": response.headers.get("ETag"),
                "last_modified": response.headers.get("Last-Modified"),
                "body_prefix_sha256": hashlib.sha256(body).hexdigest(),
                "body_prefix_bytes": len(body),
                "body_truncated": truncated,
                "authority": source["authority"],
                "scope": source["scope"],
            }
    except HTTPError as error:
        return {"id": source["id"], "state": "HTTP_ERROR", "status_code": error.code, "url": url}
    except (URLError, TimeoutError, socket.timeout, OSError) as error:
        return {"id": source["id"], "state": "FETCH_ERROR", "url": url, "error_type": type(error).__name__}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="-", help="JSON output path, or - for stdout")
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    results = [check_source(source) for source in catalog["sources"]]
    report = {
        "schema_version": "1.0.0",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "mode": catalog["policy"]["mode"],
        "automatic_repository_writes": catalog["policy"]["automatic_repository_writes"],
        "automatic_knowledge_promotion": catalog["policy"]["automatic_knowledge_promotion"],
        "results": results,
        "summary": {
            "total": len(results),
            "http_ok": sum(item["state"] == "HTTP_OK" for item in results),
            "failed_or_blocked": sum(item["state"] != "HTTP_OK" for item in results),
        },
        "promotion_note": "Freshness metadata is evidence for review only; it does not approve content changes or prove semantic correctness.",
    }
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output == "-":
        sys.stdout.write(rendered)
    else:
        Path(args.output).write_text(rendered, encoding="utf-8")
    return 0 if report["summary"]["failed_or_blocked"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

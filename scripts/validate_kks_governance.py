#!/usr/bin/env python3
"""Validate the KKS connector governance contract."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"GOVERNANCE CHECK FAILED: {message}")


def main() -> None:
    config_path = ROOT / "chatgpt-connector-channel.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"connector config is not valid JSON: {exc}")

    if config["session_termination"]["allow_autonomous_processing"] is not False:
        fail("autonomous processing must be disabled")
    if config["channel"]["storage_config"]["auto_commit"] is not False:
        fail("automatic commits must be disabled")
    if config["connector_processing"]["autonomous_mode"] is not False:
        fail("connector autonomous mode must be disabled")
    if config["channel"]["storage_config"]["write_target"] != "approved_feature_branch":
        fail("writes must target an approved feature branch")
    if config["features"]["pull_request_required"] is not True:
        fail("pull requests must be required")
    if config["features"]["human_approval_required"] is not True:
        fail("human approval must be required")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    guide = (ROOT / "CHATGPT_CONNECTOR_GUIDE.md").read_text(encoding="utf-8")
    if readme != guide:
        fail("README.md and CHATGPT_CONNECTOR_GUIDE.md must remain identical")

    required_phrases = (
        "feature branch",
        "pull request",
        "human approval",
        "public repository",
        "does not grant authorization",
    )
    lower_readme = readme.lower()
    for phrase in required_phrases:
        if phrase not in lower_readme:
            fail(f"required governance phrase is missing: {phrase}")

    forbidden_claims = (
        "full api write permissions for autonomous processing",
        "no manual intervention required",
        "auto-commit to repository",
        '"auto_commit": true',
        '"autonomous_mode": true',
    )
    for phrase in forbidden_claims:
        if phrase.lower() in lower_readme or phrase.lower() in guide.lower():
            fail(f"unsafe connector claim remains: {phrase}")

    print("KKS governance validation passed")


if __name__ == "__main__":
    main()

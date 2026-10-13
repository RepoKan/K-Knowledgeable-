#!/usr/bin/env python3
"""Offline policy check for KKS Skybridge reference metadata; NOT an MCP runtime test."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs" / "skybridge-kks-pilot.json"


def validate(data):
    errors = []
    if data.get("status") != "CANDIDATE":
        errors.append("Only CANDIDATE status is allowed before pilot validation")
    source = data.get("source", {})
    expected = {
        "repository": "https://github.com/alpic-ai/skybridge",
        "template": "https://github.com/alpic-ai/apps-sdk-template",
    }
    for field, url in expected.items():
        if source.get(field) != url:
            errors.append(f"Unverified {field} upstream: {source.get(field)!r}")
    runtime = data.get("runtime", {})
    if runtime.get("minimumNodeMajor", 0) < 24:
        errors.append("Skybridge pilot requires isolated Node 24+")
    for field in ("isolated", "mustNotUpgradeContinue"):
        if runtime.get(field) is not True:
            errors.append(f"Runtime guard missing: {field}")
    security = data.get("security", {})
    for field in ("onlySanitizedPublicSources", "noProductionData", "noCredentialsInRepository", "noRemoteDeploymentUntilApproved", "noPaymentOperations"):
        if security.get(field) is not True:
            errors.append(f"Security guard missing: {field}")
    integration = data.get("integration", {})
    if integration.get("readOnlyPilot") is not True:
        errors.append("Pilot must remain read-only")
    for field in ("modifyExistingMcpConfig", "duplicateGithubMcpServer", "deploymentApproved"):
        if integration.get(field) is not False:
            errors.append(f"Prohibited integration flag enabled: {field}")
    sha = data.get("kksGitHubBaseline", {}).get("sha", "")
    if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
        errors.append("Missing exact 40-character lowercase Git SHA")
    return errors


def main():
    try:
        data = json.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot load metadata: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print("FAIL: KKS Skybridge reference policy")
        for error in errors:
            print(f" - {error}")
        return 1
    print("PASS: KKS Skybridge reference policy (static metadata only)")
    print("NOT RUN: Skybridge startup, MCP protocol, React widget, ChatGPT connection, deployment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

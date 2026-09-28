#!/usr/bin/env python3
"""Validate the pinned Sourcebot integration without network access."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "configs/sourcebot/upstream.lock.json"
EXPECTED_REPO = "sourcebot-dev/sourcebot"
EXPECTED_URL = "https://github.com/sourcebot-dev/sourcebot.git"
EXPECTED_RELEASE = "v5.1.14"
EXPECTED_COMMIT = "3c0e5ca6f07f524b42490a5feef4ff9a0824c990"

REQUIRED_FILES = [
    ".gitmodules",
    "configs/sourcebot/config.example.json",
    "configs/sourcebot/mcp.example.json",
    "configs/sourcebot/upstream.lock.json",
    "docs/integrations/SOURCEBOT_SELF_HOSTED.md",
    ".github/skills/sourcebot-code-context/SKILL.md",
    ".github/skills/sourcebot-code-context/agents/openai.yaml",
    ".github/skills/sourcebot-code-context/references/sourcebot-mcp.md",
    "sourcebot-skills/k-knowledge-codebase-guide.md",
]


def fail(message: str) -> None:
    print(f"FAIL  {message}", file=sys.stderr)


def ok(message: str) -> None:
    print(f"ok    {message}")


def main() -> int:
    violations: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            violations.append(f"missing required Sourcebot integration file: {rel}")

    if LOCK.is_file():
        try:
            lock = json.loads(LOCK.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            violations.append(f"cannot parse {LOCK.relative_to(ROOT)}: {exc}")
            lock = {}
        expected = {
            "repository": EXPECTED_REPO,
            "clone_url": EXPECTED_URL,
            "release": EXPECTED_RELEASE,
            "commit": EXPECTED_COMMIT,
        }
        for key, value in expected.items():
            if lock.get(key) != value:
                violations.append(
                    f"{LOCK.relative_to(ROOT)}: {key} must be {value!r}, got {lock.get(key)!r}"
                )
        if not violations:
            ok(f"upstream lock pins {EXPECTED_RELEASE}@{EXPECTED_COMMIT}")
    else:
        lock = {}

    gitmodules = ROOT / ".gitmodules"
    if gitmodules.is_file():
        text = gitmodules.read_text(encoding="utf-8", errors="replace")
        if "path = tools/sourcebot" not in text:
            violations.append(".gitmodules: tools/sourcebot path is missing")
        if f"url = {EXPECTED_URL}" not in text:
            violations.append(".gitmodules: Sourcebot clone URL does not match the governed upstream")
        if "branch =" in text:
            violations.append(".gitmodules: do not configure a moving branch for the pinned Sourcebot submodule")

    try:
        entry = subprocess.check_output(
            ["git", "ls-tree", "HEAD", "tools/sourcebot"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.STDOUT,
        ).strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        violations.append(f"cannot inspect tools/sourcebot gitlink: {exc}")
        entry = ""

    if entry:
        parts = entry.split()
        if len(parts) < 4 or parts[0] != "160000" or parts[1] != "commit":
            violations.append(f"tools/sourcebot must be a gitlink, got: {entry}")
        elif parts[2] != EXPECTED_COMMIT:
            violations.append(
                f"tools/sourcebot gitlink must pin {EXPECTED_COMMIT}, got {parts[2]}"
            )
        else:
            ok(f"gitlink pins Sourcebot {EXPECTED_RELEASE}@{EXPECTED_COMMIT}")

    for rel in ("configs/sourcebot/config.example.json", "configs/sourcebot/mcp.example.json"):
        path = ROOT / rel
        if path.is_file():
            try:
                json.loads(path.read_text(encoding="utf-8"))
                ok(f"JSON parses: {rel}")
            except (OSError, json.JSONDecodeError) as exc:
                violations.append(f"{rel}: invalid JSON ({exc})")

    skill = ROOT / ".github/skills/sourcebot-code-context/SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---\n"):
            violations.append(f"{skill.relative_to(ROOT)}: missing YAML frontmatter")
        if "name: sourcebot-code-context" not in text:
            violations.append(f"{skill.relative_to(ROOT)}: skill name mismatch")
        if "TODO" in text:
            violations.append(f"{skill.relative_to(ROOT)}: TODO placeholder remains")
        if EXPECTED_COMMIT in text:
            violations.append(
                f"{skill.relative_to(ROOT)}: keep upstream version identity in the lock/reference docs, not the reusable skill"
            )
        if not any(item.startswith(str(skill.relative_to(ROOT))) for item in violations):
            ok("ChatGPT Sourcebot skill contract is present")

    native_skill = ROOT / "sourcebot-skills/k-knowledge-codebase-guide.md"
    if native_skill.is_file():
        text = native_skill.read_text(encoding="utf-8", errors="replace")
        if "command: k-knowledge-codebase-guide" not in text:
            violations.append(f"{native_skill.relative_to(ROOT)}: Sourcebot command metadata missing")
        else:
            ok("Sourcebot-native codebase guide skill is present")

    if violations:
        for item in violations:
            fail(item)
        print(f"Sourcebot integration validation: FAILED ({len(violations)} violation(s))", file=sys.stderr)
        return 1

    print("Sourcebot integration validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

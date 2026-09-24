#!/usr/bin/env python3
"""Deterministic KKS governance validation (stdlib-only, Python 3.10+).

Promotes the documented governance process into executable tooling. Checks:

1. JSON config files parse.
2. Connector metadata keeps autonomous processing and automatic commits disabled.
3. Connector metadata does not claim delete/admin capability.
4. Required governance artifacts exist.
5. Workflow files keep minimal permissions and avoid write-scoped tokens.
6. Secret-pattern scan with placeholder guarding.
7. Python files compile (syntax check).
8. Public-boundary scan (PAN heuristics, private endpoints).

Usage:
    python3 scripts/validate_kks_governance.py

Exit codes:
    0 = validation passed
    1 = violations found
    2 = validation setup error (missing required file)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# ---- contract constants (mirror AGENTS.md / governance docs) ----
CONNECTOR_CONFIG = "chatgpt-connector-channel.json"
REQUIRED_WF = ".github/workflows/kks-governance-validation.yml"
REQUIRED_GOVERNANCE_DOCS = [
    "AGENTS.md",
    "activation/PROJECT_INSTRUCTIONS.md",
    "chatgpt-connector-channel.json",
    "docs/governance/KTC_PAYMENT_THREE_SOURCE_MASTER_RULE_R1.md",
    "docs/governance/K_KNOWLEDGE_SUPPORTING_PROJECT_INHERITANCE_R1.md",
    "docs/governance/K_KNOWLEDGE_SUPPORTING_MODEL_ROUTING_R1.md",
    "docs/governance/K_KNOWLEDGE_SUPPORTING_RULE_GOVERNANCE_AGENT_R1.md",
    ".github/skills/enter/SKILL.md",
]
ENTER_SKILL = ".github/skills/enter/SKILL.md"
SCAN_TEXT_EXTS = {".md", ".txt", ".json", ".yml", ".yaml", ".py", ".sh"}
SCAN_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

# Secret patterns: (name, regex). Order matters only for reporting.
SECRET_PATTERNS = [
    ("github_pat", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
    ("ghp_token", re.compile(r"\bghp_[A-Za-z0-9]{30,}\b")),
    ("gho_token", re.compile(r"\bgho_[A-Za-z0-9]{30,}\b")),
    ("ghs_token", re.compile(r"\bghs_[A-Za-z0-9]{30,}\b")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("openai_key", re.compile(r"\bsk-[A-Za-z0-9_-]{40,}\b")),
    ("slack_token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("private_key_block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP |DSA )?PRIVATE KEY-----")),
    ("webhook_url", re.compile(r"https://(?:discord(?:app)?\.com/api/webhooks|hooks\.slack\.com)/[A-Za-z0-9/_-]+")),
]

# Text that marks a token-like match as a sanitized placeholder rather than a secret.
PLACEHOLDER_HINTS = re.compile(
    r"(x{3,}|X{3,}|\*{3,}|EXAMPLE|SAMPLE|PLACEHOLDER|REDACTED|YOUR[_-]?KEY|YOUR[_-]?TOKEN"
    r"|<[^>\n]{1,80}>|\[[^]\n]{1,80}\]|\{[^}\n]{1,80}\}|abc123|1234567890|test|demo|dummy)",
    re.I,
)

PRIVATE_ENDPOINT_RE = re.compile(
    r"https?://(?:10\.|127\.|169\.254\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.)[^\s\"'<>]+"
)

PAN_RE = re.compile(r"\b(?:\d[ -]?){13,19}\b")


def is_truthy_violation(value: object) -> bool:
    """True when a governance flag is set in a way that violates the contract."""
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "on", "1", "enabled"}
    return False


def rel(p: Path) -> str:
    return p.relative_to(REPO_ROOT).as_posix()


def iter_files(subdirs: list[str], extensions: set[str] | None = None) -> list[Path]:
    """Return each matching repository file once, even when roots overlap."""
    unique: dict[str, Path] = {}
    for sub in subdirs:
        base = REPO_ROOT / sub
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if not p.is_file():
                continue
            if any(part in SCAN_SKIP_DIRS for part in p.parts):
                continue
            if extensions is not None and p.suffix not in extensions:
                continue
            unique[rel(p)] = p
    return [unique[key] for key in sorted(unique)]


def match_context(text: str, start: int, end: int, radius: int = 80) -> str:
    """Return bounded context for classifying one candidate finding."""
    return text[max(0, start - radius) : min(len(text), end + radius)]


def is_placeholder_match(text: str, start: int, end: int) -> bool:
    """Only suppress a match when placeholder evidence is local to that match."""
    return bool(PLACEHOLDER_HINTS.search(match_context(text, start, end)))


def looks_like_date_sequence(raw: str) -> bool:
    """Recognize common date/date-range strings that can resemble PAN-length data."""
    compact = re.sub(r"\s+", "", raw.strip(" -"))
    return bool(
        re.fullmatch(
            r"(?:19|20)\d{2}[-/]\d{1,2}[-/]\d{1,2}"
            r"(?:[-–—](?:19|20)\d{2}[-/]\d{1,2}[-/]\d{1,2})?",
            compact,
        )
    )


def check_validator_regressions(violations: list[str], findings: list[str]) -> None:
    """Guard the validator against previously confirmed false-negative/coverage bugs."""
    probe = "test instructions\n" + ("q" * 200) + "\naccount=5555444433331111"
    match = PAN_RE.search(probe)
    if match is None or is_placeholder_match(probe, match.start(), match.end()):
        violations.append("validator regression: unrelated placeholder text can hide a PAN candidate")

    overlap = iter_files([".", ".github"], None)
    overlap_names = [rel(p) for p in overlap]
    if len(overlap_names) != len(set(overlap_names)):
        violations.append("validator regression: overlapping scan roots produced duplicate file results")

    root_python = REPO_ROOT / "joke-generator.py"
    if root_python.is_file():
        python_names = {rel(p) for p in iter_files(["."], {".py"})}
        if "joke-generator.py" not in python_names:
            violations.append("validator regression: root-level Python files are excluded from syntax coverage")

    if not any(item.startswith("validator regression:") for item in violations):
        findings.append("validator self-checks ok: local placeholders, deduplication, root Python coverage")


def check_json_parse(violations: list[str]) -> list[tuple[Path, dict]]:
    parsed: list[tuple[Path, dict]] = []
    json_files = iter_files(["."], {".json"})
    for p in json_files:
        try:
            with p.open(encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            violations.append(f"{rel(p)}: invalid JSON ({e})")
            continue
        except (OSError, UnicodeError) as e:
            violations.append(f"{rel(p)}: unreadable JSON ({e})")
            continue
        if isinstance(data, dict):
            parsed.append((p, data))
    return parsed


def check_connector_gates(violations: list[str], findings: list[str]) -> None:
    cfg_path = REPO_ROOT / CONNECTOR_CONFIG
    if not cfg_path.is_file():
        violations.append(f"{CONNECTOR_CONFIG}: missing required connector metadata")
        return
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeError) as e:
        violations.append(f"{CONNECTOR_CONFIG}: cannot parse connector metadata ({e})")
        return
    if not isinstance(cfg, dict):
        violations.append(f"{CONNECTOR_CONFIG}: top level must be a JSON object")
        return

    def flag_of(*keys: str) -> object:
        node: object = cfg
        for k in keys:
            if not isinstance(node, dict) or k not in node:
                return None
            node = node[k]
        return node

    # Autonomous processing / automatic commits must be disabled everywhere they appear.
    for path in (
        ("session_termination", "allow_autonomous_processing"),
        ("connector_processing", "autonomous_mode"),
        ("channel", "storage_config", "auto_commit"),
        ("features", "auto_file_creation"),
    ):
        if is_truthy_violation(flag_of(*path)):
            violations.append(f"{CONNECTOR_CONFIG}: {'.'.join(path)} must be disabled (false)")
        elif flag_of(*path) is not None:
            findings.append(f"gate ok: {'.'.join(path)} disabled")

    # Destructive/admin capability must not be claimed.
    perms = flag_of("channel", "permissions")
    if isinstance(perms, dict):
        for cap in ("delete", "admin"):
            if is_truthy_violation(perms.get(cap)):
                violations.append(f"{CONNECTOR_CONFIG}: channel.permissions.{cap} must not be enabled")
            elif cap in perms:
                findings.append(f"gate ok: channel.permissions.{cap} not enabled")

    # Write target must be the approved feature-branch strategy (HEAD contract parity).
    write_target = flag_of("channel", "storage_config", "write_target")
    if write_target is None:
        violations.append(f"{CONNECTOR_CONFIG}: channel.storage_config.write_target is required")
    elif not isinstance(write_target, str) or write_target.strip() != "approved_feature_branch":
        violations.append(
            f"{CONNECTOR_CONFIG}: write_target '{write_target}' must be 'approved_feature_branch'"
        )
    pull_required = flag_of("features", "pull_request_required")
    if pull_required is not None and not is_truthy_violation(pull_required):
        violations.append(f"{CONNECTOR_CONFIG}: features.pull_request_required must stay true")
    human_approval = flag_of("features", "human_approval_required")
    if human_approval is not None and not is_truthy_violation(human_approval):
        violations.append(f"{CONNECTOR_CONFIG}: features.human_approval_required must stay true")


def check_required_artifacts(violations: list[str]) -> None:
    for path in REQUIRED_GOVERNANCE_DOCS + [REQUIRED_WF]:
        if not (REPO_ROOT / path).is_file():
            violations.append(f"missing required governance artifact: {path}")


ENTER_SKILL_REQUIRED_TERMS = (
    "repository",
    "ref",
    "sha",
    "agents.md",
    "feature branch",
    "public repository",
)
ENTER_SKILL_PLACEHOLDERS = (
    "describe what this skill does",
    "define the functionality provided by this skill",
)


def check_enter_skill(violations: list[str], findings: list[str]) -> None:
    path = REPO_ROOT / ENTER_SKILL
    if not path.is_file():
        return
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as e:
        violations.append(f"{ENTER_SKILL}: unreadable ({e})")
        return
    lower = text.lower()
    for placeholder in ENTER_SKILL_PLACEHOLDERS:
        if placeholder in lower:
            violations.append(f"{ENTER_SKILL}: template placeholder remains: {placeholder}")
    missing = [term for term in ENTER_SKILL_REQUIRED_TERMS if term not in lower]
    if missing:
        violations.append(f"{ENTER_SKILL}: missing governed entry terms: {', '.join(missing)}")
    elif not any(placeholder in lower for placeholder in ENTER_SKILL_PLACEHOLDERS):
        findings.append("enter skill ok: governed project entry contract is present")


REQUIRED_DOC_PHRASES = (
    "feature branch",
    "pull request",
    "human approval",
    "public repository",
    "does not grant authorization",
)
FORBIDDEN_DOC_CLAIMS = (
    "full api write permissions for autonomous processing",
    "no manual intervention required",
    "auto-commit to repository",
    '"auto_commit": true',
    '"autonomous_mode": true',
)


def check_documentation_contract(violations: list[str], findings: list[str]) -> None:
    """README/guide identity and required/forbidden phrasing (HEAD contract parity)."""
    readme_path = REPO_ROOT / "README.md"
    guide_path = REPO_ROOT / "CHATGPT_CONNECTOR_GUIDE.md"
    for p in (readme_path, guide_path):
        if not p.is_file():
            violations.append(f"missing required documentation: {rel(p)}")
            return
    try:
        readme = readme_path.read_text(encoding="utf-8")
        guide = guide_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as e:
        violations.append(f"cannot read documentation contract files ({e})")
        return
    if readme != guide:
        violations.append("README.md and CHATGPT_CONNECTOR_GUIDE.md must remain identical")
    else:
        findings.append("doc contract ok: README and connector guide are identical")
    lower_readme = readme.lower()
    for phrase in REQUIRED_DOC_PHRASES:
        if phrase not in lower_readme:
            violations.append(f"required governance phrase is missing: {phrase}")
    for phrase in FORBIDDEN_DOC_CLAIMS:
        if phrase.lower() in lower_readme or phrase.lower() in guide.lower():
            violations.append(f"unsafe connector claim remains: {phrase}")


def check_workflows(violations: list[str], findings: list[str]) -> None:
    wf_dir = REPO_ROOT / ".github" / "workflows"
    if not wf_dir.is_dir():
        violations.append(".github/workflows: missing workflows directory")
        return
    # Workflows whose documented purpose requires the named elevated permission.
    elevated_allowlist = {
        "security-events: write": {"codeql"},
        "id-token: write": set(),
        "contents: write": set(),
        "packages: write": set(),
        "administration": set(),
    }
    for wf in sorted(wf_dir.glob("*.y*ml")):
        text = wf.read_text(encoding="utf-8", errors="replace")
        name = rel(wf)
        stem = wf.stem.lower()
        if "permissions" not in text:
            violations.append(f"{name}: workflow must declare explicit minimal permissions")
        else:
            findings.append(f"workflow ok: {name} declares permissions")
        for scoped, allow_stems in elevated_allowlist.items():
            if scoped in text and stem not in allow_stems:
                violations.append(f"{name}: elevated permission '{scoped}' requires owner review")


def check_secrets(violations: list[str], findings: list[str]) -> None:
    text_files = iter_files(["."], SCAN_TEXT_EXTS)
    for p in text_files:
        if p.suffix not in SCAN_TEXT_EXTS:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="strict")
        except (OSError, UnicodeError):
            continue  # binary or unreadable: skip
        for name, rx in SECRET_PATTERNS:
            for m in rx.finditer(text):
                if is_placeholder_match(text, m.start(), m.end()) and name != "private_key_block":
                    findings.append(f"placeholder ignored: {rel(p)} contains example {name}")
                    continue
                violations.append(f"{rel(p)}: possible {name} secret detected")


def check_public_boundary(violations: list[str], findings: list[str]) -> None:
    text_files = iter_files(["."], SCAN_TEXT_EXTS)
    for p in text_files:
        if p.suffix not in SCAN_TEXT_EXTS:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="strict")
        except (OSError, UnicodeError):
            continue
        for m in PRIVATE_ENDPOINT_RE.finditer(text):
            if not is_placeholder_match(text, m.start(), m.end()):
                violations.append(f"{rel(p)}: private/internal endpoint literal detected ({m.group(0)[:60]})")
        # PAN heuristic on raw text: 13-19 digits with optional single spaces/dashes.
        # Placeholder suppression is deliberately local so an unrelated "test" or
        # "demo" elsewhere in the same file cannot hide a real candidate.
        for m in PAN_RE.finditer(text):
            raw = m.group(0)
            digits = re.sub(r"[ -]", "", raw)
            if is_placeholder_match(text, m.start(), m.end()) or digits in {
                "0123456789012",
                "4111111111111111",
                "1234567890123456",
            }:
                findings.append(f"placeholder ignored: {rel(p)} contains example PAN pattern")
                continue
            if looks_like_date_sequence(raw):
                findings.append(f"date-like sequence ignored: {rel(p)}")
                continue
            violations.append(f"{rel(p)}: possible PAN-length numeric sequence detected ({digits[:4]}...{digits[-4:]})")


def check_python_syntax(violations: list[str], findings: list[str]) -> None:
    py_files = iter_files(["."], {".py"})
    if not py_files:
        findings.append("no Python files to syntax-check")
        return
    failed = 0
    for p in py_files:
        try:
            source = p.read_text(encoding="utf-8")
            compile(source, rel(p), "exec")
        except (SyntaxError, OSError, UnicodeError) as e:
            violations.append(f"{rel(p)}: Python syntax error ({e})")
            failed += 1
    if failed == 0:
        findings.append(f"python ok: {len(py_files)} file(s) compile")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="KKS deterministic governance validation")
    parser.add_argument("--quiet", action="store_true", help="print only violations and a final status")
    args = parser.parse_args(argv)

    violations: list[str] = []
    findings: list[str] = []

    parsed = check_json_parse(violations)
    if not args.quiet:
        findings.append(f"json ok: {len(parsed)} JSON object file(s) parse")

    check_validator_regressions(violations, findings)
    check_connector_gates(violations, findings)
    check_required_artifacts(violations)
    check_enter_skill(violations, findings)
    check_documentation_contract(violations, findings)
    check_workflows(violations, findings)
    check_secrets(violations, findings)
    check_public_boundary(violations, findings)
    check_python_syntax(violations, findings)

    if not args.quiet:
        for f in findings:
            print(f"  ok    {f}")
    for v in violations:
        print(f"  FAIL  {v}", file=sys.stderr)
    if violations:
        print(f"KKS governance validation: FAILED ({len(violations)} violation(s))", file=sys.stderr)
        return 1
    print("KKS governance validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

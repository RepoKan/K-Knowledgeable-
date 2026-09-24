#!/usr/bin/env python3
"""Regression tests for KKS governance validation."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("validate_kks_governance.py")
SPEC = importlib.util.spec_from_file_location("validate_kks_governance", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class GovernanceValidatorTests(unittest.TestCase):
    def test_iter_files_deduplicates_overlapping_roots(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "nested").mkdir()
            (root / "nested" / "config.json").write_text("{}", encoding="utf-8")
            with patch.object(validator, "REPO_ROOT", root):
                files = validator.iter_files([".", "nested"], {".json"})
            self.assertEqual([p.relative_to(root).as_posix() for p in files], ["nested/config.json"])

    def test_unrelated_test_word_does_not_hide_numeric_candidate(self) -> None:
        text = "test instructions\n" + ("x" * 200) + "\naccount=5555444433331111"
        match = validator.PAN_RE.search(text)
        self.assertIsNotNone(match)
        assert match is not None
        self.assertFalse(validator.is_placeholder_match(text, match.start(), match.end()))

    def test_nearby_placeholder_still_suppresses_example(self) -> None:
        text = "sample PAN 5555444433331111"
        match = validator.PAN_RE.search(text)
        self.assertIsNotNone(match)
        assert match is not None
        self.assertTrue(validator.is_placeholder_match(text, match.start(), match.end()))

    def test_root_python_file_is_syntax_checked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "broken.py").write_text("def broken(:\n    pass\n", encoding="utf-8")
            violations: list[str] = []
            findings: list[str] = []
            with patch.object(validator, "REPO_ROOT", root):
                validator.check_python_syntax(violations, findings)
            self.assertTrue(any("broken.py: Python syntax error" in item for item in violations))

    def test_placeholder_enter_skill_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / ".github" / "skills" / "enter" / "SKILL.md"
            skill.parent.mkdir(parents=True)
            skill.write_text(
                "---\nname: enter\ndescription: Describe what this skill does\n---\n"
                "Define the functionality provided by this skill",
                encoding="utf-8",
            )
            violations: list[str] = []
            findings: list[str] = []
            with patch.object(validator, "REPO_ROOT", root):
                validator.check_enter_skill(violations, findings)
            self.assertTrue(any("template placeholder remains" in item for item in violations))


if __name__ == "__main__":
    unittest.main()

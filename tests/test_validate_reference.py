import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_reference import validate

with (ROOT / "configs" / "skybridge-kks-pilot.json").open(encoding="utf-8") as fh:
    GOOD = json.load(fh)


class PolicyTest(unittest.TestCase):
    def test_candidate_passes(self):
        self.assertEqual(validate(GOOD), [])

    def test_deployment_blocked(self):
        bad = copy.deepcopy(GOOD)
        bad["integration"]["deploymentApproved"] = True
        self.assertTrue(validate(bad))

    def test_prod_data_blocked(self):
        bad = copy.deepcopy(GOOD)
        bad["security"]["noProductionData"] = False
        self.assertTrue(validate(bad))

    def test_node22_blocked(self):
        bad = copy.deepcopy(GOOD)
        bad["runtime"]["minimumNodeMajor"] = 22
        self.assertTrue(validate(bad))

    def test_unverified_upstream_blocked(self):
        bad = copy.deepcopy(GOOD)
        bad["source"]["repository"] = "https://github.com/example/skybridge"
        self.assertTrue(validate(bad))

    def test_missing_sha_blocked(self):
        bad = copy.deepcopy(GOOD)
        bad["kksGitHubBaseline"]["sha"] = "latest"
        self.assertTrue(validate(bad))


if __name__ == "__main__":
    unittest.main()

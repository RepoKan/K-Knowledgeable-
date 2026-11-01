import unittest
from unittest.mock import patch

from scripts.check_official_source_freshness import check_source


class FakeResponse:
    status = 200
    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "ETag": '"test-etag"',
        "Last-Modified": "Sat, 31 Oct 2026 00:00:00 GMT",
    }

    def __init__(self, body=b"official documentation", final_url="https://kotlinlang.org/docs/home.html"):
        self.body = body
        self.final_url = final_url

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def geturl(self):
        return self.final_url

    def read(self, _limit):
        return self.body


class OfficialSourceFreshnessTests(unittest.TestCase):
    def test_success_records_digest_and_metadata(self):
        source = {
            "id": "kotlin",
            "title": "Kotlin docs",
            "url": "https://kotlinlang.org/docs/home.html",
            "allowed_hosts": ["kotlinlang.org"],
            "authority": "official",
            "scope": "language docs",
        }
        with patch("scripts.check_official_source_freshness.urlopen", return_value=FakeResponse()):
            result = check_source(source)
        self.assertEqual(result["state"], "HTTP_OK")
        self.assertEqual(result["status_code"], 200)
        self.assertTrue(result["body_prefix_sha256"])
        self.assertEqual(result["etag"], '"test-etag"')

    def test_redirect_outside_allowlist_is_blocked(self):
        source = {
            "id": "kotlin",
            "title": "Kotlin docs",
            "url": "https://kotlinlang.org/docs/home.html",
            "allowed_hosts": ["kotlinlang.org"],
            "authority": "official",
            "scope": "language docs",
        }
        response = FakeResponse(final_url="https://attacker.example/redirect")
        with patch("scripts.check_official_source_freshness.urlopen", return_value=response):
            result = check_source(source)
        self.assertEqual(result["state"], "BLOCKED_REDIRECT_HOST")

    def test_catalog_host_mismatch_is_blocked_before_network(self):
        source = {
            "id": "kotlin",
            "url": "https://attacker.example/",
            "allowed_hosts": ["kotlinlang.org"],
        }
        with patch("scripts.check_official_source_freshness.urlopen") as mocked:
            result = check_source(source)
        self.assertEqual(result["state"], "BLOCKED_HOST")
        mocked.assert_not_called()


if __name__ == "__main__":
    unittest.main()

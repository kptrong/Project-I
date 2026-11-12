"""Chỉ kiểm tra phần đọc dữ liệu; hàm lọc là bài tập chưa hoàn thành."""

import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import mock_open, patch

from src.data_loader import load_rules

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/data_loader"


class LoadRulesTests(unittest.TestCase):
    def test_mixed_statuses_and_vietnamese_are_preserved(self):
        records = load_rules(FIXTURES / "mixed_statuses.json")
        self.assertEqual(len(records), 3)
        self.assertEqual(records[0]["title"], "Mục kiểm tra đã duyệt")
        self.assertEqual(
            [record["review_status"] for record in records],
            ["approved", "draft", "approved"],
        )

    def test_all_draft_records_are_still_loaded(self):
        records = load_rules(FIXTURES / "all_draft.json")
        self.assertEqual(len(records), 2)
        self.assertTrue(all(record["review_status"] == "draft" for record in records))

    def test_broken_json_raises_decode_error(self):
        with self.assertRaises(json.JSONDecodeError):
            load_rules(FIXTURES / "broken.json")

    def test_wrong_container_or_item_is_rejected(self):
        for text in ['{"id": "demo-001"}', '[null]']:
            with self.subTest(text=text):
                with patch.object(Path, "open", mock_open(read_data=text)):
                    with self.assertRaises(ValueError):
                        load_rules("unused.json")

    def test_empty_list_is_loaded(self):
        with patch.object(Path, "open", mock_open(read_data="[]")):
            self.assertEqual(load_rules("unused.json"), [])

    def test_cli_reports_broken_json_without_traceback(self):
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(ROOT / "src/data_loader.py"),
             str(FIXTURES / "broken.json")],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("LỖI JSON", result.stdout)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()

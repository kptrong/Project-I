"""Kiểm tra các lỗi dữ liệu và lỗi đọc tệp của bộ kiểm tra JSON."""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from src.validate_data import REQUIRED_FIELDS, validate_data

ROOT = Path(__file__).resolve().parents[1]


class ValidateDataTests(unittest.TestCase):
    def setUp(self):
        sample = ROOT / "data/examples/law11_illustration_valid.json"
        self.data = json.loads(sample.read_text(encoding="utf-8"))

    def test_both_allowed_statuses_are_accepted(self):
        # Chỉ thử giá trị trạng thái; không duyệt hoặc sửa dữ liệu mẫu trên đĩa.
        self.data[1]["review_status"] = "approved"
        self.assertEqual(validate_data(self.data), [])

    def test_each_required_field_is_checked(self):
        for field in REQUIRED_FIELDS:
            with self.subTest(field=field):
                item = copy.deepcopy(self.data[0])
                del item[field]
                errors = validate_data([item])
                self.assertEqual(len(errors), 1)
                self.assertIn(f"thiếu trường {field!r}", errors[0])

    def test_repeated_id_reports_first_occurrence(self):
        self.data.append(copy.deepcopy(self.data[0]))
        self.data.append(copy.deepcopy(self.data[0]))
        errors = validate_data(self.data)
        self.assertEqual(len(errors), 2)
        for position, error in zip([3, 4], errors):
            self.assertIn(f"Mục {position}", error)
            self.assertIn("đã xuất hiện ở mục 1", error)

    def test_status_must_match_exactly(self):
        for status in ["pending", "Approved", "draft "]:
            with self.subTest(status=status):
                self.data[0]["review_status"] = status
                self.assertTrue(any("trạng thái duyệt" in e for e in validate_data(self.data)))

    def test_edition_reference_skips_missing_edition(self):
        del self.data[0]["edition"]
        third = copy.deepcopy(self.data[1])
        third["id"] = "demo-law11-003"
        third["edition"] = "ILLUSTRATION-ONLY-v2"
        self.data.append(third)
        errors = validate_data(self.data)
        self.assertEqual(len(errors), 2)
        self.assertIn("Mục 3", errors[1])
        self.assertIn("ở mục 2", errors[1])

    def test_wrong_shapes_and_types_report_errors_without_crashing(self):
        for data in [{}, [], None, [None], [1], ["text"]]:
            with self.subTest(data=data):
                self.assertTrue(validate_data(data))
        self.data[0].update(id=[], law_number=True, edition={}, review_status=[])
        self.data[1]["title"] = "  "
        self.assertEqual(len(validate_data(self.data)), 5)

    def test_invalid_example_reports_all_five_errors(self):
        path = ROOT / "data/examples/law11_illustration_invalid.json"
        errors = validate_data(json.loads(path.read_text(encoding="utf-8")))
        self.assertEqual(len(errors), 5)
        for fragment in ["explanation_vi", "source_url", "mã trùng", "trạng thái duyệt", "phiên bản"]:
            self.assertTrue(any(fragment in error for error in errors), fragment)

    def test_cli_handles_bom_bad_json_and_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "mau co khoang trang.json"
            cases = [
                (json.dumps(self.data, ensure_ascii=False), "utf-8-sig", 0),
                ('[{"id":]', "utf-8", 2),
            ]
            for text, encoding, expected in cases:
                with self.subTest(expected=expected):
                    path.write_text(text, encoding=encoding)
                    result = self.run_cli(path)
                    self.assertEqual(result.returncode, expected)
                    self.assertEqual(result.stderr, "")
            result = self.run_cli(Path(folder) / "missing.json")
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stderr, "")

    @staticmethod
    def run_cli(path):
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(ROOT / "src/validate_data.py"), str(path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
        )


if __name__ == "__main__":
    unittest.main()

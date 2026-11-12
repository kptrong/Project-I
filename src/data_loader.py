"""Đọc dữ liệu JSON và khung bài tập lọc các mục đã duyệt."""

import argparse
import json
from pathlib import Path


def load_rules(path: str | Path) -> list[dict]:
    """Đọc JSON UTF-8 và trả về danh sách các từ điển, chưa lọc trạng thái.

    Lỗi đọc tệp hoặc cú pháp JSON được chuyển cho nơi gọi xử lý.
    Hàm chỉ kiểm tra dạng list[dict]; kiểm tra đủ trường bằng validate_data.py.
    """
    path = Path(path)
    # utf-8-sig đọc được cả UTF-8 thường và UTF-8 có BOM trên Windows.
    with path.open(encoding="utf-8-sig") as file:
        records = json.load(file)

    if not isinstance(records, list):
        raise ValueError("Dữ liệu gốc phải là một danh sách JSON.")

    for position, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Mục {position} phải là một đối tượng JSON.")

    return records


def filter_approved_rules(records: list[dict]) -> list[dict]:
    approved_rules = []
    for record in records:
        if record.get("review_status") == "approved":
            approved_rules.append(record)

    return approved_rules

def main() -> int:
    """Chạy thử riêng bước đọc tệp; chưa gọi hàm lọc đang chờ hoàn thành."""
    parser = argparse.ArgumentParser(description="Đọc dữ liệu JSON UTF-8, chưa lọc trạng thái duyệt.")
    parser.add_argument("path", type=Path, help="Đường dẫn tệp JSON cần đọc")
    args = parser.parse_args()

    try:
        records = load_rules(args.path)
    except json.JSONDecodeError as error:
        print(f"LỖI JSON: dòng {error.lineno}, cột {error.colno}: {error.msg}")
        return 2
    except (OSError, UnicodeError) as error:
        print(f"KHÔNG ĐỌC ĐƯỢC TỆP: {args.path}: {error}")
        return 2
    except ValueError as error:
        print(f"DỮ LIỆU KHÔNG ĐÚNG DẠNG: {error}")
        return 1

    print(f"Đã đọc {len(records)} mục từ {args.path} (chưa lọc trạng thái duyệt).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


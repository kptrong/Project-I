"""Kiểm tra cấu trúc JSON; không xác minh nội dung luật hoặc việc duyệt."""

import argparse # nhận đương dẫn tệp từ dòng lệnh
import json # chuyển đổi giữa chuỗi JSON và đối tượng Python
from pathlib import Path # làm việc với đường dẫn tệp

REQUIRED_FIELDS = (
    "id",
    "law_number",
    "section",
    "title",
    "original_text",
    "explanation_vi",
    "source_url",
    "edition",
    "review_status",
)
REVIEW_STATUSES = {"draft", "approved"}


def validate_data(data: object) -> list[str]:
    """Trả về tất cả lỗi; vị trí mục bắt đầu từ 1 để dễ tra trong tệp."""
    if not isinstance(data, list):
        return ["Dữ liệu gốc phải là một danh sách JSON."]
    if not data:
        return ["Danh sách dữ liệu không được rỗng."]

    errors = [] # Danh sách lỗi phát hiện trong quá trình kiểm tra
    seen_ids = {} # Lưu trữ các id đã thấy để phát hiện trùng lặp
    reference_edition = None 
    reference_position = None 

    for position, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            errors.append(f"Mục {position}: phải là một đối tượng JSON.")
            continue

        label = f"Mục {position} (id={item.get('id', '<thiếu>')!r})" # Tên của mục hiện tại
        for field in REQUIRED_FIELDS:
            if field not in item:
                errors.append(f"{label}: thiếu trường {field!r}.")
                continue

            value = item[field]
            if field == "law_number":
                # bool cũng là lớp con của int trong Python, nên loại riêng.
                if type(value) is not int or value <= 0:
                    errors.append(f"{label}: 'law_number' phải là số nguyên dương.")
            elif not isinstance(value, str) or not value.strip():
                errors.append(f"{label}: {field!r} phải là chuỗi không rỗng.")

        item_id = item.get("id")
        if isinstance(item_id, str) and item_id.strip():
            if item_id in seen_ids:
                errors.append(
                    f"{label}: mã trùng {item_id!r}, "
                    f"đã xuất hiện ở mục {seen_ids[item_id]}."
                )
            else:
                seen_ids[item_id] = position

        status = item.get("review_status")
        if isinstance(status, str) and status.strip() and status not in REVIEW_STATUSES:
            errors.append(
                f"{label}: trạng thái duyệt {status!r} không hợp lệ; "
                "chỉ chấp nhận 'draft' hoặc 'approved'."
            )

        edition = item.get("edition")
        if isinstance(edition, str) and edition.strip():
            if reference_edition is None:
                reference_edition = edition
                reference_position = position
            elif edition != reference_edition:
                errors.append(
                    f"{label}: phiên bản {edition!r} khác phiên bản mốc "
                    f"{reference_edition!r} ở mục {reference_position}."
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Kiểm tra cấu trúc dữ liệu JSON, không xác minh nội dung luật."
    )
    parser.add_argument("path", type=Path, help="Đường dẫn tệp JSON cần kiểm tra")
    args = parser.parse_args()

    try:
        # utf-8-sig đọc được cả UTF-8 thông thường và UTF-8 có BOM trên Windows.
        with args.path.open(encoding="utf-8-sig") as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        print(
            f"LỖI JSON: {args.path}, dòng {error.lineno}, cột {error.colno}: "
            f"{error.msg}"
        )
        return 2
    except (OSError, UnicodeError) as error:
        print(f"KHÔNG ĐỌC ĐƯỢC TỆP: {args.path}: {error}")
        return 2

    errors = validate_data(data)
    if errors:
        print(f"KHÔNG HỢP LỆ: {args.path} — phát hiện {len(errors)} lỗi:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"HỢP LỆ: {args.path} — {len(data)} mục đạt kiểm tra cấu trúc.")
    print("Kết quả này không xác nhận nội dung luật đúng hoặc đã được duyệt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Điểm chạy dòng lệnh của dự án chatbot giải thích luật bóng đá."""

EXIT_COMMANDS = {"thoat", "thoát", "exit", "quit", "q"}

from dbm import error

from src.data_loader import load_rules, filter_approved_rules

def main() -> None:
    """Hiển thị phạm vi và nhận lệnh; chưa xử lý câu hỏi về luật."""
    print("CHATBOT GIẢI THÍCH LUẬT BÓNG ĐÁ BẰNG TIẾNG VIỆT")
    print("Project 1 cá nhân tại HUST — thời gian dự kiến: 8 tuần.")
    print(
        "Phạm vi dự kiến: giải thích các luật cơ bản của bóng đá sân 11 người "
        "bằng tiếng Việt, dựa trên tài liệu có nguồn và phiên bản rõ ràng."
    )
    print("Trạng thái: chưa triển khai trả lời câu hỏi, tìm kiếm hoặc tích hợp AI.")
    print("Để thoát: nhập thoat, thoát, exit, quit hoặc q; hoặc nhấn Ctrl+C.")

    try:
        records = load_rules("data/processed/rules.json")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Không đọc được dữ liệu: {error}")
        return

    approved_rules = filter_approved_rules(records)

    if not approved_rules:
        print("Chưa có mục nào được duyệt.")

    for rule in approved_rules:
        print(f"\nMã: {rule['id']}")
        print(f"Tiêu đề: {rule['title']}")
        print(f"Nguồn: {rule['source_url']}")
    
    while True:
        try:
            user_input = input("\nBạn: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nĐã thoát chương trình.")
            break

        if user_input.casefold() in EXIT_COMMANDS:
            print("Đã thoát chương trình.")
            break
        if not user_input:
            continue

        print("Tính năng trả lời câu hỏi chưa được triển khai.")


if __name__ == "__main__":
    main()

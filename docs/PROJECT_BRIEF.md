# Mô tả dự án

## Mục tiêu

Xây dựng chatbot giải thích luật bóng đá 11 người bằng tiếng Việt cho Project 1 cá nhân tại HUST trong 8 tuần. Nội dung giải thích cần dễ hiểu và có thể đối chiếu với tài liệu nguồn cùng phiên bản luật đã chọn.

## Phạm vi

- Phạm vi dự án: hỗ trợ Điều 11–14 của luật bóng đá 11 người.
- Bộ dữ liệu đầu tiên: chỉ gồm Điều 11 về việt vị.
- Chỉ bổ sung Điều 12–14 sau khi bộ dữ liệu Điều 11 và cách kiểm tra đã được hoàn thiện.
- Nguồn cho bộ dữ liệu Điều 11 đầu tiên: trang IFAB tiếng Anh, phiên bản **2026/27**, thu thập ngày **11/11/2026**. Bản nguồn và bảng truy xuất từng khoản nằm tại `data/raw/IFAB_LAW11_SOURCE.md`. Chưa xác minh quyền tái phân phối toàn văn; cần làm rõ trước khi công bố dữ liệu.
- Buổi 2 chỉ xác định phạm vi, thiết kế mẫu dữ liệu và kiểm tra JSON; chưa xây dựng tính năng trả lời, giao diện, tìm kiếm hoặc tích hợp AI.

## Tổ chức dữ liệu

- `data/raw/`: tài liệu luật thật ở dạng gốc cùng thông tin nguồn và phiên bản.
- `data/processed/`: dữ liệu luật thật đã xử lý; vẫn phải giữ thông tin nguồn và trạng thái duyệt.
- `data/examples/`: dữ liệu minh họa để học cấu trúc và kiểm tra chương trình; không dùng để trả lời về luật.

Hai tệp `law11_illustration_valid.json` và `law11_illustration_invalid.json` trong `data/examples/` chỉ chứa văn bản thay thế. URL thuộc miền `.invalid` và phiên bản `ILLUSTRATION-ONLY-v1` là dấu hiệu minh họa, không phải nguồn trích dẫn hoặc phiên bản luật có thật. Tệp thứ hai cố ý chứa lỗi cấu trúc để thử bộ kiểm tra.

## Định dạng một mục

Tệp JSON chứa một danh sách các đối tượng. Mỗi đối tượng có đủ các trường sau:

| Trường | Kiểu | Ý nghĩa |
|---|---|---|
| `id` | Chuỗi không rỗng | Mã duy nhất trong tệp |
| `law_number` | Số nguyên dương | Số điều luật; bộ dữ liệu đầu tiên dùng `11` |
| `section` | Chuỗi không rỗng | Phần hoặc tiểu mục để đối chiếu nguồn |
| `title` | Chuỗi không rỗng | Tiêu đề của mục |
| `original_text` | Chuỗi không rỗng | Nguyên văn phần nội dung khoản; chỉ đổi cách trình bày HTML sang văn bản. Mẫu trong `data/examples/` dùng lời nhắc giữ chỗ |
| `explanation_vi` | Chuỗi không rỗng | Diễn giải bằng tiếng Việt, giữ điều kiện và ngoại lệ của bản gốc; mẫu trong `data/examples/` chưa có nội dung luật |
| `source_url` | Chuỗi không rỗng | URL của tài liệu nguồn; mẫu dùng miền `.invalid` |
| `edition` | Chuỗi không rỗng | Phiên bản luật, phải thống nhất trong cùng tệp |
| `review_status` | Chuỗi | Chỉ nhận `draft` hoặc `approved` |

### Trạng thái duyệt

- `draft`: mục đang chờ người dùng kiểm tra.
- `approved`: chỉ đặt sau khi người dùng đã tự đối chiếu nội dung với nguồn và xác nhận.
- Bộ kiểm tra không tự chuyển trạng thái. JSON hợp lệ vẫn có thể chứa nội dung luật sai; cần duyệt nội dung riêng.
- Tất cả mục minh họa hợp lệ hiện là `draft`; không giả định rằng người dùng đã duyệt bất kỳ mục nào.

## Quy tắc kiểm tra buổi 2

- Tệp phải đọc được dưới dạng JSON UTF-8; chấp nhận UTF-8 có BOM từ trình soạn thảo Windows.
- Dữ liệu gốc phải là danh sách không rỗng; mỗi phần tử phải là một đối tượng.
- Kiểm tra trường bắt buộc, kiểu dữ liệu, chuỗi rỗng, mã trùng, trạng thái duyệt và tính thống nhất của phiên bản.
- Mã được so sánh chính xác, có phân biệt hoa thường. Khi trùng, báo cả vị trí hiện tại và vị trí xuất hiện đầu tiên, đánh số từ 1.
- Phiên bản của mục đầu tiên có `edition` là chuỗi không rỗng được dùng làm mốc. Mỗi mục khác phiên bản này đều được báo lỗi; chương trình không quyết định phiên bản nào là phiên bản luật đúng.
- Bộ kiểm tra không truy cập URL, không xác minh nội dung luật và không xác nhận việc duyệt. Trường bổ sung ngoài các trường bắt buộc được phép tồn tại.

## Bước tiếp theo

Đã tạo `data/processed/rules.json` gồm 4 mục, mỗi mục ứng với một khoản 11.1–11.4, phiên bản `2026/27`, trạng thái ban đầu `draft`. Người dùng đối chiếu nguyên văn và bản diễn giải theo `docs/LAW11_REVIEW.md` trước khi đặt từng mục thành `approved`. Sau đó mới mở rộng dữ liệu và xây dựng các chức năng chatbot theo yêu cầu tiếp theo.

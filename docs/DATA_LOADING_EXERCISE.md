# Bài tập đọc và lọc dữ liệu Điều 11

## Phần đã có trong `src/data_loader.py`

`load_rules(path)` nhận đường dẫn tệp JSON, mở bằng `utf-8-sig` (đọc được UTF-8 thông thường và UTF-8 có BOM), gọi `json.load(file)`, kiểm tra dạng dữ liệu rồi trả về `records`.

Sau khi đọc `data/processed/rules.json`:

- Toàn bộ dữ liệu là một `list` của Python, hiện chứa 4 mục.
- Mỗi mục là một `dict` gồm các trường như `id`, `title`, `source_url`, `review_status`.
- Chuỗi JSON thành `str`, số `law_number` thành `int`.
- `records[0]` lấy mục đầu tiên; `records[0]["review_status"]` lấy trạng thái duyệt của mục đó.
- Việc đọc không đổi `draft` thành `approved` và không bỏ các mục chờ duyệt.

Hàm chỉ kiểm tra dữ liệu có dạng danh sách các từ điển. Việc kiểm tra đủ 9 trường, mã trùng, trạng thái và phiên bản vẫn dùng `src/validate_data.py`. Danh sách rỗng `[]` đọc được ở bước này; bộ kiểm tra dữ liệu luật hiện yêu cầu danh sách không rỗng.

## Chạy thử phần đọc

Chạy trong PowerShell tại thư mục gốc dự án:

```powershell
conda activate ml_env
python src/data_loader.py data/processed/rules.json
```

Chương trình chỉ báo số mục đã đọc. Chưa gọi hàm lọc và chưa nối vào `app.py`.

## Ví dụ đầu vào để tự viết hàm lọc

Đây là dữ liệu minh họa rút gọn, không phải nội dung luật hoặc các mục đã được duyệt thật:

```python
records = [
    {"id": "demo-001", "review_status": "approved"},
    {"id": "demo-002", "review_status": "draft"},
    {"id": "demo-003", "review_status": "approved"},
]
```

Bạn hãy hoàn thành `filter_approved_rules(records)` trong `src/data_loader.py`, theo các dòng TODO:

1. Tạo danh sách kết quả rỗng.
2. Dùng `for` xét từng từ điển trong `records`.
3. Kiểm tra giá trị `review_status`; dùng `.append(...)` thêm cả từ điển phù hợp vào kết quả.
4. Đặt `return` sau vòng lặp để xét được mọi mục.

Kết quả mong đợi là danh sách chứa **hai từ điển** có mã `demo-001` và `demo-003`, giữ đúng thứ tự. Không chỉ trả về danh sách mã và không thay đổi danh sách đầu vào.

Nếu toàn bộ mục là `draft`, kết quả phải là `[]`. Nếu đầu vào là `[]`, kết quả cũng phải là `[]`. Trạng thái được so sánh chính xác với `"approved"`.

Dòng `raise NotImplementedError(...)` đánh dấu bài tập chưa được viết. Sau khi hoàn thành, bỏ dòng này. Hiện gọi riêng hàm lọc sẽ báo chưa triển khai; đó không phải lỗi của phần đọc JSON.

Bạn gửi lại hàm đã viết để được góp ý trước khi nối vào `app.py`. Sau đó mới bổ sung phần liệt kê **mã, tiêu đề và nguồn** của các mục đã duyệt, thông báo khi không có mục nào được duyệt và kiểm tra luồng chạy của ứng dụng.

## Những trường hợp có thể thử ngay

Các tệp trong `tests/fixtures/data_loader/` là mẫu kiểm tra phần đọc, chỉ có vài trường, không phải dữ liệu luật thật và không dùng để kiểm tra đầy đủ schema của luật.

```powershell
python src/data_loader.py tests/fixtures/data_loader/mixed_statuses.json
python src/data_loader.py tests/fixtures/data_loader/all_draft.json
python src/data_loader.py tests/fixtures/data_loader/broken.json
```

| Tệp | Kết quả của phần đọc hiện tại | Kết quả lọc cần kiểm tra sau khi bạn viết hàm |
|---|---|---|
| `mixed_statuses.json` | Đọc đủ 3 mục, mã thoát 0 | Giữ 2 mục có trạng thái `approved` |
| `all_draft.json` | Đọc đủ 2 mục, mã thoát 0 | Trả về `[]` |
| `broken.json` | Báo lỗi cú pháp JSON, mã thoát 2 | Không chạy bước lọc vì chưa đọc được dữ liệu |

Tệp `broken.json` cố ý có dấu phẩy thừa trước `}`. Lỗi cú pháp JSON khác với dữ liệu đọc được nhưng không có mục đã duyệt.

Kiểm tra tự động riêng phần đọc:

```powershell
python -m unittest discover -s tests -p test_data_loader.py -v
```

Các kiểm tra hiện tại chưa gọi hàm lọc vì hàm đó là phần bạn sẽ tự viết.

# Tiến độ dự án

## 12/11/2026 — Hoàn tất TODO 3 trong hàm lọc

- Phần kiểm tra `review_status == "approved"` và `results.append(record)` đã có trong mã; giữ nguyên và xóa chú thích TODO 3 đã hoàn thành.
- Kiểm tra trực tiếp trong Conda `ml_env`: xem danh sách `results` tại thời điểm hàm báo `NotImplementedError`; dữ liệu hỗn hợp giữ đúng các record approved, đúng thứ tự và cùng đối tượng ban đầu; toàn draft và đầu vào rỗng đều cho danh sách rỗng. Trường hợp thiếu trạng thái được bỏ qua. Kiểm tra đạt, mã thoát `0`.
- Giới hạn: TODO 4 vẫn chưa hoàn thành nên gọi hàm vẫn báo `NotImplementedError`; chưa kiểm tra tích hợp ứng dụng.
- Bước tiếp theo: hoàn thành phần trả về danh sách ở TODO 4 khi được yêu cầu.

## 11/11/2026 — Bài học đọc JSON và khung lọc mục đã duyệt

### Đã làm

- Đọc hướng dẫn, README, tiến độ và mã hiện có trước khi sửa. Giữ nguyên `app.py`, bộ kiểm tra dữ liệu và `data/processed/rules.json`.
- Tạo `src/data_loader.py` với `load_rules(path)`: đọc UTF-8 (chấp nhận BOM), chuyển JSON thành danh sách từ điển, kiểm tra dạng tổng thể và trả nguyên danh sách, chưa lọc trạng thái duyệt. Lệnh chạy riêng xử lý lỗi đọc tệp, JSON sai cú pháp và sai dạng dữ liệu.
- Tạo khung `filter_approved_rules(records)` với TODO để người dùng tự viết vòng lặp `for`. Dòng `NotImplementedError` thể hiện rõ hàm chưa hoàn thành; không tạo kết quả lọc giả. Lệnh đọc dữ liệu chưa gọi hàm này.
- Tạo `docs/DATA_LOADING_EXERCISE.md`: giải thích `list`/`dict`, ví dụ nhỏ, kết quả mong đợi và gợi ý từng bước; cập nhật lệnh chạy trong README.
- Thêm ba tệp mẫu kiểm tra tại `tests/fixtures/data_loader/` và `tests/test_data_loader.py`. Đây là dữ liệu minh họa rút gọn cho phần đọc, không phải luật thật hoặc dữ liệu đầy đủ schema.

### Kiểm tra đã thực hiện trong Conda `ml_env`

- `python src/data_loader.py data/processed/rules.json`: đọc đủ **4 mục**, mã thoát `0`.
- Mẫu `mixed_statuses.json` có mục đã duyệt và chờ duyệt: đọc đủ **3 mục**, giữ nguyên trạng thái, mã thoát `0`.
- Mẫu `all_draft.json`: đọc đủ **2 mục**, mã thoát `0`; phần đọc không tự bỏ các mục `draft`.
- Mẫu `broken.json`: báo lỗi cú pháp JSON ở dòng 2, cột 47, mã thoát `2`; không có traceback từ lệnh đọc.
- `python -m unittest discover -s tests -p test_data_loader.py -v`: **6 kiểm tra đạt**, bao phủ dữ liệu có tiếng Việt/trạng thái hỗn hợp, toàn bộ draft, JSON hỏng, sai dạng dữ liệu, danh sách rỗng và thông báo lỗi qua dòng lệnh.

### Phần đang chờ người dùng tự viết

- Chưa thực hiện hoặc kiểm tra kết quả của `filter_approved_rules`. Kết quả mong đợi sau khi hoàn thành: mẫu hỗn hợp giữ 2 mục approved, mẫu toàn draft trả `[]`, JSON hỏng dừng trước bước lọc.
- Chưa nối vào `app.py` để liệt kê mã, tiêu đề và nguồn, theo yêu cầu làm sau khi người dùng gửi code. Chưa kiểm tra luồng liệt kê trong ứng dụng.

### Bước tiếp theo

1. Người dùng hoàn thành các TODO của hàm lọc bằng `for` và gửi code để được góp ý.
2. Kiểm tra hàm lọc với dữ liệu hỗn hợp, toàn draft và danh sách rỗng; sau đó tích hợp việc liệt kê vào `app.py`.
3. Kiểm tra ứng dụng với mục đã duyệt, không có mục đã duyệt và JSON sai cú pháp; cập nhật lệnh chạy và tiến độ theo kết quả thực tế.

## 11/11/2026 — Kiểm tra trạng thái duyệt sau bước 4

- Người dùng thông báo đã chuyển cả 4 mục sang `approved`.
- Kiểm tra tệp `data/processed/rules.json` trên đĩa tại thời điểm này: `law11-001`, `law11-003`, `law11-004` là `approved`; riêng `law11-002` (khoản 11.2) vẫn là `draft`. Chưa ghi nhận cả 4 mục đã được duyệt trong bản lưu; có thể còn thay đổi chưa lưu trong trình soạn thảo.
- Chạy `python src/validate_data.py data/processed/rules.json` trong Conda `ml_env`: **4 mục hợp lệ về cấu trúc**, mã thoát `0`. Tệp được phép có cả `draft` và `approved`.
- Giữ nguyên nội dung và trạng thái trong JSON; không tự chuyển mục còn lại sang `approved`. Cập nhật cách mô tả trạng thái trong tài liệu để lấy JSON làm nơi ghi trạng thái hiện tại.
- Bước tiếp theo: người dùng kiểm tra trạng thái của `law11-002`, lưu tệp bằng Ctrl+S nếu đã sửa, rồi chạy lại bộ kiểm tra. Không suy ra rằng nội dung luật đúng chỉ từ kết quả kiểm tra cấu trúc.

## 11/11/2026 — Tuần 1, bước 4: dữ liệu Điều 11 và diễn giải tiếng Việt

### Đã làm

- Đọc hướng dẫn dự án, quy ước JSON, bộ kiểm tra hiện có, hồ sơ nguồn và toàn bộ nội dung bốn khoản trong HTML đã lưu. Giữ nguyên mã nguồn hiện có, bao gồm các chú thích người dùng đã bổ sung trong `src/validate_data.py`.
- Tạo `data/processed/rules.json` gồm 4 mục theo toàn bộ khoản 11.1–11.4, mã riêng `law11-001` đến `law11-004`; đầy đủ 9 trường đã thống nhất ở bước 2.
- Lấy `original_text` trực tiếp từ phần nội dung các khối `article` của bản nguồn IFAB đã lưu, giữ câu chữ, dấu câu và chú thích; chỉ bỏ thẻ HTML, giải mã ký tự và định dạng lại đoạn/danh sách. Không lấy FAQs hoặc thanh điều hướng.
- Viết `explanation_vi` cho từng khoản, giữ các điều kiện và ngoại lệ trong nguồn. Khoản 11.2 giữ chung các nhóm hành vi, định nghĩa, thời điểm và tình huống trình tự lỗi; khoản 11.4 giữ các mốc thời gian và điều kiện cảnh cáo. Đây là bản diễn giải nháp đang chờ người dùng kiểm tra nội dung.
- Mỗi mục ghi `section` chính thức, URL có fragment trỏ đến khoản và `edition` là `2026/27`. Tất cả mục mới có `review_status` là `draft`.
- Tạo `docs/LAW11_REVIEW.md` với bảng ánh xạ ID–khoản–vị trí nguồn, giải thích cách chia đoạn qua ví dụ 11.3 và hướng dẫn duyệt từng mục. Cập nhật README và PROJECT_BRIEF theo dữ liệu mới.

### Kiểm tra đã thực hiện trong Conda `ml_env`

- `python src/validate_data.py data/processed/rules.json`: **4 mục hợp lệ về cấu trúc**, mã thoát `0`.
- Đọc lại JSON đã lưu và đối chiếu tự động với toàn bộ văn bản của từng khối nguồn bằng một lượt phân tích HTML riêng: câu chữ và dấu câu của cả bốn `original_text` đều khớp, sau khi bỏ khác biệt khoảng trắng và dấu đầu dòng trình bày.
- Xác nhận đủ cả bốn khoản, ID không trùng, mỗi mục đúng 9 trường yêu cầu, số điều luật 11, phiên bản 2026/27, URL trỏ đến đúng khối nguồn và toàn bộ trạng thái còn là `draft`.
- SHA-256 của HTML vẫn là `2a378103e19124b3e4e88f3fd1f3151e2b4f0d70c597934c5dbaf7b541e3d3c1`; bản nguồn không bị sửa. Các liên kết tệp cục bộ trong README và tài liệu duyệt đều tồn tại.
- Rà bản diễn giải với nội dung nguồn trong quá trình biên soạn; chưa có xác nhận duyệt nội dung từ người dùng. Không chạy lại toàn bộ unittest vì không thay đổi chương trình kiểm tra; đã chạy trực tiếp công cụ trên dữ liệu mới.

### Giới hạn

- Kiểm tra cấu trúc và đối chiếu nguyên văn không tự xác nhận chất lượng bản diễn giải. Chưa có mục nào được người dùng duyệt thành `approved`.
- URL nguồn còn dùng `latest`; phiên bản và bản lưu cố định trong hồ sơ nguồn là mốc đối chiếu khi nội dung online thay đổi.
- Chưa bổ sung Điều 12–14, giao diện, tìm kiếm hoặc tích hợp AI; `app.py` vẫn chưa trả lời câu hỏi.

### Bước tiếp theo

1. Người dùng đối chiếu từng mục theo `docs/LAW11_REVIEW.md`, bắt đầu với `law11-003` (khoản 11.3).
2. Sửa các diễn giải cần điều chỉnh; chỉ chuyển đúng mục đã kiểm tra đầy đủ từ `draft` sang `approved` và ghi ID/ngày duyệt vào tiến độ.
3. Chạy lại `python src/validate_data.py data/processed/rules.json` sau khi sửa. Nếu thay đổi nội dung mục đã duyệt, đưa lại về `draft` để kiểm tra lại.

## 11/11/2026 — Tuần 1, bước 3: thu thập nguồn Điều 11

### Đã làm và đã xác minh

- Đọc `README.md`, `AGENTS.md`, `docs/PROJECT_BRIEF.md` và tiến độ trước khi làm. Tài liệu trước bước này chưa chọn phiên bản luật thật; các phiên bản trong `data/examples/` chỉ là minh họa.
- Mở nguồn chính thức `https://www.theifab.com/laws/latest/offside/` bằng công cụ web; tải trực tiếp bản HTML từ cùng URL với HTTP `200 OK`.
- Lưu nguyên byte tại `data/raw/ifab_law11_source_2026-11-11.html` và thông tin phản hồi tại `data/raw/ifab_law11_source_2026-11-11.http.txt`.
- Xác minh phiên bản đang được chọn trong HTML là **2026/27**; `2025/26` là lựa chọn khác. Ghi nhận 2026/27 làm phiên bản nguồn Điều 11 đầu tiên trong README và PROJECT_BRIEF.
- Tạo `data/raw/IFAB_LAW11_SOURCE.md`: tên tài liệu, tổ chức phát hành, ngôn ngữ, phiên bản, URL, ngày thu thập (11/11/2026, Asia/Bangkok), HTTP, kích thước, SHA-256, bảng truy xuất bốn khoản và hướng dẫn đối chiếu khoản 11.3.

### Kiểm tra đã thực hiện

- Phân tích HTML đã lưu bằng `html.parser` của thư viện chuẩn Python trong Conda `ml_env`: đủ bốn khối `article`, đúng thứ tự và tiêu đề khoản 11.1–11.4, có nội dung và thẻ đóng.
- Xác định các ID thực tế: `offside-position`, `offside-offence`, `no-offence`, `offences-and-sanctions`; ghi dòng đầu/cuối của từng khối vào hồ sơ nguồn. Khối 11.3 chứa 3 mục danh sách.
- Bản HTML có kích thước **317442 byte**; SHA-256: `2a378103e19124b3e4e88f3fd1f3151e2b4f0d70c597934c5dbaf7b541e3d3c1`.
- Kiểm tra cuối bằng Python: mã băm và HTTP khớp hồ sơ; bốn fragment và khoảng dòng khớp HTML; các liên kết tệp cục bộ trong README/hồ sơ tồn tại; README, PROJECT_BRIEF và PROGRESS cùng ghi 2026/27; chưa có JSON trong `data/processed/`. Tất cả đạt.
- Lần tải qua shell trong sandbox không kết nối được proxy; chạy lại với quyền được cấp đã tải thành công. Đã bỏ tệp header rỗng do lần tải thất bại tạo ra.
- Thử mở URL theo phiên bản `/laws/2026-27/offside/` bằng công cụ web không thành công; không dùng URL đó làm nguồn đã xác minh. Giữ URL gốc được yêu cầu và snapshot cục bộ để truy xuất.

### Giới hạn

- Đây là kiểm tra nguồn và cấu trúc trang; người dùng chưa tự đối chiếu từng khoản, chưa có nội dung nào được đánh dấu `approved`.
- Bản lưu là HTML của trang; không lưu đầy đủ tài nguyên phụ hoặc PDF. FAQs và điều hướng đi kèm trang không thuộc bốn khoản được lập bảng.
- URL `latest` có thể thay đổi; dòng trong bảng chỉ áp dụng cho bản HTML có mã băm đã ghi. Phiên bản hiển thị không xác nhận luật áp dụng cho mọi giải đấu.
- Chưa xác minh quyền tái phân phối/công bố toàn văn; cần làm rõ trước khi công bố dữ liệu.
- Không tạo diễn giải tiếng Việt hoặc JSON dữ liệu luật thật; giữ nguyên mã chương trình và dữ liệu minh họa.

### Bước tiếp theo — bước 4

1. Người dùng đối chiếu thủ công khoản 11.3 theo hướng dẫn trong hồ sơ nguồn, rồi kiểm tra các khoản còn lại.
2. Biên soạn diễn giải tiếng Việt và chuyển nội dung thành JSON ở trạng thái `draft`, dùng phiên bản `2026/27` và nguồn/vị trí của từng khoản.
3. Chạy bộ kiểm tra cấu trúc; chỉ đổi sang `approved` sau khi người dùng đã kiểm tra nội dung với nguồn.

## 11/11/2026 — Buổi 2: phạm vi và kiểm tra dữ liệu JSON

### Đã làm

- Đọc `README.md`, `AGENTS.md`, nhật ký tiến độ và mã hiện có trước khi triển khai.
- Tạo `docs/PROJECT_BRIEF.md`: mục tiêu giải thích bằng tiếng Việt, phạm vi Điều 11–14 của luật bóng đá 11 người; bộ dữ liệu đầu tiên chỉ gồm Điều 11 về việt vị.
- Tạo `data/examples/law11_illustration_valid.json` gồm 2 mục minh họa ở trạng thái `draft`, đủ 9 trường yêu cầu. Chưa có mục nào được người dùng duyệt; không đặt `approved` cho dữ liệu mẫu trên đĩa.
- Tạo `data/examples/law11_illustration_invalid.json` cố ý chứa lỗi để kiểm tra. Cả hai tệp dùng văn bản giữ chỗ, URL miền `.invalid` và phiên bản minh họa, tách riêng khỏi `data/raw/` và `data/processed/` dành cho luật thật.
- Viết `src/validate_data.py` nhận đường dẫn JSON, báo lỗi theo vị trí và `id`: thiếu trường, sai kiểu/chuỗi rỗng, trùng mã, sai trạng thái duyệt và khác phiên bản mốc. Có xử lý lỗi đọc tệp và sai cú pháp JSON.
- Bổ sung `tests/test_validate_data.py` bằng `unittest` của thư viện chuẩn; cập nhật README với lệnh chạy, kết quả dự kiến và cách phát hiện mã trùng. Không cài thêm thư viện hay thay đổi `app.py`.

### Kiểm tra đã thực hiện trong Conda `ml_env`

- `python src/validate_data.py data/examples/law11_illustration_valid.json`: 2 mục đạt kiểm tra cấu trúc, mã thoát `0`.
- `python src/validate_data.py data/examples/law11_illustration_invalid.json`: phát hiện đúng 5 lỗi, mã thoát `1`:
  - Mục 2 (`demo-law11-001`): thiếu `explanation_vi`, thiếu `source_url` và trùng mã với mục 1.
  - Mục 3 (`demo-law11-003`): `review_status` là `pending` và phiên bản `ILLUSTRATION-ONLY-v2` khác mốc `ILLUSTRATION-ONLY-v1` ở mục 1.
- `python -m unittest discover -s tests -v`: cả 8 kiểm tra đạt. Bao phủ hai trạng thái được phép, từng trường bắt buộc, mã lặp nhiều lần, trạng thái sai, cách chọn phiên bản mốc, dữ liệu sai kiểu, mẫu có lỗi và các lỗi đọc tệp qua dòng lệnh.
- Kiểm tra dòng lệnh bao gồm đường dẫn có khoảng trắng, UTF-8 có BOM, JSON hỏng và tệp không tồn tại. JSON hỏng và tệp không tồn tại trả mã thoát `2`, không có traceback.
- `python src/validate_data.py --help`: hiển thị hướng dẫn và tham số đường dẫn, mã thoát `0`.
- Lần chạy unittest đầu bị sandbox chặn thao tác với thư mục Temp của Windows. Đã chạy lại ngoài sandbox với quyền được cấp: tất cả đạt. Đặt `PYTHONIOENCODING=utf-8` trong phiên chạy để thu đầu ra tiếng Việt.

### Giới hạn

- Chưa thu thập hoặc xác minh nội dung luật thật; phiên bản luật chính thức vẫn chưa được chọn.
- Kiểm tra cấu trúc không xác nhận tính đúng đắn của luật, nguồn URL hoặc việc người dùng đã duyệt. Chương trình không tự chuyển `draft` thành `approved`.
- Phiên bản được đối chiếu với mục đầu tiên có `edition` là chuỗi không rỗng; mốc này không có nghĩa là phiên bản luật đúng.
- Không làm giao diện, tìm kiếm hoặc tích hợp AI trong buổi này.

### Bước tiếp theo

1. Chọn tài liệu chính thức cho Điều 11 và thống nhất một phiên bản cùng điều kiện sử dụng.
2. Thu thập văn bản gốc vào `data/raw/`; biên soạn dữ liệu thật vào `data/processed/` ở trạng thái `draft`, kèm nguồn để đối chiếu.
3. Chạy bộ kiểm tra cấu trúc; người dùng tự kiểm tra nội dung trước khi chuyển từng mục sang `approved`. Không dùng dữ liệu minh họa làm kiến thức luật.

## 11/11/2026 — Chuyển sang chạy bằng Conda

### Đã làm

- Theo lựa chọn của người dùng, từ nay chạy chương trình bằng môi trường Conda `ml_env`.
- Cập nhật `README.md` với lệnh kích hoạt Conda, chạy chương trình và chọn interpreter trong VS Code; bổ sung lựa chọn môi trường vào `AGENTS.md`.
- Giữ nguyên `app.py`, cấu hình VS Code và thư mục `.venv` đã có; không cài hoặc thay đổi gói trong Conda.

### Kiểm tra đã thực hiện

- `conda env list`: tìm thấy `ml_env` trên máy.
- `conda activate ml_env`: kích hoạt thành công trong phiên PowerShell kiểm tra.
- `python --version`: Python 3.11.16.
- `sys.executable`: `C:\Users\Lenovo\miniconda3\envs\ml_env\python.exe`.
- Chạy trực tiếp `'exit' | python app.py` trong `ml_env`: hiển thị đúng thông tin khởi động và thoát, mã thoát 0. Đặt `PYTHONIOENCODING=utf-8` trong phiên kiểm tra để thu đầu ra tiếng Việt qua pipe.

### Giới hạn và bước tiếp theo

- Chưa kiểm tra lựa chọn interpreter trong giao diện VS Code; người dùng có thể chọn **Python: Select Interpreter → ml_env**.
- Phiên terminal của người dùng cần tự kích hoạt `ml_env`; việc kích hoạt trong phiên kiểm tra không đổi môi trường của terminal khác.
- Tiếp tục chốt phạm vi, nguồn tài liệu luật và tiêu chí đánh giá. Chương trình vẫn chưa có tính năng trả lời câu hỏi.

## 11/11/2026 — Khởi tạo dự án

### Đã làm

- Kiểm tra thư mục: ban đầu chỉ có `.vscode/settings.json`; giữ nguyên nội dung cấu hình Conda.
- Tạo `AGENTS.md` quy định đọc tài liệu trước khi sửa, làm từng nhiệm vụ, kiểm tra, không bịa luật hoặc số liệu và cập nhật tiến độ.
- Tạo môi trường `.venv` bằng `py -3.12 -m venv .venv`, dùng Python 3.12.0 đã có trên máy; chưa cài thêm thư viện bên ngoài.
- Tạo `app.py`, `src/`, `data/raw/`, `data/processed/` và `docs/`; các thư mục trống có `.gitkeep` để được giữ trong Git.
- Tạo chương trình dòng lệnh hiển thị tên, phạm vi dự kiến, trạng thái chưa triển khai và hướng dẫn thoát; không giả lập câu trả lời về luật.
- Tạo `README.md` hướng dẫn cài đặt, chạy trên PowerShell và giải thích cấu trúc; tạo `.gitignore` bỏ qua môi trường và bộ nhớ đệm Python.

### Kiểm tra đã thực hiện

- `.\.venv\Scripts\python.exe --version`: Python 3.12.0.
- `.\.venv\Scripts\python.exe -m pip --version`: pip 23.2.1 trong `.venv`.
- Kiểm tra `sys.executable` trỏ đến `.venv\Scripts\python.exe` và `sys.prefix != sys.base_prefix`: đạt.
- Chạy trực tiếp `'exit' | .\.venv\Scripts\python.exe app.py`: hiển thị đúng tên, phạm vi, hướng dẫn và lời chào kết thúc; mã thoát 0.
- Chạy chương trình qua tiến trình con cho các trường hợp: nhập câu hỏi rồi thoát, dòng trống rồi `QUIT` có khoảng trắng, lệnh `thoát`, hết đầu vào (EOF): tất cả đạt, mã thoát 0, không có lỗi trên stderr.
- Nhập câu hỏi chỉ nhận thông báo tính năng chưa triển khai, không sinh nội dung luật.
- Kiểm tra nhánh xử lý `KeyboardInterrupt` bằng mô phỏng trong Python: đạt. Chưa kiểm tra thao tác nhấn Ctrl+C trong terminal tương tác.
- Xác nhận đủ các thư mục yêu cầu và cấu hình Conda hiện có được giữ nguyên.
- Lần kiểm tra tự động đầu bị lỗi do PowerShell truyền mã kiểm tra chứa tiếng Việt qua pipe với mã hóa mặc định. Đã đặt `$OutputEncoding` và `PYTHONIOENCODING` là UTF-8 cho phiên kiểm tra rồi chạy lại thành công; không phải lỗi trong chương trình.

### Giới hạn hiện tại

- Chưa có dữ liệu luật hoặc nội dung giải thích đã xác minh.
- Chưa làm giao diện đồ họa, tìm kiếm hoặc tích hợp AI.

### Bước tiếp theo

1. Chốt phạm vi luật bóng đá sân 11 người và tiêu chí đánh giá của Project 1 với giảng viên.
2. Chọn tài liệu luật chính thức; ghi rõ nguồn, phiên bản, ngôn ngữ và điều kiện sử dụng trong `data/raw/` trước khi thu thập.
3. Sau khi chốt nguồn và phạm vi, lập kế hoạch phần việc cho 8 tuần và chuẩn bị bộ câu hỏi đánh giá có đáp án đối chiếu với nguồn.

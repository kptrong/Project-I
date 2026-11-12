# Chatbot giải thích luật bóng đá bằng tiếng Việt

Dự án Project 1 cá nhân tại HUST, dự kiến thực hiện trong 8 tuần, sử dụng Python.

## Trạng thái hiện tại

Đã khởi tạo chương trình dòng lệnh, bộ kiểm tra JSON, bản nguồn IFAB và dữ liệu Điều 11 ở bước 4. `data/processed/rules.json` có 4 mục diễn giải tiếng Việt; trạng thái duyệt hiện tại được ghi trong trường `review_status` của từng mục. Xem lịch sử kiểm tra và duyệt trong `docs/PROGRESS.md`. Chương trình **chưa trả lời câu hỏi về luật**, chưa có giao diện đồ họa, tìm kiếm hay tích hợp AI.

Phạm vi dự án: giải thích bằng tiếng Việt Điều 11–14 của luật bóng đá 11 người. Bộ dữ liệu đầu tiên chỉ gồm Điều 11 về việt vị; nguồn IFAB đã lưu là phiên bản **2026/27**, thu thập ngày **11/11/2026**. Xem mục tiêu và quy ước dữ liệu tại [docs/PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md).

## Cài đặt trên Windows (PowerShell)

Môi trường sử dụng từ nay là Conda `ml_env`. Mở PowerShell đã có lệnh `conda` (hoặc Anaconda PowerShell Prompt):

```powershell
cd D:\football-rules-chatbot
conda activate ml_env
python --version
python -c "import sys; print(sys.executable)"
```

Dự án đã chạy thành công với Python 3.11.16 trong `ml_env` trên máy hiện tại. Chương trình chỉ dùng thư viện chuẩn, chưa cần cài thêm gói.

Khi chuyển sang máy khác chưa có `ml_env`, sau khi cài Conda có thể tạo môi trường cho phần chương trình hiện tại bằng:

```powershell
conda create -n ml_env python=3.11
conda activate ml_env
```

Lệnh tạo môi trường trên chỉ phục vụ chương trình hiện tại, không sao chép các gói khác trong `ml_env` của máy cũ. `.venv` được tạo ở lần khởi tạo vẫn được giữ lại nhưng không cần dùng hoặc kích hoạt khi chạy bằng Conda.

## Chạy chương trình

Sau khi kích hoạt `ml_env`, chạy:

```powershell
python app.py
```

Nhập `thoat`, `thoát`, `exit`, `quit` hoặc `q` rồi nhấn Enter để thoát. Cũng có thể nhấn `Ctrl+C`. Trong Windows, kết thúc đầu vào bằng `Ctrl+Z` rồi Enter cũng sẽ thoát.

Nếu nhập câu hỏi, chương trình chỉ thông báo tính năng trả lời chưa được triển khai. Đây là hành vi dự kiến của bản khởi tạo, không phải câu trả lời về luật.

## Kiểm tra nhanh

```powershell
conda activate ml_env
python --version
python -c "import sys; print(sys.executable)"
'exit' | python app.py
```

Đường dẫn Python phải thuộc môi trường `ml_env`. Lệnh cuối cần in tên chương trình, phạm vi dự kiến, hướng dẫn thoát và lời chào kết thúc; không trả lời câu hỏi về luật.

## Cấu trúc và nhiệm vụ

```text
football-rules-chatbot/
├── app.py                  # Điểm chạy chương trình dòng lệnh
├── src/
│   ├── data_loader.py      # Đọc JSON và khung bài tập lọc mục đã duyệt
│   └── validate_data.py    # Kiểm tra cấu trúc dữ liệu JSON
├── data/
│   ├── examples/           # JSON minh họa, tách riêng khỏi dữ liệu luật thật
│   ├── raw/                # Tài liệu nguồn gốc và thông tin nguồn/phiên bản
│   └── processed/          # Dữ liệu sau xử lý từ tài liệu nguồn
├── docs/
│   ├── PROJECT_BRIEF.md    # Mục tiêu, phạm vi và quy ước dữ liệu
│   └── PROGRESS.md         # Tiến độ, kiểm tra và bước tiếp theo
├── tests/                  # Kiểm tra tự động cho bộ kiểm tra dữ liệu
├── AGENTS.md               # Quy tắc dành cho trợ lý khi sửa dự án
├── README.md               # Hướng dẫn cài đặt và chạy
├── .gitignore              # Bỏ qua môi trường và tệp Python sinh tự động
├── .venv/                  # Môi trường cũ được giữ lại, hiện không dùng
└── .vscode/settings.json   # Cấu hình VS Code đã có, được giữ nguyên
```

Các tệp `.gitkeep` giữ những thư mục chưa có nội dung trong Git, không chứa dữ liệu luật.

VS Code hiện được cấu hình dùng Conda. Dùng **Python: Select Interpreter** và chọn **ml_env**. Với terminal đang mở, chạy `conda activate ml_env` trước khi chạy chương trình. Môi trường Conda thường nằm ngoài thư mục dự án; không sao chép thư mục môi trường vào Git.

## Bước tiếp theo

Tự hoàn thành `filter_approved_rules(records)` theo [bài tập đọc dữ liệu](docs/DATA_LOADING_EXERCISE.md), rồi gửi code để được góp ý trước khi nối vào `app.py`. Trạng thái duyệt dữ liệu được hướng dẫn tại [docs/LAW11_REVIEW.md](docs/LAW11_REVIEW.md). Xem nhật ký tại `docs/PROGRESS.md`.

## Buổi 2: kiểm tra dữ liệu JSON

Hai tệp trong `data/examples/` là **dữ liệu minh họa**, không chứa luật thật và không dùng để trả lời câu hỏi. Văn bản, URL miền `.invalid` và phiên bản `ILLUSTRATION-ONLY-v1` chỉ là giá trị giữ chỗ. Tệp có hậu tố `invalid` cố ý chứa lỗi; lỗi trạng thái và phiên bản trong đó cũng phục vụ kiểm tra.

Chạy từ thư mục gốc của dự án trong PowerShell:

```powershell
conda activate ml_env
python src/validate_data.py data/examples/law11_illustration_valid.json
python src/validate_data.py data/examples/law11_illustration_invalid.json
```

- Tệp thứ nhất: 2 mục hợp lệ về cấu trúc, đều là `draft`, mã thoát `0`.
- Tệp thứ hai: 5 lỗi gồm 2 trường thiếu, 1 mã trùng, 1 trạng thái sai và 1 phiên bản khác mốc; mã thoát `1` là kết quả dự kiến.
- Không đọc được tệp hoặc JSON sai cú pháp: báo lỗi và trả mã thoát `2`.
- Có thể thay đường dẫn bằng tệp khác; đặt đường dẫn trong dấu ngoặc kép nếu có khoảng trắng. Tệp phải là danh sách JSON không rỗng với các trường nêu trong `docs/PROJECT_BRIEF.md`.

`draft` nghĩa là chờ bạn duyệt; chỉ đặt `approved` sau khi bạn đã kiểm tra nội dung với nguồn. Chương trình chỉ kiểm tra tên trạng thái, không tự duyệt hay xác minh nội dung luật.

Để phát hiện mã trùng, chương trình lưu từng `id` cùng vị trí đầu tiên vào một từ điển Python. Khi gặp lại cùng mã, nó báo mục hiện tại và mục đã dùng mã đó. Phiên bản được đối chiếu với mục đầu tiên có `edition` là chuỗi không rỗng.

Chạy các kiểm tra tự động bằng thư viện chuẩn (không cần cài thêm gói):

```powershell
python -m unittest discover -s tests -v
```

## Bước 3: bản nguồn Điều 11

Nguồn chính thức: [IFAB — Điều 11](https://www.theifab.com/laws/latest/offside/). Bản HTML thu thập ngày 11/11/2026 hiển thị phiên bản **2026/27**.

Mở [data/raw/IFAB_LAW11_SOURCE.md](data/raw/IFAB_LAW11_SOURCE.md) để xem tên tài liệu, URL, ngày thu thập, mã băm, bảng tiêu đề/vị trí bốn khoản 11.1–11.4 và cách tự đối chiếu khoản 11.3. Hồ sơ cũng ghi rõ cách xác minh phiên bản và những phần chưa xác minh. Chưa tạo diễn giải tiếng Việt hoặc JSON luật thật ở bước này.

## Bước 4: dữ liệu Điều 11 và duyệt nội dung

[data/processed/rules.json](data/processed/rules.json) chứa 4 mục tương ứng khoản 11.1–11.4, phiên bản `2026/27`. Mỗi mục giữ nguyên văn nguồn trong `original_text`, có diễn giải tiếng Việt trong `explanation_vi`, nguồn trỏ đến từng khoản và mã riêng `law11-001` đến `law11-004`. Các mục mới đều là `draft`.

```powershell
conda activate ml_env
python src/validate_data.py data/processed/rules.json
```

Xem [docs/LAW11_REVIEW.md](docs/LAW11_REVIEW.md) để hiểu cách chia đoạn, đối chiếu bản gốc và chuyển riêng các mục đã kiểm tra sang `approved`. Kiểm tra cấu trúc thành công không tự xác nhận nội dung luật hoặc duyệt thay người dùng.

## Bài tập đọc dữ liệu bằng Python

Đã tạo `src/data_loader.py`: `load_rules(path)` đọc JSON bằng UTF-8 và trả về danh sách từ điển; `filter_approved_rules(records)` còn TODO để bạn tự viết bằng vòng lặp `for`. Phần đọc chưa lọc theo trạng thái và chưa nối vào `app.py`.

```powershell
conda activate ml_env
python src/data_loader.py data/processed/rules.json
python -m unittest discover -s tests -p test_data_loader.py -v
```

Đọc giải thích dữ liệu đầu vào, ví dụ nhỏ, kết quả mong đợi và các lệnh thử JSON lỗi tại [docs/DATA_LOADING_EXERCISE.md](docs/DATA_LOADING_EXERCISE.md). Sau khi bạn gửi hàm đã viết, mới góp ý và tích hợp phần liệt kê mã, tiêu đề, nguồn của các mục đã duyệt vào ứng dụng.

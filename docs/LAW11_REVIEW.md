# Đối chiếu và duyệt dữ liệu Điều 11

## Bộ dữ liệu bước 4

Tệp [rules.json](../data/processed/rules.json) có 4 mục, tương ứng đầy đủ bốn khoản của Điều 11. Các mục đều được tạo ở trạng thái ban đầu `draft`; trạng thái hiện tại được ghi trong `review_status` của từng mục, lịch sử duyệt được ghi trong `docs/PROGRESS.md`.

Nguồn là bản HTML IFAB tiếng Anh phiên bản **2026/27**, lưu ngày **11/11/2026**, không lấy lại nội dung từ URL `latest` trong bước này. Hồ sơ nguồn và mã SHA-256 nằm tại [IFAB_LAW11_SOURCE.md](../data/raw/IFAB_LAW11_SOURCE.md).

| ID | Khoản | Tiêu đề nguồn | Vị trí trong bản HTML |
|---|---|---|---|
| `law11-001` | 11.1 | Offside position | Dòng 637–663, `article#offside-position` |
| `law11-002` | 11.2 | Offside offence | Dòng 663–722, `article#offside-offence` |
| `law11-003` | 11.3 | No offence | Dòng 722–742, `article#no-offence` |
| `law11-004` | 11.4 | Offences and sanctions | Dòng 742–760, `article#offences-and-sanctions` |

`section` giữ số khoản chính thức, `title` là tiêu đề tiếng Việt do dự án biên soạn. `source_url` trỏ đến đúng ID của khoản trên IFAB; `edition` là `2026/27`.

`original_text` giữ nguyên câu chữ và dấu câu trong phần nội dung của khoản, kể cả chú thích. Khi chuyển HTML sang chuỗi JSON, chỉ giải mã ký tự HTML, bỏ thẻ trình bày, chuyển đoạn thành xuống dòng và danh sách thành dấu `-` với thụt lề. Tiêu đề khoản được truy xuất bằng `section` và bảng trên. Các ký tự `\n` trong mã JSON biểu diễn xuống dòng, không phải chữ trong nguồn. Không lấy thanh điều hướng hoặc FAQs vào nội dung luật.

## Vì sao chia theo toàn bộ khoản?

Mỗi khoản là một đơn vị chính thức có thể truy lại trên trang nguồn. Khoản 11.2 được giữ nguyên một mục vì các nhóm hành vi, mốc thời điểm, định nghĩa chủ động chơi bóng/cứu thua, ngoại lệ và trình tự xử lý lỗi cần được đọc cùng nhau. Khoản 11.4 cũng giữ nguyên các điều kiện về cầu thủ ngoài sân và thời điểm chấm dứt cách xác định vị trí. Chưa chia những nội dung này thành các đoạn nhỏ dễ mất điều kiện đi kèm.

Ví dụ `law11-003`: giữ câu dẫn và cả ba mục danh sách của khoản 11.3 trong cùng một mục. Cụm `directly` trong câu dẫn áp dụng cho toàn bộ danh sách. Nếu tách từng gạch đầu dòng mà bỏ câu dẫn, dữ liệu sẽ mất điều kiện nhận bóng trực tiếp. Mục kết thúc trước khoản 11.4 vì nội dung chuyển sang xử phạt và các tình huống cầu thủ ngoài sân.

## Quy trình kiểm tra một mục

1. Trong VS Code, mở `data/processed/rules.json` và tìm đúng `id`, ví dụ `law11-003`. Đọc `section`, `source_url`, `edition` trước khi kiểm tra nội dung.
2. Mở bản [HTML đã lưu](../data/raw/ifab_law11_source_2026-11-11.html) cạnh bên. Tìm `id="no-offence"` cho khoản 11.3; dùng bảng trên để tìm các khoản khác. Nếu dùng URL online, kiểm tra phiên bản vẫn là `2026/27`; khi khác phiên bản, đối chiếu với bản lưu trước.
3. So toàn bộ `original_text` với nội dung khoản: đủ câu, danh sách, chú thích, dấu câu và không lẫn FAQs. Khác cách xuống dòng/dấu đầu dòng do chuyển từ HTML không có nghĩa là khác câu chữ.
4. Đọc `explanation_vi` và đối chiếu từng ý với bản gốc. Kiểm tra chủ thể, mốc thời điểm, điều kiện kết hợp, ngoại lệ và cách xử lý. Không chỉ kiểm tra xem tiếng Việt có dễ đọc hay không.
5. Với `law11-003`, kiểm tra rằng cả ba trường hợp nguồn đều có trong diễn giải và điều kiện **nhận bóng trực tiếp** vẫn áp dụng cho cả ba. Không mở rộng ngoại lệ sang tình huống khác.
6. Nếu thiếu hoặc sai ý, sửa `explanation_vi` và giữ `draft` để kiểm tra lại. Chỉ đổi mục bạn đã đối chiếu đầy đủ sang `approved`.

Gợi ý các điểm cần chú ý ở những mục còn lại:

| Mục | Các điều kiện cần đối chiếu kỹ |
|---|---|
| `law11-001` | Chỉ có vị trí việt vị chưa phải lỗi; hai điều kiện vị trí đồng thời; đường giữa sân; phần cơ thể được xét; ngang hàng |
| `law11-002` | Ba nhóm hành vi; bốn dạng can thiệp đối phương; chú thích thời điểm tiếp xúc bóng; chủ động chơi bóng và ngoại lệ cứu thua; các dấu hiệu kiểm soát; ba tình huống trình tự lỗi |
| `law11-004` | Vị trí phạt gián tiếp; hai mốc chấm dứt cách xét cầu thủ ngoài sân; các điều kiện cảnh cáo; ngoại lệ khi cầu thủ ở trong cầu môn |

Để in rõ một mục ra terminal, không cần đọc các ký tự `\n` trên một dòng JSON, chạy từ thư mục dự án sau khi kích hoạt `ml_env`:

```powershell
python -c "import json; from pathlib import Path; items=json.loads(Path('data/processed/rules.json').read_text(encoding='utf-8')); item=next(x for x in items if x['id']=='law11-003'); print(item['original_text']); print(); print(item['explanation_vi'])"
```

## Đổi trạng thái sau khi kiểm tra

Trong **đúng đối tượng có ID đã kiểm tra**, thay dòng:

```json
"review_status": "draft"
```

bằng:

```json
"review_status": "approved"
```

Giữ nguyên trạng thái của các mục chưa kiểm tra. Lưu tệp, rồi chạy:

```powershell
conda activate ml_env
python src/validate_data.py data/processed/rules.json
```

Ghi ID và ngày bạn đã duyệt vào `docs/PROGRESS.md`, ví dụ: `Đã đối chiếu và duyệt law11-003, phiên bản 2026/27, ngày ...`. Nếu sửa nội dung một mục đã duyệt, đưa mục đó về `draft` và đối chiếu lại trước khi duyệt tiếp.

Bộ kiểm tra chỉ kiểm tra cấu trúc và giá trị trạng thái, không chứng minh bản diễn giải đúng. Việc hoàn thành bước thu thập nguồn không đồng nghĩa toàn bộ bản diễn giải mới đã được duyệt.

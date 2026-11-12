# Hồ sơ nguồn Điều 11 — Việt vị

## Thông tin nguồn đã xác minh

| Thuộc tính | Giá trị |
|---|---|
| Tổ chức phát hành | The International Football Association Board (The IFAB) |
| Bộ tài liệu | Laws of the Game |
| Tên trang hiển thị | Law 11 — Offside |
| Phiên bản nguồn | **2026/27** |
| Ngôn ngữ nguồn | Tiếng Anh |
| URL được yêu cầu | https://www.theifab.com/laws/latest/offside/ |
| URL cuối sau khi tải | https://www.theifab.com/laws/latest/offside/ |
| Ngày thu thập | **11/11/2026**, múi giờ Asia/Bangkok (UTC+07:00) |
| Kết quả HTTP | `200 OK`, `Content-Type: text/html; charset=UTF-8` |
| Bản nguồn lưu tại máy | [ifab_law11_source_2026-11-11.html](ifab_law11_source_2026-11-11.html) |
| Thông tin phản hồi HTTP | [ifab_law11_source_2026-11-11.http.txt](ifab_law11_source_2026-11-11.http.txt) |
| Kích thước bản HTML | `317442` byte |
| SHA-256 của bản HTML | `2a378103e19124b3e4e88f3fd1f3151e2b4f0d70c597934c5dbaf7b541e3d3c1` |
| Trạng thái | Đã xác minh nguồn, phiên bản hiển thị và sự hiện diện của bốn khoản; **chưa được người dùng đối chiếu thủ công** |

HTML được tải trực tiếp từ IFAB và giữ nguyên byte, không dịch hoặc biên tập nội dung. Đây là bản lưu của trang web, không phải PDF hay bản lưu đầy đủ mọi tệp CSS/JavaScript/hình ảnh. Trang còn chứa thanh điều hướng và FAQs; phạm vi thu thập cho bước này là bốn khối `article` của Điều 11 bên dưới, không phải các câu hỏi FAQs.

## Đối chiếu phiên bản với tài liệu dự án

Trước bước 3, `README.md` và `docs/PROJECT_BRIEF.md` đều ghi chưa chọn phiên bản luật thật. Các chuỗi `ILLUSTRATION-ONLY-v1` và `ILLUSTRATION-ONLY-v2` chỉ nằm trong dữ liệu minh họa, không phải phiên bản IFAB và không được dùng làm mốc so sánh với nguồn thật.

Tại ngày thu thập, HTML từ URL được yêu cầu có nút phiên bản đang chọn là `2026/27` (lớp `cursor-default`); `2025/26` là lựa chọn khác. Do đó, ghi nhận **2026/27** làm phiên bản nguồn cho bộ dữ liệu Điều 11 đầu tiên và cập nhật tài liệu dự án tương ứng. Đây là xác minh phiên bản của trang đã tải, không phải kết luận về phiên bản áp dụng cho mọi giải đấu.

Không có URL cố định theo phiên bản nào được xác minh thành công trong buổi này. Một lần thử truy cập đường dẫn `/laws/2026-27/offside/` qua công cụ web không mở được; không coi đường dẫn đó là nguồn đã xác minh.

## Bảng truy lại bốn khoản

Tiêu đề được giữ theo bản tiếng Anh. Các dòng tính từ 1 trong **bản HTML có mã SHA-256 nêu trên**, từ thẻ mở đến thẻ đóng `article`. Dòng đầu/cuối của hai khoản có thể trùng nhau vì HTML đặt các thẻ trên cùng dòng.

| Khoản | Tiêu đề gốc | Vị trí trong bản HTML lưu tại máy | Vị trí trên trang IFAB |
|---|---|---|---|
| 11.1 | Offside position | Dòng 637–663; `article#offside-position` | [Mở khoản 11.1](https://www.theifab.com/laws/latest/offside/#offside-position) |
| 11.2 | Offside offence | Dòng 663–722; `article#offside-offence` | [Mở khoản 11.2](https://www.theifab.com/laws/latest/offside/#offside-offence) |
| 11.3 | No offence | Dòng 722–742; `article#no-offence` | [Mở khoản 11.3](https://www.theifab.com/laws/latest/offside/#no-offence) |
| 11.4 | Offences and sanctions | Dòng 742–760; `article#offences-and-sanctions` | [Mở khoản 11.4](https://www.theifab.com/laws/latest/offside/#offences-and-sanctions) |

Các mã fragment sau `#` được đối chiếu với thuộc tính `id` thực tế trong HTML. Link online dùng `latest`, vì vậy khi mở lại vẫn cần kiểm tra phiên bản; bảng dòng chỉ áp dụng cho bản lưu này.

## Vì sao phải lưu cả phiên bản và URL?

URL cho biết nơi lấy tài liệu; phiên bản cho biết bộ luật nào đã được sử dụng. URL chứa `latest` có thể giữ nguyên trong khi nội dung chuyển sang phiên bản mới. Nếu chỉ lưu URL, sau này bạn có thể mở đúng địa chỉ nhưng đọc một bản khác với bản đã dùng để làm dữ liệu.

Ngày thu thập xác định thời điểm lấy nguồn. Bản HTML giữ nội dung đã nhận tại thời điểm đó; SHA-256 giúp kiểm tra bản lưu có bị thay đổi byte hay không. Mã băm không tự chứng minh nội dung luật đúng hoặc việc người dùng đã duyệt.

## Tự kiểm tra thủ công khoản 11.3

1. Mở link khoản 11.3 trong bảng trên. Kiểm tra tên miền `www.theifab.com`, phiên bản đang chọn là **2026/27**, rồi tìm đúng khoản **11.3** và tiêu đề trong bảng. Nếu link không tự cuộn, dùng `Ctrl+F` tìm tiêu đề hoặc cuộn đến Điều 11.
2. Trong VS Code, mở `data/raw/ifab_law11_source_2026-11-11.html`. Nhấn `Ctrl+G`, nhập `722` để đến khu vực đầu khoản; dùng `Ctrl+F` tìm `id="no-offence"` để xác định đúng thẻ mở. Thanh điều hướng cũng có thể lặp tiêu đề, nên cần tìm đúng `article` này.
3. Đối chiếu toàn bộ phần nội dung trong khối `article` với trang online: tiêu đề, câu dẫn và **3 mục trong danh sách**. Đọc đến thẻ `</article>` trước khối `article` của khoản 11.4; chưa dịch hoặc viết lời giải thích.
4. Nếu muốn xem bản lưu trong trình duyệt, mở tệp HTML bằng trình duyệt và tìm tiêu đề. Một số phần trình bày/tương tác có thể phụ thuộc tài nguyên online; bản mã HTML trong VS Code là phương án đối chiếu dự phòng.
5. Ghi nhận kết quả đối chiếu và ngày kiểm tra vào `docs/PROGRESS.md`. Nếu có khác biệt, kiểm tra lại phiên bản trước; giữ nguyên bản lưu và lưu bản mới dưới tên khác để so sánh. Chưa gán trạng thái `approved` cho nội dung chưa kiểm tra.

Kiểm tra mã băm trên PowerShell:

```powershell
Get-FileHash .\data\raw\ifab_law11_source_2026-11-11.html -Algorithm SHA256
```

So sánh với mã ở đầu hồ sơ; chữ hoa và chữ thường trong cách hiển thị mã băm là tương đương.

## Phạm vi đã kiểm tra và phần chưa làm

- Đã mở được trang IFAB bằng công cụ web và tải trực tiếp qua HTTPS với HTTP 200.
- Đã phân tích bản HTML lưu tại máy bằng thư viện chuẩn Python trong Conda `ml_env`: đủ bốn khối `article`, đúng thứ tự, đúng tiêu đề, có nội dung và thẻ đóng; khối 11.3 chứa 3 mục danh sách.
- Đã kiểm tra nút phiên bản đang chọn, kích thước tệp, mã băm và các dòng bắt đầu/kết thúc cho bảng truy xuất.
- Bản lưu chứa nội dung được IFAB bảo lưu quyền; buổi này lưu nguồn để học tập và đối chiếu nội bộ. Chưa xác minh quyền tái phân phối hoặc công bố lại toàn văn cho sản phẩm; cần làm rõ trước khi công bố dữ liệu.
- Chưa dịch, chưa soạn diễn giải tiếng Việt, chưa tạo JSON luật thật, chưa xác nhận nội dung ở trạng thái `approved`. Những phần này thuộc bước 4 sau khi người dùng đối chiếu nguồn.

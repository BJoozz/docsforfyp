# Bộ ảnh/clip cho CA Presentation

Bản gọn, chụp từ app thật ngày **15–16/11/2026**: **6 ảnh chính + 2 ảnh dự phòng + 2 MP4**. Không có GIF. App ở `main`, commit `346e84b`; docs đã pull tới `99990d0` trước khi chuẩn bị.

**Mở [START_HERE.html](START_HERE.html) để xem và chọn ngay.** Trang này chạy tại máy, không cần server. Bấm ảnh để mở bản đầy đủ. Khi đưa lên slide, dùng PNG/MP4 gốc trong các thư mục, không chụp lại trang xem nhanh.

| Thư mục | Dùng để làm gì |
| --- | --- |
| `01_main_slides` | 6 ảnh đã chọn, tên có số thứ tự |
| `02_short_clips` | Graph 7,8 giây; Sorting 10,4 giây; MP4 H.264, không âm thanh |
| `03_backup` | Hover sang A ở cùng frame cuối; cây sau Apply |
| `04_reproduce` | Input, thao tác, script và log kiểm chứng; không cần mở khi ráp slide |

## Nên chọn gì

| Ảnh | Ý cần nói, không phải bài giảng thuật toán |
| --- | --- |
| `01_editor_entry_points.png` | Bắt đầu từ input của mình; Graph Editor và Tree Editor có vùng riêng |
| `02_dijkstra_decision.png` | “1 + 1 < 4 · update” giải thích quyết định ngay trên đỉnh A, khớp Status và pseudocode |
| `03_dijkstra_final_path_t.png` | Chạy xong vẫn khám phá đường đi S → B → A → T, tổng 4 |
| `04_tree_insert_preview.png` | Insert(5) là bản xem thử; Apply mới thay cây gốc |
| `05_sorting_compare.png` | Bubble/Selection, cùng 12 số, cùng đồng hồ; ở ảnh cả hai đang tại operation 48 |
| `06_v10_layout.png` | Status được kéo xuống dưới canvas; run vẫn ở frame 21/21 |

Đây là **asset lựa chọn**, không phải sáu slide bắt buộc. Nếu thiếu thời gian, dùng ảnh 02, 04, 05 cho phần Algorithm Visualizers; ảnh 01 cho mở đầu demo; ảnh 06 cho phần shared shell. Ảnh 03 hoặc cặp 03 + ảnh backup A dùng khi giải thích khám phá kết quả.

## Hai clip

- **`01_graph_paused_step.mp4` (7,8s):** frame 11 đứng yên nhưng streak/glow tiếp tục chạy; bấm Next sang frame 12 hiện ghi chú; kéo B mà frame vẫn là 12. Đây là pause + giải thích bước + tách layout khỏi run trong một clip.
- **`02_sorting_shared_clock.mp4` (10,4s):** hai thuật toán chạy trên cùng input, cùng dừng ở operation 48, rồi chạy tiếp. Cuối clip có thao tác Last để tới kết quả; **không dùng thời gian clip để kết luận thuật toán nào nhanh hơn**.

Chỉ cần phát **một lần** ở đúng chỗ. Có thể dùng cả hai làm phương án dự phòng cho demo trực tiếp; không cộng thêm một vòng trình diễn vào ngân sách 4–5 phút. Tổng video khoảng 18 giây.

## Đã kiểm và chưa kiểm

Đã mở app, kiểm tra font, đọc trạng thái thực trong browser, chụp ảnh, xuất và giải mã toàn bộ hai MP4, xem các frame mẫu. Các phiên capture cuối không có page error. Đã kiểm: frame dừng không tiến; note/Status cùng phép tính; kéo không đổi frame; hover A/T không đổi frame; preview chưa sửa text cây, Apply mới thêm `6 5`; kéo Status xuống bottom giữ frame.

Chưa chạy lại toàn bộ test suite, chưa rehearsal presentation qua Zoom, chưa kiểm chứng hiệu quả học tập. Ảnh là bản hiện tại, **không phải early prototypes**. Chưa làm deck hoặc quay mọi thuật toán. Hình lịch sử trong report được giữ riêng cùng revision cũ.

[Captions và câu nói ngắn](CAPTIONS_AND_CUES.md) · [Nguồn và trạng thái từng asset](manifest.json) · [Tái tạo](04_reproduce/README.md)

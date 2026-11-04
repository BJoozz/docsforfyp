# Bản tiếng Việt của báo cáo CA VisuAlgo+

**Cập nhật nguồn ngày 4/11/2026:** `full.tex` và `summary.tex` đã đồng bộ với bản Anh về thử nghiệm V10 tuần 10 và floating text. Hai PDF đã được biên dịch lại từ nguồn này ngày 4/11/2026 bằng MiKTeX 25.12 (XeLaTeX). Lệnh `\page` trong `style.tex` chỉ ngắt trang khi trang hiện tại đã đầy khoảng ba phần tư, thay cho `\clearpage` cứng từng để lại trang gần trống.

Chuẩn bị ngày 4/11/2026 để Bao đọc và rà soát.

## Hai tài liệu

- `VisuAlgo_CA_Report_VI.pdf`: bản dịch đầy đủ, biên dịch từ `full.tex` đã đồng bộ với bản Anh trong cùng phiên bản.
- `VisuAlgo_CA_Summary_VI.pdf`: bản tóm tắt tiếng Việt để đọc nhanh; nguồn `summary.tex`.

Bản dịch giữ đầy đủ các phần nội dung, bảng, số liệu, hình và mức độ khẳng định của bản gốc. Có thêm mục lục và chú giải thuật ngữ để đọc thuận tiện. Tên công trình trong bibliography và chữ trên ảnh giao diện được giữ nguyên; chú thích và nhãn sơ đồ đã dịch. Phần kế hoạch tương lai vẫn là đề xuất, không phải công việc đã hoàn thành.

## Biên dịch

Chạy từ thư mục `report/vi/`, dùng **XeLaTeX** (font Unicode DejaVu Serif/Sans/Mono):

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=VisuAlgo_CA_Report_VI full.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=VisuAlgo_CA_Summary_VI summary.tex
```

Hai tài liệu dùng chung `style.tex`. Bản đầy đủ dùng hình ở `../figures/` và bibliography `../references.bib`. Muốn biên dịch riêng trên Overleaf, tải cả thư mục `report/`; giữ nguyên cấu trúc và chọn XeLaTeX. Nếu môi trường không giải quyết đường dẫn tương đối từ thư mục `vi`, biên dịch từ chính `vi/` bằng các lệnh trên.

## Đồng bộ khi sửa

Nguồn đối chiếu chính là bản tiếng Anh. Khi sửa `report/main.tex`, cập nhật phần tương ứng trong bản dịch và bản tóm tắt, sau đó biên dịch lại PDF. Ghi rõ commit nguồn mới nếu bản dịch đã được đối chiếu với một phiên bản tiếng Anh khác.

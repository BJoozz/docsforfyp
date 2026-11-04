# Review tổng hợp CA Report — VisuAlgo+ (CP4101)

**Ngày:** 2026-11-04, ~12:15 SGT. **Hạn nộp:** hôm nay 17:00 SGT (softcopy cho A/P Halim **và** Main Evaluator).
**Bản được review:** `report/main.tex` + `report/VisuAlgo_CA_Report_Draft.pdf` tại commit `f399626` (16 trang; macro `\page` có điều kiện đã được commit trong `f399626`). Build lại trên cloud (TeX Live) cho đúng 16 trang, 0 undefined reference, 0 overfull box.
**Nguồn:** kết quả 15 finder + 15 verifier trong [`fyp-audit-panel-results.json`](fyp-audit-panel-results.json) và [`FYP_AUDIT_HANDOFF.md`](FYP_AUDIT_HANDOFF.md). Bản này thay cho agent synthesis bị lỗi. **Không chạy lại panel.** Kiểm tra thêm trong phiên này: xem trực tiếp F6 và F1 (khớp với finding), build lại PDF.

**Nhãn trạng thái dùng trong file:**
- **XÁC NHẬN** — verifier thứ hai đã tái hiện bằng chứng (122 finding gốc). Không có nghĩa là Bao đã đồng ý.
- **CHƯA KIỂM CHỨNG** — 34 finding do verifier *thêm vào* (`*-added-*`, chưa có agent thứ ba kiểm tra) + 9 finding *UNCERTAIN* (cần Bao trả lời). Riêng `floating-added-2`/`crit-technical-added-1` (hình 6) và một phần `contributions-added-1` (dòng credit trên F1 ghi "built by Kerk and Bao") đã được tôi xem ảnh và xác nhận.
- **BÁC BỎ** — 11 finding bị verifier bác (mục 3.4); không nêu lại.

Trọng số dùng bên dưới là **trọng số chính thức** (CA Evaluation Form 2026-02), không phải trọng số trong brief: Supervisor = Understanding 30 / Technical 40 / Effort & Initiative 20 / Report 10; Main Evaluator = Understanding 30 / Technical 40 / Project & Resource Mgmt 10 / Report & Discussion 20. Literature review tính trong *Understanding*.

---

## 1. Đánh giá tổng thể

Báo cáo **có nội dung kỹ thuật thật và trung thực**: mọi con số kỹ thuật kiểm tra với code `662e7b3` đều khớp (3,273 unit test, 151 browser case, 11 thuật toán graph, 7 tree workspace, 8 sorting, 2,048/60,000 operation, 4,000 thao tác layout ngẫu nhiên...), giới hạn được nêu rõ. Nhưng **chưa sẵn sàng nộp nguyên trạng** vì: (1) còn chữ "Draft" ở 4 chỗ; (2) 16 trang so với "10–15 pages" chính thức; (3) đoạn Week 10 → floating text (thêm ngày 4/11) không theo kỷ luật bằng chứng của phần còn lại — không có ngày, và còn trích dẫn [8, 6], là nguồn nói *không có* user evaluation; (4) có ~12 câu sai lệch nhỏ so với code/hình. Tất cả sửa được trong 2–3 giờ, không cần viết lại.

| Tiêu chí (trọng số chính thức) | Nhận định một dòng |
|---|---|
| Understanding of the problem (30%, cả hai form; gồm literature) | **Trung bình.** Objectives liệt kê rõ, nhận thức giới hạn rất tốt; nhưng thiếu problem statement, objectives không đo được, literature mỏng (3 bài peer-reviewed, mới nhất 2012). |
| Technical Achievement (40%) | **Khá–tốt về thực chất, bị "undersell" khi trình bày.** Mọi claim đúng; thiếu câu contribution rõ ràng, thiếu WHY/alternatives, test chưa gắn với rủi ro. Vài câu sai nhỏ (timing note, hình 6, floor 360×320, 700 inputs). |
| Effort & Initiative (20%, Supervisor) | **Mạnh.** Khối lượng Sem 1 lớn và có dấu ngày (4 repo standalone → V10 → one app → 6 thuật toán mới → step notes). |
| Project & Resource Mgmt (10%, Main Evaluator) | **Trung bình.** Table 5 bỏ qua hạn chính thức 7/4/2027 và buổi CA presentation; không kể thách thức như vấn đề đã giải quyết; trial Week 10 thiếu ngày/số người/consent. |
| Report (10%) / Report & Discussion (20%) | **Trung bình–khá.** Cấu trúc khớp guideline; nhưng 16 trang, caveat lặp ~13 lần, chữ trong screenshot in ra ~3–4 pt, nhiều hình/bảng không được nhắc trong text, viết tắt chưa giải thích, [6]–[8] là repo private. |
| Accuracy & Evidence | **Tốt ở phần cũ, yếu ở phần thêm 4/11.** Phần Week 10, survey V2/V7 và các câu về supervisor cần chỉnh theo câu trả lời của Bao. |

---

## 2. Top 5 việc phải sửa trước khi nộp

1. **Xóa mọi dấu "Draft"** — cover `DRAFT FOR REVIEW` (`main.tex:48`), header `CP4101 CA Report | Draft` (l.27), PDF title metadata (l.13), tên file `VisuAlgo_CA_Report_Draft.pdf` → `VisuAlgo_CA_Report.pdf`. *(Critical; official-OFF-1, crit-report-QR-1)*
2. **Sửa đoạn Week 10 / floating text** (p.1, 4, 11, 13): ghi ngày theo câu trả lời của Bao; bỏ `[8, 6]` khỏi câu "Following the Week 10 trial…"; nếu buổi trial không chắc trước 23/10 thì đổi thành "during Week 10, alongside the trial"; thêm 1 câu consent/ethics; "refinements" → số ít nếu chỉ có floating text. *(timeline-TL-1/2, floating-FT-1/2, crit-accuracy-ACC-2/14/15, qa-QA-1/2, crit-management-PM-2/6)*
3. **Sửa các câu sai so với code/hình/nguồn** (không cần Bao trả lời): timing note (p.11), caption hình 6 (p.10), caption hình 9 + câu catalogue (p.12), floor 360×320 (p.7), lịch sử sorting "unbounded" (p.6), 700 inputs (p.9), End node (p.9), "V10 wins" (p.4), hình 1–2 (p.5, 7), "Halim 2012 present VisuAlgo" + URL OpenDSA (p.3, 15), 266 CI runs (p.12), "developer checks" (p.13). Chi tiết ở mục 3.
4. **Đưa về ≤ 15 trang (tính cả cover + references)** và xử lý [6]–[8] private: xóa 2 ghi chú p.16 (riêng việc này → 15 trang), gộp caveat lặp (→ 14 trang); giữ một câu nguồn ngắn ở cuối References; [6]–[8] ghi rõ cách truy cập theo lựa chọn của Bao. *(crit-report-QR-2/3/8, official-OFF-2, literature-LIT-1, crit-literature-LR-5, qa-QA-5)*
5. **Sửa đoạn survey V2/V7 + định nghĩa V10 + plan theo lịch chính thức**: survey của Kerk → Kerk và Bao chọn V2, V7 trong 9 layout của wireframe Kerk → Bao build cả hai (20–27/9) → V10 (Bao đề xuất 16/10). Table 5 thêm CA presentation (Reading Week 14–20/11/2026), final report **Wed 7/4/2027 17:00**, presentation 19–23/4/2027 (tentative). *(contributions-CONTRIB-1/2, crit-accuracy-ACC-4, qa-QA-3/7, crit-technical-TA-4, official-OFF-3, crit-management-PM-1)*

Nếu còn thời gian (khuyến nghị, tăng điểm Understanding 30%): thêm problem statement ~120 từ (dựa trên 3 design questions sẵn có) và nâng cấp §2 bằng 4–5 nguồn đã kiểm metadata (mục 5).

---

## 3. Findings đã khử trùng lặp

Định dạng: **[trang, §] vấn đề → cách sửa (cơ sở; ID)**. Trang theo PDF 16 trang hiện tại.

### 3.1 Critical

- **[p.1–16, cover/header/metadata/tên file]** Bản nộp vẫn ghi "Draft" ở 4 chỗ → xóa cả 4, đổi tên file. (VERIFIED; `official-OFF-1`, `crit-report-QR-1`) — XÁC NHẬN.

### 3.2 Important

- **[p.1/4/11/13; Abstract, §3.1, §4.8, §6.1]** Trial Week 10 không có ngày nhưng được viết là *nguyên nhân* của floating text. Bản ghi duy nhất có ngày là yêu cầu của Bao **23/10** (TP-34; PR #29 mở 13:36 SGT), Week 10 = 19–23/10; floating text lên Pages lần đầu 25/10. Câu này còn trích `[8, 6]` (snapshot `67ce56c` ghi "no user evaluation") → ghi ngày theo Bao; trích addendum hoặc không trích; nếu không chắc thì làm mềm. (VERIFIED; `timeline-TL-1`, `timeline-TL-2`, `floating-FT-2`, `literature-LIT-6`, `crit-accuracy-ACC-2`, `crit-accuracy-ACC-14`; UNCERTAIN `floating-FT-1`, `crit-accuracy-ACC-1`)
- **[p.4, 13; §3.1, §6.1, §6.3, Table 4]** Trial thiếu số người, build, nội dung test, quan sát cụ thể; có quay video nhưng không nói consent/lưu trữ; nghiên cứu 6–10 sinh viên chưa có bước ethics → thêm số liệu Bao cung cấp + 1 câu consent + "ethics review confirmed with supervisor before recruitment". (VERIFIED/INFERENCE; `crit-management-PM-2`, `qa-QA-1`, `qa-QA-2`, `crit-management-PM-6`, `official-added-1`; UNCERTAIN `crit-accuracy-ACC-15`)
- **[p.4, §3.1 ¶2]** Survey bị mô tả sai: theo câu trả lời Q8 của Bao, survey có trước, sau đó Kerk và Bao **chọn V2 và V7 trong 9 layout của wireframe Kerk** (wireframe không được credit); "We also implemented both variants" làm giảm phần của Bao (cả 3 PR V2/V7 là của Bao); "V10" không được định nghĩa; hai nghĩa của "V2" (Graph Visualizer V2 và layout V2) trên cùng trang → viết lại 3 câu (bản nháp ở mục 7). (DOCUMENTED/VERIFIED; `contributions-CONTRIB-1/2`, `crit-accuracy-ACC-4`, `timeline-TL-3`, `qa-QA-3`, `qa-QA-7`, `crit-technical-TA-4`, `crit-problem-added-1`, `crit-management-added-1`, `contributions-added-2`, `crit-technical-added-5`)
- **[p.2, 4, 11, 16]** Câu về supervisor (đồng ý V10; "canvas-focused educational goal") chỉ dựa trên lời kể của Bao 3–4/11, và chỉ được ghi nguồn ở chữ nhỏ p.16; p.2 viết "A/P Steven Halim", p.11 viết "Prof. Halim" → gắn nhãn ngay trong câu ("by my account"), thống nhất "A/P Halim". (DOCUMENTED; `crit-accuracy-ACC-5`, `crit-report-QR-7`, `crit-report-QR-12`; UNCERTAIN `contributions-CONTRIB-3`)
- **[p.15–16, refs [6]–[8]]** 13/20 lệnh cite trỏ vào evidence pack của chính mình, trong repo **private** (`BJoozz/docsforfyp`); trông như ấn phẩm; evaluator mở link sẽ bị 404; báo cáo không cho cách nào xem app → chọn một cách truy cập (câu hỏi Q6–Q7), đổi tên mục thành "Project records", giảm số cite trong body. (VERIFIED; `literature-LIT-1`, `crit-literature-LR-5`, `crit-report-QR-8`, `qa-QA-5`, `counts-added-1`, `floating-added-1`, `crit-accuracy-added-1`, `official-added-3`, `crit-report-added-2`)
- **[toàn bộ, p.16]** 16 trang; guideline: "a short report (10–15 pages)", không nói cover/references có tính hay không → đọc chặt: ≤ 15 trang kể cả cover. Xóa p.16 (đã thử: 15 trang), gộp caveat (đã thử: 14 trang). (VERIFIED; `crit-report-QR-2`, `official-OFF-2`)
- **[p.2–3, §1.1, §1.3, §2.3]** Không có problem statement; 3 design questions (rất tốt) nằm cuối §2.3, không nối với objectives; objectives không có tiêu chí thành công; objective 1 (chọn công nghệ) không được lập luận như một lựa chọn; objective 3 mất chữ "redesign" nên floating text không gắn với objective nào → thêm problem statement ngắn, đưa 3 câu hỏi lên §1, khôi phục "redesign", thêm 1 câu "why React Flow". (VERIFIED; `crit-problem-PU-1/2/3`, `official-OFF-7`, `contributions-CONTRIB-5`, `qa-QA-9`, `literature-LIT-8`)
- **[p.3, §2; p.15]** Literature mỏng, cũ, mang tính tóm tắt: 3 bài peer-reviewed (2002–2012), không so sánh với hệ thống nào khác ngoài trang web OpenDSA; không cite visualgo.net; "Halim et al. [2] present VisuAlgo" sai (bài 2012 chưa dùng tên VisuAlgo; Halim 2015 mới dùng); V10 mô phỏng VS Code editor groups nhưng không credit; URL OpenDSA lỗi TLS → xem mục 5 (thêm nguồn). (VERIFIED; `literature-LIT-2/3/4/5/7`, `crit-literature-LR-1/2/3/4/6`, `crit-problem-PU-8`, `official-OFF-5`, `literature-added-1/2/3`)
- **[p.11, §4.8 timing]** Sai 3 chỗ: ngưỡng 200 ms áp cho *thời gian hiển thị còn lại* (= 90% step interval), không phải interval; note không có "configured delay" (delayMs = 0); note chỉ hiện khi đi **tiến** một bước (Next/autoplay), không phải "manually inspected" → thay bằng câu đúng (mục 7). (VERIFIED trong code; `floating-FT-4`, `counts-NUM-1`, `crit-accuracy-ACC-18`, `crit-technical-TA-11`)
- **[p.12, §5 + Figure 9]** "30 cards, 12 open; eight full and four partial" trộn 2 thẻ Editor của VisuAlgo+ với module của visualgo.net; "full" chưa định nghĩa (đếm theo tên thuật toán). Caption hình 9 nói có "clearly marked future topics" nhưng ảnh 1440×900 **không có thẻ "Coming soon" nào** (tôi đã xem F1) → viết lại câu (mục 7); dùng crop từ `figures/F1-home-catalogue-fullpage.png` hoặc sửa caption. (VERIFIED; `crit-accuracy-ACC-6`, `qa-QA-6`, `counts-added-2`, `crit-problem-added-2`, `algorithms-ALGFIG-1`, `counts-NUM-5`, `crit-report-QR-9`)
- **[p.14, §7, Table 5]** "Dates are working windows, not confirmed assessment deadlines" trong khi hạn chính thức đã công bố: final report **Wed 7/4/2027 17:00**, presentation 19–23/4/2027 (tentative), e-copy 10/5/2027; CA presentation trong Reading Week. Table 5 để "prepare the final report" vào tháng 4 → trễ hạn. (VERIFIED; `official-OFF-3`, `crit-management-PM-1`)
- **[p.1–9]** Technical contribution bị "undersell": không có câu contribution kiểm chứng được; quyết định chỉ có WHAT; test không gắn với rủi ro báo cáo tự nêu; V2/V7 build của Bao ghi là "we". → Trong thời gian còn lại: thêm 1 đoạn contribution 3 gạch đầu dòng ở cuối §3.2 và 1 cột/câu "risk → check" (tùy chọn). (VERIFIED/INFERENCE; `crit-technical-TA-1/2/3/4`)
- **[p.4, §3]** Không có thách thức nào được kể như "vấn đề đã xảy ra → phát hiện → sửa" (repo có nhiều ví dụ: edit/run canvas lệch nhau ở V1 → V2; parallel-edge bridge); không nói cách lập kế hoạch/theo dõi tiến độ. (VERIFIED; `crit-management-PM-3`, `official-OFF-6`, `crit-management-PM-9`)
- **[trình bày, p.1–15]** Caveat lặp ~13 lần; chữ trong screenshot in ra ~3–4 pt; text chỉ nhắc Figure 3–4 và Table 1–2 (các hình/bảng còn lại không được tham chiếu); viết tắt chưa giải thích (LCA, BST, AVL, CI, RPC, WASM, DFS/BFS…); câu "evidence bookkeeping" (§1.1, §6.2 ¶1, p.16). (VERIFIED; `crit-report-QR-3/4/5/6/7`, `crit-problem-PU-6`, `algorithms-added-1`, `crit-accuracy-ACC-3`, `official-added-2`, `qa-QA-16`)

### 3.3 Minor (theo trang)

| Trang, § | Vấn đề → sửa | ID |
|---|---|---|
| p.1 Abstract | "11 graph algorithm identifiers" là đơn vị nội bộ → "11 graph algorithms (counting the DFS variants separately)" | `crit-accuracy-ACC-7` |
| p.1 cover | Hash `662e7b3`/`67ce56c` vô nghĩa với evaluator → chuyển xuống caption Table 3 hoặc thay bằng link public | `crit-report-QR-16` (UNCERTAIN) |
| p.2 §1.2 | "many programming competitions… strong results" không nêu cụ thể → nêu 1–2 thành tích/vai trò dạy, hoặc giữ nguyên | `crit-problem-PU-7` |
| p.2 §1.3 | Desktop-only không có lý do; mobile/cross-browser trong hay ngoài scope? | `qa-QA-14`, `crit-problem-PU-5` |
| p.3–4 | Dòng mồ côi "remains necessary." đầu p.4; "Octo-ber" bị ngắt trong Table 1 | `crit-report-QR-10` |
| p.4 §3.1 | "V1 began on 28 July" → "V1's first recorded commit is dated 28 July 2026" (commit đầu đã có app chạy được) | `timeline-TL-5` (UNCERTAIN), `timeline-added-2` |
| p.4 Table 1 | Recursive DFS, Bellman–Ford, Prim (29/9–5/10) nằm sai hàng; thiếu trial Week 10; caption "not formal assessment weeks" mâu thuẫn với "Week 10" | `timeline-TL-4`, `crit-management-PM-4` |
| p.4 §3.2 | "Later choices 27–48 and the subsequent 'V10 wins'" sai thứ tự ("V10 wins" 18/10 nằm giữa choice 32 và 33) và không nêu ai → "Choices 27–48 (18–22 October) and the 18 October decision to keep only V10 were made by Kerk and me together and implemented by Kerk." Số hiệu "26 recorded V10 choices" khó hiểu với người ngoài | `crit-accuracy-ACC-9`, `contributions-CONTRIB-4`, `timeline-added-1`, `qa-QA-4` |
| p.4 §3.2 | Danh sách đóng góp bỏ sót test tự động và decision records (DD/TP/SP); không nói ai build website (F1 ghi "built by Kerk and Bao") | `contributions-CONTRIB-8`, `contributions-added-1` |
| p.5 Fig. 1 | Vẽ rendering đi qua shared layer → mỗi module tự render (React Flow + d3-force / d3-hierarchy; Canvas 2D) | `architecture-ARCH-1` |
| p.5 §4.1 | "saved layout preferences use local storage" đúng nhưng thiếu (đúng hơn: layout V10 versioned) | `architecture-ARCH-6` |
| p.6 Table 2, §4.2 | "topology revision", "run identity", "Clear Apply" chưa định nghĩa | `crit-technical-TA-10` |
| p.6 §4.3 | "retained history remains unbounded" sai (input cap 240 giá trị); "distant seeks" sai mô hình chi phí (luôn replay từ đầu tới target) | `architecture-ARCH-4`, `crit-technical-TA-6` |
| p.7 Fig. 2 | Bottom region vẽ full-width; thực tế chỉ nằm dưới canvas, giữa hai cột | `architecture-ARCH-2` |
| p.7 §4.4 | Floor 360×320 chỉ là của graph; tree 320×200/240; sorting 320×200 (Study) | `counts-NUM-3`, `architecture-ARCH-3` |
| p.8/14 | Kế hoạch automate drag/split browser tests đảo ngược lựa chọn "guides only" ngày 28/10 (PR #36) — Bao xác nhận | `architecture-added-1`, `crit-technical-added-4`, `crit-management-added-2` |
| p.9 §4.6 | "End node where applicable" → chỉ BFS, Dijkstra, Bellman–Ford | `algorithms-ALGFIG-6`, `crit-accuracy-ACC-8` |
| p.9 §4.6 | "700 graph inputs" đọc như 700 phép so oracle → 400 so với oracle + 300 kiểm tra luật DFS-root | `counts-NUM-2`, `algorithms-ALGFIG-2` |
| p.9 Fig. 5 | "CP4 4.7" không giải thích/cite; caption không nói đọc hình thế nào | `literature-LIT-9`, `algorithms-ALGFIG-4` |
| p.10 Fig. 6 | Caption "1 moves above 7" sai: frame 3/9 là bước **so sánh trước khi swap** (Status "Compare parent", Latest swap None) — đã xem ảnh | `counts-NUM-4`, `algorithms-ALGFIG-3`, `floating-added-2`, `crit-technical-added-1` |
| p.10 §4.7 | Không mô tả e-Lecture và example graph lấy từ visualgo.net (phục vụ objective 2) | `crit-technical-added-3`, `qa-added-1` |
| p.11 §4.8 | "beside the relevant node or edge" → note chỉ neo vào node (Dijkstra: đỉnh đích) hoặc đỉnh canvas; không nói relaxation bị reject cũng có note đỏ; 4 tên cho 1 tính năng | `floating-FT-5`, `floating-FT-7`, `qa-QA-13`, `floating-FT-3`, `crit-accuracy-ACC-13` |
| p.12 §5 | "266 CI runs" nằm giữa kết quả 1/11 → thực ra 4 workflow, 4/9–30/10, chỉ 105 run test visualizer | `crit-accuracy-ACC-11` |
| p.12 Table 3 | Cột Interpretation chỉ nêu thư mục; "case" chưa định nghĩa | `qa-QA-12` |
| p.13 §6.2 | "developer checks lack a complete recorded protocol" sai → có 3 checklist (20/10/26 mục), chỉ là không ghi lại lần chạy | `crit-accuracy-ACC-17`, `qa-added-2` |
| p.13 §6.2 | Engine experiment chạy trên engine của Kerk — chưa nói; kết quả quá chung chung | `contributions-CONTRIB-6`, `qa-QA-8` |
| p.14 Table 5 | Không có owner/dependency; completion evidence khó kiểm; không có danh sách "out of scope" Sem 2 | `crit-management-PM-5`, `crit-management-PM-8` |
| p.15 Refs | [1] gộp 2 URL, ngắt "https:"; cite không sắp xếp "[8, 6]"; [3] thiếu DOI 10.1006/jvlc.2002.0237 | `crit-report-QR-14`, `crit-literature-LR-8` |
| p.8–10 captions | Caption nêu kết luận mà không nói nhìn vào đâu | `crit-report-QR-11` |

Các Minor còn lại (`crit-technical-TA-5` Fig. 1–2 hơi trang trí; `crit-technical-added-2` run session là code standalone của Bao; `literature-added-4` D3 chỉ được credit force/tree; `crit-literature-added-1/2/3`; `crit-report-added-1`) — giá trị thấp so với thời gian, đề xuất **bỏ qua** cho CA.

### 3.4 Bị bác bỏ (không nêu lại)

`architecture-ARCH-5` (thêm số đo eager timeline), `algorithms-ALGFIG-5`, `contributions-CONTRIB-7`, `crit-accuracy-ACC-16` (câu "Bellman–Ford and Prim … with Codex under my requirements and review" là đúng, AI attribution đã chốt), `algorithms-ALGFIG-7` (caption hình 8 đúng), `floating-FT-6` (aria-hidden mô tả đúng), `crit-management-PM-7` (risk register), `crit-report-QR-15` (tách §6/§7), `crit-accuracy-ACC-10` ("review"), `crit-accuracy-ACC-12` (abstract "will"), `qa-QA-15` (mục reflection — chỉ chuẩn bị cho Q&A).

---

## 4. Bảng đối chiếu claim

| Claim trong báo cáo | Trang | Nguồn kiểm | Kết quả |
|---|---|---|---|
| 11 graph algorithm ids; BFS, DFS stack, Dijkstra, Kruskal, Edmonds–Karp kế thừa | 1, 9 | `types.ts:13-24`; V2 `c8b14e6` | MATCH |
| 7 tree workspaces; 8 sorting algorithms | 1, 10 | `workspaceModes.ts:14-22`; `sort.ts:1-9` | MATCH |
| 3,273 unit tests = 654 + 1,881 + 571 + 143 + 24 | 1, 12 | log 1/11; chạy lại 4/11 (654/654, 2,619/2,619); CI `41095633732` | MATCH |
| 151 browser cases, 14 specs, Chromium | 1, 12 | CI log "151 passed"; đếm tĩnh | MATCH (Playwright không chạy lại 4/11) |
| Lint 0 errors, 2 warnings; chunk ~705/206 kB | 12 | oxlint 4/11; CI | MATCH |
| Node 24.17.0, npm 11.13, Playwright 1.64.1, Windows 11 | 12 | `package-lock.json`; note 07 | MATCH (Windows 11: DOCUMENTED) |
| 266 CI runs, 8 failed rồi xanh | 12 | `gh run list` | MATCH số liệu; MISMATCH ngữ cảnh (4 workflow, chỉ 105 run test visualizer) |
| 30 cards, 12 open, 8 full + 4 partial, 18 soon | 12 | `src/site/modules.ts` | MATCH số; MISMATCH ý nghĩa (chỉ 4 module visualgo.net "full"; 4 còn lại là Trie, LCA, 2 Editor) |
| Fig. 9 "clearly marked future topics" | 12 | `F1-home-catalogue.png` (đã xem) | MISMATCH (không có thẻ "Coming soon" trong ảnh) |
| Buffer 2,048 ops; priming 60,000 ops; seek replay không checkpoint | 6 | `operationBuffer.ts:7, :246`; `comparisonPlayback.ts` | MATCH |
| Sorting history "unbounded"; "distant seeks" | 6, 13 | input cap 240; replay từ đầu | MISMATCH |
| Group min 240×120 | 7 | `groupsModel.ts:86-90` | MATCH |
| Drawing floor 360×320 (cho cả shell) | 7 | floors theo module | MISMATCH (chỉ graph) |
| 4,000 seeded random ops, nhiều viewport, round trip | 7 | `groupsModel.test.ts:1210-1340` | MATCH |
| Default layout: Action + e-Lecture trái; Pseudocode, Status phải | 6–8 | `DEFAULT_LAYOUT` | MATCH |
| Fig. 2: bottom region full-width | 7 | shell code; Fig. 3–4 | MISMATCH |
| Fig. 1: rendering qua shared layer | 5 | imports | MISMATCH |
| WASM engine chưa kết nối | 2, 5, 13 | không import trong `prototypes/src` | MATCH |
| Parallel-edge rule: bỏ qua parent *edge* theo id | 9 | `createCutVertexBridgeSequence.ts:169-175` | MATCH |
| Oracles: remove-and-recount; Floyd–Warshall; exhaustive forests | 9 | property tests | MATCH |
| 700 / 140 / 20 randomized cases | 9 | doc 02:95-100 | MATCH tổng; MISMATCH diễn đạt (400 oracle + 300 root rule) |
| End node "where applicable" | 9 | chỉ BFS, Dijkstra, Bellman–Ford | MISMATCH (mơ hồ) |
| Fig. 5: cut vertices 1, 3, 4; bridges 0–1, 3–4 | 9 | PNG frame 51/51; e2e | MATCH |
| Fig. 3: BFS step 8 of 22 | 8 | PNG "Frame 8/22" | MATCH |
| Fig. 6: "1 moves above 7" | 10 | PNG frame 3/9 (đã xem) | MISMATCH |
| Fig. 7: Merge/Bubble/Quick/Radix, 48 phần tử | 10 | PNG; `INITIAL_SIZE 48` | MATCH |
| Fig. 8: 4 + 3 < 8, E 8→7 | 11 | PNG frame 24/31; DD-61 | MATCH |
| Note coverage: Dijkstra, LCA, BST, AVL, Heap | 11 | `*StepNotes.ts` | MATCH |
| Note 1,600 ms; aria-hidden | 11 | `floatingTextTiming.ts:11`; `StepNoteLayer.tsx:81` | MATCH |
| "Suppressed for intervals below 200 ms"; "configured delay" | 11 | timing code | MISMATCH |
| Notes "beside the relevant node or edge" | 11 | anchor code | MISMATCH (chỉ node/đỉnh canvas) |
| V1 28/7; V2 tháng 8; sorting 19/8; tree 3–17/9 | 4 | `f3a0db8`, `92fa193`, `9236a65` | MATCH ("began" → "first recorded commit") |
| 18/10 Kerk consolidated one app + shared layer | 4 | `0394b64`, PR #20 | MATCH |
| First 26 V10 choices của Bao; 27–48 joint | 4 | blame V10 proposal; Q3 | MATCH |
| "subsequent 'V10 wins'" | 4 | `0394b64` 21:37 18/10 | MISMATCH thứ tự |
| Survey "to inform the choice between V2 and V7"; "We implemented both" | 4 | Q8 của Bao; PR V2/V7 | MISMATCH |
| "Kerk, our supervisor and I agreed on V10" | 4 | chỉ lời Bao 3/11 | UNVERIFIABLE (không có bản ghi) |
| "Following the Week 10 trial, I introduced floating text" `[8, 6]` | 11 | TP-34 23/10; `67ce56c` | UNVERIFIABLE thời điểm; MISMATCH nguồn trích |
| Trial: 15–20 phút, video, post-use test, người dùng đa dạng | 4, 13 | addendum 4/11 | UNVERIFIABLE (chỉ có lời kể + ảnh folder) |
| "Prof. Halim's canvas-focused educational goal" | 11 | chỉ lời Bao 4/11 | UNVERIFIABLE |
| Hundhausen et al.: meta-study 24 studies | 3 | abstract JVLC 2002 | MATCH |
| "Halim et al. [2] present VisuAlgo" | 3 | bài 2012 không dùng tên | MISMATCH (Halim 2015 mới dùng) |
| Shaffer et al.: availability, quality, coverage | 3 | abstract TOCE 2010 | MATCH |
| OpenDSA URL [4] | 15 | lỗi TLS | MISMATCH (dùng `opendsa-server.cs.vt.edu`) |
| Abstract 182 từ; cover có tên, matric, supervisor, AY | 1 | đếm | MATCH |

---

## 5. Thêm gì, cắt gì

**Cắt (đã thử biên dịch bằng biến thể trong `fyp-audit-artifacts/cut-list/`):**

| Cắt | Vị trí (`main.tex`) | Tiết kiệm |
|---|---|---|
| "Report scope and evidence" + "Source note" (thay bằng 1 câu dưới References) | l.368–371, p.16 | ~1 trang → **15 trang** (v1) |
| ¶ chọn renderer lặp §2.2 | l.167, p.5 | ~5 dòng |
| ¶ engine adapter lặp Fig. 1/§6.2/§7.1 | l.169, p.5–6 | ~4 dòng, hết orphan p.5 |
| ¶ failure cases lặp §4.4 | l.235, p.8 | ~4 dòng |
| ¶ hedge survey | l.117, p.4 | ~4 dòng |
| ¶ thủ tục trial ở §3.1 → 1 câu trỏ tới §6.1 | l.119, p.4 | ~3 dòng |
| Câu hedge lặp: l.101 (2 câu), cuối l.108, cuối l.136, cuối l.224/226, cuối l.273, đầu l.275, câu 2 caption Fig. 8, cuối l.279, cuối l.300, l.312 "Separate developer checks…", l.314 "WASM-powered…", l.337 "Dates are working windows…" | p.3–14 | ~20 dòng |
| Tổng (v3) | | **14 trang**, trang cuối đầy |

**Thêm (dùng chỗ trống vừa có; giữ ≤ 15 trang):**

| Thêm | Vị trí | Ước tính |
|---|---|---|
| Problem statement ~120 từ + 3 design questions đưa lên §1, khôi phục "redesign" ở objective 3 | p.2 | +8 dòng |
| Định nghĩa V10/V1–V9 + survey viết lại (mục 7) | p.4 | ±0 |
| Ngày trial + consent (theo Bao) | p.4, 13 | +2 dòng |
| Table 5 theo hạn chính thức | p.14 | +2 dòng |
| Nhắc Figure/Table trong text, giải thích viết tắt lần đầu | rải rác | +3 dòng |
| Literature (chỉ nguồn đã kiểm metadata): Halim 2015 (*Olympiads in Informatics* 9, doi:10.15388/ioi.2015.20) — VisuAlgo + Online Quiz; visualgo.net; VS Code editor groups (precedent V10); Fouh et al. 2014 (OpenDSA, *Sci. Comput. Program.* 88, doi:10.1016/j.scico.2013.11.040) thay trang web; Saraiya et al. 2004 (SIGCSE, doi:10.1145/971300.971432 — pace control quan trọng nhất; pseudocode/back-up không có hiệu ứng có ý nghĩa) | p.3, 15 | +6 dòng |
| (Tùy chọn) 3 gạch đầu dòng "Contributions" cuối §3.2 | p.4–5 | +4 dòng |

Không thêm: số đo hiệu năng (TA-9), so sánh bridge với visualgo.net (TA-7), Naps/Chandler–Sweller (chưa đọc bản gốc), TOC/glossary (không cần ở độ dài này).

---

## 6. Câu hỏi cho Bao

Xem tin nhắn chat (cùng nội dung): Q1 ngày trial; Q2 chi tiết trial; Q3 consent; Q4 câu về supervisor; Q5 survey V2/V7; Q6 truy cập evidence [6]–[8]; Q7 link app public; Q8 title đăng ký + Main Evaluator; Q9 phạm vi sửa; Q10 bản tiếng Việt; Q11 các mục nhỏ chưa chắc. Câu trả lời sẽ được ghi lại vào file này sau khi nhận.

---

## 7. Bản nháp câu sửa (chỉ áp dụng sau khi Bao duyệt)

- **§4.8 timing (thay l.273):** "A note appears only when a step is reached by moving one step forward (Next or autoplay). After Next it lasts 1,600 ms; during autoplay it is shortened to 90% of the step interval and omitted when less than 200 ms would remain, so fast playback does not accumulate unreadable text."
- **Figure 6:** "Heap insertion of 1, frame 3 of 9: the new item at index 10 is compared with its parent 7 at index 5. The note “1 < 7 · swap up” states the decision before the swap, and the array strip marks the same two items."
- **§5 catalogue:** "Of the 30 catalogue cards, 12 open a module and 18 are marked coming soon. Of the 26 cards transcribed from visualgo.net, eight open: four offer every algorithm the original module lists (Sorting, BST/AVL, Binary Heap, MST) and four offer some of them (Segment Tree, Graph Traversal, SSSP, Max Flow). The other four are Trie and LCA, and this project's own Graph and Tree Editors. “Full” counts algorithms, not operations."
- **§3.1 survey (theo Q8):** "Kerk's wireframe of the visualization page drew nine layouts, V1–V9. After a user survey organized by Kerk, Kerk and I chose two of them, V2 (split rails) and V7 (docks), and I built the graph, tree and sorting visualizers in both with comparable functionality (20–27 September). On 16 October I proposed V10, a tenth layout that merges V2 and V7; [ai] agreed to adopt it. These layout numbers are unrelated to the standalone Graph Visualizer V1 and V2."
- **§3.2:** "Choices 27–48 (18–22 October) and the 18 October decision to keep only V10 were made by Kerk and me together and implemented by Kerk."
- **§4.4 floors:** "Expanded groups keep at least 240 px of width and 120 px of height; each module sets its own drawing floor (graph 360×320 px, tree 320×200 or 320×240 px), which the resolver keeps when the viewport allows."
- **§4.3:** "However, retained history is never trimmed (only the 240-value input cap bounds it), and a backward seek replays operations from the start to the target, so its cost grows with how late the target lies."
- **§4.6:** "BFS, Dijkstra and Bellman–Ford also accept an optional End node; their last frame then draws the shortest path to it." / "…700 random multigraphs for cut vertices and bridges (400 compared with the removal oracle and 300 checking the DFS-root rule), 140 signed graphs…"
- **§6.2:** "Manual developer checklists (20, 10 and 26 items) were run, but no run was recorded; they are separate from the Week 10 trial."
- **§7:** "Fixed SoC dates: CA presentation in Reading Week (14–20 November 2026); final report by Wednesday 7 April 2027, 5 pm; final presentation 19–23 April 2027 (tentative). Other windows are proposals."

---

## 8. Chuẩn bị CA presentation và Q&A

**Lịch:** CA presentation trong **Reading Week 14–20/11/2026**; Bao tự hẹn với Supervisor và Main Evaluator. Main Evaluator chấm "Report and **Discussion**" 20% → Q&A có trọng số thật.

**12 câu hỏi dễ gặp → chuẩn bị:**
1. *Phần nào của bạn, phần nào của Kerk?* → slide 3 cột Mine / Joint / Kerk với artefact + PR (V10 model/shell/tests PR #15–#17: Bao; one-app consolidation PR #18–#21: Kerk).
2. *Trial Week 10: mấy người, khi nào, test gì, thấy gì, đổi gì? Làm sao biết floating text giúp ích?* → số người, ngày, build, 2–3 quan sát → thay đổi; consent; nói thẳng "effect not measured".
3. *Survey của Kerk làm thế nào?* → so sánh gì, khi nào, bao nhiêu người — credit Kerk.
4. *V10 là gì? V1–V9 ở đâu?* → wireframe 9 layout của Kerk; build V2 + V7; V10 = layout thứ 10 (16/10); khác Graph Visualizer V1/V2.
5. *Làm sao biết thuật toán và từng bước đúng?* → oracle độc lập, seed cố định; AVL Delete so với tham chiếu textbook; heap create 200 list ngẫu nhiên; parallel-edge case (>100 graph có cạnh đôi tới parent).
6. *Sao chọn React Flow + panel tự viết thay vì D3/SVG hay docking library? Graph lớn tới đâu?* → lý do 1 dòng (DD-02, DD-09, DD-50 canvas render một lần); sample lớn nhất 48–63 đỉnh; chưa benchmark.
7. *Sao WASM engine chưa nối? Kế hoạch?* → Edge của engine là (u, v) không có edge id; engine sở hữu history; study M1–M3 xong, M4 chưa; slice tháng 1 có fallback.
8. *Số test trong Table 3 nghĩa là gì? Coverage?* → 1 case = 1 `test()`; property test tính 1; không có coverage tool.
9. *Sao chỉ desktop? Accessibility?* → lý do + vị trí trong Sem 2.
10. *Đã rebuild bao nhiêu % VisuAlgo? "Full" là gì?* → 8/26 module visualgo.net mở (4 full theo danh sách thuật toán, 4 partial) + Trie, LCA, 2 editor.
11. *Sem 2 còn gì, sản phẩm cuối là gì?* → Table 5; backup slide các feature ứng viên để supervisor xếp ưu tiên (SCC, 2-SAT, Ford–Fulkerson/Dinic, Segment Tree min/max, notes cho thuật toán còn lại).
12. *Bạn học được gì?* → 3–4 bài học (đo trước khi redesign; model test ≠ pointer test; eager vs lazy; review loop AI).

**Slide outline (~15 phút + demo 4 phút):** (1) Aim & roles; (2) Problem, 5 objectives, 3 design questions; (3) Hành trình & ai làm gì (Table 1 + trial); (4) Kiến trúc & state ownership (Fig. 1, Table 2); (5) V10 panel groups (Fig. 2–4, 4,000 random ops, drag test thủ công); (6) Thuật toán & correctness (Fig. 5–6, parallel edge, oracles) → **DEMO**; (7) Floating text & trial (Fig. 8, timing, chưa đo hiệu quả); (8) Status, giới hạn, kế hoạch (Table 3, 5). Backup: survey của Kerk; breakdown Table 3; engine study; sorting buffer; số liệu scale.

**Demo "Dijkstra trên graph mặc định /sssp" (~4 phút; quay video dự phòng):**
1. Home → *Single-Source Shortest Paths* (Dijkstra, start A). Chỉ layout V10 mặc định.
2. Nhấn **Next** của footer một lần (bắt đầu run), rồi Next tới **Frame 22/31**: B→D bị từ chối, note đỏ "already settled" trên D. Thông điệp: hình không đổi, note giải thích tại sao. (Note chỉ hiện khi đi tiến; Previous rồi Next để xem lại.)
3. Next 2 lần tới **Frame 24/31**: note xanh "4 + 3 < 8 · update", E 8→7, pseudocode dòng 7.
4. Kéo đỉnh E ~60 px: run vẫn ở frame 24, note đi theo E (layout ≠ input).
5. Action → *Draw graph*, đổi "B E 3" thành "B E 5": run biến mất ("No run") — sửa ngữ nghĩa làm run mất hiệu lực. (Frame "4 + 5 > 8 · keep" là suy luận, **cần tập trước**.)
6. Kéo tab STATUS: thấy preview, thả xuống vùng bottom; kéo splitter; reload — layout giữ nguyên; Settings → *Reset panel layout*.
7. (Tùy chọn 30 s) `/dfsbfs/cut-vertex-bridge`, preset "CP4 4.7", Next → Last: cut vertices 1, 3, 4; bridges 0–1, 3–4.

Chuẩn bị: cửa sổ guest mới ~1440×900, có mạng (font Inter), hoặc build Pages của `662e7b3`. Nếu lỗi: Previous/Next, Reset layout, hoặc chạy video.

---

## 9. Điểm mạnh nên giữ (tối đa 10)

1. Mọi con số kỹ thuật kiểm tra với code `662e7b3` đều khớp; Table 3 tái hiện được (chạy lại 4/11).
2. Ranh giới bằng chứng rõ: test ≠ learning, operation index ≠ runtime, engine chưa nối.
3. Ví dụ parallel-edge bridge (p.9) — câu chuyện chiều sâu kỹ thuật mạnh nhất; test cố ý gồm >100 graph có cạnh đôi tới parent.
4. Oracle độc lập (remove-and-recount, Floyd–Warshall, exhaustive forests) + "not a formal proof".
5. Table 2 "Example consequence" và ví dụ "kéo B vs đổi trọng số" — dễ hiểu, demo được.
6. Ba design questions ở §2.3 — xương sống tốt cho §4.
7. Credit Kerk chính xác (design system, engine, CI/Pages, consolidation 18/10); đoạn AI use một đoạn, đủ.
8. Fig. 1–2 dạng vector sạch, dùng lại được cho slide; caption Fig. 8 là mẫu tốt.
9. §6.4 kế hoạch đo (máy cố định, ≥ 5 lần, median + spread) và §7.1 fallback cho engine.
10. Abstract thật sự là abstract (182 từ), cover đầy đủ hơn yêu cầu.

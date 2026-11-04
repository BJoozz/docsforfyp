# FYP CA Report Audit: Handoff

**Written:** 2026-11-04, about 11:40–12:00 SGT, by the local Claude Code session (Opus 5.5). The owner paused the work so a Claude Code Cloud session can continue it.

**Hard deadline:** the CP4101 CA report is due **today, Wed 2026-11-04, 17:00 SGT**. It goes as a softcopy to the supervisor **and** the Main Evaluator.

**State in one line:** the 15-agent review of the CA report finished its research and verification (30 of 31 agents). The final synthesis agent failed on a usage limit, so no merged review exists yet. Nobody has edited the report because of the review.

**Goal for the next session (owner's words, 2026-11-04):** "Nên nhớ mục tiêu hiện tại của chúng ta là cho CA của FYP". The aim is the CA, so convey what is needed for it and move fast.

How this file was made:
- Sections 1–10 are hand-written from the full session transcript, the memory files and the panel results.
- The parts marked *(generated)* and Appendices A–C are copied from the agents' returned data by [`fyp-audit-artifacts/gen-handoff.js`](fyp-audit-artifacts/gen-handoff.js) and [`fyp-audit-artifacts/assemble.js`](fyp-audit-artifacts/assemble.js). They are not retyped.
- In generated text, every `|` became `/` and every line break a space, to keep the Markdown intact. The exact text is in [`fyp-audit-panel-results.json`](fyp-audit-panel-results.json).

---

## 1. Project Overview and Original Objectives

### 1.1 The project

- **VisuAlgo+** rebuilds VisuAlgo (visualgo.net, by A/P Steven Halim) on a modern foundation, with a redesigned interface, while keeping its educational purpose.
- **Student:** Truong Van Quoc Bao ("Bao"), A0276275U, GitHub `BJoozz`. The module is **NUS SoC CP4101** (B.Comp. Dissertation, 12 units), AY2026/27 Semester 1 (CA) and Semester 2 (final).
- **Bao's scope**, from his own project description of 2026-11-03, quoted in evidence doc 05 §1.1: the visualization and interaction layer. That covers the graph, tree and sorting visualizers, input editing and step-by-step playback, and integration into one consistent interface.
- **Kerk Tai Heng** is a fellow CP4101 student with the same supervisor. His scope is the engine/WASM foundation, the website design system, and shared infrastructure (web, cache, cloud). He also did the one-app consolidation on 2026-10-18. Integration with the WASM engine is future work.
- **Supervisor's early direction**, in Bao's words: the existing Laravel/PHP, MySQL, d3.js and jQuery stack should move to a modern foundation for both the interface and the execution engine.
- **The five project objectives**, from Bao's description, also on report p.2:
  1. Select suitable modern, widely adopted technologies.
  2. Preserve VisuAlgo's useful exploration, input editing and step-by-step explanation.
  3. Provide a consistent, redesigned interface across modules.
  4. Set clear boundaries for extending visualizers and integrating engines.
  5. Validate the rebuilt functionality and identify what still needs technical and user evaluation.

### 1.2 Objectives of this work (three stages in this session)

1. **Evidence pack** (asked 2026-11-01, done 2026-11-03). An audit of the project history, collecting traceable evidence for the CA report: five Markdown documents, figures and research notes in `BJoozz/docsforfyp`. The brief explicitly said **not** to write the report. Its full rules are in section 3.1.
2. **Compile the CA report to PDF** (asked 2026-11-04 09:40, done). Codex had written the LaTeX report and could not compile it.
3. **Review the CA report** (asked 2026-11-04 10:08, **paused at the synthesis step**). Bao asked in Vietnamese, translated: *"Run an overall re-check, cross-checking against the commits and files to see whether anything is inaccurate, and ask me if something needs confirming. Also tell me if something should be added or cut."* The review brief he pasted is reproduced verbatim:

> Review my **NUS SoC CP4101 FYP Continuous Assessment (CA) Report** critically, based on the official CA guidelines and evaluation criteria.
>
> This is a **Semester 1 progress report (10–15 pages), not the final FYP report**. Evaluate it against these key criteria:
>
> 1. **Problem Understanding (30%)**: Are the motivation, problem statement, objectives, scope, and limitations clearly explained?
> 2. **Technical Achievement (40%)**: Are the methodology, design decisions, implementation, individual contributions, and preliminary results technically convincing and supported by evidence?
> 3. **Literature Review**: Are relevant existing works discussed critically, with clear comparisons and justification for the chosen approach?
> 4. **Project Management (10–20%)**: Does the report demonstrate meaningful Semester 1 progress, initiative, challenges addressed, and a realistic Semester 2 plan?
> 5. **Report & Communication (10–20%)**: Is the report well-structured, concise, readable, properly referenced, and understandable to a Main Evaluator unfamiliar with the project?
> 6. **Accuracy & Evidence**: Are claims supported by actual implementations, experiments, screenshots, or references? Are completed work, ongoing work, future plans, and contributions from collaborators clearly distinguished?
>
> **Review instructions:**
> - Check both technical content and PDF presentation (formatting, figures, captions, readability, page count).
> - Identify missing information, unsupported claims, inconsistencies, repetition, and weak explanations.
> - Prioritize issues by severity: **Critical / Important / Minor**.
> - Provide actionable improvements with specific page or section references.
> - Assess how well the report prepares the reader for the CA Presentation and Q&A.
> - Give an overall readiness assessment and the **top 5 fixes before submission**.
>
> Be strict but fair. Do not expect a fully completed project or final experimental results. Distinguish official NUS requirements from recommendations, and do not invent missing evidence.

**Correction to the brief's weights.** The official CA forms put Project Management at 10% on the Main Evaluator's form only, and Report at 10% (supervisor) or 20% (Main Evaluator). See section 7.3.

### 1.3 Expected final deliverables (still owed)

1. **A review for Bao, in Vietnamese.** Technical terms, file names and quoted report text stay in English. Its parts, in order:
   1. Overall readiness: 5–8 sentences, with a one-line judgement per criterion, using the **official** weights.
   2. Top 5 fixes before submission.
   3. Deduplicated findings by severity (Critical / Important / Minor), ordered by page, each as "[page, §] issue → fix (basis)".
   4. A claim-check table: claim | page | source | MATCH / MISMATCH with the true value / UNVERIFIABLE. Include the matches.
   5. What to add and what to cut, with page references and lines saved.
   6. Questions for Bao, with options.
   7. CA presentation preparation: likely questions, slide outline and demo script.
   8. At most 10 strengths to keep.
2. **After Bao approves fixes:** a revised `report/main.tex`, with `report/vi/full.tex` and `report/vi/summary.tex` kept in sync. Then rebuilt PDFs at **≤ 15 pages** with **no "Draft" marker**.
3. **Optionally:** record Bao's trial answers in `report/week10_user_trial_addendum.md`.

---

## 2. Full Session Context and Important Discussions

All dates and times are SGT (UTC+8). This one Claude Code session (`dd1448ed-3ceb-4759-a934-c360d565fa8f`) has run since early October 2026 and was compacted several times.

### 2.1 Before the FYP work: 4–31 October, app development in the same session

- **Work done.** Bao and Claude built most of the current VisuAlgo+ features in the app repo through PRs #6–#37. Examples: V10 groups shell, LCA, heap operations, graph traversal methods, and step notes ("floating text"; PR #29 opened 2026-10-23, PR #30/#31, Dijkstra notes PR #32). Then came three Codex review sessions (PRs #34–#37). `main` reached **`662e7b3` on 2026-10-31**, the report's application snapshot.
- **Why it matters.** Details are in the design records and memory files. They matter for the CA only as content, which the evidence pack already covers.
- **Lessons from that period that still apply** (memory): CI on Linux and Windows differ by about 1 px in Inter text widths; a stacked PR merged by the owner landed on its base branch, not main; agents and Playwright may leave stray vite servers.

### 2.2 The 2026-11-01 evidence-pack request

- **23:04, access check.** Bao asked which of his GitHub repos (shown in a screenshot) Claude could read. **All 7 were readable** via `gh` as BJoozz, including private ones. `BJoozz/visualgo` is a fork of stevenhalim's VisuAlgo and serves as reference only. `BJoozz/visualgo-plus-design` is a fork mirroring upstream.
- **23:15, the evidence-pack brief.** Bao asked, translated: "read all commits and the details in them, all the files, to find as much useful information as possible… add anything you think useful, especially watch the timeline to understand my process… ask me if you have important questions… put the files in folder docsforfyp… take time until noon tomorrow… use Opus." The pasted brief's rules are in section 3.1.
- **23:44, Bao's six answers:**
  1. **Dates.** FYP = AY2026/27 Sem 1. Treat all earlier work as "week 0"; the real start is August. The CA is due 17:00 04/11/2026 SGT, as a softcopy to the Supervisor and the Main Evaluator.
  2. **Roles.** Kerk is on the same FYP with the same supervisor. In practice Kerk does engine/WASM plus web, cache and cloud; Bao does the graph, tree and sorting visualizers plus integration. Both of them and the supervisor intervene in each other's choices when needed. This is a working description, not a formal assignment. "Không mặc định toàn bộ shell hoặc engine là đóng góp của tôi trừ khi quá rõ ràng; các thử nghiệm engine của tôi cần ghi riêng" (do not assume the whole shell or engine is my contribution unless it is very clear; my engine experiments must be recorded separately).
  3. **Identity.** `123baoek31@gmail.com` and `BJoozz` are his; both author strings to be confirmed. They were confirmed on 11-03.
  4. **"The owner" in V10.** Do not infer the decider from the committer or PR; mark it QUESTION. Send him the link. He was sent PR #19 and `ae63a62`.
  5. **AI use.** Present it briefly and transparently. A Co-Authored-By trailer proves tool use only.
  6. **Supervisor.** A/P Steven Halim. Do not present the work direction as his assignment or feedback without an email, notes or Bao's confirmation.
- **Phase 1** (workflow `wf_62a7f64d-5a9`, 8 readers plus a synthesis, 76 min) produced research notes 01–09. They are now in `docsforfyp/evidence/research-notes/`.
- **Figures.** F1–F8 were captured on 2026-11-01 at 23:52–53 from `662e7b3`, at 1440×900. **The capture script was lost.** `figures/README.md` has a replay script written later.
- **Phase 2** (`wf_092b4e1f-d18`) **failed entirely**: every agent hit "You've hit your session limit". It was relaunched lean as `wf_6f7d66ee-c39`: 5 writers, then 3 adversarial reviewers, a fix pass and a final check. The reviewers raised 54 findings, and 50 were fixed.
- **2026-11-02 13:48.** "bỏ giới hạn thời gian, cứ chạy đi": the noon-11-02 deadline was lifted, and only the CA due date stands.

### 2.3 2026-11-03: questions, answers and the owner's steer

- **The request.** Bao asked: "những thứ bạn cần hỏi hãy đưa ra giải thích cụ thể kèm link và đưa các option để tôi chọn" (whatever you need to ask, explain concretely with links and give options to choose from). Sixteen questions went out in four batches. His answers are listed in section 3.3 and applied in all five docs; doc 01's top table records them.
- **The steer, while the answers were being applied.**
  - "mục tiêu chính là tập hợp các chi tiết quan trọng giúp tôi viết CA report, các phần phân quyền hay author ko quan trọng đến vậy" (the main goal is the important details for writing the CA report; attribution and authorship matter less).
  - "tất cả AI đều hoạt động dưới yêu cầu của tôi, các lựa chọn của tôi và xác nhận của tôi nên đừng lan man quá về vấn đề này" (all AI work was done under my requests, my choices and my confirmation, so do not dwell on this).
  - Result: the attribution scaffolding was removed from the docs, and AI is mentioned once.
- **Project description.** Bao supplied his written project description (background, five objectives, his scope and Kerk's). It is quoted in full in doc 05 §1.1, with an objective→evidence table.
- **Commits to `BJoozz/docsforfyp`.** `3e9a139` (pack) and `67ce56c` (answers applied) exist there. **This Claude session did not make these commits**; the brief forbade it, and they were made outside this session.

### 2.4 2026-11-03/04: Codex wrote the report

- Codex, not this session, wrote the CA report into `docsforfyp/report/` and committed directly:
  - `675fc73`: complete draft, LaTeX, PDF.
  - `089ef85`: Vietnamese translation and summary.
  - `c6c371e` (2026-11-04 09:37): the Week 10 V10 user trial and the floating-text rationale.
- Bao pasted Codex's message about `c6c371e`, translated:
  - "Section 6: added the Week 10 V10 trial, how it was organised, the participant group, feedback and the role of the videos."
  - "Floating text: briefly explained as a caption right beside the object, an improvement after the trial to reduce looking at Status and keep attention on the canvas, following Prof Halim's direction."
  - "Synced the English, Vietnamese and summary versions and the follow-up evaluation plan; removed the statement 'no V10 user trial yet'."
  - "LaTeX sources updated; the PDF is still the old one because the build environment is unavailable; noted in the README."
- **The Week 10 trial's only written source** is `report/week10_user_trial_addendum.md`: Bao's account of 4 Nov plus a screenshot of a shared folder, "VisuAlgo+ Prototype Testing Footage". It lists `experienced-tester-1.mp4`, `experienced-tester-2.mp4` and a truncated inexperienced-tester file. **This session never saw that screenshot or the videos.** The dates, participant count, tested build, questions and scores are recorded nowhere.

### 2.5 2026-11-04 09:40–10:05: PDF compilation (done; uncommitted)

- **No TeX on the machine.** I started Docker Desktop and pulled `texlive/texlive:latest-medium`. Bao asked "sao ko tải thẳng biên dịch latex về luôn" (why not install LaTeX directly?). I installed **MiKTeX 25.12** with winget for the user, enabled automatic package installs, and installed the `dejavu` font package. I then stopped Docker. The Docker image (~2 GB) is still on the machine, unused. Direct install is the preferred approach.
- **Page-count regression found.** Codex's sources used 14 hard `\page`=`\clearpage` breaks tuned to the old text. After the Week 10 additions, the English PDF grew from 15 to **19 pages**, with three pages of 1–4 lines. The pre-update source compiles to 15 pages on MiKTeX too, so the toolchain is not the cause.
- **The fix.** `\page` is now `\par\penalty0 \ifdim\pagetotal>.72\textheight\clearpage\else\vspace{8pt}\fi`, in `main.tex` line 32 and `vi/style.tex`. The five `\clearpage` lines in `vi/full.tex` now use `\page`. `\penalty0` is required: without it, `\pagetotal` still counts an overflowing line and the macro breaks wrongly.
- **Result:** English **16 pages**, Vietnamese full 21, Vietnamese summary 4. There are 0 undefined references and 0 overfull boxes. The three PDFs were copied in, and both READMEs were updated.
- **None of this is committed** (8 modified files; see 4.3). Bao has not explicitly approved the macro change.

### 2.6 2026-11-04 10:08–11:30: the review panel

- **Inputs.** I made a page-annotated text of the 16-page PDF (now `fyp-audit-artifacts/report-snapshot/report-pages-16p.txt`) and 80-dpi page PNGs. The PNGs are local only and not preserved; rebuild them from the PDF.
- **The panel.** Workflow `ca-report-review`, run `wf_976de5d7-7c7`, ran 15 finders, each with one slice, and 15 adversarial verifiers, all Opus at max effort. It took about 51 minutes and 7.07 M subagent tokens.
- **The failure.** The synthesis agent failed: "You've hit your 5-hour limit · resets 2:40pm (Asia/Singapore)".
- **The pause.** Bao then paused everything, asked for this handoff, and switched the session model to Opus 5.5.

### 2.7 Insights worth keeping (from all stages)

- **The Week 10 chronology.** The Registrar puts Week 10 at **19–23 Oct 2026**. The only dated record of the floating-text decision is Bao's request of **23 Oct** (TP-34 in `prototypes/docs/tree/DESIGN_DECISIONS.md`; PR #29 opened 13:36 SGT), and it mentions no trial. Floating *number* popups already existed (`ff77eca`, 13 Oct, TP-20). "Following the Week 10 trial" (p.11) is therefore true only if every session came before the 23 Oct request.
- **The cited evidence contradicts the trial.** The pinned snapshot `67ce56c` (refs [6]–[8]) says **no user evaluation exists**. A reader who follows the citation on the trial sentence finds the opposite claim.
- **The V2/V7 survey.** The report says Kerk's survey informed "the choice between V2 and V7". Bao's recorded answer says the survey came first, then Kerk and Bao picked V2 and V7 from the **nine** layouts in **Kerk's wireframe** (`69aa8e4`), and both were built by Bao.
- **Evidence references.** `BJoozz/docsforfyp` is **private** (`isPrivate=true`; only BJoozz is a collaborator), so examiners following [6]–[8] get a 404. A public build exists at https://kerktaiheng.github.io/visualgo-plus-design/ (`official-added-3`).
- **The 2026-11-01 test run** recorded 3,273 unit tests (654 graph node:test plus 2,619 vitest) and 151 browser cases, all passing. On 2026-11-04 the `counts` agent re-ran graph (654/654), vitest (2,619/2,619) and lint (0 errors, 2 warnings) live. Playwright was not re-run.

---

## 3. User Requirements, Preferences, and Decisions

### 3.1 Rules from the 2026-11-01 evidence-pack brief (still in force for audit work)

- **Repository changes:** "Do not modify application code, switch the working branch, reset files, merge, commit, or push. Preserve uncommitted work."
- **Access limits:** state any limit on access or history; never claim to have reviewed what was inaccessible.
- **Labels:** VERIFIED / DOCUMENTED / INFERENCE / QUESTION.
- **Tests:** a test file proves a test exists, not that it passes. Keep historical results separate from tests run during the audit.
- **Claims:** do not invent performance gains, user feedback, usability or educational benefits, or novelty. If there is no benchmark or user study, say so.
- **Prototypes:** do not present prototypes as the current product.
- **Ownership:** do not infer it from a filename, commit count or merge commit.

### 3.2 Standing preferences (memory files and repeated instructions)

- **Language:** write to Bao in **Vietnamese**; commits, PRs and docs in **English**.
- **Questions:** ask with **concrete explanations, links and options** (2026-11-03). Ask only when a choice is truly his.
- **Review findings:** verify each finding before fixing it, explain the current rules, offer fix options, then let Bao choose. This applies to pasted Codex reviews and to this panel.
- **Codex output:** Bao does **not** read Codex's plans or reviews. A pasted one is input, never his agreement.
- **AI-assisted work is Bao's own** (2026-11-03). Say it once; build no attribution scaffolding.
- **Rule changes:** DD/TP/SP records, AGENTS.md rules and test invariants change only on Bao's word.
- **Commits:** by explicit paths only; never from `git status`, since Codex and other sessions write into the same worktrees. Push only when told. Bao merges PRs himself.
- **Agents:** every agent runs on **Opus at max effort, never Fable** (since 2026-10-21). Keep the fan-out small, and test only what a change can affect.
- **Dev servers:** never touch one you did not start; port 5186 may be Bao's own. Stop your own by port or PID after checking ownership. Pass Playwright `--output` outside OneDrive.
- **Docs:** describe the current state; no stage logs.
- **Priority now:** the CA. Focus, speed, and only the needed information (2026-11-04).

### 3.3 Bao's dated answers (settled facts; do not re-litigate)

| Date | Topic | Answer |
|---|---|---|
| 11-01 | FYP period | AY2026/27 Sem 1; FYP proper began in **Week 1 = Mon 10 Aug 2026** (date confirmed by the Registrar calendar on 11-04); 28 Jul to about 9 Aug is "week 0"; all standalone work is in scope |
| 11-01 | Kerk | Fellow CP4101 student, same supervisor; split as in 2.2 |
| 11-03 Q2 | Identities | Both BJoozz author strings are Bao's |
| 11-03 Q3 | V10 choices 27–48, "V10 wins" (`0394b64`), `40a63bd`, `a074f50` | Decided by Kerk **and Bao together**, implemented by Kerk; choices 1–26 are Bao's |
| 11-03 Q4 | AI review | Bao read diffs, ran the app by hand, ran tests or watched CI. The 8 Bellman-Ford/Prim stage commits were made with Codex; the other 6 untrailered commits were by hand. (He also picked "Other" but no text arrived.) |
| 11-03 Q5 | Records naming no person | Implementer's defaults Bao accepted, so his decisions |
| 11-03 Q6 | Late-October review sessions | Codex reviews that Bao read first; Claude verified each finding; Bao chose the fixes |
| 11-03 Q7 | visualgo.net material | Prof Halim knows and agrees (no written source) |
| 11-03 Q8 | V2/V7 | Chosen by Kerk and Bao together after a user-group survey **Kerk** ran; Bao keeps no record of it |
| 11-03 Q9 | Engine study | Bao's own idea, parked by him to focus on the visualizers |
| 11-03 Q11 | Manual checklists | Run partly by hand, partly by agents; nothing recorded |
| 11-03 Q12 | Local commits `053064f`, `53d2ef4` | Stay local, not pushed |
| 11-03 | Figures | 7 screenshots (F1–F4, F6–F8) plus 2 diagrams (D1, D2); F5 is spare |
| 11-03 | Doc length | Docs 02/03 stay long |
| 11-03 | Objectives | Bao's written project description (doc 05 §1.1) |
| 11-03 / 11-04 (report README) | Clarifications in the report | Personal motivation (competitive programming and teaching); **Bao, Kerk and the supervisor agreed on V10** after the survey and the V2/V7 builds. This rests only on Bao's clarification of 3 Nov; no repo record names the supervisor |
| 11-04 (via Codex) | Week 10 trial | Account in the addendum (2.4). Floating text was presented as a post-trial change following Prof Halim's canvas-focused goal, "as recalled by Bao" |

### 3.4 Decisions made in this session, with reasons

- **Evidence pack, not the report.** Codex wrote the report; this session audited and compiled it.
- **Toolchain.** MiKTeX installed directly instead of Docker, at Bao's request ("sao ko tải thẳng").
- **The `\page` macro.** It became conditional instead of a hard break, to remove nearly empty pages without changing any text. **This still needs Bao's approval** and is uncommitted.
- **The review panel design.** One finder per slice plus one adversarial verifier each gives independent checking. The synthesis was to be a single agent.
- **Handoff placement.** It lives in `docsforfyp/docs/`, the repo that holds the report, not in the app repo. The app repo is Kerk's shared repo, and the audit rules keep it untouched.

---

## 4. Current Project State and Completed Work

### 4.1 Application repo: `kerktaiheng/visualgo-plus-design`

- **State.** Branch `main` at **`662e7b3`** (2026-10-31); clean. Local path `C:/Users/123ba/nuss/OneDrive - National University of Singapore/workplace/vstudio/learn/code/visualgo-plus-design`.
- **Layout.** One React 19 + TypeScript + Vite app in `prototypes/` (`src/site`, `src/graph`, `src/tree`, `src/sorting`, `src/shared`). It is served from the repo root on port 5186. Kerk's engine lives in `wasm-arch/`.
- **Design records:** `prototypes/docs/graph/DESIGN_DECISIONS.md` (DD-01..61; 01–22 inherited), `prototypes/docs/tree/DESIGN_DECISIONS.md` (TP-01..36) and `prototypes/docs/sorting/DESIGN_DECISIONS.md` (SP-01..20). The V10 proposal, with choices 1–48, is `design/proposals/viz-shell-v10/README.md`.
- **Inventory** (VERIFIED 2026-11-01):
  - 282 commits on all refs (267 on main), 38 remote branches, 37 PRs (Bao 33; Kerk #18–#21).
  - Authors: BJoozz `123baoek31@gmail.com` 231, BJoozz no-reply 30, Kerk Tai Heng 17, kerktaiheng 4.
  - 199 of Bao's 213 own main commits carry Claude trailers.
  - 90 of Bao's commits reached main directly between 09-29 and 10-15: 29 in PR #6, 61 in no PR.
  - **No PR has a review or comment.**
  - Kerk initialised the repo on 2026-09-03; Bao's first commit was `986deba` on 2026-09-13.
- **CI and the public build:**
  - CI runs `app.yml`, `ci.yml` and `pages.yml`; `pages.yml` deploys every push to main to GitHub Pages, which is the public build.
  - There were 266 CI runs up to the audit, with 8 failures, all fixed later.
  - The CI app run at `662e7b3` is `41095633732`.
- **Standalone repos** (local read-only clones in `C:/Users/123ba/AppData/Local/Temp/fyp-repos/`):

| Repo | Dates | Commits |
|---|---|---|
| graph-algorithm-visualizer (V1) | 2026-07-28 → 08-19 | 55 |
| sorting-algorithm-visualizer | 08-19 | 1, squashed |
| graph-visualizer-v2 | 08-20 → 09-11 | 53 |
| tree-visualizer | 09-03 → 09-17 | 50 |

- **The engine experiment:** `origin/bj/engine-v2-experiment` holds 4 commits (stable edge identity `478174f`, reusable browser engine client `e348a6d`, and others). Two further commits, `053064f` and `53d2ef4`, exist only locally.

### 4.2 Evidence pack: `BJoozz/docsforfyp` (private)

- **State.** HEAD `c6c371e`. Local path `C:/Users/123ba/nuss/OneDrive - National University of Singapore/workplace/vstudio/learn/code/docsforfyp`. The evidence snapshot pinned by the report is `67ce56c`; `git diff 67ce56c c6c371e` touches only `report/`.
- **Contents:**
  - Five documents: `01_scope_and_timeline.md` (its top table records the owner's answers), `02_contribution_evidence.md` (contributions C1–C14), `03_architecture_and_decisions.md`, `04_figures_and_validation.md` and `05_report_mapping_and_questions.md` (§1.1 holds Bao's project description and the objective→evidence table).
  - `figures/`: F1–F8 PNGs and `README.md`, which has the replay script. **F2 shows BFS paused at frame 8/22**; an earlier note claiming "No active run" was wrong and was corrected.
  - `evidence/`: research notes 01–09 and the inputs (`prs.txt`, `branches.tsv`, `commits-*.tsv`).
  - `report/` (2.4).
- **Recommended central contributions** (doc 05): C6 the V10 groups shell (`groupsModel.ts` is all Bao's by blame), C7 the graph algorithms with property/oracle tests, C1+C2 the standalone foundations, C10 step notes on a shared layer, and C13 process and verification.

### 4.3 The CA report (`docsforfyp/report/`) as reviewed

- **`main.tex`** is the English report, built with pdfLaTeX into `VisuAlgo_CA_Report_Draft.pdf`. It has **16 pages**: cover p1, body p2–15 (references on p15), and two meta notes on p16.
- **Sections:** 1 Introduction and Objectives; 2 Background and Related Work; 3 Development Approach and Responsibilities; 4 System Design and Implementation (4.1–4.8, floating text in 4.8); 5 Current Results and Validation; 6 User Evaluation, Limitations and Next Steps (6.1 Week 10 trial); 7 Plan for the Remaining Project; References.
- **Floats:** 9 figures (two TikZ diagrams plus the screenshots F1–F4 and F6–F8) and 5 tables.
- **Vietnamese versions:** `vi/full.tex` (21 pages) and `vi/summary.tex` (4 pages), built with XeLaTeX and DejaVu.
- **Other files:** `references.bib` (9 entries, 3 of them self-citations [6]–[8]), `week10_user_trial_addendum.md`, and `README.md` (build steps and a pre-submission checklist that already says to remove the "Draft" markers).
- **Uncommitted changes in `docsforfyp`** (from 2.5; Bao decides): `report/README.md`, `report/VisuAlgo_CA_Report_Draft.pdf`, `report/main.tex`, `report/vi/README.md`, `report/vi/VisuAlgo_CA_Report_VI.pdf`, `report/vi/VisuAlgo_CA_Summary_VI.pdf`, `report/vi/full.tex` and `report/vi/style.tex`. In addition, `docs/` (this handoff) is **untracked**.

### 4.4 Completed versus not completed

| Item | Status |
|---|---|
| Evidence pack (5 docs, figures, notes) and the owner's 16 answers | DONE (2026-11-03) |
| Report written (by Codex) | DONE, as a draft |
| PDFs compiled; page-break regression fixed | DONE, uncommitted |
| Review: 15 finders and 15 verifiers | DONE |
| Review: synthesis (merged Vietnamese review, top 5, claim table) | **NOT DONE** (agent failed) |
| Bao's answers to the new questions (section 9) | **NOT ASKED YET** |
| Report fixes | **NOT STARTED**; need Bao's choices |
| Submission by 17:00 | Bao's action, pending |

---

## 5. 15-Agent Investigation Results

| Phase | Agents | Status |
|---|---|---|
| Find | 15 | **All completed.** 142 findings: 4 Critical, 67 Important, 71 Minor (finder severities). The notes are verbatim below. |
| Verify | 15 | **All completed.** Each of the 142 findings got a verdict, and 34 more were added. |
| Synthesize | 1 | **FAILED** (usage limit). Its output does not exist. |

After verification (severities as the verifiers corrected them):

{{STATS}}

- **"Confirmed"** means a second Opus agent reproduced the evidence and agreed the finding is fair. It does **not** mean Bao agreed.
- **The 34 items "added by a verifier"** were not checked by a third agent.
- **Refuted items** (Appendix B) should not be raised again without new evidence.
- **Slice prompts.** Each slice's exact prompt is in the workflow script (local only: `~/.claude/projects/<project>/dd1448ed-3ceb-4759-a934-c360d565fa8f/workflows/scripts/ca-report-review-wf_976de5d7-7c7.js`). The task summaries below are condensed from it. The shared rules every agent got: read-only repositories, cite exact evidence, VERIFIED/DOCUMENTED/INFERENCE labels, AI attribution and the owner's answers settled, page numbers from the 16-page text, strict but fair for a progress report.

### 5.1 Agent-by-agent progress *(generated; finder notes verbatim)*

The notes hold each criterion reviewer's verdict, the `crit-report` **cut list to ≤ 15 pages**, the `official` source list, and the `qa` **likely evaluator questions, slide outline and demo script**.

{{GEN_AGENTS}}

---

## 6. Verified Findings and Supporting Evidence

### 6.1 Consolidated picture (hand-grouped from the confirmed findings; **preliminary, not a verified synthesis**)

I grouped the findings from their IDs and first sentences, with no new checking. The full text and evidence for each is in Appendix A.

**Critical.**
- **The PDF still says "draft" in four places:**
  - "DRAFT FOR REVIEW" on the cover (`main.tex` line 48).
  - The header "CP4101 CA Report | Draft" on pp. 2–16 (line 27).
  - The PDF title metadata "VisuAlgo+ — CA Report Draft" (line 13).
  - The file name `VisuAlgo_CA_Report_Draft.pdf`.
  - Findings: `official-OFF-1`, `crit-report-QR-1`.

**Factual inaccuracies:** the report states something the code, git or the cited source contradicts.

| Claim in the report | What the panel found | IDs |
|---|---|---|
| p.11: notes "are suppressed for intervals below 200 milliseconds"; duration "limited by the step interval and configured delay" | Misstates the code. The 200 ms floor applies to the note's remaining life, which is 90% of the step interval minus the delay. | `floating-FT-4`, `counts-NUM-1`, `crit-accuracy-ACC-18` |
| p.10, Figure 6: "the new value 1 moves above 7" | The frame (3 of 9) shows the comparison **before** the swap; 1 is still below 7. | `counts-NUM-4`, `algorithms-ALGFIG-3`, `floating-added-2` |
| p.12, Figure 9: "presents the rebuilt modules alongside clearly marked future topics" | The 1440×900 capture shows no "Coming soon" card. | `algorithms-ALGFIG-1`, `counts-NUM-5` |
| p.12: "Of the 30 catalogue cards, 12 open a module; eight are labelled full and four partial" | The counts are right, but they mix VisuAlgo+'s two editor cards with visualgo.net modules. "Full" is undefined, and 4 of the 8 "full" cards are not visualgo.net modules. | `counts-added-2`, `crit-accuracy-ACC-6`, `qa-QA-6`, `crit-problem-added-2` |
| p.7: "the drawing has a target floor of 360 by 320 pixels" (as if shared) | Graph only; tree and sorting pass their own floors. | `counts-NUM-3`, `architecture-ARCH-3` |
| p.5, Figure 1: rendering drawn as passing through the shared layer | The modules render directly. | `architecture-ARCH-1` |
| p.7, Figure 2: bottom region drawn full width | The left and right columns run full height; the bottom sits under the canvas. | `architecture-ARCH-2` |
| p.6 and p.13: sorting history "remains unbounded" | Never trimmed, but bounded: input is capped at 240 values. | `architecture-ARCH-4` |
| p.9: "700 graph inputs for cut-vertex/bridge checks" right after the oracle sentence | Only seeds 1–400 are oracle-compared. | `counts-NUM-2`, `algorithms-ALGFIG-2` |
| p.9: "End node where applicable" | Only BFS, Dijkstra and Bellman–Ford take one. | `algorithms-ALGFIG-6`, `crit-accuracy-ACC-8` |
| p.4: "Later choices 27–48 and the subsequent 'V10 wins' changes were joint decisions" | "V10 wins" (18 Oct) came after choices 27–32 and before 33–48. It names the one-app consolidation, which the next sentence credits to Kerk. | `timeline-added-1`, `crit-accuracy-ACC-9`, `contributions-CONTRIB-4` |
| p.4: "Kerk conducted a user survey to inform the choice between the V2 split-rail and V7 dock-based layouts" | Recorded answer: survey first, then Kerk and Bao picked V2/V7 from **nine** layouts in **Kerk's wireframe**, which is never credited. | `timeline-TL-3`, `contributions-CONTRIB-1`, `contributions-CONTRIB-2`, `crit-accuracy-ACC-4`, `qa-QA-3`, `crit-problem-added-1`, `crit-management-added-1` |
| p.4: "We also implemented both variants" | The V2 and V7 builds were Bao's; the sentence undersells him. | `crit-technical-TA-4` |
| p.4: two different "V2"s; "V10" never defined | Ambiguous to an outsider. | `contributions-added-2`, `qa-QA-7` |
| p.4, Table 1 periods | Graph extensions started in late September; pre-semester V1 work is merged into "Late July–August". | `timeline-TL-4`, `timeline-added-2` |
| p.11: "Following the Week 10 trial, I introduced floating text … [8, 6]" | The cited snapshot says there is no user evaluation. The dated record gives Bao's request of 23 Oct with no trial (see 2.7). | `timeline-TL-1`, `timeline-TL-2`, `floating-FT-2`, `literature-LIT-6`, `crit-accuracy-ACC-2`, `crit-accuracy-ACC-14`; uncertain: `floating-FT-1`, `crit-accuracy-ACC-1` |
| p.11: notes sit "beside the relevant node or edge" | Overstates the anchoring. | `floating-FT-5` |
| p.11: rejected relaxation as the example, Figure 8 accepted | The text never says rejected relaxations get notes. | `floating-FT-7` |
| p.3: "Halim et al. [2] present VisuAlgo" | The 2012 paper presents the predecessor and never uses the name; Halim 2015 calls VisuAlgo its continuation. | `literature-LIT-4`, `crit-literature-LR-3` |
| p.15, ref [4] | The OpenDSA URL fails with a TLS error. | `literature-LIT-5` |
| p.12: "266 CI runs" | Sits among the 1 November results, but the runs span 4 workflows and the whole history. | `crit-accuracy-ACC-11` |
| p.13: "developer checks … lack a complete recorded protocol" | The protocol exists (checklists of 20, 10 and 26 items); only the runs went unrecorded. | `crit-accuracy-ACC-17` |
| p.2, p.11, p.16: supervisor statements | They rest only on Bao's later account. | `crit-accuracy-ACC-5`; uncertain: `contributions-CONTRIB-3` |

**Important themes** (score-relevant, not factual errors):

- **Week 10 trial underspecified, and ethics not mentioned.**
  - There are no dates, participant count, tested build, test content or observations.
  - Video was recorded, but there is no word on consent or storage.
  - The planned 6–10-student study has no ethics or consent step.
  - IDs: `crit-management-PM-2`, `qa-QA-1`, `crit-management-PM-6`, `qa-QA-2`, `official-added-1`; uncertain: `crit-accuracy-ACC-15`.
- **Private evidence references [6]–[8]** are the most-cited sources and look like publications. IDs: `counts-added-1`, `floating-added-1`, `literature-LIT-1`, `crit-literature-LR-5`, `crit-report-QR-8`, `qa-QA-5`, `crit-accuracy-added-1`, `official-added-3`.
- **16 pages against the official "10-15".**
  - Dropping p.16 alone gives 15 pages (variant v1).
  - Prose de-duplication plus flexible floats gives 14 (v3/v4).
  - Cropped screenshots give 15 (v6).
  - IDs: `crit-report-QR-2`, `official-OFF-2`; cut list in the `crit-report` notes (5.1).
- **No explicit problem statement; objectives not measurable or traced.** Objective 1 has no selection rationale. IDs: `crit-problem-PU-1`, `crit-problem-PU-2`, `crit-problem-PU-3`, `official-OFF-7`, `contributions-CONTRIB-5`.
- **Literature review is thin, dated and descriptive.**
  - The newest peer-reviewed work is from 2012, and the work is not positioned against other systems.
  - VS Code is not credited as V10's precedent, and visualgo.net is not cited.
  - The literature counts under Understanding (30%).
  - IDs: `literature-LIT-2/3/7/8/9`, `literature-added-1..4`, `crit-literature-LR-1..6`, `crit-problem-PU-8`, `official-OFF-5`.
- **Technical contribution not stated crisply.** Decisions are given as WHAT with little WHY, although the 95 decision records have the reasons. Validation is not tied to the risks it addresses, and the scale of the work is undersold. IDs: `crit-technical-TA-1..4`, `qa-QA-9`.
- **Project management.** Table 5 ignores the 7 Apr 2027 final-report deadline. Challenges are not presented as real problems. Process evidence is invisible to the Main Evaluator. IDs: `crit-management-PM-1`, `official-OFF-3`, `crit-management-PM-3`, `official-OFF-6`.
- **Presentation:**
  - Caveats are repeated 13 times (`crit-report-QR-3`).
  - Screenshot text prints at about 3–4 pt (`QR-4`).
  - Most figures and tables are never referenced in the text (`QR-5`, `algorithms-added-1`).
  - Abbreviations are left unexpanded (`QR-6`).
  - Evidence-bookkeeping sentences sit in the body (`QR-7`, `official-added-2`, `crit-accuracy-ACC-3`).
  - One feature goes by four names (`floating-FT-3`, `crit-accuracy-ACC-13`).

**Candidate top 5 (my preliminary ranking; the next session should confirm or adjust it):**

1. Remove every "draft" marker.
2. Fix the Week 10 and floating-text passage: date it, cite the addendum instead of [8, 6], make the chronology fit 23 Oct, and add consent and ethics. This needs Bao's answers.
3. Correct the factual inaccuracies above.
4. Make the evidence reachable and reach ≤ 15 pages.
5. Add a problem statement and measurable objectives, and cut the repeated caveats.

### 6.2 Index of confirmed findings *(generated; full text with evidence in Appendix A)*

{{GEN_INDEX}}

---

## 7. Technical Details, References, and Relevant Files

### 7.1 Paths (Bao's Windows machine)

| What | Path | In the cloud? |
|---|---|---|
| Evidence pack, report and this handoff | `C:/Users/123ba/nuss/OneDrive - National University of Singapore/workplace/vstudio/learn/code/docsforfyp` = `BJoozz/docsforfyp` | Yes, after commit and push; it needs access to a private repo |
| App repo | `C:/Users/123ba/nuss/OneDrive - National University of Singapore/workplace/vstudio/learn/code/visualgo-plus-design` = `kerktaiheng/visualgo-plus-design` at `662e7b3` | Yes, by clone |
| Standalone clones | `C:/Users/123ba/AppData/Local/Temp/fyp-repos/{graph-algorithm-visualizer, graph-visualizer-v2, tree-visualizer, sorting-algorithm-visualizer}` | Re-clone from BJoozz's GitHub if needed |
| Session scratchpad (review work files, page PNGs, agent downloads) | `C:/Users/123ba/AppData/Local/Temp/claude/c--Users-123ba-...-visualgo-plus-design/dd1448ed-3ceb-4759-a934-c360d565fa8f/scratchpad/` | **No.** What matters was copied to `docs/fyp-audit-artifacts/` |
| Review journal (raw) | `~/.claude/projects/c--Users-123ba-...-visualgo-plus-design/dd1448ed-3ceb-4759-a934-c360d565fa8f/subagents/workflows/wf_976de5d7-7c7/journal.jsonl` | **No.** Its content is in `fyp-audit-panel-results.json` |
| Evidence-pack workflows | runs `wf_62a7f64d-5a9` (phase 1), `wf_092b4e1f-d18` (failed), `wf_6f7d66ee-c39` (phase 2) | **No.** Their outputs are the docsforfyp files |
| Memory | `~/.claude/projects/c--Users-123ba-...-visualgo-plus-design/memory/` (`fyp-evidence-audit.md`, `ai-work-is-owners.md`, `miktex-local-build.md`, `codex-plans-unreviewed.md`, `verify-reviews-before-fixing.md`, ...) | **No.** Their FYP-relevant content is in sections 2–3 |

### 7.2 Files preserved with this handoff (`docsforfyp/docs/`)

- **`FYP_AUDIT_HANDOFF.md`:** this file.
- **`fyp-audit-panel-results.json`:** all raw panel results. The `tasks` key holds the slice descriptions. `finder.<slice>` holds findings, positives and notes. `verifier.<slice>` holds verdicts and the added findings. `derived.{confirmed, uncertain, refuted, positives}` holds the merged lists, sorted. `failed` lists the failed agent.
- **`fyp-audit-artifacts/official/`:**
  - The CA guideline (PDF and text) and the CA evaluation form (text, extract PDF, and page images `CA-Evaluation-Form-2026-02-pages/form-1..9.png`).
  - The Registrar calendar (PDF and text), the text of the SoC FYP pages, and `nusmods-cp4101.json`.
- **`fyp-audit-artifacts/cut-list/`:**
  - `variants.py` builds the variants: `python variants.py <report_dir> <out_root>`.
  - `variants/*.tex` holds the six compiled variants; `PAGES.txt` gives v1 15, v2 15, v3 14, v4 14, v5 15 and v6 15 pages.
  - Helper scripts: `pngrows.py`, `inkrows.py` and `hedges.py`.
  - The variants were built from the 16-page source and are **proposals only**.
- **`fyp-audit-artifacts/factcheck/`:** the live test logs of 11-04 (`graph-test.log`, `vitest.log`, `lint.log`), the CI run list `runs.json`, and two counting scripts.
- **`fyp-audit-artifacts/report-snapshot/report-pages-16p.txt`:** the reviewed PDF as text with page markers. All panel page numbers refer to it.
- **Generator files:** `gen-handoff.js`, `assemble.js`, `head.md` and `mid.md` (the first handoff version's hand-written parts).
- **Not copied:** downloaded papers (copyrighted; URLs are in the findings), the 640 KB CI log, the 912 KB vitest JSON, the page PNGs and the variant PDFs. All can be regenerated.

### 7.3 Official NUS requirements (verified by the `official` slice; copies in `official/`)

| Source | Content |
|---|---|
| [CA Report Guidelines (Oct 2022)](https://www.comp.nus.edu.sg/wp-content/uploads/2023/10/FYP_CA_Report_Guidlines_Oct_22.pdf) | "The CA Report is a short report (10-15 pages) that covers: project title; project objectives description; literature review; progress made so far (perhaps covering design/investigation alternatives, and thoughts on preliminary design/investigation); and research plan for the next semester. list of references." Softcopy to the supervisor **and** the Main Evaluator by Wednesday of Week 12. It does not say whether the cover or references count. It sets no format or AI rule. |
| [Report Writing page](https://www.comp.nus.edu.sg/programmes/ug/project/fyp/report/) | CA = 30% of the final grade (supervisor 15%, Main Evaluator 15%). Title changes go through the Project Update Form. |
| [CA Evaluation Form (2026-02)](https://www.comp.nus.edu.sg/wp-content/uploads/2026/02/CA-Evaluation-Form.pdf) | **Supervisor:** Understanding of the problem 30%, Technical Achievement 40%, Effort and Initiative 20%, Report 10%. **Main Evaluator:** Understanding 30%, Technical 40%, Project and Resource Management 10%, Report and Discussion 20%. The literature review counts under Understanding. Technical Achievement starts with "Formulation and problem statement". A or A+ only with justification. The form text confirms the weights (lines 24, 41, 62, 72, 139, 158, 177, 193). |
| [AY26/27 FYP timeline](https://www.comp.nus.edu.sg/wp-content/uploads/2026/05/to-uploadFYP-Term2610-start-TIMELINE_FOR_FYP_PRESENTATION_AND_REPORT_SUB.rtf_-1.pdf) | CA report 4 Nov, 17:00; CA presentation in Reading Week (Bao arranges it). Final report **Wed 7 Apr 2027, 17:00**; presentation 19–23 Apr (tentative); e-copy 10 May 2027. |
| [Registrar AY2026/27 calendar](https://nus.edu.sg/registrar/docs/default-source/calendar/ay2026-2027.pdf) | Week 1 10–14 Aug 2026; recess 19–27 Sep; **Week 10 19–23 Oct**; Week 12 2–6 Nov; Reading Week 14–20 Nov; exams 21 Nov – 5 Dec. Sem 2 Week 1 is 11–15 Jan 2027. |
| AI use | No CP4101 rule. NUS Libraries: "you should always acknowledge the use". The CTLT policy PDF could not be fetched. |
| [Final Report format](https://www.comp.nus.edu.sg/wp-content/uploads/2023/10/FYP-Report-Format-final_000.pdf) | Final report only (≤ 55 pages, 12 pt, APA). **Not** binding for the CA. |
| Not checked | Registered title and project number (needs an NUS login); the Main Evaluator's name. |

### 7.4 Building the PDFs

- **Bao's machine:** MiKTeX 25.12, at `C:\Users\123ba\AppData\Local\Programs\MiKTeX\miktex\bin\x64`, on the user PATH.
- **Cloud:** TeX Live with `latexmk`, `xelatex`, DejaVu fonts (`fonts-dejavu` or `texlive-fonts-extra`), and the packages used by `main.tex` and `vi/style.tex` (geometry, booktabs, tabularx, enumitem, float, xcolor, tikz, caption, fancyhdr, titlesec, hyperref, microtype, lmodern, needspace, placeins, fontspec).
- **Build outside OneDrive** (copy `report/` to a temp folder), then copy the PDFs back:

```sh
cd report && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex     # → main.pdf; rename for submission (drop "Draft")
cd report/vi && latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=VisuAlgo_CA_Report_VI full.tex
cd report/vi && latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=VisuAlgo_CA_Summary_VI summary.tex
```

- **After building, check:**
  - The page count, with `pdfinfo`.
  - The log for `undefined` and `Overfull`.
  - `pdftotext` output, grepped for "Draft".
  - Page renders (`pdftoppm -r 60`), to spot nearly empty pages.

---

## 8. Remaining Tasks and Priorities

Bao is the one who submits, before **17:00 SGT today**. Everything below serves that.

1. **Ask Bao the blocking questions (section 9.1), in Vietnamese,** with the evidence links and options. Questions 1–6 decide the Week 10, consent, supervisor and evidence-access wording.
2. **Finish the synthesis the failed agent should have produced** (deliverable 1.3/1).
   - Deduplicate `derived.confirmed`.
   - Write the review with the top 5 and the claim table. The claim table can use the MATCH items in the fact-check notes.
   - **Do not re-run the finders or verifiers.**
3. **Re-check each finding before acting on it,** in the repos rather than the scratchpad. This applies above all to the 34 "added by a verifier" items, 6 of them Important.
4. **Agree the fix list with Bao,** offering options for each. He decides the wording about his account, the trial, the supervisor, Kerk's credit, the cuts and the title.
5. **Apply the approved edits.**
   - Edit `report/main.tex`, then mirror the edits into `report/vi/full.tex` and `report/vi/summary.tex`.
   - Rebuild (7.4) and check: ≤ 15 pages; no "Draft" in the cover, header, metadata or file name; no undefined references; figures readable.
   - Update `report/README.md` and the addendum.
6. **Commit only when Bao asks, and only by explicit paths.** Do not push unless told.
7. **Bao submits** the softcopy to Prof Halim and the Main Evaluator by 17:00.
8. **Afterwards: the CA presentation in Reading Week (14–20 Nov).** Use the `qa` notes (slice 15 in 5.1): likely questions, slide outline and demo script.

---

## 9. Unresolved Questions and Risks

### 9.1 Questions only Bao can answer

1. **Week 10 session dates.** On which dates between Mon 19 and Fri 23 Oct were the sessions held? Were all of them before the floating-text request on 23 Oct (PR #29 opened 13:36)? If not, "Following the Week 10 trial" and "post-trial" must soften to "during Week 10, alongside the trial". (`timeline-TL-1`, `floating-FT-1`)
2. **Tested build.** Was it the public Pages site, and on which day, or a local build at which commit? (`timeline-TL-1`)
3. **Trial details.** Can the report give a participant count and one or two concrete observations? Or must it stay "several users"? (`crit-management-PM-2`, `qa-QA-1`)
4. **Consent.** Did participants consent to video? Should the report say ethics review will be confirmed with the supervisor before the follow-up study? (`crit-accuracy-ACC-15`, `official-added-1`)
5. **The supervisor's part.** Was he part of the V10 decision, and of the "canvas-focused goal" behind floating text? Both rest only on Bao's 3–4 Nov account. (`contributions-CONTRIB-3`, `crit-accuracy-ACC-5`)
6. **Evidence access.** Will examiners get access to `BJoozz/docsforfyp`? Or should [6]–[8] be replaced by the public app link and an appendix, or dropped from sentences? (`literature-LIT-1`, `crit-report-QR-8`, `qa-QA-5`)
7. **Title.** Is "VisuAlgo+ / Rebuilding Interactive Algorithm Visualizations" the registered title? (`official-OFF-4`, `crit-report-QR-16`)
8. **Main Evaluator.** Who is it? The softcopy must reach them too.
9. **The `\page` macro.** Does Bao accept the uncommitted change (2.5)?
10. **Uncertain minor items:**
    - "V1 began on 28 July", when the first commit already holds a working app (`timeline-TL-5`).
    - Whether to say the parallel-edge rule deliberately differs from VisuAlgo (`crit-technical-TA-7`).
    - Whether to present any performance observation (`crit-technical-TA-9`).
11. **Still open from the evidence pack** (doc 05 §4):
    - Kerk's survey data: date, size, questions, results.
    - Which supervisor remarks to quote, and their source.
    - Whether to cite the dated profiles and run Kerk's wasm-arch suite.
    - Standalone history before the first commits.
    - Minor: PR #36's body says drag, split and splitter are all tested by hand, although PR #35 added a splitter e2e case. Bao may fix the PR text.

### 9.2 Uncertain findings *(generated)*

{{GEN_UNCERTAIN}}

### 9.3 Risks

- **Time.** The report is due at 17:00 today. Fixes must be prioritised: the Critical items, then the factual errors, then ≤ 15 pages. A full rewrite is not realistic.
- **Usage limits.** Two workflows died on usage limits (`wf_092b4e1f-d18` and this panel's synthesis). Keep any new agent work small, or do it inline.
- **Unverifiable trial claims.** There are no dates, count, data or consent record. Overclaiming here is the biggest accuracy risk; keep the wording to what Bao confirms.
- **The private repository.** A cloud session needs access to `BJoozz/docsforfyp`. Examiners cannot open it either.
- **Uncommitted work.** The 8 report files and `docs/` are uncommitted on Bao's machine. If they are not committed and pushed, the cloud sees only `c6c371e`: the 19-page source with the hard breaks, and no handoff.
- **Shared worktrees.** OneDrive, Codex and other sessions write into the same folders. Commit by explicit path, and re-read files before editing.

### 9.4 What could not be recovered or was never available

- **The synthesis agent's output** never existed, because the agent failed.
- **The Week 10 trial material** (videos, the folder screenshot Codex was given, test questions, scores) was never seen by this session.
- **Codex's own sessions** (how it wrote the report and the 4 Nov account) are not accessible; only its commits and the message Bao pasted are.
- **Bao's answer text for Q4 "Other"** (2026-11-03) never arrived.
- **The figure capture script** of 2026-11-01 was lost; `figures/README.md` has a reconstructed replay script.
- **The full transcript** is local only, at `~/.claude/projects/c--Users-123ba-...-visualgo-plus-design/dd1448ed-3ceb-4759-a934-c360d565fa8f.jsonl` (157 MB). Every user message since 2026-11-01 was read for this handoff; the October app-development messages were only skimmed via memory.
- **The CTLT AI policy PDF** and **the registered project title** were not retrievable.

---

## 10. Exact Instructions for the Next Claude Session

1. **Set up.** Clone `BJoozz/docsforfyp`, which needs access to the private repo, and check that `docs/FYP_AUDIT_HANDOFF.md` is there. If `report/main.tex` line 32 still reads `\newcommand{\page}{\clearpage}`, the 8 local report changes were not pushed: ask Bao, or re-apply the macro from 2.5. Clone `kerktaiheng/visualgo-plus-design` and check out `662e7b3` for any code check. **Do not edit the app repo.**
2. **Read sections 1–9,** then load `docs/fyp-audit-panel-results.json` (structure in 7.2). The full findings with evidence are in Appendix A.
3. **Talk to Bao in Vietnamese.** Start with the questions in 9.1, giving each with its evidence (file and line, commit, PR link) and options. Bao asked for exactly that.
4. **Produce the synthesis review** (deliverable 1.3/1) from the JSON. Do not spawn a new research panel. If agents are needed, use Opus at max effort, keep them few, and make each one narrow.
5. **Before proposing any fix, reproduce the finding** in the repo. Before editing the report, get Bao's choice. Never invent trial data, quotes, counts or scores. Never re-open the settled facts in 3.3. Mention AI use at most once (the report already does, on p.5).
6. **After edits,** rebuild and check as in 7.4. Keep the English and Vietnamese versions in sync, and record what changed in `report/README.md`.
7. **Commit only on request, by explicit paths, in English,** ending with the attribution line the harness gives. Do not push unless told.

**Mistakes and rejected approaches not to repeat:**

- **Hard `\clearpage` breaks** tuned to one version of the text inflate pages after edits. Use the conditional macro or flexible floats, and re-check the page count after every edit.
- **Large agent fan-outs** died twice on usage limits. Prefer inline work or small batches near the deadline.
- **Docker for LaTeX** was rejected in favour of a direct TeX install.
- **Attribution scaffolding** (decider tags, "QUESTION who decided", trailer caveats) was rejected by Bao.
- **Never treat a Codex plan or review as Bao's agreement.**
- **Describe a screenshot only from what it shows.** One note once said F2 showed "No active run"; it actually shows BFS at frame 8/22. View PNGs before captioning.
- **Do not cite the pinned evidence snapshot `67ce56c`** for anything about the Week 10 trial; it says there was none.
- **Shell quoting in tool commands.** In this environment a doubled backslash typed into a shell command arrives single, and an apostrophe breaks single-quoted `node -e` scripts. Put scripts with backslashes or quotes in files.
- **Playwright** (if screenshots must be recaptured): pass `--output` outside OneDrive. Blank pages may be Chromium's `ERR_NETWORK_CHANGED` rather than a code bug. Do not touch port 5186 if a server is already there.

---

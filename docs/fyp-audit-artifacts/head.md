# FYP CA Report Audit: Handoff

**Written:** 2026-11-04, about 11:40 SGT, in the local Claude Code session. The owner paused the review at that point so it can move to a Claude Code Cloud session.
**Deadline that still applies:** the CP4101 CA report is due **today, 2026-11-04, 17:00 SGT**. It goes as a softcopy to the supervisor and the Main Evaluator.
**State in one line:** the review panel finished its research and verification (30 of 31 agents). Its final synthesis agent failed on a usage limit, so no merged review, top 5 or claim table exists yet. Nobody has edited the report because of the panel.

Every finding in this file is copied from the agents' returned data by a script ([`fyp-audit-artifacts/gen-handoff.js`](fyp-audit-artifacts/gen-handoff.js)), not retyped. To keep Markdown tables and bullets intact, the generated text replaces every `|` with `/` and every line break with a space; the JSON keeps the exact text. Sections 0 to 8 were written by hand. Section 9 onward and the appendices are generated. The complete raw results are in [`fyp-audit-panel-results.json`](fyp-audit-panel-results.json).

---

## 0. Read this first (next Claude session)

1. **Do not re-run the research.** The JSON archive holds all 15 finder results and all 15 verifier results. Use it; do not spawn a new panel.
2. **The handoff files are not committed yet.** They sit in the local working copy of `BJoozz/docsforfyp` under `docs/`. A cloud session sees them only after the owner commits and pushes them, or pastes them in. The same working copy also has **8 uncommitted report changes** from earlier today (section 2.5). Commit by explicit path so the two sets stay separate.
3. **Paths inside the findings are Windows paths on Bao's machine.**
   - `C:/Users/123ba/nuss/OneDrive - National University of Singapore/workplace/vstudio/learn/code/docsforfyp` is the root of `BJoozz/docsforfyp`.
   - `.../code/visualgo-plus-design` is the app repo `kerktaiheng/visualgo-plus-design`.
   - Anything under `C:/Users/123ba/AppData/Local/Temp/...` (the scratchpad) is **not** available to a cloud session. The only exception is what was copied to `docs/fyp-audit-artifacts/` (section 2.8).
4. **Before you change the report because of a finding, reproduce that finding.** This is the owner's standing rule. Then offer fix options and let Bao choose. Never edit report wording on a point that is Bao's call (section 6) without his answer.
5. **Write to Bao in Vietnamese.** Keep technical terms, file names and quoted report text in English. Ask with concrete options and links. He has asked that open questions always come with explanations, links and options.

---

## 1. Original task and objectives

### 1.1 The owner's request (2026-11-04, after the PDFs were rebuilt)

Translated from Vietnamese: *"Run an overall re-check. Cross-check against the commits and files to see whether any content is inaccurate, and ask me if something needs confirming. Also say what should be added or cut."* He then pasted this review brief, which is reproduced verbatim:

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

### 1.2 How the review was run

One workflow ran on Opus at max effort: `ca-report-review`, run `wf_976de5d7-7c7`.
- **Find:** 15 finders, each with one slice. Eight checked facts: timeline, numbers, architecture, algorithms and figures, floating text, contributions, literature, official NUS rules. Seven reviewed criteria: problem, technical, literature, management, report quality, accuracy, presentation Q&A.
- **Verify:** for each finder, an adversarial verifier tried to refute every finding against the same sources. It marked each one CONFIRMED, REFUTED or UNCERTAIN, corrected its severity, page and fix, and added findings the finder missed.
- **Synthesize:** one agent was to merge everything into a Vietnamese review. **It failed** ("You've hit your 5-hour limit · resets 2:40pm (Asia/Singapore)").
- Severity scale given to the verifiers: **Critical** misleads the evaluator or breaches a requirement; **Important** noticeably weakens a criterion; **Minor** is polish.
- Every finding carries a basis label. VERIFIED means checked in code, git, PNG or the web. DOCUMENTED means a project document or the owner says so. INFERENCE means reasoning.

### 1.3 Earlier work in the same session (context, done)

- **Evidence pack, done 2026-11-03.** Five documents `01_..05_*.md`, `evidence/` and `figures/` in this repository. The owner's 16 answers of 2026-11-03 are applied.
- **CA report, written by Codex.** Codex wrote it into `report/` and committed it directly: `675fc73` (draft), `089ef85` (Vietnamese translation and summary), `c6c371e` (Week 10 trial and floating-text rationale, 2026-11-04 09:37).
- **PDFs rebuilt locally on 2026-11-04.** I rebuilt all three PDFs (section 2.5). This is not yet committed.

---

## 2. Project context

### 2.1 People

- **Truong Van Quoc Bao ("Bao"),** A0276275U, GitHub `BJoozz`. He is the student and the owner of this audit. Both of his git identities are his: `BJoozz <123baoek31@gmail.com>` and the GitHub no-reply address.
- **Kerk Tai Heng.** A fellow CP4101 student with the same supervisor. He works on the engine/WASM foundation (`wasm-arch/`), the website design system, shared infrastructure and the one-app consolidation of 2026-10-18 (`0394b64`).
- **A/P Steven Halim.** The supervisor and the creator of VisuAlgo.
- **Main Evaluator:** name not known (not in the evidence pack; needs an NUS login).

### 2.2 Repositories and snapshots

| What | Where | State |
|---|---|---|
| Application | `kerktaiheng/visualgo-plus-design`, branch `main` | `662e7b3`, the report's "application snapshot"; clean. 282 commits on all refs (267 on main), 37 PRs, app in `prototypes/` |
| Evidence pack and report | `BJoozz/docsforfyp` (**private**; only BJoozz has access) | HEAD `c6c371e` plus uncommitted changes (2.5). The report pins the evidence snapshot `67ce56c`. `git diff 67ce56c c6c371e` touches only `report/` |
| Standalone pre-integration repos | local clones in `C:/Users/123ba/AppData/Local/Temp/fyp-repos/` (graph V1, graph-visualizer-v2, tree-visualizer, sorting) | read-only; dates are in evidence doc 01 and research note 02 |

### 2.3 Report files (in `BJoozz/docsforfyp/report/`)

- `main.tex`: the English report (pdfLaTeX). Output `VisuAlgo_CA_Report_Draft.pdf`. **16 pages:** cover p1, body p2–15 (references on p15), back matter p16.
- `vi/full.tex` and `vi/summary.tex`: Vietnamese reading aids (XeLaTeX with DejaVu fonts, shared `vi/style.tex`). Outputs are 21 and 4 pages.
- `references.bib`: 9 entries. Three are self-citations of the evidence pack ([6] to [8]).
- `figures/`: 7 screenshots F1–F4 and F6–F8, captured at 1440×900 from `662e7b3`. Figures 1 and 2 are TikZ diagrams in `main.tex`.
- `week10_user_trial_addendum.md`: the **only written source for the Week 10 user trial.** It records Bao's account of 4 November and a screenshot of a shared folder, "VisuAlgo+ Prototype Testing Footage". It says the dates, the participant count, the tested build, the questions and the scores are still to be documented.
- `README.md`: build steps and a pre-submission checklist. It already says to remove the "Draft" markers.
- A page-annotated text snapshot of the 16-page PDF that the panel reviewed is in [`fyp-audit-artifacts/report-snapshot/report-pages-16p.txt`](fyp-audit-artifacts/report-snapshot/report-pages-16p.txt). All panel page numbers refer to it.

### 2.4 Building the PDFs

- **Bao's machine:** MiKTeX 25.12 for the current user, with packages installing automatically.
- **Cloud:** any TeX Live (the original PDFs came from TeX Live 2023 pdfTeX) with `latexmk`, `xelatex` and `fonts-dejavu` or `texlive-fonts-extra`.
- The same source gives the same page count on both, which was checked.

```sh
# from report/
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex      # then copy main.pdf to VisuAlgo_CA_Report_Draft.pdf (or a new final name)
# from report/vi/
latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=VisuAlgo_CA_Report_VI full.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -jobname=VisuAlgo_CA_Summary_VI summary.tex
```

### 2.5 Uncommitted changes in `BJoozz/docsforfyp` (made earlier today; the owner decides)

There are 8 modified files: three PDFs, `main.tex`, `vi/style.tex`, `vi/full.tex`, `README.md` and `vi/README.md`.

- **The page-break problem.** Codex's sources used 14 hard `\clearpage` breaks, each written `\page`, tuned to the older and shorter text. After the Week 10 additions they left three almost empty pages, and the English PDF grew from 15 to 19 pages.
- **The macro change.** `\page` now breaks only when the page is more than 72% full: `\par\penalty0 \ifdim\pagetotal>.72\textheight\clearpage\else\vspace{8pt}\fi`. It is defined in `main.tex` line 32 and `vi/style.tex`. The five `\clearpage` lines in `vi/full.tex` now use `\page`. No text changed.
- **Result:** English 16 pages, Vietnamese full 21, Vietnamese summary 4.
- **The READMEs** now record the rebuild instead of saying "PDF is stale".
- **Status:** none of this is committed. The panel reviewed this 16-page build. Bao has not yet been asked to approve the macro change explicitly.

### 2.6 Settled facts: do not re-litigate (owner's dated answers, 2026-11-01 and 11-03)

- **AI-assisted work is Bao's own.** It was done under his requests, choices and confirmation. The report discloses AI use once, on p.5, and that is enough.
- **V10 choices.** Choices 27 to 48, the "V10 wins" changes, `40a63bd` and `a074f50` were decided by Kerk and Bao together and implemented by Kerk. Choices 1 to 26 are Bao's.
- **V2 and V7.** Kerk and Bao chose them together **after** a user-group survey that Kerk organised, out of the nine layouts in Kerk's wireframe. Bao holds no record of the survey.
- **visualgo.net material.** Prof Halim knows of its use and agrees.
- **Engine study.** It was Bao's own idea, parked by his choice so he could focus on the visualizers.
- **Manual checklists.** They were run by hand and by agents; nothing was recorded.
- **The three late-October review sessions.** Codex reviewed, Bao read the findings first, Claude verified each one, and Bao chose the fixes.
- **Records that name no person** are implementer's defaults that Bao accepted, so they are his decisions.
- **Week 1 of Semester 1.** It is Mon 10 Aug 2026, now confirmed by the Registrar calendar.

### 2.7 Official NUS requirements (verified by the `official` slice, with URLs; preserved copies in `fyp-audit-artifacts/official/`)

| Source | What it says |
|---|---|
| [CA Report Guidelines (Oct 2022)](https://www.comp.nus.edu.sg/wp-content/uploads/2023/10/FYP_CA_Report_Guidlines_Oct_22.pdf) | "The CA Report is a short report (10-15 pages) that covers: project title; project objectives description; literature review; progress made so far (perhaps covering design/investigation alternatives, and thoughts on preliminary design/investigation); and research plan for the next semester. list of references." Softcopy to the supervisor **and** the Main Evaluator by Wednesday of Week 12. It does not say whether the cover or references count toward the pages. It sets no rule on format or AI use. |
| [Report Writing page](https://www.comp.nus.edu.sg/programmes/ug/project/fyp/report/) | CA is 30% of the final grade: 15% from the supervisor and 15% from the Main Evaluator. Title changes go through the Project Update Form. |
| [CA Evaluation Form (2026-02)](https://www.comp.nus.edu.sg/wp-content/uploads/2026/02/CA-Evaluation-Form.pdf); text in `official/CA-Evaluation-Form-2026-02.txt`, page images in `official/CA-Evaluation-Form-2026-02-pages/` | **Supervisor form:** Understanding of the problem 30%, Technical Achievement 40%, Effort and Initiative 20%, Report 10%. **Main Evaluator form:** Understanding 30%, Technical 40%, Project and Resource Management 10%, Report and Discussion 20%. So the brief's "Project Management 10–20%" needs correcting: management is 10% and appears only on the Main Evaluator's form. The literature review counts under Understanding (30%). A or A+ may be ticked only with written justification. |
| [AY26/27 FYP timeline](https://www.comp.nus.edu.sg/wp-content/uploads/2026/05/to-uploadFYP-Term2610-start-TIMELINE_FOR_FYP_PRESENTATION_AND_REPORT_SUB.rtf_-1.pdf) | Semester 1: CA report due 4 Nov, 17:00; CA presentation during Reading Week. Semester 2: final report due **Wed 7 Apr 2027, 17:00**; presentation 19–23 Apr (tentative); e-copy 10 May 2027. |
| [NUS Registrar AY2026/27 calendar](https://nus.edu.sg/registrar/docs/default-source/calendar/ay2026-2027.pdf) | Week 1 is 10–14 Aug 2026. Recess runs 19–27 Sep. **Week 10 is Mon 19 to Fri 23 Oct 2026.** Week 12 is 2–6 Nov. Reading Week is 14–20 Nov. Exams run 21 Nov to 5 Dec. |
| AI use | No SoC CP4101 page, guideline or form contains an AI rule. NUS Libraries says "you should always acknowledge the use". The CTLT AI policy PDF could not be fetched. |
| Not checked | The registered project title and project number, and the Main Evaluator's name. |

The `crit-report` agent could not read the form's weight tables, which are images. The `official` agent read them. The preserved text extract confirms 30/40/20/10 and 30/40/10/20 (`CA-Evaluation-Form-2026-02.txt`, lines 24, 41, 62, 72, 139, 158, 177 and 193).

### 2.8 Artifacts preserved with this handoff (`docs/fyp-audit-artifacts/`)

- **`official/`:** the CA guideline (PDF and text), CA form text and page images, the Registrar calendar (PDF and text), text of the SoC FYP pages, and the NUSMods CP4101 record.
- **`cut-list/`:**
  - `variants.py` builds the cut-list variants from `main.tex`: `python variants.py <report_dir> <out_root>`.
  - `pngrows.py`, `inkrows.py` and `hedges.py` are the helper scripts the agents used.
  - `variants/*.tex` holds the `crit-report` agent's six compiled variants; `variants/PAGES.txt` records each one's page count. v1 (drop the p16 back matter) gives 15 pages. v3 and v4 (prose de-duplication plus flexible floats) give 14. v6 (cropped screenshots) gives 15.
  - The variants were built from the 16-page source of 2.5. **They are proposals, not applied.**
- **`factcheck/`:** the `counts` agent's live test runs on 2026-11-04 (`graph-test.log`: 654/654; `vitest.log`: 2,619/2,619; `lint.log`: 0 errors and 2 warnings). It also holds `runs.json` (the CI run list) and the two counting scripts.
- **Not copied:** the downloaded papers (copyrighted; their URLs are in the findings), the 640 KB CI log (run `41095633732` at `662e7b3`), and the vitest JSON (912 KB).

---


# 01 · Scope and timeline: Bao's VisuAlgo+ work, 2026-07-28 to 2026-10-31
Audit date: 2026-11-01/02 · CA report due **2026-11-04 17:00 SGT**, softcopy to the Supervisor and the Main Evaluator\
Repository: `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3`\
Evidence labels: VERIFIED / DOCUMENTED / INFERENCE / QUESTION\
The owner's answers of 2026-11-01 are applied (Q1 to Q4; part of Q6 and Q7; Q5 unanswered); what they leave open stays QUESTION.

**Reading notes**

- VERIFIED = seen in git, a diff, a GitHub API answer or a test run. DOCUMENTED = a doc, commit message, PR body or the owner's answer says it. INFERENCE = a reading of the evidence. QUESTION = Bao must answer. Question ids Q1 to Q17 and contribution ids C1 to C14 are those of [09].
- "Bao" means the two BJoozz git identities; that both author strings are his is still Q2 (section 1.3). "Kerk" means Kerk Tai Heng's two identities.
- Dates are git author dates in the author's own time zone (+07:00 or +08:00). GitHub PR times are UTC, so a PR can look a day earlier than its merge commit.
- [01] to [09] are the phase-1 notes in `evidence/research-notes/`. Every hash, date and author below was re-checked in git on 2026-11-02 (all but `03bfaa3`, which only the GitHub API shows [01]), and the GitHub facts through the API the same day. Commit counts are context, never a measure of effort or ownership.

**How the owner's answers are applied**

| Q | Owner's answer, 2026-11-01 (DOCUMENTED) | Applied here |
|---|---|---|
| Q1 | The FYP is NUS AY2026/27 Semester 1. All work from the first standalone commit (2026-07-28) through the summer is "week 0" and in scope; the FYP proper began in August 2026 | Scope 2026-07-28 to 10-31; week 0 = from 2026-07-28 to the FYP's start in August, so at least 07-28 to 07-31; the start date stays QUESTION |
| Q2 | `123baoek31@gmail.com` and the BJoozz account are Bao's; he will confirm both author strings first | Attribution stays QUESTION (section 1.3) |
| Q3 | Kerk is a fellow FYP student on the same project and supervisor. A working description, not a formal assignment: Kerk the engine/WASM work and the web, cache and cloud infrastructure; Bao the three visualizers and their integration into the shared interface; both students and the supervisor intervened in each other's choices | Section 2.3, which also sets out whose V10 choices are whose; the decider is kept apart from the implementer |
| Q4 | AI use may be described briefly; what Bao did himself in reviewing and testing must be verified first | Counts only (section 1.4) |
| Q5 | Not answered | Records that name no person stay QUESTION |
| Q6, Q7 (part) | The supervisor is A/P Steven Halim; the current direction must not be presented as his assignment or feedback without evidence | Named only; no remark of his is quoted |

## 1. Repositories, branches, identities and coverage

### 1.1 The five repositories

All five are private on GitHub. VERIFIED (clone logs and the GitHub API, 2026-11-02).

| Repository | Created on GitHub | First commit | Last commit | Commits (all refs / `main`) | PRs | What it is |
|---|---|---|---|---|---|---|
| [`kerktaiheng/visualgo-plus-design`](https://github.com/kerktaiheng/visualgo-plus-design) | 2026-09-03 | `634b5be` 2026-09-03 (Kerk) | `662e7b3` 2026-10-31 (merge of PR #37) | 282 / 267 | 37 | The shared VisuAlgo+ repository, owned by Kerk; Bao has write access, not admin. Kerk's design system, wireframes and `wasm-arch/` engine; the one app in `prototypes/` (`src/site`, `src/graph`, `src/tree`, `src/sorting`, `src/shared`) |
| [`BJoozz/graph-algorithm-visualizer`](https://github.com/BJoozz/graph-algorithm-visualizer) | 2026-07-28 | `f3a0db8` 2026-07-28 | `5fc06a0` 2026-08-19 | 55 / 24 | 8 | Graph V1 (`package.json` name `js-ts-learning`): BFS, DFS, Dijkstra, Edmonds-Karp with minimum cut, Kruskal. Never copied into VisuAlgo+ |
| [`BJoozz/sorting-algorithm-visualizer`](https://github.com/BJoozz/sorting-algorithm-visualizer) | 2026-08-19 | `9236a65` 2026-08-19 | the same (one squashed commit) | 1 / 1 | 0 | "Sorting Room": 8 algorithms recorded as typed operations, 1, 2 or 4 panes, a Canvas renderer, a profiler |
| [`BJoozz/graph-visualizer-v2`](https://github.com/BJoozz/graph-visualizer-v2) | 2026-09-03 (history from 08-20) | `92fa193` 2026-08-20 | `c8b14e6` 2026-09-11 | 53 / 52 | 14 | A rewrite of V1: separate state owners around one persistent canvas; records DD-01 to DD-22 |
| [`BJoozz/tree-visualizer`](https://github.com/BJoozz/tree-visualizer) | 2026-09-03 | `e687099` 2026-09-03 | `46ce0a7` 2026-09-17 | 50 / 50 | 8 | Six rooted-tree workspaces: LCA (Binary Lifting), BST, AVL, Min Heap, Trie, Segment Tree |

Also relevant: Bao's private fork [`BJoozz/visualgo-plus-design`](https://github.com/BJoozz/visualgo-plus-design) (created 2026-09-28; its 7 branches equal origin's; it carried the Vercel commits behind PR #5), and the private `BJoozz/visualgo`, a copy of visualgo.net's source that the sample graphs cite (`prototypes/src/graph/algorithms/visualgoExamples.ts:5`; not read). GitHub Pages deploys the app at <https://kerktaiheng.github.io/visualgo-plus-design/>. The Pages site is public although the repository is private; `/` and `/engine/` answered HTTP 200 on 2026-11-02 (VERIFIED by `curl`; not opened in a browser).

### 1.2 Branches

Origin has 38 branches: `main` and 37 others, the same list as `evidence/inputs/branches.tsv`. Merge status comes from `git merge-base --is-ancestor` and `git cherry`, re-checked 2026-11-02. All are Bao's except `deploy-v10-pages`. VERIFIED.

| Purpose | Branches (PR) | Dates | Reached `main` by | In `main`? |
|---|---|---|---|---|
| Joining | `bj/visualization-work` | 09-13 to 09-16 | the base of PR #1 | yes |
| Engine study (C3) | `bj/engine-v2-experiment` | 09-17 | never | **no**: 4 commits found nowhere in `main` |
| V2/V7 prototypes (C4) | `bj/graph-wireframe-v2-v7` (#1), `bj/tree-wireframe-v2-v7` (#2), `bj/sorting-wireframe-v2-v7` (#3) | 09-20 to 09-27 | merges `6a621df`, `495fa73`, `ca56cef` | yes |
| Site (C5) | `bj/visualgo-web-site` (#4) | 09-28 | merge `9cc009f` | yes |
| Pushed to `main` with no merge commit | `bj/visualgo-web-editors` (#6, empty body), `bj/segment-tree-lazy`, `bj/bst-avl-operations`, `bj/uiux-pass-1`, `bj/dock-drop-zones` (no PR) | 09-29 to 10-15 | 90 commits on `main`'s first-parent line | yes |
| First PR round | `bj/fix-traversal-ci` (#7), `bj/sssp-end-node` (#8, #9), `bj/live-layout-off` (#10), `bj/footer-centre-transport` (#11), `bj/final-frame-motion` (#12), `bj/visualgo-samples` (#13), `bj/node-label-fit` (#14) | 10-14 to 10-17 | merge commits | yes |
| V10 shell (C6) | `bj/viz-shell-v10` (#15), `bj/faint-scrollbars-trim-hints` (#16), `bj/v10-review-fixes` (#17, merged by Kerk) | 10-16 to 10-18 | merges `c899b69`, `f286712`, `b9ec8fa` | yes; the extra commit `46234cd` on `bj/viz-shell-v10` is in `main` as the same patch `9bf60f6` |
| Kerk's deployment (C14) | `deploy-v10-pages` (#18) | 10-18 | merge `94cdaf3` | yes. Kerk's branches for #19 to #21 are gone from origin; their commits are in `main` |
| Tree features (C8, C10) | `bj/tree-centre-edges` (#22), `bj/lca-two-runs` (#23, into #22's branch), `bj/lca-hover-ancestors` (#24), `bj/heap-operations` (#25), `bj/heap-rename-ids` (#26), `bj/heap-value-rule` (#27), `bj/step-notes` (#29, #31), `bj/step-notes-2` (#30, into `bj/step-notes`), `bj/legend-trim` (#33) | 10-19 to 10-26 | merge commits | yes |
| Graph features (C7, C10) | `bj/graph-traversal-ts-bgc-cvb` (#28), `bj/dijkstra-step-notes` (#32) | 10-21 to 10-25 | merges `4621b1f`, `b5506e9` | yes |
| Reviews and docs (C13) | `bj/review-session-1` (#34), `bj/tab-strip-reveal` (#35), `bj/docs-graph-sorting` (#36), `bj/review-session-3` (#37) | 10-28 to 10-30 | merges `ad5e119`, `4dedee1`, `f58ed5f`, `662e7b3` | yes |
| - | `main` | to 10-31 | - | - |

**PRs.** 37 in all: 36 merged, and #5 (from the fork's `main`, "Configure Vercel SPA routing for both websites") closed unmerged on 2026-10-25. Bao opened 33 (#1 to #17, #22 to #37) and Kerk 4 (#18 to #21). Bao merged 31 and Kerk 5 (#17 and #18 to #21). PR #19 reached `main` through #20. VERIFIED (API).

**Local-only branches** (in the audit clone, never on origin). VERIFIED (`git cherry main`).

| Branch | Tip, date | Unique content |
|---|---|---|
| `bj/engine-package-spike` | `053064f` 09-17 | the M4a packaging spike, on top of the 4 pushed engine commits; checked out in an empty worktree folder (Q12) |
| `bj/bfs-wasm-spike` | `53d2ef4` 09-17 | one commit, "currently paused": an earlier engine-client draft (Q12) |
| `bj/vercel-spa-routing` | `c9e4598` 09-29 | `vercel.json` for the two V2/V7 sites; once the fork's `main` behind PR #5 (Q15) |
| `backup/before-reword-044908` | `d3ab325` 09-28 | none: its 5 patches are in `main` (PR #4 before its messages were reworded) |
| `bj/viz-shell-v10-stage0` | `8d4c15f` 10-17 | none: both patches are in `main` |
| `live_prototype` | `4bd9ca9` 09-16 | none: the same commit as `bj/visualization-work` |

### 1.3 Author identities

| Git author string | On `main` | Elsewhere | Whose | Label |
|---|---|---|---|---|
| `BJoozz <123baoek31@gmail.com>` | 216: 213 own commits and 3 merges of `main` into his branches (`4bd9ca9`, `876ed0d`, `6fa4981`) | all 129 local commits of the four standalone repositories; all 6 engine-study commits | the email is Bao's (owner's answer) | counts VERIFIED; attribution QUESTION (Q2) |
| `BJoozz <83776047+BJoozz@users.noreply.github.com>` | 30, all GitHub PR merge commits | 30 merges and squashes made on GitHub in V1, v2 and tree | GitHub's no-reply address for account id 83776047, which is `BJoozz` (API); the account is Bao's (owner's answer) | counts VERIFIED; attribution QUESTION (Q2) |
| `Kerk Tai Heng <taihengkerk@gmail.com>` | 17 own commits | none | Kerk | VERIFIED |
| `kerktaiheng <42596694+kerktaiheng@users.noreply.github.com>` | 4 PR merges (#17, #18, #20, #21) | none | the no-reply address of account `kerktaiheng` | VERIFIED |

So `main`'s 267 commits are Bao 246 (213 own + 33 merges) and Kerk 21 (17 + 4). By month: September, Bao 46 commits (+5 merges) and Kerk 8; October, Bao 167 (+28) and Kerk 9 (+4); none after `662e7b3`. VERIFIED.

### 1.4 AI co-author trailers and tool mentions (facts only)

| Where | Own (non-merge) commits | With `Co-Authored-By: Claude …` | Trailer names (count) | First trailer |
|---|---|---|---|---|
| graph-algorithm-visualizer | 50 | 0 | - | - |
| sorting-algorithm-visualizer | 1 | 0 | - | - |
| graph-visualizer-v2 | 38 | 20 | Fable 5.1 (16), Opus 5 (1M context) (4) | 2026-09-07 |
| tree-visualizer | 41 | 34 | Fable 5.1 (21), Opus 5 (1M context) (13) | 2026-09-12 |
| `main`, Bao | 213 | 199 | Fable 5.1 (91), Opus 5.5 (73), Opus 5 (1M context) (30), Opus 5 (4), Fable 5 (1) | 2026-09-20, `0073875` |
| `main`, Kerk | 17 | 14 | Opus 5.5 (9), Fable 5.1 (4), Opus 5 (1) | 2026-09-03, `b3e86ba` |
| Engine study (unmerged) | 6 | 4 | Fable 5.1 (3), Opus 5 (1M context) (1) | 2026-09-17 |

- No merge commit carries a trailer. Bao's 14 own commits on `main` without one: `986deba`, `c458755`, `75d9760`, `1af2c72`, `e7a44f9`, `3a6443b` and the 8 Bellman-Ford and Prim stage commits (`aef5d0b`, `0aac567`, `6417767`, `4bd0879`, `5428ed3`, `686c06b`, `65634cf`, `490e1d1`). VERIFIED.
- 30 of the 37 PR bodies contain "Generated with [Claude Code]". Codex is named in 8 commit messages on `main` and in 3 PR bodies. DD-38 and DD-39 record Bellman-Ford and Prim as planned and built with Codex, and that "the owner" has not reviewed those designs except dated choices (`prototypes/docs/graph/DESIGN_DECISIONS.md:601-602`, `:665`). VERIFIED (counts), DOCUMENTED (content).
- Agent rules files: `graph-visualizer-v2/AGENTS.md` (from its second commit `fc62e5a`, 2026-08-20) and `sorting-algorithm-visualizer/AGENTS.md` (814 lines); on `main`, `prototypes/AGENTS.md` (62 of its 70 lines Kerk's by blame) and `prototypes/docs/{graph,tree,sorting}/AGENTS.md`. VERIFIED.
- A trailer shows that a tool took part in a commit. It does not show who had the idea, who chose, who reviewed, or how much each contributed; a missing trailer does not show that no tool was used (INFERENCE). What Bao did himself in reviewing and testing is Q4.

### 1.5 Audit date and history coverage

The audit ran on 2026-11-01 (notes [01] to [09], and the test run of [07] §2 at 22:34 to 22:39 +07:00) and on 2026-11-02 (the re-checks for this document). Every command was read-only; the working tree stayed clean on `main` at `662e7b3`.

**Read**

| Source | What was read | Label |
|---|---|---|
| `kerktaiheng/visualgo-plus-design` | all 282 commits on all refs (267 on `main`), the 38 remote and 6 local-only branches; logs, key diffs and blame [01] to [08] | VERIFIED |
| Pull requests | all 37 bodies (`evidence/inputs/prs.txt`); authors, mergers, merge times and bases from the API | VERIFIED (metadata), DOCUMENTED (bodies) |
| GitHub Actions | the 266 runs of 2026-09-04 to 10-30, and the logs of the failed ones [07] | VERIFIED |
| The four standalone clones | all refs, their PR lists, docs and code [02] | VERIFIED |
| The fork `BJoozz/visualgo-plus-design` | branches, compare and events through the API [01] | VERIFIED |
| The two worktrees | their state only: 0 files on disk; `git status` lists 314 and 2,544 deletions; the commits are intact | VERIFIED |
| The deployed site | HTTP status only, on 2026-11-01 [07] and 2026-11-02 | VERIFIED (status) |

**Not read, or not accessible**

| Source | Status |
|---|---|
| PR reviews, review comments, PR comments | none exist: 0, 0 and 0 (API, re-checked 2026-11-02) |
| Issues, wiki, releases, tags | none: 0 issues, no wiki repository, 0 releases, 0 tags |
| `BJoozz/visualgo` (visualgo.net source); `kerktaiheng/visualgo` (the design system's stated source) | not read |
| Meeting notes, emails, chat, the supervisor's remarks | not available |
| AI session transcripts (Claude Code sessions, Codex plans and reviews) | not read; only what commits, records and PR bodies say |
| Uncommitted work in the two worktree folders | unknowable: the folders are empty (Q12) |
| The fork's Vercel commit `03bfaa3` (2026-10-17) | seen only in the API's events; not in the local object store [01] |
| NUS documents (module rules, the semester calendar) | not read; the dates come from the owner's answers |

## 2. Baseline and responsibilities

### 2.1 Kerk's base in the shared repository, before Bao's first commit there

| Item | Commits | What it is | Label |
|---|---|---|---|
| Design system, `design/design-system` | `634b5be` 09-03 | Tokens with nine themes, 26 components and two UI kits (`ui_kits/visualgo-web`, whose `HomeScreen.jsx` the homepage later follows, and `ui_kits/test-mode`). Its `github.md` says "Last sync 2026-08-27" and that it was read from `kerktaiheng/visualgo`, a fork of `stevenhalim/visualgo`. Its `SKILL.md` and `*.prompt.md` files look like an AI design tool's export | VERIFIED (files); DOCUMENTED (sync date, source); INFERENCE (tool, Q8) |
| Engine prototype, `wasm-arch/` | `b3e86ba` 09-03; `8a59115`, `e396e06`, `aa541a1` 09-04 | Protobuf RPC between a page and a C++20 engine compiled to WASM, with a reversible journal of Deltas; a Python engine that traces sorts in Pyodide; one log stream; the CI and Pages workflows | VERIFIED |
| Wireframes, `design/wireframes` | `69aa8e4` 09-04 | "wireframe 2 viz desktop": nine layouts V1 to V9 of the visualisation page (V2 "Split rails"; V7 "Docks, draggable", with V8 and V9 its drag states); mobile "held pending". The two other files ("CDC Companion") are not about VisuAlgo (Q16) | VERIFIED |
| Clean-up | `598193b` 09-13, `df99dac` 09-14 | `Zone.Identifier` files removed; CI and Pages fixed | VERIFIED |

At `df99dac`, before Bao's first commit reached `main`, the repository tracked 279 files (`design/` 197, `wasm-arch/` 78) and had no `prototypes/` folder. Only Kerk has ever changed `wasm-arch/` on `main` (5 commits). Nothing in `prototypes/src` uses the engine; Pages builds it as a separate demo at `/engine/`. VERIFIED. Third-party libraries (React, React Flow, d3, Vite and others) are ordinary dependencies, not part of this baseline.

### 2.2 Bao's earlier standalone repositories (week 0 and after)

All four are in the report's scope (owner's answer, Q1). Week 0 ends on the FYP's start date in August (Q1): it holds V1's first four days for certain and the August work depending on that date; the September work is FYP proper.

| Repository | Dates | Before 2026-08-01 (week 0 for certain) | How it reached VisuAlgo+ | Files still byte-identical in the app [02] | C |
|---|---|---|---|---|---|
| graph-algorithm-visualizer (V1) | 07-28 to 08-19 | 25 of its 55 commits (07-28 to 07-31): the first editor, BFS and DFS, `VisualizationPlayer`, the start of Dijkstra | not copied; only through v2's rewrite (DD-01: V1 is "reference material") | - | C1 |
| sorting-algorithm-visualizer | 08-19; its performance doc is dated 08-13 | none on record; the history before the squash is missing (Q10) | forked at `9236a65` into `ee4bb72` (09-25) | 17 of 45 | C2 |
| graph-visualizer-v2 | 08-20 to 09-11 | none | submodule pinned at `c8b14e6` (`986deba`); copied into `0073875` (09-20) | 53 of 173 `src` files | C1 |
| tree-visualizer | 09-03 to 09-17 | none | copied at `46ce0a7` into `7b16bf3` (09-22); the submodule pin stayed `1477cda` | 88 of 289 | C2 |

Dates and copy points VERIFIED [02]. Every commit in these repositories is by a BJoozz identity, with none by Kerk. The work came before, or ran beside, the shared repository, and it is the inherited base of today's graph, tree and sorting modules.

### 2.3 Intended responsibilities: the owner's working description

| Person | Working description (owner, 2026-11-01; not a formal assignment) | What this repository shows | Label |
|---|---|---|---|
| Kerk Tai Heng, a fellow FYP student on the same project, same supervisor | the engine/WASM work; web, cache and cloud infrastructure | `wasm-arch/`; `ci.yml`, `pages.yml`, `app.yml`; the design system and wireframes; the one-app consolidation `0394b64`; chrome and footer changes (`c59c155`, `a074f50`, `01a1a4a`); seven records first written in his commits (DD-57 to DD-59, TP-28, TP-29, SP-19, SP-20). A search of his commit messages finds no cache or cloud work beyond Pages and CI | DOCUMENTED (description); VERIFIED (commits) |
| Bao | the graph, tree and sorting visualizers and their integration into the shared interface | the four standalone repositories; the V2/V7 prototypes; the site; the V10 shell (apart from Kerk's drop-band tuning and its move into `src/shared`); the features and fixes of PRs #22 to #37. The engine study is recorded separately (C3) | DOCUMENTED (description); VERIFIED (commits; Q2 pending) |
| Both students and A/P Steven Halim | each intervened deeply in the others' choices when needed | not in git, apart from the choices quoted in records and proposals | DOCUMENTED (owner) |

- Kerk's academic role and each student's formal scope are QUESTION (Q3). Nothing here assumes that the whole shell or the engine is Bao's.
- "The owner" in Kerk's commits of 2026-10-18 to 10-22 is unconfirmed. The V10 choices 1 to 26 are quoted in Vietnamese in Bao's commits, so they are Bao's (VERIFIED by quotation, `design/proposals/viz-shell-v10/README.md` §0.1). Choices 27 to 41 (`ae63a62`, `c59c155`) and 42 to 48 (`3c79d36`, `a074f50`, `01a1a4a`) are quoted in informal English in Kerk's commits, which points to a person other than Bao (Kerk, or feedback Kerk relayed). For those, the decider is QUESTION (Q3) and the implementer is Kerk (VERIFIED).
- The current direction, visualizations and integration experiments for VisuAlgo+, is Bao's description; it is not on record as the supervisor's assignment or feedback (Q6).

## 3. Major milestones

### 3.1 Dated table

**Period.** Week 0 runs from 2026-07-28 to the FYP's start, a date in August not yet given (Q1): row 1 is week 0 for certain, and a row marked "Aug (Q1)" may fall on either side of that date. Semester = from 2026-08-01. All rows are in the report's scope. Dates, authors and hashes are VERIFIED (2026-11-02); "What happened" is DOCUMENTED (commit subjects, PR titles, notes [01] to [08]) unless marked.

| # | Dates (2026) | Period | Phase | Where | What happened | Who | Evidence | C |
|---|---|---|---|---|---|---|---|---|
| 1 | 07-28 to 07-31 | Week 0 | Standalone | graph-algorithm-visualizer, `main`, PR #1 | Graph V1's first version: editor, force layout, BFS and DFS with pseudocode, queue and stack; a generic `VisualizationPlayer`; the Dijkstra branch begins | Bao | `f3a0db8`, `2c4feaa`, merge `ab3676a`, `788af81` | C1 |
| - | August (date: Q1) | - | FYP proper begins | - | "The FYP proper began in August 2026" (owner's answer, DOCUMENTED); the exact date is not given | - | - | - |
| 2 | 08-03 to 08-19 | Aug (Q1) | Standalone | graph V1, PRs #2 to #8 | Weighted Dijkstra; parallel edges; Edmonds-Karp with a residual view; minimum cut and samples; fullscreen; Kruskal with Union-Find, Playwright and a GitHub Actions workflow; an editor sidebar (V1's last commit) | Bao | `265d6a7`, `3103aff`, `447abc0`, `87566f9`, `4315111`, `b0bb316`, `5fc06a0` | C1 |
| 3 | 08-19 (doc dated 08-13) | Aug (Q1) | Standalone | sorting-algorithm-visualizer | One squashed commit: 8 algorithms as typed operations, 1, 2 or 4 panes, a Canvas renderer, a profiler | Bao | `9236a65` | C2 |
| 4 | 08-20 to 09-03 | Aug (Q1) | Standalone | graph-visualizer-v2 | A rewrite of V1: `AGENTS.md` rules, one workspace around one canvas, the five algorithms, ARCHITECTURE and DD-01 to DD-22, samples, large graphs | Bao | `92fa193`, `fc62e5a`, `f6149f1`, `f864de7`, `c5dfb43`, `0f5b49a`, `e8a73be` | C1 |
| 5 | 09-03 to 09-14 | Semester | Baseline (Kerk) | visualgo-plus-design, `main` | Repository created; design system; C++/WASM engine with protobuf RPC; Python tracing engine; logging; wireframe 2 with layouts V1 to V9; clean-up and a CI/Pages fix | Kerk (Claude trailers on 4 of his 6 commits of 09-03/04) | `634b5be`, `b3e86ba`, `e396e06`, `69aa8e4`, `aa541a1`, `df99dac` | base |
| 6 | 09-03 to 09-17 | Semester | Standalone | tree-visualizer, PRs #1 to #8 | Six workspaces (LCA, BST, AVL, Min Heap, Trie, Segment Tree); Binary Lifting; review fixes, accessibility, shortcuts, samples | Bao (Claude trailers from 09-12) | `e687099`, `015469e`, `1477cda`, `a4b6d08`, `46ce0a7` | C2 |
| 7 | 09-07 to 09-11 | Semester | Standalone | graph-visualizer-v2, PRs #1 to #14 | Tests by glob, Playwright, CI, typed IDs, inspector and legend; `c8b14e6` is the commit copied later | Bao (Claude trailers from 09-07) | `ce0cb7b`, `d9abac1`, `acc3062`, `c8b14e6` | C1 |
| 8 | 09-13 to 09-16 | Semester | Joining | `bj/visualization-work` | Bao's first commit in the shared repository: graph and tree submodules; then a merge of `main` | Bao | `986deba`, `4bd9ca9` | C4 |
| 9 | 09-17 | Semester | Engine study | `bj/engine-v2-experiment`; local `bj/engine-package-spike`, `bj/bfs-wasm-spike` | M0 to M4a in `wasm-arch/`: stable edge IDs, a browser engine client, a BFS runtime for hosts with string IDs, a packaging spike. Never merged; no PR, no CI | Bao, on Kerk's engine (trailers on 4 of 6) | `478174f`, `e348a6d`, `ffb9274`, `053064f`, `53d2ef4` | C3 |
| 10 | 09-20 to 09-21 | Semester | V2/V7 layouts | PR #1 | Graph prototypes in Kerk's wireframe layouts V2 (split rails) and V7 (docks); the first prototype CI (`prototypes.yml`) | Bao | `0073875`, `37075b1`, merge `6a621df` | C4 |
| 11 | 09-22 to 09-23 | Semester | V2/V7 layouts | PR #2 | Tree V2/V7 prototypes in the graph's page shell | Bao | `7b16bf3`, merge `495fa73` | C4 |
| 12 | 09-23 to 09-27 | Semester | V2/V7 layouts | PR #3 | Sorting submodule; sorting V2/V7 with Study and Compare, pseudocode and exact seeking | Bao | `e7a44f9`, `ee4bb72`, `5ccef45`, `fed2420`, merge `ca56cef` | C4, C9 |
| 13 | 09-28 to 09-29 | Semester | Site | PR #4; the fork; PR #5 | Two VisuAlgo+ websites (V2 and V7) that mount the real visualizers under one bar; static-host support. A Vercel attempt from the fork (PR #5) was closed unmerged on 10-25 | Bao | `87db4a3`, `8aeb543`, `57912e8`, merge `9cc009f`; `c9e4598` | C5, C14 |
| 14 | 09-29 to 10-08 | Semester | Growth | `bj/visualgo-web-editors` (PR #6: no merge commit, empty body) | Dijkstra's distances on the nodes; recursive DFS; Graph and Tree Editor cards; edge waves (DD-37); Bellman-Ford and Prim; an extra panel and the LCA ancestor strip; the homepage credit "by Kerk and Bao" | Bao; Bellman-Ford and Prim recorded as planned and built with Codex (DD-38, DD-39; Bao's part Q4), their 8 stage commits without a trailer | `6fc6150`, `4ab075c`, `cc38942`, `bcbed32`, `aef5d0b`, `4bd0879`, `00ed4c2`, `ae2f31f` | C5, C7, C8, C11 |
| 15 | 10-09 to 10-10 | Semester | Growth | `bj/segment-tree-lazy`, `bj/bst-avl-operations` (no PR) | Lazy segment tree with exact decimals; tree e-Lectures; BST/AVL Min/Max, Predecessor/Successor, Lower Bound, Select, traversals, AVL Delete | Bao | `fc4172d`, `a521c13`, `3a429ad`, `c364204`, `e7f2fec`, `9a2f04b`, `c620145` | C8, C12 |
| 16 | 10-10 to 10-15 | Semester | Growth | `bj/uiux-pass-1`, `bj/dock-drop-zones` (no PR) | Play replaces Go; paused-step motion (DD-42, TP-17); drag with Live layout off (DD-43); merged steps (DD-44, TP-18, SP-11); end badges; value popups; see-through legend; the rule "upstream is a reference only"; V7 drop zones. `main` red in the old CI from 10-10 to 10-14 (one font-sensitive test) | Bao | `117975a`, `7e92baf`, `74a4958`, `38c726f`, `0d1f6de`, `28e08f8`, `ff77eca`, `c3f6508`, `f510477` | C4, C10, C11, C13 |
| 17 | 10-14 to 10-17 | Semester | First PR round | PRs #7 to #14 | CI font fix; End node (DD-45); Live layout starts off (DD-46); centred footer; final-frame motion (DD-47); visualgo.net's sample graphs (DD-48); node label size (DD-49) | Bao | `3a6443b`, `9e6e7bd`, `6b953d5`, `d6ce97b`, `be570eb`, `bc46260`, `e360df1` | C7, C11, C12 |
| 18 | 10-16 to 10-18 | Semester | V10 | PRs #15 to #17 | V10 "Panel groups": proposal and frames V10/V11; the groups model; the shell; graph, tree, sorting and site copies; review fixes. Records DD-50 to DD-56, TP-21 to TP-27, SP-12 to SP-18 | Bao; choices 1 to 26 Bao's (VERIFIED by quotation); PR #17 merged by Kerk | `55f3387`, `72450e1`, `a876206`, `d445364`, merges `c899b69`, `f286712`, `b9ec8fa` | C6 |
| 19 | 10-18 | Semester | One app | Kerk's PRs #18 to #21 | Pages serves V10 at `/` and the engine demo at `/engine/`; choices 27 to 41 applied; the V2/V7 folders, their two sites and the submodules deleted; one app in `prototypes/` with `app.yml` CI; the site becomes the only top bar and theme writer | Kerk (implementer); decider of the choices and of "V10 wins": QUESTION (Q3) | `c39b3cf`, `ae63a62`, `0394b64`, `c59c155`, merges `94cdaf3`, `8d7a63a`, `fae8418` | C14, C5, C6 |
| 20 | 10-19 to 10-22 | Semester | One app | `main`, pushed directly | Choices 42 to 48 (LCA indentation, no Save image, Full screen and Shortcuts beside Settings, stepping first, Autoplay beside Stop, coloured chips) and the landing tips removed ("the owner's request") | Kerk (implementer); decider: QUESTION (Q3) | `3c79d36`, `40a63bd`, `a074f50`, `01a1a4a` | C5, C11 |
| 21 | 10-19 to 10-21 | Semester | Features | PRs #22 to #27 | Tree edges centre to centre (TP-30); LCA as two runs (TP-31) and its hover (TP-32); Binary Heap with Min/Max and visualgo.net's operations (TP-33, PRs #25 to #27) | Bao | `499cb42`, `e55de1c`, `60ccc44`, `7d39c38`, `ea37326` | C8 |
| 22 | 10-21 to 10-22 | Semester | Features | PR #28 | Topological Sort, Bipartite Check, Cut Vertex & Bridge, with a Method control (DD-60) | Bao | `b88952d`, `84c5917`, `0fc105c`, merge `4621b1f` | C7 |
| 23 | 10-23 to 10-26 | Semester | Features | PRs #29 to #33 | Step notes in the tree (TP-34, TP-36) and for Dijkstra (DD-61) on one shared note layer; a smaller shared legend; one CI failure, fixed 11 minutes later | Bao | `d82aa18`, `7180d81`, `94ec5db`, `08590ef`, `6b1a4fc`, `19aaef3`, `b47d437`, `b309309` | C10 |
| 24 | 10-26 to 10-30 | Semester | Reviews | PRs #34 to #37 | Findings of review sessions 1 to 3 (dated 10-26, 10-27, 10-29): Inter font guard, Node 22.12 floor, flag forwarding, CI traces; the tab strip keeps its tab in view; a docs sweep and the shell copy rule retired; a shared playback countdown; sorting restarts always play | Bao (implementer); who produced the findings: QUESTION (Q6) | `a5bb08f`, `fd9ff5c`, `02c4e12`, `9baa117`, merges `ad5e119`, `4dedee1`, `f58ed5f`, `662e7b3` | C13, C11, C6 |
| 25 | 10-31 to 11-01 | Semester | End of record; audit | `main` at `662e7b3` | `662e7b3` (PR #37's merge, 10-31 01:04 +08:00; GitHub: 10-30 17:04 UTC) is the last commit, with no CI run after it. On 11-01 the full check set passed on it: typecheck; lint 0 errors, 2 warnings; 654 + 2,619 = 3,273 unit cases; build; 151 of 151 browser cases | audit | [07] §2 (VERIFIED) | C13 |
| 26 | 11-04, 17:00 SGT | Semester | CA deadline | - | CA report due, softcopy to the Supervisor and the Main Evaluator (owner's answer, DOCUMENTED) | Bao | - | - |

### 3.2 The phases in brief

**Standalone foundations (07-28 to 09-17; C1, C2).** Four visualizers were built in Bao's own repositories, before and beside the shared one; only V1's first four days are certainly week 0; the August work depends on the FYP's start date (Q1). v2 rebuilt V1 in a new repository rather than continuing it (DD-01, DOCUMENTED). The sorting repository is one squashed commit, so its process is not evidenced (Q10). All commits are BJoozz's; Claude trailers begin on 09-07 in v2 and on 09-12 in tree. VERIFIED.

**Joining the shared repository (09-13 to 09-21; C4).** Bao's first commit there, `986deba`, adds v2 and tree as git submodules, which reached `main` with PR #1; sorting followed on 09-23. The pins never moved until Kerk's `0394b64` removed them on 10-18. VERIFIED.

**The engine study (09-17; C3).** Within twelve hours, six commits explored running BFS on Kerk's C++/WASM engine from the graph host (M0 to M4a). Nothing was merged or run in CI, two of the commits exist only in this clone, and the test results are only in commit messages (DOCUMENTED). On 09-20 `0073875` put "the engine integration" "outside this prototype" (VERIFIED); why the study stopped, and who decided, is Q9.

**V2/V7 layouts (09-20 to 10-15; C4).** PRs #1 to #3 put the three visualizers into two of the nine layouts of Kerk's wireframe 2, giving six app folders kept in step by hand (DOCUMENTED [03]). Who chose V2 and V7 is Q8. The folders were deleted on 10-18; their features lived on in the V10 copies, which were made from the docks copies (VERIFIED [03]).

**The site (09-28 to 09-29; C5).** PR #4 added two websites that mount the real visualizers under one top bar, built on Kerk's design system and following his UI kit's homepage (VERIFIED [03]). A Vercel attempt from Bao's fork (PR #5) was closed unmerged; no Vercel deployment was found (Q15).

**Growth by direct pushes (09-29 to 10-15; C5, C7, C8, C11, C12).** 90 of Bao's commits went to `main` with no merge commit: 29 that GitHub records as PR #6 (empty body) and 61 that belong to no PR. They added graph algorithms, tree operations, the editor cards and a UI/UX pass. VERIFIED.

**V10 "Panel groups" (10-16 to 10-18; C6).** Bao proposed a third layout that merges V2's and V7's ideas, then added its pure groups model, the shell and copies for the three visualizers and the site (PRs #15 to #17). VERIFIED. The dates support no productivity claim ([09] §5, item 21).

**One app (10-18 to 10-22; C14).** In one evening Kerk's PRs #18 to #21 deployed V10 to Pages, deleted the V2/V7 folders, their sites and the submodules, and made one app in `prototypes/`; four direct pushes followed (choices 42 to 48). Kerk implemented all of it (VERIFIED). `0394b64` cites "The owner's decision of 2026-10-18: V10 wins"; who that owner is, is Q3 (section 2.3).

**Features through PRs (10-19 to 10-26; C7, C8, C10).** From PR #7 on, all of Bao's work came by PR. PRs #22 to #33 added tree operations and the Binary Heap, three graph traversals, and step notes on one layer shared by the tree and the graph. VERIFIED.

**Reviews (10-26 to 10-30; C13).** PRs #34 to #37 fix the findings of three review sessions dated 10-26, 10-27 and 10-29 (DOCUMENTED); who produced the findings is Q6. The last commit, `662e7b3`, passed the full check set on 2026-11-01 ([07] §2).

## 4. Missing sources and uncertainties

| # | Missing source or open point | What it limits | Status | Q |
|---|---|---|---|---|
| 1 | The date in August 2026 when the FYP proper began, which ends week 0 | Week 0 or FYP proper for milestone rows 2 to 4 (the September rows are FYP proper) | QUESTION | Q1 |
| 2 | Bao's confirmation of both BJoozz author strings | Every "Bao" attribution | QUESTION (email, account and no-reply id known) | Q2 |
| 3 | Kerk's formal academic role; each student's formal scope | Section 2.3 | QUESTION | Q3 |
| 4 | The decider of choices 27 to 48, of "V10 wins" and of the deletions of 10-18; "the owner" in Kerk's commits of 10-18 to 10-22 and in PR #37 (`a074f50`, "the owner's commit") | Credit in C5, C6, C9, C11, C13, C14; DD-52, DD-57 to DD-59, TP-23, TP-28, TP-29, SP-14, SP-19, SP-20 | QUESTION (Kerk implemented, VERIFIED) | Q3 |
| 5 | Bao's own direction, review, testing and acceptance in AI-assisted changes; the tools behind commits with no trailer | Any claim about Bao's role; the workflow section | QUESTION | Q4 |
| 6 | Whose decisions the records that name no person are; the unwritten rules | Design-rationale sections | QUESTION (unanswered) | Q5 |
| 7 | Code review: no PR review or comment; 90 of Bao's commits (09-29 to 10-15) with no merge commit | No "peer-reviewed" claim; who produced the review-session findings | VERIFIED (absence); QUESTION | Q6 |
| 8 | Meeting notes, emails, chat, the supervisor's remarks | No supervisor assignment or feedback, and no agreement between the students, can be cited | not available | Q6 |
| 9 | `BJoozz/visualgo`; permission for the copied visualgo.net material and the branding on the public site | C5, C12 | not read; QUESTION | Q7 |
| 10 | `kerktaiheng/visualgo`; how the design system was made; who chose V2 and V7 | C4, C5 | not read; QUESTION | Q8 |
| 11 | The engine study's purpose, review and stop; it never ran in CI | C3 | results DOCUMENTED only | Q9 |
| 12 | V1 history before 07-28 (its first commit adds about 3,000 lines besides the lockfile); sorting history before the squash | The start of week 0; the sorting process | not in any clone | Q10 |
| 13 | Records of manual checks; feedback from users, Kerk or the supervisor; benchmarks | Any evaluation claim | none in the repository (VERIFIED [07]); who made the English requests behind choices 27 to 48 is Q3 | Q11, Q3 |
| 14 | Work left in the empty worktree folders; `053064f` and `53d2ef4` exist only in this clone | Possible loss of work | QUESTION | Q12 |
| 15 | Any Vercel deployment (`c9e4598`, `03bfaa3`); the fork's push of 2026-11-01 | Deployment history | none found; QUESTION | Q15 |
| 16 | AI session transcripts; Codex's plans and reviews | What the tools proposed against what Bao chose | not read | Q4, Q6 |

Q13, Q14, Q16 and Q17 (stale docs, coverage wording, unrelated files, small facts) do not change the scope or the dates; they are listed in [09] §4.

**Evidence trail (2026-11-02, read-only).** `git show -s --format="%h %ad %an %s"` on every hash above; `git log --all`, `git rev-list --count`, `git merge-base --is-ancestor`, `git cherry` and `git blame` in the repository and the clones; `gh api` for repositories, branches, pulls, reviews, comments, issues, users and Pages; `curl` for the deployed site. Nothing was written inside the repository, the clones or the worktrees.

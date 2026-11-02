# 05 · Report mapping, central contributions and open questions

Audit date: 2026-11-01/02 (the git, GitHub and file checks behind this document were re-run on 2026-11-02; no test was run for it)\
Repository: `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3`\
Evidence labels: VERIFIED / DOCUMENTED / INFERENCE / QUESTION. Ids C1–C14 and Q1–Q17 are those of `evidence/research-notes/09-candidate-contributions.md`.\
The owner's answers of 2026-11-01 and 2026-11-03 are applied (doc 01, the table at its top); his project description of 2026-11-03 is quoted in §1.1.

**What this document is for.** Bao is writing the CA report, due 2026-11-04 17:00 Singapore time as a softcopy to the Supervisor and the Main Evaluator. This document says which evidence belongs in which report section (§1), which contributions to put at the centre (§2), what a development-workflow paragraph can say (§3), what Bao must still answer (§4) and which claims to avoid (§5). The detail is in the companion documents: `01_scope_and_timeline.md` (repositories, identities, milestones), `02_contribution_evidence.md` (one record per contribution), `03_architecture_and_decisions.md` (architecture, diagrams, decisions) and `04_figures_and_validation.md` (figures, tests, gaps).

## 1. Evidence for each section of the report

### 1.1 Introduction and Objectives

**Bao's project description (2026-11-03).** Written by Bao for this audit, it is the report's statement of background, objectives and scope and the only written record of them (DOCUMENTED). Quoted in full:

> **Project Background and Motivation**
>
> VisuAlgo+ aims to rebuild VisuAlgo using modern and widely adopted development tools, while preserving the educational goals and strengths of the original platform.
>
> In an early discussion, our supervisor, A/P Steven Halim, highlighted the existing technology stack, including Laravel/PHP, MySQL, d3.js and jQuery, and encouraged us to explore a more modern foundation for the platform. This direction involves substantial changes to both the user interface and the underlying algorithm execution engine.
>
> The project therefore takes the form of a new implementation guided by the original VisuAlgo's purpose, existing functionality and successful design ideas. It provides an opportunity to reconsider the software architecture, improve UI/UX, and establish a foundation for future development.
>
> **Overall Project Objective**
>
> The overall objective is to develop VisuAlgo+ as a modern successor to VisuAlgo: an interactive platform for learning data structures and algorithms, with a redesigned interface and a renewed technical foundation.
>
> The main objectives are to:
>
> 1. Select suitable modern and widely adopted technologies for rebuilding the platform.
> 2. Preserve the educational purpose, useful functionality and effective interactions of the original VisuAlgo.
> 3. Redesign the interface and user interactions to support consistent exploration of different algorithms and data structures.
> 4. Develop an architecture that supports the evolution and integration of visualization modules and algorithm execution engines.
> 5. Validate the rebuilt functionality and identify areas requiring further technical and user evaluation.
>
> **My Scope within the Project**
>
> Within this shared project, my main focus is the visualization and interaction layer. This includes developing graph, tree and sorting visualizers, designing their editing and playback interactions, and integrating them into the shared VisuAlgo+ interface.
>
> My initial standalone prototypes provided a way to explore these behaviours before integration. The later work on shared layouts, algorithm features and on-canvas explanations contributes to the broader goal of rebuilding the platform.
>
> Kerk's work includes the engine/WASM foundation, the website design system and shared infrastructure. Our work overlaps during interface development and integration. At the current stage, the visualization application uses its own TypeScript algorithm implementations; integration with the separate WASM engine remains future work.

The supervisor's early direction (the old stack; a more modern foundation) is recorded here in Bao's words; no email or meeting note was available to the audit, so the report should give it as Bao's account.

**Each objective against the evidence.** The mapping is an INFERENCE; the evidence carries the labels of the documents cited.

| # | Objective | What the repository shows | Where |
|---|---|---|---|
| 1 | Modern, widely adopted technologies | React 19, TypeScript, Vite, React Flow, d3, Vitest and `node:test`, Playwright, GitHub Actions and Pages; Kerk's C++20/WebAssembly engine with protobuf RPC beside it. visualgo.net's stack as the description names it: Laravel/PHP, MySQL, d3.js, jQuery | doc 03 §1.1, §2.3; §1.2 below |
| 2 | Preserve VisuAlgo's purpose, functionality and interactions | 37 example graphs copied with their positions (DD-48); e-Lecture decks written after visualgo.net's (TP-14); the card catalogue in visualgo.net's order; pseudocode highlighting per step; operations rebuilt after visualgo.net (Binary Heap, TP-33; BST/AVL, TP-15; Graph Traversal, DD-60); 12 of 30 cards open | doc 02 C7, C8, C12; §1.4 below |
| 3 | A redesigned interface for consistent exploration | one site and one page shell for three visualizers (V10 panel groups, after V2 and V7 were built and compared); one footer transport (DD-24); the Graph and Tree editors; step notes on the canvas (C10); paused-step and final-frame motion (C11); nine themes | doc 02 C4, C5, C6, C10, C11; figures F1–F4, F6 |
| 4 | An architecture for evolving and integrating modules and engines | one app with a route per module and a shared layer (`prototypes/src/shared`); separate state owners and eager typed sequences (v2's DD-01 to DD-12); the engine boundary kept open: Kerk's `wasm-arch` deployed beside the app at `/engine/`, Bao's unmerged integration study (C3) | doc 03 §1, §2.3; doc 02 C3 |
| 5 | Validate the rebuilt functionality; identify what still needs evaluation | 3,273 unit and 151 browser cases green on 2026-11-01; 266 CI runs; property tests against independent oracles; 95 decision records; no user evaluation yet, with proposals in doc 04 §4 | doc 04 §2, §3, §4 |

**The problem, in the project's own words.** Quote these beside the description; do not add objectives that no record states.

| Statement | Where | Label |
|---|---|---|
| "The goal: a runnable site where a visitor lands on Kerk's homepage, picks a module, and uses our *real* visualizers inside one consistent shell — with everything we have not built labelled honestly as coming soon." | `design/proposals/visualgo-web-site/README.md:16-18` (Bao's proposal for PR #4) | DOCUMENTED |
| "This site is an experimental version adapted from Prof Halim's visualgo.net, built by Kerk and Bao." | `prototypes/src/site/HomePage.tsx:152-153` (`ae2f31f`) | VERIFIED (the text) |
| "this is a prototype site, not a replacement deployment of visualgo.net" | PR #4 body | DOCUMENTED |
| Two layouts "had to be compared on the same functionality"; V10 is to be "one version that keeps both strengths" | DD-23; `design/proposals/viz-shell-v10/README.md:124-128` | DOCUMENTED |
| Gaps that started features: "The Graph Traversal card listed seven of visualgo.net's algorithms and had three" (PR #28); Bao's request, quoted in Vietnamese in TP-34, asked for text "right on the canvas instead of showing too much in Status, especially the dead steps, the ones that change nothing on the visualization" (TP-34, the record's English translation; PR #29) | PR bodies, records | DOCUMENTED |

A one-sentence summary of the current build (INFERENCE), consistent with the description's overall objective: VisuAlgo+ is an experimental version of visualgo.net in which the graph, tree and sorting visualizers run as routes of one site, in one page layout, on Kerk's design system.

**Scope, as the owner stated it** (DOCUMENTED: owner's answers of 2026-11-01 and 2026-11-03):

- The FYP is NUS AY2026/27 Semester 1. All work from the first standalone commit (`f3a0db8`, 2026-07-28) counts as "week 0" and is in the report's scope. The FYP proper began in Week 1 of the semester, about 2026-08-10 (exact date to confirm), so week 0 is 2026-07-28 to about 08-09: V1's PRs #1 to #5; everything after is FYP proper.
- Roles, as a working description and not a formal assignment, and as the description above says: the visualization and interaction layer is Bao's focus (the graph, tree and sorting visualizers, their editing and playback interactions, their integration into the shared interface); Kerk's work is the engine/WASM foundation, the website design system and shared infrastructure; the two overlap in interface development and integration. In this repository Kerk's 17 commits show the design system, the wireframe, `wasm-arch/`, the CI and Pages workflows, the one-app consolidation and chrome changes; no cache or cloud work is in it (VERIFIED, `git log --author`).
- Supervisor: A/P Steven Halim. His early direction is recorded only in Bao's description above; the repository never mentions a supervisor (`git grep -i supervisor`: 0 hits, note 07 §6; VERIFIED). Bao will add the supervisor's own remarks with their source.

**Scope limits written in the repository** (DOCUMENTED): desktop and laptop windows only, and "the phone version will be designed separately" (`prototypes/docs/graph/AGENTS.md:36-45`; Kerk's wireframe: "Mobile. Held pending further instructions"); the standalone repositories are "a reference only", never changed or synced ("The owner's decision, 2026-10-12", `38c726f`); "the separate Wasm engine integration [is] outside this prototype" (`prototypes/docs/graph/README.md:451`).

**Not in the repository:** objectives, research questions, success criteria or an evaluation plan (VERIFIED: `git grep` for objective, goal, aim and purpose in the docs and proposals finds only the statements above, the purposes of sorting's Study and Compare modes, and the engine's own goals in `wasm-arch/docs/ARCHITECTURE.md`). The objectives come from Bao's description above; success criteria and an evaluation plan are still to be written (doc 04 §4 holds proposals).

### 1.2 Background and Related Work

| Topic | What the evidence supports | Label |
|---|---|---|
| visualgo.net, the reference | Cards "transcribed from visualgo.net's own homepage table" (`prototypes/src/site/modules.ts:3-7`); graph samples "copied from its source" in the private repository BJoozz/visualgo (`prototypes/src/graph/algorithms/visualgoExamples.ts:1-7`, DD-48); e-Lecture decks written after its lectures (TP-14); Kerk's design system "measured out of" a visualgo fork's CSS and JS (`design/design-system/readme.md:18-38`). Used with Prof Halim's knowledge and agreement (owner, 2026-11-03) | DOCUMENTED |
| Libraries the app builds on | React 19 and React Router 7. React Flow (`@xyflow/react` ^12.12) draws the graph and tree canvases; `d3-force` the graph's force layout (`prototypes/src/graph/graph/layout/forceLayout.ts`); `d3-hierarchy` the tree layout (`prototypes/src/tree/tree/layout/createTreeLayout.ts`); sorting draws on a Canvas 2D with `d3-ease` and `d3-interpolate`. Tooling: Vite ^8.2 (8.3.4 in the 2026-11-01 build), Vitest ^4 and Node's `node:test`, Playwright ^1.63 (1.64.1 installed), TypeScript ~6.0, oxlint (`prototypes/package.json`) | VERIFIED |
| Kerk's base, before Bao's first commit in the shared repository | The design system with nine themes (`634b5be`, 2026-09-03); the wireframe with nine page layouts V1 to V9 (`69aa8e4`, 2026-09-04); the `wasm-arch` engine prototype: protobuf RPC, a C++ engine compiled to WebAssembly, a Python engine in Pyodide (`b3e86ba`, 2026-09-03, and three commits on 2026-09-04) | VERIFIED |
| Bao's standalone visualizers (week 0 and the first FYP weeks) | graph-algorithm-visualizer (V1, 2026-07-28 to 08-19), sorting-algorithm-visualizer (one squashed commit `9236a65`, 08-19), graph-visualizer-v2 (08-20 to 09-11), tree-visualizer (09-03 to 09-17); every commit Bao's. They are contributions C1 and C2, not related work: Background only names them as the starting point | VERIFIED |

**Topics that need external literature** (topics only; this audit cites no source):

1. Algorithm visualization, and how its effect on learning is evaluated.
2. Step-by-step animation of algorithms: pacing, playback controls, and explanations placed on the drawing.
3. Interface layout and docking patterns: tab groups, split panes, drag-and-drop feedback such as VS Code's.
4. Graph and tree drawing: force-directed layout, tidy tree layout.
5. Property-based testing and test oracles.
6. WebAssembly engines in the browser.
7. Accessibility of visualizations: colour contrast, reduced motion, keyboard access.

### 1.3 System Design

| Subsection | Contribution | What to describe (detail in) | Figure | Say with it |
|---|---|---|---|---|
| Architecture overview | C5, C14 | One Vite and React single-page app in `prototypes/`; routes `/`, `/:slug`, `/:slug/:algorithm`; three visualizers mounted by `prototypes/src/site/ModulePage.tsx`; shared code in `prototypes/src/shared`; state in React and `localStorage`; no network call in `prototypes/src` (VERIFIED: no `fetch`, XHR or WebSocket). Doc 03 §1, the current implementation | D1 (doc 04 §1.4) | The one-app structure is Kerk's consolidation (`0394b64`, PR #20) |
| What the app keeps from the standalone visualizers | C1, C2 | Separate owners for the graph document, its layout, the run session and the presentation; one canvas that stays mounted; a run's steps built when it starts (graph, tree) or pulled lazily (sorting) (DOCUMENTED, v2's DD-01 to DD-12). The graph and tree session reducers are byte-identical to graph-visualizer-v2 at `c8b14e6` and tree-visualizer at `46ce0a7` (VERIFIED, blob hashes). Doc 03 §2, earlier and experimental architectures | — | Bao's week-0 and early-FYP work, in his own repositories |
| Host boundary | C5 | The site owns the top bar, routing and theme; each visualizer owns its panels, state and transport, through `HostChromeContext` and `renderTopBar` (`prototypes/src/site/HostedModule.tsx`) (VERIFIED). Doc 02, record C5 | F1 (homepage) | Built on Kerk's design system and UI kit; the site as the only bar and theme writer is Kerk's `c59c155` |
| Panel-groups shell (V10) | C6, with C4 before it | A pure model (`prototypes/src/shared/components/layout/groupsModel.ts`): left, right and bottom regions, each a stack of collapsible tab groups, around a canvas that is never a tab; `resolveLayout` holds every minimum (drawing floor 360 × 320, groups at least 240 px wide and 120 px high); drop targets; a saved layout (VERIFIED, constants). DD-50 to DD-56, TP-21 to TP-27, SP-12 to SP-18. Doc 02, record C6 | F2 (default layout, BFS frame 8), F3 (a tab drag with its drop preview) | Kerk tuned the drop bands (choices 27 and 33, decided together) and moved the shell into `src/shared`; drag and split are checked by hand only |
| Explanation on the canvas | C10 | One step-note layer in `prototypes/src/shared` (`visualization/stepNotes.ts`, `visualization/stepNotePlacement.ts`, `visualization/floatingTextTiming.ts`, `components/canvas/StepNoteLayer.tsx`) used by the tree and by Dijkstra (VERIFIED). TP-34, TP-36, DD-61. Doc 02, record C10 | F4, F5, F6 | Partial: no notes in sorting, the segment trees, Trie or the other graph algorithms |
| Motion and playback | C11 | The footer as the only transport (DD-24); edge waves (DD-37); paused-step motion (DD-42, TP-17); merged steps (DD-44); final-frame motion (DD-47); a shared countdown (`prototypes/src/shared/visualization/playbackCountdown.ts`) | F2 (the footer; a still shows no motion) | Autoplay beside Stop, and Next as a start, come from Kerk's `a074f50` and `01a1a4a` (decided together) |
| Algorithms | C7, C8, C9 | The Method control (DD-60) and the End node (DD-45); the tree operations (TP-13, TP-15, TP-31 to TP-33); sorting's exact seeking (SP-05) and its 60,000-operation eager gate | F8, F7 | Bellman-Ford and Prim were built with Codex at Bao's request (DD-38, DD-39) |
| The engine boundary | Kerk's engine; C3 | The app imports nothing from `wasm-arch` (VERIFIED: no `wasm-arch`, `WebAssembly` or `.wasm` in `prototypes/src`); Pages serves Kerk's demo separately at `/engine/` (`c39b3cf`); Bao's study of 2026-09-17 (M0 to M4a) is unmerged. Doc 03 §2, earlier and experimental architectures | — | Say "not integrated"; the engine is Kerk's |

Labels in this table: record ids (DD, TP, SP) name DOCUMENTED decisions; file, symbol and author facts are VERIFIED (note 06 and the checks listed at the end); the joint decisions are DOCUMENTED (owner, 2026-11-03).

### 1.4 Progress and Preliminary Results

| Result | Value | Label |
|---|---|---|
| Homepage catalogue | 30 cards: 12 open (8 full, 4 partial) and 18 "coming soon" (`prototypes/src/site/modules.ts`). Of the 26 cards transcribed from visualgo.net, 8 open: 4 full (Sorting, BST/AVL, Binary Heap, MST) and 4 partial (Segment Tree, Graph Traversal, SSSP, Max Flow). The other 4 cards (Trie, LCA, Graph Editor, Tree Editor) are full | VERIFIED |
| What "full" means | "Every algorithm the real module has" (`modules.ts:22`): algorithm names, not operations. BST/AVL was already "full" on 2026-09-28 with five operations, and the SSSP card does not count BFS. State the definition next to every count (Q14) | VERIFIED |
| Visualizers | Graph: 11 algorithm ids, 5 inherited and 6 built here. Tree: 7 workspaces. Sorting: 8 inherited algorithms in Study (1 pane) and Compare (2 or 4 panes). e-Lecture: graph 11 decks (40 slides), tree 7 (111), sorting 1 (9) | VERIFIED (note 08) |
| Audit-time run of 2026-11-01 | Typecheck clean; lint 0 errors and 2 warnings; 654 `node:test` and 2,619 vitest cases, 3,273 unit cases in all, passed; the build passed (with a chunk-size warning); 151 of 151 browser cases in 14 specs passed, in Chromium. Note 07 §2; doc 04. Seven graph test files ran again on 2026-11-02: 67 of 67 passed (doc 02) | VERIFIED |
| Standalone suites | Run on 2026-11-01 for note 02, on archive copies: V1 162/162, v2 276/276, tree 664/664, sorting 334/335 (the one failure comes from the machine's vi-VN locale) | VERIFIED (note 02) |
| CI | 266 GitHub Actions runs, 2026-09-04 to 2026-10-30; 8 failed, and each failing workflow passed again on a later commit; the runs for `662e7b3` passed | VERIFIED (note 07 §4; totals re-counted 2026-11-02) |
| Review sessions | Three reviews (2026-10-26, 10-27, 10-29): findings F01 to F04, S2-01 to S2-03, S3-01 to S3-03, answered in PRs #34 to #37; PRs #34, #35 and #37 say each finding was reproduced before the fix | DOCUMENTED; Codex reviews that Bao read first, each reproduced before its fix, the fixes his choices (owner, 2026-11-03) |

For progress over time, use doc 01's milestones (37 PRs, 33 opened by Bao; from week 0 to the review sessions). Do not report as results: the test counts in PR bodies (the implementer's own reports), the dated profiles (doc 04), or any effect on users.

### 1.5 Limitations and Evaluation Plan

**Gaps** (VERIFIED, note 07 §6; doc 04, "what does not exist"): no user study or feedback record in the repository (an early survey of a group of users, run by Kerk, informed the choice of V2 and V7; its data is not with Bao); no benchmark and no performance test in CI; no coverage tool; tests in Chromium at desktop sizes only; no automated accessibility audit (contrast is checked for a sample of text); the manual checklists were run by hand and by agents but never recorded; tab drag and split stay manual (PR #36, review S2-02), and one graph case drives a column splitter (`prototypes/e2e/graph.spec.ts:299`). No PR has a review or a comment: 37 PRs, 0 reviews, 0 comments, 0 issues (VERIFIED, GitHub API, 2026-11-02).

**Design limits named in the backlogs** (DOCUMENTED; the backlogs say none is implemented): Bellman-Ford builds its whole timeline with no cap (graph item 12: about 25,700 frames and 32 MiB for 40 nodes and 160 edges, measured once on 2026-10-03 in the V2 build, before DD-44, as "observations, not guarantees or supported limits"; doc 04 §2.7); the build warns above 500 kB (graph 6); some shared colours are below the contrast minimums (graph 14); step notes are partial (graph 20, tree 17); four sorting chrome files have drifted from the graph's (sorting 1); some docs are stale (note 04 §9). Sorting has no paused motion and no step notes (VERIFIED: absent from `prototypes/src/sorting`).

**Evaluation plan.** Take the proposals in doc 04 ("proposed future evaluation"), keep each labelled as a proposal that has not been carried out, and agree them with the supervisor before the report calls them the plan.

### 1.6 Future Work

| Item | Source | Label |
|---|---|---|
| Strongly Connected Components and 2-SAT | Graph backlog 19; DD-60: "later rounds" (Bao's choice 1 of 2026-10-21) | DOCUMENTED |
| Range Min and Range Max on the Segment Tree card | The card is partial (`prototypes/src/site/modules.ts:272`) | VERIFIED (absent) |
| Ford-Fulkerson and Dinic on the Max Flow card | The card is partial | VERIFIED (absent) |
| Step notes for more algorithms; paused motion and notes in sorting | Graph backlog 20, tree backlog 17; absent in `prototypes/src/sorting` | DOCUMENTED; VERIFIED (absent) |
| Engine integration | Bao's study stopped before M4: "M4 proper (presenter, `GraphPresentation`, async player, canvas integration) has not started" (`wasm-arch/docs/PACKAGE.md:110-112` on the local `053064f`); the docs keep it outside the app; the engine is Kerk's area; Bao parked his study to focus on the visualizers (2026-11-03) | DOCUMENTED |
| A phone layout | "Mobile. Held pending further instructions" (wireframe); the target-screens rule | DOCUMENTED |
| User evaluation | None exists; the proposals in doc 04 | VERIFIED (absence) |
| The 18 "coming soon" cards; Training, quizzes and slides that drive the visualization; the full Graph Traversal decks; BST/AVL batch insert and remove | `modules.ts`; TP-14; tree backlog 6 and 10; graph backlog 17 | VERIFIED; DOCUMENTED |

## 2. Recommended central contributions

Note 09 §3 ranked contributions by four criteria: diff and blame evidence that the work is Bao's (never commit counts), its status in today's app, engineering depth, and tests that passed on 2026-11-01. The owner's answers change one thing: C1 and C2 are now in scope as week-0 and early-FYP work, so they become a central contribution instead of a conditional one.

| Rank | Contribution | Why it is central | Must be said with it | Section; figures |
|---|---|---|---|---|
| 1 | **C6 V10 "Panel groups" shell** | Bao's design, model, code and tests: `groupsModel.ts` 1,441 of 1,441 lines and `groupsModel.test.ts` 1,355 of 1,355 by `git blame` (VERIFIED, 2026-11-02); the only layout, used by all three visualizers; dated records DD-50 to DD-56 with tree and sorting twins; choices 1 to 26 written in Bao's commits, their quotes in Vietnamese (VERIFIED, blame of `design/proposals/viz-shell-v10/README.md`) | Kerk's drop-band tuning (41 of 388 lines of `dropTargets.ts`, `git blame -w`) for choices 27 and 33, decided together, and his move into `src/shared`; drag and split are tested by hand only | System Design; F2, F3, D2 (doc 04 §1.4) |
| 2 | **C7 Graph algorithms beyond upstream**, led by PR #28 and the End node (DD-45, PR #8) | Six algorithms not in upstream, among them Topological Sort, Bipartite Graph Check and Cut Vertex & Bridge (`b88952d`, `84c5917`, `0fc105c`) and recursive DFS (`4ab075c`); seeded property tests against independent oracles (`*Property.test.ts`; the oracles DOCUMENTED in PR #28); a correctness point, the parent edge skipped by edge id (DOCUMENTED, PR #28); 654/654 graph `node:test` cases in the 2026-11-01 run | Bellman-Ford and Prim were built with Codex at Bao's request (DD-38, DD-39): say so where they are named | System Design (algorithms); Results; F8 |
| 3 | **C1 and C2 Standalone foundations** (week 0 and early FYP) | In scope by the owner's answer; the architecture the app still runs (session reducers byte-identical, VERIFIED); every commit by a BJoozz identity | sorting's history is one squashed commit (Q10); week 0 is 2026-07-28 to about 08-09 (V1 to PR #5), the rest FYP proper | Background (starting point); System Design (state owners) |
| 4 | **C10 Step notes and on-canvas explanation** | Bao's commits (`d82aa18`, `08590ef` and the rest of PRs #29 to #32); one layer serving two visualizers; records quote the dated requests (TP-34, TP-36, DD-61); unit and browser tests passed on 2026-11-01 | Partial coverage; describe the mechanism and its tests, not a learning effect | System Design; F4, F5, F6 |
| 5 (supporting) | **C13 Process and verification evidence** | What lets the report state the other results safely: the green run of 2026-11-01, the CI history, 95 decision records | No PR review; 90 of Bao's commits (2026-09-29 to 10-15) reached main with no merge commit; no user evaluation, coverage figure, cross-browser run or accessibility audit; stated together with the AI facts of §3 | Progress and Results; Limitations; §3 |

Labels in this table: counts, authors, blame, trailers and test results are VERIFIED (2026-11-02 checks, or note 07 §2 for tests) unless marked DOCUMENTED; the ranking itself is an INFERENCE.

**Why these.** All five are integrated in today's app and rest on diffs and blame, not on counts. The first four also match the owner's working description of Bao's part (the visualizers and their integration into the shared interface); C13 is shared ground, since Kerk wrote the current CI workflow `app.yml` and 7 of the 95 records (VERIFIED, blame and first-adding commits). **Where the others go:** C4 is the exploration before V10 (history, one paragraph); C5, the host boundary, sits inside C6's chapter with the design credited to Kerk; C8 gives one deep case if space allows (the Binary Heap round, PR #25, TP-33); C9 gives a design example (exact seeking, the eager gate) on an inherited core; C11 is design rationale; C12 belongs in Background, with credit; C3 is one paragraph, Bao's own study, parked to focus on the visualizers; C14 is Kerk's work, context only.

**A possible chapter order** (INFERENCE): Introduction; Background (visualgo.net, Kerk's base, Bao's standalone visualizers); System Design (architecture; C6 with C4 and C5; C7 with one C8 case; C10; C11); Progress and Results (coverage, tests, CI, reviews: C13); Limitations and Evaluation Plan; Future Work; Development process (§3).

## 3. Development workflow: material for one paragraph

Bao's steer (2026-11-03): the AI assistants worked under his requests, choices and confirmation; the report says so briefly and moves on. Facts for the paragraph (VERIFIED unless marked):

- A `Co-Authored-By: Claude …` trailer is on 199 of Bao's 213 non-merge commits on `main` and on 14 of Kerk's 17; in the standalone repositories on 20 of 38 in graph-visualizer-v2 (from 2026-09-07) and 34 of 41 in tree-visualizer (from 2026-09-12), none in V1 or sorting. 30 of the 37 PR bodies carry "Generated with Claude Code". Per-model counts: doc 01 §1.4.
- Bellman-Ford and Prim were built with Codex (DD-38, DD-39); 8 commit messages on `main` name Codex, mostly for its reviews; its later plans were "input only" (DD-61, PR #28). Of the 14 untrailered commits, the 8 Bellman-Ford and Prim stage commits were made with Codex and the other 6 by hand (owner, 2026-11-03; DOCUMENTED).
- Rules files "for coding agents": `graph-visualizer-v2/AGENTS.md` (from `fc62e5a`, 2026-08-20), `sorting-algorithm-visualizer/AGENTS.md`, the three now "Historical" `prototypes/docs/*/AGENTS.md` and the live `prototypes/AGENTS.md` (created in Kerk's `0394b64`).
- Choices are quoted with their dates in the records and kept apart from "Implementer's defaults" (`design/proposals/viz-shell-v10/README.md:95`), which Bao has accepted as his (owner, 2026-11-03).
- Review findings were "reproduced before the fix" (PRs #27 to #29, #34, #35, #37; DOCUMENTED). The three review sessions of 2026-10-26 to 10-29 were Codex reviews that Bao read first, with the fix options his choices (owner, 2026-11-03).
- Tests in the same change: 159 of Bao's 213 commits on `main` change a test file. 95 decision records (DD-23 to DD-61, TP-01 to TP-36, SP-01 to SP-20): 88 first written in Bao's commits, 7 in Kerk's.
- Bao's own checks before accepting a change (owner, 2026-11-03): reading the diffs, running the app by hand, running the suites or watching CI.

**A draft paragraph:**

> The software was developed with AI coding assistants under my direction. A Claude model is named as co-author on 199 of my 213 commits in the shared repository, most pull-request descriptions carry the footer "Generated with Claude Code", and two algorithms (Bellman-Ford and Prim) were built with Codex, which also reviewed some changes. The assistants read the code, proposed options, implemented changes and drafted documents under rules files (`AGENTS.md`) in graph-visualizer-v2, the sorting repository and the shared one. I set the requirements, made the design choices, which the decision records (DD, TP, SP) quote with their dates, and accepted each change after reading the diff, running the application and running the test suites or checking CI. Review findings, including three Codex review sessions, were reproduced before they were fixed, and I chose the fixes. Changes carried their tests: 159 of my 213 commits change a test file. A full run of every check on 2026-11-01 passed.

## 4. Questions for Bao

**Answered on 2026-11-03 and applied throughout** (doc 01, the table at its top): Q2 (both author strings are his), Q3 (choices 27 to 48, "V10 wins", `40a63bd` and `a074f50` were decided by Kerk and Bao together), Q4 (AI-assisted work was under his requests, choices and confirmation; he read diffs, ran the app and the tests), Q5 (unnamed records are implementer's defaults he accepted), Q6 (the review findings were Codex reviews he read first; the fixes his choices), Q7 (Prof Halim knows and agrees), Q8 (V2 and V7 chosen together after Kerk's user survey), Q9 (the engine study was his idea, parked), Q11 (the checklists were run by hand and by agents, unrecorded), Q12 (the local commits stay local), the figures (7 screenshots and 2 diagrams), the documents' length (kept) and the project description (§1.1).

**Still open.** None blocks a contribution claim.

| # | Id | Question | Why it matters | Blocks |
|---|---|---|---|---|
| 1 | Q8 | Kerk's survey of a group of users behind V2 and V7: when, how many people, what was asked, what came out; is there a form or a sheet? | The only user feedback the project has. Without the data the report can say only that a survey informed the choice | Background (the layout exploration); Limitations |
| 2 | Q1 | The exact date of Week 1 of the semester (about 2026-08-10) | The week-0 boundary in doc 01 | the timeline's labels |
| 3 | Q6 | Which supervisor remarks will you add, and from what source (email, meeting notes)? | The project description gives his early direction in your words; anything more needs a source | Introduction; Limitations |
| 4 | Q11 | Should the dated profiles (2026-08-13, 10-03, 10-05) be cited? Should Kerk's `wasm-arch` suite and the study's tests be run for the report? | Results can report only what exists | Progress and Results |
| 5 | Q10 | V1's history before 2026-07-28 and sorting's before its squash; did tree-visualizer start from v2's code? | Only the week-0 narrative | Background |

Still open in note 09 but not blocking: Q13 (stale docs and known debt), Q14 (coverage wording; §1.4 states the definition), Q15 (the Vercel attempt), Q16 (the unrelated wireframes and upload), Q17 (small facts).

## 5. Claims to avoid without more evidence

Condensed from the 24 of note 09 §5 (their numbers in the last column), plus three that follow from the owner's answers; updated for the answers of 2026-11-03.

| # | Do not write | Why | Write instead | Note 09 §5 |
|---|---|---|---|---|
| 1 | VisuAlgo+ helps students learn, is easier to use, or is preferred to visualgo.net | No user study exists in the repository (VERIFIED, note 07 §6); the one survey, Kerk's on the layouts, has no data with Bao | "VisuAlgo+ has not yet been evaluated with users beyond an early layout survey; an evaluation is proposed." | 1 |
| 2 | It is fast, scales to large inputs or uses little memory | No benchmark. The only timings are dated observations of earlier builds (sorting 2026-08-13 on the standalone engine; Bellman-Ford 2026-10-03; Prim 2026-10-05) whose scripts are gone (VERIFIED) | "No performance measurement of the current app exists." Quote an observation only with its date, build and caveat | 2, 20 |
| 3 | A feature is novel, the first or unique | The repository holds no comparison with other tools or with literature (note 09 §5); V10's drag feedback "follows VS Code" (DOCUMENTED, PR #15); the content follows visualgo.net | Describe the design and the reasons the records give | 3 |
| 4 | Bao wrote N lines, N% of the code or N commits, as a measure of effort or ownership | Two or three copies of each visualizer until 2026-10-18, folder moves and code from his own repositories inflate counts; blame shows the last change only (VERIFIED, notes 01 and 08) | Name the commits and files whose diffs and blame show the work | 4 |
| 5 | "Claude wrote X", or "Bao wrote X without AI" | The assistants worked under Bao's requests, choices and confirmation (owner, 2026-11-03); a trailer records tool use only, and a missing one proves nothing (DD-38, DD-39) | the one paragraph of §3 | new |
| 6 | Bao designed Bellman-Ford and Prim himself | DD-38 and DD-39 record the plans as Codex's, with Bao's dated choices (DOCUMENTED) | "Added to the graph module, built with Codex at my request (DD-38, DD-39)" | 5 |
| 7 | The app runs on Kerk's WebAssembly engine; the integration is done; the study's tests pass; Bao co-built the engine | Nothing in `prototypes/src` uses `wasm-arch`; the study is unmerged; its pass results are only in commit messages, with no CI run; no Bao commit on main touches `wasm-arch/` (VERIFIED) | "An unmerged integration study (2026-09-17) on Kerk's engine; its tests were not independently run" | 6, 7 |
| 8 | The work was code-reviewed or peer-reviewed (by Kerk or the supervisor) | 37 PRs, 0 reviews, 0 comments (VERIFIED, 2026-11-02); 90 of Bao's commits (2026-09-29 to 10-15) reached main with no merge commit | "Three Codex review sessions, which I read first; each finding was reproduced before its fix, and I chose the fixes (PRs #34 to #37)" | 8 |
| 9 | The supervisor asked for, approved or commented on X, beyond the early direction in §1.1 | No email or meeting notes were available to this audit (VERIFIED, doc 01 §1.5); the repository never mentions a supervisor (VERIFIED) | the early direction as Bao's description gives it; add other remarks only with a source | new |
| 10 | Choices 27 to 48, or "V10 wins", were Bao's alone (or Kerk's alone) | They are quoted in English in Kerk's commits (VERIFIED, blame); Bao says Kerk and he decided them together (DOCUMENTED, 2026-11-03) | "decided with Kerk after testing the deployed build, implemented in Kerk's commit `<hash>`". For choices 1 to 26: "my choices, quoted in my commits" | 14, 24 |
| 11 | Bao made the design system, the wireframes or the homepage design; or Kerk only set up deployment | Kerk added them (`634b5be`, `69aa8e4`), and also consolidated the app (`0394b64`), made the site the only bar and theme writer (`c59c155`) and changed the footer (`a074f50`, `01a1a4a`) (VERIFIED) | "Built on Kerk's design system, wireframe and UI kit"; credit Kerk's consolidation and chrome changes | 15, 23 |
| 12 | The app is accessible or WCAG compliant, or works in every browser and on phones | Contrast is checked for a sample of text only; tests run in Chromium at desktop sizes (VERIFIED, note 07); some colours fall below the minimums (DOCUMENTED, graph backlog 14); mobile is "held pending" (DOCUMENTED, wireframe) | "Text contrast is tested at 4.5:1 for a sample of chrome text in all nine themes; tested in Chromium at desktop window sizes" | 9, 10 |
| 13 | High test coverage; the site is deployed on Vercel; CI was always green; the browser suite tests panel drag and split, or always covered the modules; the PR-body test counts are verified results | No coverage tool; no Vercel deployment was found and PR #5 was closed (Q15); 8 of 266 CI runs failed; tab drag and split are manual, and the specs went from 208 files to 12 on 2026-10-18; PR counts are the implementer's reports (VERIFIED) | "3,273 unit and 151 browser cases passed on 2026-11-01"; "deployed by GitHub Pages; each CI failure was fixed by a later commit"; say which scenarios are automated | 11, 16, 17, 18 |
| 14 | VisuAlgo+ covers or replaces visualgo.net, or uses its material with permission | 8 of visualgo.net's 26 listed modules open here (4 full) and 18 cards are "coming soon" (VERIFIED); PR #4: "not a replacement" (DOCUMENTED); the agreement is Prof Halim's by Bao's account, not written (DOCUMENTED) | Give the counts with the definition of "full"; "adapted from visualgo.net with Prof Halim's agreement" | 12, 13 |
| 15 | History claims: the FYP began in July; V2 and V7 are part of the product; V10 was built in a day; tree-visualizer was built from v2's code | Week 0 is Bao's framing and the FYP proper began in Week 1 of the semester, about 2026-08-10 (DOCUMENTED, owner's answer); V2 and V7 were deleted on 2026-10-18 (VERIFIED, `0394b64`); the commits were made in agent-run stages, so dates are no basis for productivity (INFERENCE); tree from v2 is an INFERENCE (Q10) | "Work from 2026-07-28 to about 08-09 is included as week 0"; "two earlier layouts, compared and then merged into V10"; dates without conclusions | 19, 21, 22; new (the July start) |

## Sources and checks

Phase-1 notes `evidence/research-notes/01` to `09` and `evidence/inputs/prs.txt`. Re-checked for this document on 2026-11-02, read-only: date, author and subject of every hash cited; commit, merge and trailer counts and the first-parent commits on main; the four clones' first and last commits and trailers; `prototypes/package.json` and the library imports; the card statuses in `prototypes/src/site/modules.ts`; `git blame` of the V10 choices table, `groupsModel.ts`, `dropTargets.ts`, `src/site` and `prototypes/AGENTS.md`; the session reducers' blob hashes; PR reviews, comments and issues (GitHub GraphQL API); CI runs (`gh run list`). The main repository stayed clean on main.

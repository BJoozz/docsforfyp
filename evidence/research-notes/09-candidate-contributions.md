# 09 - Candidate contributions: timeline, groups, shortlist, questions

Synthesis for Bao's FYP interim report (Truong Van Quoc Bao, GitHub BJoozz). Collaborator and repository owner: Kerk Tai Heng (GitHub kerktaiheng). Written 2026-11-01. Repository `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3`.

## How this note was made

- **Sources.** The eight audit notes `01` to `08` in this folder, read in full, and `in/prs.txt` (all 37 PR bodies). Each claim names its source note in brackets, for example [03]. The label comes from that note: its author saw the evidence on 2026-11-01.
- **My own checks** (read-only, 2026-11-01): `git status` (clean, on `main` at `662e7b3`); `git show -s` on 22 key commits (authors and dates match the notes); `git blame` of `prototypes/src/shared/components/layout/groupsModel.ts` (1,441 lines, all BJoozz); the `Co-Authored-By` trailers of 6 commits; `git grep` for "Codex" in `prototypes/docs/graph/DESIGN_DECISIONS.md` (lines 601-602, 665, 2614-2617); `git ls-tree` of the graph algorithm tests and the `src/shared` tests. Claims I checked myself say "re-checked".
- **Tests.** I ran none for this note. Every test result quoted comes from a note: [02] the four standalone repositories; [03] three shell and site files; [06] 340 cases; [07] the full check set on `662e7b3` (2026-11-01, 22:34 to 22:39 +07:00); [08] 654 + 2,619 unit cases.
- Nothing was written inside the repository, the clones or the worktrees.

**Labels.** VERIFIED: seen in code, a diff, a log or a test run. DOCUMENTED: a doc, commit message or PR body says it, not checked against code. INFERENCE: a reading of the evidence. QUESTION: Bao must answer (questions are numbered Q1 to Q17 in section 4).

**"The owner".** In Bao's branches the owner is Bao (to be confirmed, Q3). In Kerk's commits of 2026-10-18 to 2026-10-22 the owner is not known, so every such attribution below is a QUESTION.

**"Bao"** below means the two BJoozz identities, `123baoek31@gmail.com` and `83776047+BJoozz@users.noreply.github.com` (Q2).

## Key facts

1. Before VisuAlgo+, Bao built four standalone repositories, all commits by the BJoozz identities: graph V1 (2026-07-28 to 08-19), sorting (one squashed commit, 08-19), graph-visualizer-v2 (08-20 to 09-11) and tree-visualizer (09-03 to 09-17). VERIFIED [02]
2. Kerk created `visualgo-plus-design` on 2026-09-03 with his design system and his WASM engine prototype, and added the wireframes with nine page layouts on 09-04. VERIFIED [01]
3. Bao's first commit there is `986deba` (2026-09-13). On `main` Bao has 213 own commits and 33 merges, Kerk 17 and 4. Bao opened 33 of the 37 PRs. VERIFIED [01]
4. Kerk's `0394b64` (PR #20, 2026-10-18) deleted the V2/V7 copies, their sites and the submodules, and made one app in `prototypes/`. VERIFIED [01]
5. 199 of Bao's 213 own commits on `main` carry a `Co-Authored-By: Claude` trailer. The records also name Codex as the planner and builder of Bellman-Ford and Prim. VERIFIED [01], [04] (re-checked)
6. The whole check set passed on 2026-11-01: typecheck, lint (0 errors, 2 warnings), 3,273 unit cases, the build, and 151 of 151 browser cases. VERIFIED [07]
7. No PR has a review or a comment, and 90 of Bao's commits reached `main` without a merge commit. VERIFIED [01]
8. The repository holds no user study, benchmark, coverage figure or automated accessibility audit. VERIFIED [07]

## 1. Timeline, 2026-07-28 to 2026-10-31

Dates are git author dates in the author's own time zone (+07:00 or +08:00). GitHub merge times are UTC, so a PR can look one day earlier than its merge commit [01]. **Period:** "Prep" = preparatory work before the likely semester start; "Sem" = work after it. The semester start is a QUESTION (Q1), and so is whether the standalone repositories count as FYP work at all. A second possible boundary is 2026-09-13, when Bao's work entered the shared repository (row 9).

| # | Dates (2026) | Period | Phase | Repository / branch | What happened | Who | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | 07-28 to 07-31 | Prep | 0. Graph V1 | graph-algorithm-visualizer, `main`, PR #1 | First version (editor, force layout, BFS and DFS with pseudocode, queue and stack); a generic `VisualizationPlayer`; Vitest added | Bao | `f3a0db8`, `2c4feaa`, merge `ab3676a`, `788af81` [02] |
| 2 | 07-31 to 08-09 | Prep | 0. Graph V1 | same, PRs #2 to #5 | Weighted Dijkstra; parallel edges; Edmonds-Karp with a residual view; minimum cut and samples | Bao | `265d6a7`, `3103aff`, `447abc0`, `87566f9` [02] |
| - | **about 08-10** | - | **Likely semester start** | - | **NUS AY2026/27 Semester 1 began around 2026-08-10. QUESTION (Q1): confirm the date, and when the FYP itself started.** | - | task brief |
| 3 | 08-11 to 08-19 | Sem | 1. Standalone | graph V1, PRs #6 to #8 | Fullscreen and polish; Kruskal with Union-Find; Playwright and a GitHub Actions workflow; editor sidebar (V1's last commit) | Bao | `4315111`, `b0bb316`, `2a94a7e`, `5fc06a0` [02] |
| 4 | by 08-13 to 08-19 | Sem | 1. Standalone | sorting-algorithm-visualizer | One squashed commit: 8 algorithms, typed operations, 1, 2 or 4 panes, Canvas renderer, profiler. Its performance doc is dated 08-13 | Bao | `9236a65` [02] |
| 5 | 08-20 to 09-03 | Sem | 1. Standalone | graph-visualizer-v2 | A rewrite of V1: agent rules file, one workspace and one canvas, the five algorithms, docs with DD-01 to DD-22, samples, large graphs | Bao | `92fa193`, `fc62e5a`, `f6149f1`, `f864de7`, `c5dfb43`, `0f5b49a`, `e8a73be` [02] |
| 6 | 09-03 to 09-04 | Sem | 2. Kerk's base | visualgo-plus-design, `main` | Repository created; design system (its own file says "Last sync 2026-08-27"); C++/WASM engine with protobuf RPC; Python tracing engine; logging; wireframes with page layouts V1 to V9 | Kerk (Claude trailers on 4 of his 6 commits of these two days) | `634b5be`, `b3e86ba`, `e396e06`, `69aa8e4`, `aa541a1` [01], [03], [05] |
| 7 | 09-03 to 09-17 | Sem | 1. Standalone | tree-visualizer | Six workspaces (LCA, BST, AVL, Min Heap, Trie, Segment Tree); Binary Lifting; PRs #1 to #8 (review fixes, accessibility, shortcuts, samples) | Bao (Claude trailers from 09-12) | `e687099`, `015469e`, `1477cda`, `a4b6d08`, `46ce0a7` [02] |
| 8 | 09-07 to 09-11 | Sem | 1. Standalone | graph-visualizer-v2, PRs #1 to #14 | Tests by glob, Playwright, CI, typed IDs, inspector and legend UX; the last commit is the one copied later | Bao (Claude trailers from 09-07) | `ce0cb7b`, `d9abac1`, `acc3062`, `c8b14e6` [02] |
| 9 | 09-13 to 09-16 | Sem | 3. Joining | `bj/visualization-work` | Bao's first commit in the shared repository: graph and tree submodules; a merge of `main` | Bao | `986deba`, `4bd9ca9` [01] |
| 10 | 09-13 to 09-14 | Sem | 2. Kerk's base | `main` | Clean-up; CI and Pages fixed | Kerk | `598193b`, `df99dac` [01] |
| 11 | 09-17 | Sem | 3. Engine study | `bj/engine-v2-experiment`, plus two local branches | Milestones M0 to M4a in `wasm-arch/`: stable edge IDs, a browser engine client, a BFS runtime, a packaging spike. Never merged | Bao (Claude trailers on 4 of 6) | `478174f`, `e348a6d`, `ffb9274`, local `053064f`, `53d2ef4` [05] |
| 12 | 09-20 to 09-21 | Sem | 4. Layouts | `bj/graph-wireframe-v2-v7`, PR #1 | Graph prototypes in Kerk's wireframe layouts V2 (split rails) and V7 (docks); the first prototype CI | Bao | `0073875`, `37075b1`, merge `6a621df` [01], [03] |
| 13 | 09-22 to 09-23 | Sem | 4. Layouts | PR #2 | Tree V2/V7 prototypes in the graph's page shell | Bao | `7b16bf3`, merge `495fa73` [01] |
| 14 | 09-23 to 09-27 | Sem | 4. Layouts | PR #3 | Sorting submodule; sorting V2/V7 with Study and Compare, pseudocode, exact seeking, a 60,000-operation eager cap | Bao | `e7a44f9`, `ee4bb72`, `5ccef45`, `fed2420`, merge `ca56cef` [01], [08] |
| 15 | 09-28 to 09-29 | Sem | 4. Site | PR #4; the fork; PR #5 | VisuAlgo+ V2 and V7 websites with the real visualizers under one bar; static-host support. A Vercel attempt from the fork (PR #5, closed 10-25, never merged) | Bao | `87db4a3`, `8aeb543`, `57912e8`, merge `9cc009f`; `c9e4598` [03] |
| 16 | 09-29 to 10-08 | Sem | 5. Growth | `bj/visualgo-web-editors` (PR #6: fast-forward, empty body) | Dijkstra's distances on the nodes; recursive DFS; Graph and Tree Editor cards; an omitted weight reads as 1; edge waves; Bellman-Ford and Prim (the records say Codex planned and built them); extra panel and LCA ancestor strip; homepage credit "by Kerk and Bao" | Bao (the 8 Bellman-Ford and Prim stage commits have no trailer) | `6fc6150`, `4ab075c`, `cc38942`, `0919126`, `bcbed32`, `aef5d0b`, `4bd0879`, `00ed4c2`, `ae2f31f` [03], [08] |
| 17 | 10-09 to 10-10 | Sem | 5. Growth | `bj/segment-tree-lazy`, `bj/bst-avl-operations` (pushed to `main`, no PR) | Lazy segment tree with exact decimals; tree e-Lectures; BST/AVL operations (Min/Max, Pred/Succ, Lower Bound, Select, traversals, AVL Delete) | Bao | `fc4172d`, `a521c13`, `3a429ad`, `c364204`, `e7f2fec`, `9a2f04b`, `c620145` [08] |
| 18 | 10-10 to 10-15 | Sem | 5. Growth | `bj/uiux-pass-1` (44 commits), `bj/dock-drop-zones` (pushed to `main`, no PR) | Go folded into Play; a presets picker; paused-step motion; drag with Live off; merged steps; end badges; value popups; see-through legend; "upstream is a reference only" rule; V7 drop zones. `main` red in CI from 10-10 to 10-14 (one font-sensitive test) | Bao | `117975a`, `57d0144`, `7e92baf`, `74a4958`, `38c726f`, `0d1f6de`, `28e08f8`, `ff77eca`, `f510477` [01], [04], [07], [08] |
| 19 | 10-14 to 10-17 | Sem | 6. PR flow | PRs #7 to #14 | CI font fix; End node (DD-45); Live layout starts off (DD-46); centred footer; final-frame motion (DD-47); visualgo.net's sample graphs (DD-48); node label size (DD-49) | Bao | `3a6443b`, `9e6e7bd`, `6b953d5`, `d6ce97b`, `be570eb`, `bc46260`, `e360df1` [01], [08] |
| 20 | 10-16 to 10-18 | Sem | 6. V10 | PRs #15 to #17 | V10 "Panel groups": proposal and frames V10/V11; the pure groups model; the shell; graph, tree, sorting and site copies; review fixes (choices 24 to 26) | Bao (PR #17 merged by Kerk) | `55f3387`, `72450e1`, `a876206`, `d445364`, merges `c899b69`, `f286712`, `b9ec8fa` [03] |
| 21 | 10-18 | Sem | 7. One app | PRs #18 to #21 | Pages serves V10 at `/` and the engine demo at `/engine/`; choices 27 to 41; V2/V7, two sites and the submodules deleted; one app and `app.yml` CI; the site becomes the only bar and theme writer | Kerk (Claude Opus 5.5 trailers; "owner" QUESTION) | `c39b3cf`, `ae63a62`, `0394b64`, `c59c155`, merges `94cdaf3`, `8d7a63a`, `fae8418` [01], [03] |
| 22 | 10-19 to 10-22 | Sem | 7. One app | `main`, pushed directly | Choices 42 to 48: no Save image; Full screen and Shortcuts beside Settings; homepage tips removed; Autoplay beside Stop and Next starts a run; coloured chips | Kerk ("owner" QUESTION) | `3c79d36`, `40a63bd`, `a074f50`, `01a1a4a` [01] |
| 23 | 10-19 to 10-22 | Sem | 8. Features | PRs #22 to #28 | Tree edges centre to centre (TP-30); LCA as two runs (TP-31) and its hover (TP-32); Binary Heap with Min/Max and visualgo.net's operations (TP-33, three PRs); Topological Sort, Bipartite Check, Cut Vertex & Bridge (DD-60) | Bao | `499cb42`, `e55de1c`, `60ccc44`, `7d39c38`, `ea37326`, `b88952d`, `84c5917`, `0fc105c`, merge `4621b1f` [08] |
| 24 | 10-23 to 10-26 | Sem | 8. Features | PRs #29 to #33 | Step notes in the tree (TP-34, TP-36) and for Dijkstra (DD-61) on one shared note layer; a smaller shared legend. One CI failure, fixed 11 minutes later | Bao | `d82aa18`, `7180d81`, `94ec5db`, `08590ef`, `6b1a4fc`, `19aaef3`, `b47d437`, `b309309` [07], [08] |
| 25 | 10-26 to 10-30 | Sem | 9. Reviews | PRs #34 to #37 | Review sessions 1 to 3: Inter font guard, Node 22.12 floor, flag forwarding, CI traces; the tab strip keeps its tab in view; docs sweep and the copy rule retired; a shared playback countdown; sorting restarts always play | Bao (who produced the findings: QUESTION) | `a5bb08f`, `fd9ff5c`, `02c4e12`, `9baa117`, merges `ad5e119`, `4dedee1`, `f58ed5f`, `662e7b3` [07] |
| 26 | 10-31 | Sem | - | `main` | `662e7b3` is the last commit (merged 2026-10-30 17:04 UTC). Nothing after it; this audit ran on 11-01 | - | [01] |

**Preparatory versus semester work** (INFERENCE from the dates; depends on Q1):

- **Preparatory, before about 08-10:** rows 1 and 2 only, graph V1 from its first version to maximum flow and minimum cut.
- **Semester, standalone, in Bao's own repositories:** rows 3, 4, 5, 7 and 8 (V1's finish, sorting, graph-visualizer-v2, tree-visualizer).
- **Semester, in the shared repository:** rows 6 and 9 to 26. Kerk's own work is rows 6, 10, 21 and 22; the rest is Bao's.
- If the FYP began only when Bao joined the shared repository (2026-09-13), rows 1 to 8 are all preparatory or prior work.

## 2. Candidate major contributions

Fourteen groups, not a changelog. C1 to C3 come before or beside the shared app; C4 to C12 are the app's features; C13 and C14 are process and infrastructure. "Bao's part" rests on diffs, blame and logs, never on commit counts or merge commits alone.

| ID | Contribution | Period (2026) | Status now | Whose, in short | Report value |
|---|---|---|---|---|---|
| C1 | Graph visualizer: V1, then the v2 redesign | 07-28 to 09-11 | V1 superseded; v2 is the base of today's graph module | Bao (v2 with Claude trailers from 09-07) | High as the foundation, if it counts as FYP work (Q1) |
| C2 | Tree and sorting standalone visualizers | 08-13 to 09-17 | the base of today's tree and sorting modules | Bao | Medium-high as the foundation |
| C3 | Engine integration study on Kerk's WASM engine | 09-17 | experimental, never merged | Bao, on Kerk's engine | Low-medium |
| C4 | Layout prototypes V2 (split rails) and V7 (docks) | 09-13 to 10-15 | removed on 10-18; ideas kept in V10 | Bao, from Kerk's wireframe | Medium (design exploration) |
| C5 | The VisuAlgo+ site and its host boundary | 09-28 to 10-20 | integrated and deployed | Bao's build on Kerk's design system; later chrome changes by Kerk | High, with careful credit |
| C6 | V10 "Panel groups" shell | 10-16 to 10-30 | integrated; the only layout | Bao (Kerk: band tuning, move to `src/shared`) | Highest |
| C7 | Graph algorithms beyond upstream | 09-29 to 10-22 | integrated | Bao; Bellman-Ford and Prim recorded as Codex-built | High |
| C8 | Tree operations beyond upstream | 10-07 to 10-21 | integrated | Bao | Medium-high |
| C9 | Sorting in the shell: Study, Compare, exact seeking | 09-23 to 10-30 | integrated | Bao, on the inherited sorting core | Medium |
| C10 | Step notes and other on-canvas explanations | 10-13 to 10-26 | integrated, partial coverage | Bao | High |
| C11 | Motion and playback semantics | 10-02 to 10-30 | integrated | Bao; two footer changes by Kerk | Medium |
| C12 | Content from visualgo.net: samples, e-Lectures, catalogue | 09-28 to 10-22 | integrated | Bao; the source is visualgo.net | Medium-low (credit matters) |
| C13 | Process and verification evidence | 09-20 to 10-30 | in use | mostly Bao; 7 records and the CI file by Kerk | High (evaluation chapter) |
| C14 | One app, CI and deployment | 09-03 to 10-30 | integrated and deployed | mostly Kerk | Context only |

### C1. Graph visualizer: V1, then the v2 redesign (standalone)

| Field | Content |
|---|---|
| Period | 2026-07-28 to 2026-09-11 |
| Where | `BJoozz/graph-algorithm-visualizer` (V1: 55 commits on all refs, 24 on `main`, 8 PRs, HEAD `5fc06a0`) and `BJoozz/graph-visualizer-v2` (53 commits, 14 PRs, HEAD `c8b14e6`) [02] |
| Problem | An editable weighted graph that plays BFS, DFS, Dijkstra, Edmonds-Karp with minimum cut and Kruskal step by step. v2 rebuilt V1's structure: V1 had one large `App`, separate edit and run canvases, topology snapshots per step and eager timeline regeneration; v2 splits the state into owners (`GraphDocument`, `GraphLayout`, `VisualizationSession`, `GraphPresentation`) around one canvas that stays mounted, with typed sequences built only when a run starts. DOCUMENTED [02] (v2 README, AGENTS.md, DD-01 to DD-12) |
| Bao's part | Every commit in both repositories is by a BJoozz identity. VERIFIED [02]. V1 has no Claude trailer on its 50 non-merge commits; v2 has one on 20 of 38, all from 2026-09-07; v2's 14 PRs came from `agent/*` branches, and its `AGENTS.md` ("for coding agents") dates from its second commit. VERIFIED [02] |
| Kerk's part | None found. VERIFIED [02] |
| Inherited | The create-vite template (v2's first commit `92fa193`; template files in V1's first commit). A few V1 files were ported into v2 (`CenteredGraphEdge`, `parallelEdges`, `CsaGraphNode`, the Union-Find of `kruskalEngine`). VERIFIED (shared-line counts), INFERENCE (ported) [02] |
| Status now | V1: superseded, never copied into VisuAlgo+ (0 mentions on `main`). v2: integrated; copied at `c8b14e6` into `0073875`; 53 of its 173 `src` files are still byte-identical, among them `visualization/sessionReducer.ts`; its DD-01 to DD-22 are inherited records. VERIFIED [02], [06] |
| Strongest evidence | Unit runs on 2026-11-01: V1 162/162, v2 276/276; v2's CI was green on `c8b14e6`. VERIFIED [02]. v2's ARCHITECTURE (493 lines) and DESIGN_DECISIONS (DD-01 to DD-22, 16 commits, all BJoozz). VERIFIED [02], [04] |
| Verdict | High value for a "foundations and design rationale" chapter, but only if this period counts as FYP work (Q1); V1 alone is background. |

### C2. Tree and sorting standalone visualizers

| Field | Content |
|---|---|
| Period | Sorting: by 2026-08-13 (the date in its performance doc) to 08-19. Tree: 2026-09-03 to 09-17 |
| Where | `BJoozz/sorting-algorithm-visualizer` (one commit, `9236a65`); `BJoozz/tree-visualizer` (50 commits, 8 PRs, HEAD `46ce0a7`) [02] |
| Problem | Tree: one persistent rooted-tree workspace for LCA (Binary Lifting), BST, AVL, Min Heap, Trie and Segment Tree, with a tidy layout and previews that change the tree only on Apply. Sorting: algorithms that record typed delta operations, playback that applies and reverses them, 1, 2 or 4 panes on one global tick, a Canvas renderer and lazy operation streams. DOCUMENTED [02] |
| Bao's part | All commits by BJoozz. Tree: Claude trailers on 34 of 41 non-merge commits, all from 09-12. Sorting: one squashed commit with no trailer and an 814-line `AGENTS.md`. VERIFIED [02] |
| Kerk's part | None found. [02] |
| Inherited | INFERENCE: the tree began from v2's architecture and session code (its `sessionReducer.ts` shares 72 lines with v2's); no doc says so (Q10). [02] |
| Status now | Integrated. The tree was copied at `46ce0a7` into `7b16bf3` (all 106 algorithm files byte-identical at the copy; 88 of 289 files still identical). Sorting's domain was forked at `9236a65` into `ee4bb72` (17 of 45 files still identical). The tree's session reducer and paces are byte-identical in the app. VERIFIED [02], [06], [08] |
| Strongest evidence | Unit runs on 2026-11-01: tree 664/664; sorting 334/335, the one failure caused by the PC's vi-VN locale in `Metrics.test.tsx`, an assertion the app does not contain. Neither repository has CI. VERIFIED [02] |
| Verdict | Medium-high as the foundation of the tree and sorting modules. The sorting process is not evidenced (one squashed commit, Q10), and its 2026-08-13 performance numbers describe the standalone engine only. |

### C3. Engine integration study on Kerk's WASM engine (M0 to M4a)

| Field | Content |
|---|---|
| Period | 2026-09-17, 01:12 to 13:09 +08:00 |
| Where | `origin/bj/engine-v2-experiment` (`478174f`, `e348a6d`, `ee65bef`, `ffb9274`), local `bj/engine-package-spike` (`053064f`), local `bj/bfs-wasm-spike` (`53d2ef4`); all inside `wasm-arch/`; no PR and no CI run. VERIFIED [05] |
| Problem | Kerk's engine finds an edge by its two endpoints, so a parallel edge cannot be reached (`wasm-arch/engine/src/session.cc:154`, VERIFIED [05]). M1 gives every edge a stable ID through engine, journal and Delta; M2 adds a reusable `GraphEngineClient` whose one-way lifecycle rejects pending calls on any worker failure; M3 adds `KerkBfsRuntime` for hosts with string IDs (one call at a time, a generation counter against stale responses); M4a packages it privately. DOCUMENTED, with the code VERIFIED [05] |
| Bao's part | All six commits by the BJoozz gmail identity; Claude trailers on 4 of 6. Test definitions counted at M1, M2, M3 and M4a: 44, 59, 125 and 130 Node tests. VERIFIED (counts) [05]. That they pass: DOCUMENTED only, in commit messages; no CI ran. |
| Kerk's part | The engine itself (2026-09-03 to 09-14): one protobuf message type per service, a symmetric RPC, a C++20 coroutine engine compiled to WASM with a reversible journal of Deltas, and a Python engine that traces sorts in Pyodide. Its 25 Node and 9 Python tests pass in CI on `662e7b3`; the deployed demo's self-test passed 15/15 on 2026-11-01. VERIFIED [05] |
| Inherited | Kerk's engine, at base `4bd9ca9`. |
| Status now | Experimental: never merged and not used by the app (no engine names in `prototypes/src`). `053064f` and `53d2ef4` exist only in this local clone, and the spike worktree's files are gone from disk. VERIFIED [01], [05] |
| Strongest evidence | `git cherry main` marks all 4 pushed commits "+"; the branch docs `EDGE_IDENTITY.md` (partly Vietnamese), `ENGINE_CLIENT.md`, `KERK_BFS_RUNTIME.md`, `PACKAGE.md`. VERIFIED [01], [05] |
| Verdict | Low-medium: at most a short "integration study, parked" section, said to be unmerged and not tested in CI (Q9). |

### C4. Layout prototypes V2 (split rails) and V7 (docks) for the three visualizers

| Field | Content |
|---|---|
| Period | 2026-09-13 (submodules) to 2026-10-15 (V7 drop zones); deleted 2026-10-18 |
| Where | PRs #1 (graph), #2 (tree), #3 (sorting); `bj/dock-drop-zones` (pushed to `main`); six folders `*-split-rails` and `*-docks` [01] |
| Problem | Put the three visualizers into Kerk's wireframe-2 page (top bar; Action, e-Lecture, Pseudocode and Status panels; a footer transport) and compare two of its nine layouts, V2 split rails and V7 movable docks. VERIFIED (frames in the wireframe file) [03]; the purpose is DOCUMENTED (PR #1) |
| Bao's part | All six folders added by BJoozz (`0073875`, `7b16bf3`, `ee4bb72`). VERIFIED [01]. The copy discipline (fix V2 first, then V7, checked with `diff -rq` and `cmp`) is DOCUMENTED [03]; a blob comparison at `94cdaf3` gives, for graph, 340 identical files and 38 that differ. VERIFIED [03]. DD-23 to DD-28 date from this time. VERIFIED [04] |
| Kerk's part | The wireframe with layouts V1 to V9 (`69aa8e4`) and the design-system themes reached through the `@ds` alias. VERIFIED [03]. Who picked V2 and V7 from the nine is a QUESTION (Q8). |
| Inherited | The domain code of C1 and C2. |
| Status now | Removed by Kerk's `0394b64` (2,573 files deleted). The features built in these copies survived, because the V10 copies were made from the docks copies, and `groupsModel.ts` names V7's `docksModel.ts` as the source of its region maths. VERIFIED [03] |
| Strongest evidence | Merges `6a621df`, `495fa73`, `ca56cef`. The PR bodies' test counts are the implementer's, and PRs #3 and #4 say the final suites were "not independently rerun" (DOCUMENTED [03]). The old CI matrix never ran sorting or the sites. VERIFIED [03] |
| Verdict | Medium: the comparison step that led to V10; cite it as history, not as part of the product. |

### C5. The VisuAlgo+ site and its host boundary

| Field | Content |
|---|---|
| Period | 2026-09-28 (PR #4) to 2026-10-20 (Kerk's last site edit) |
| Where | PR #4 (`87db4a3`, `8aeb543`, `a8dd634`, `57912e8`), PR #6 (`cc38942` editor cards, `ae2f31f` credit line), `5e745b2`, PR #15 (`d445364`); now `prototypes/src/site` [03], [08] |
| Problem | One site that mounts the real visualizers under one top bar: a homepage catalogue of 30 cards (8 full, 4 partial, 18 "soon"); routes `/`, `/:slug` and `/:slug/:algorithm` with redirects for former ids; one owner of the theme (`html[data-theme]`); static hosting under a subpath (`VA_BASE`, a `404.html` fallback). VERIFIED [03], [06] |
| Bao's part | Created the site and the host-chrome boundary (`HostChromeContext`, `renderTopBar`). `git blame`: 1,854 of 1,910 lines of `src/site`; `scripts/static-fallback.mjs` 29/29; `prototypes/e2e` (19 files) 5,236 of 5,306 lines. VERIFIED [03]. The Graph Editor and Tree Editor cards. VERIFIED [08] |
| Kerk's part | The design system (tokens, nine themes, 26 components) and its UI kit `HomeScreen.jsx`, which the homepage follows; the site imports 5 of the components, and the site proposal calls the page "Kerk's homepage" and the kit "Kerk's UI kit". VERIFIED (imports), DOCUMENTED (wording) [03]. 56 blame lines (bar buttons, the account flag, the tips removal). `c59c155` made the site the only bar and the only theme writer by deleting the visualizers' own bars, menus and theme writers. `prototypes/vite.config.ts` is 72/72 his (rewritten in `0394b64`, keeping Bao's `VA_BASE`). VERIFIED [03], [06]. Whose choices 33 to 45 are: QUESTION (Q3) |
| Inherited | The card list is "transcribed from visualgo.net's own homepage table" by way of the design system's `data.js` (DOCUMENTED [08]). The VisuAlgo name and the NUS Computing and Optiver logos (VERIFIED [03]; their use: Q7) |
| Status now | Integrated, and deployed by GitHub Pages (HTTP 200 on 2026-11-01; not opened in a browser). VERIFIED [07] |
| Strongest evidence | `modules.test.ts` 24/24; the `home`, `journey`, `chrome` and `themes` specs inside the 151/151 run; `themes.spec.ts` computes the WCAG contrast ratio of a sample of chrome text in all nine themes. VERIFIED [03], [07] |
| Verdict | High for a "system integration" section, if credited as Bao's build on Kerk's design system and UI kit, with the single theme writer credited to Kerk's `c59c155`. |

### C6. V10 "Panel groups" shell

| Field | Content |
|---|---|
| Period | 2026-10-16 (proposal `55f3387`) to 2026-10-18 (PR #17); a later fix on 2026-10-28 (PR #35) |
| Where | PR #15 (20 commits: `72450e1` model and drop geometry, `a876206` shell, `950ab6f` graph page, `12cdf92` DD-50 to DD-56, the tree, sorting and site copies), PRs #16, #17 and #35; now `prototypes/src/shared/components/layout` [03], [06] |
| Problem | After V2 and V7 had been built and compared, V10 merges their ideas (PR #15: "V2's and V7's ideas merged"): three regions (left, right, bottom), each a stack of collapsible tab groups, around a fixed canvas that is never a tab and never remounted; drag feedback in VS Code's style; one pure model whose invariants every operation keeps; one resolver, `resolveLayout`, that holds every minimum (a 360x320 drawing floor, groups at least 240px wide and 120px high). DOCUMENTED (PR #15, the file's header) [03]; the constants VERIFIED [03] |
| Bao's part | `git blame` at `HEAD`: `groupsModel.ts` 1,441 of 1,441 lines (re-checked), `groupsModel.test.ts` 1,355/1,355, `GroupsLayout.tsx` 637/639, `dropTargets.ts` 347/388, and `GroupView`, `TabMenu`, `Splitter`, `useGroups` 658/658. VERIFIED [03]. Frames V10 and V11 added to Kerk's wireframe file (`55f3387`). The proposal (7 of its 13 commits) and the owner's choices 1 to 26, written in Bao's commits with Vietnamese quotes. VERIFIED [03]; that this owner is Bao is an INFERENCE (Q3). Claude Fable 5.1 trailers on `72450e1` and `a876206` (re-checked). |
| Kerk's part | Drop-band tuning: 41 lines of `dropTargets.ts`, from choices 27 and 33 (owner: QUESTION). The move into `src/shared` in `0394b64` (a pure move), so one copy now serves the three visualizers. He merged PR #17. VERIFIED [01], [03] |
| Inherited | Region maths from V7's `docksModel.ts` (DOCUMENTED, a code comment [03]). No upstream repository has tab groups. VERIFIED [06] |
| Status now | Integrated: the only layout since 2026-10-18, imported by all three visualizers. VERIFIED [06] |
| Strongest evidence | `groupsModel.test.ts` (62 cases) and `dropTargets.test.ts` (15) passed on 2026-11-01 [03], within the full vitest run of 2,619/2,619 [07]. Records DD-50 to DD-56, TP-21 to TP-27, SP-12 to SP-18 [04]. The browser case `e2e/graph.spec.ts:299` (tab strip, DD-54) [07]. **Gap:** drag, split and splitter scenarios have no browser test; they stay manual by the owner's choice of 2026-10-28 (DOCUMENTED, PR #36), and 74 shell spec files went on 2026-10-18 [07]. |
| Verdict | The strongest single contribution: Bao's design, model, code and tests, used by all three visualizers, with dated records. |

### C7. Graph algorithms beyond upstream

| Field | Content |
|---|---|
| Period | 2026-09-29 (recursive DFS) to 2026-10-22 (Cut Vertex & Bridge) |
| Where | PR #6 (pushed to `main`): `4ab075c`, `6fc6150`, `0919126`, `aef5d0b` to `e6ce1ac` (Bellman-Ford), `4bd0879` to `6b1791a` (Prim); PRs #8 and #9 (End node, `9e6e7bd`); PR #28 (`b88952d`, `84c5917`, `0fc105c`) [08] |
| Problem | Upstream had five graph algorithms; visualgo.net's Graph Traversal, SSSP and MST pages list more. There are now 11 ids: recursive DFS, Bellman-Ford with signed weights and a negative-cycle witness, lazy Prim, Topological Sort (DFS or Kahn), Bipartite Check (DFS or BFS) and Cut Vertex & Bridge; plus a Method control in the run form and an End node that only the last frame reads. VERIFIED [06], [08] |
| Bao's part | Every first-add commit is by the BJoozz gmail identity. VERIFIED [06], [08] (re-checked for `b88952d`, `84c5917`, `0fc105c`). Topological Sort, Bipartite Check and Cut Vertex & Bridge follow the owner's choices of 2026-10-21 (Vietnamese quotes, DD-60); Codex's research note was "input only". DOCUMENTED [04], PR #28 |
| Codex | DD-38 and DD-39 say the owner "had Codex plan and build" Bellman-Ford and Prim and has not reviewed those designs, apart from dated choices (re-checked: `DESIGN_DECISIONS.md` lines 601-602, 665). Their 8 stage commits carry no trailer. VERIFIED [03], [07]. Bao's own part in them: QUESTION (Q4) |
| Kerk's part | None in these engines. VERIFIED [08] |
| Inherited | BFS, stack DFS, Dijkstra, Edmonds-Karp and Kruskal from v2, changed here by 5 to 28 lines each. VERIFIED [08] |
| Status now | Integrated. Not built: SCC and 2-SAT (a later round), Ford-Fulkerson, Dinic. VERIFIED [08] |
| Strongest evidence | Seeded property tests `topologicalSortProperty`, `bipartiteCheckProperty` and `cutVertexBridgeProperty` (re-checked: a seeded generator, 400 random multigraphs in one case), and oracle tests for Bellman-Ford (all pairs) and Prim (exhaustive search). VERIFIED [07]. The graph suite passed 654/654. VERIFIED [07], [08]. The `graph-traversal` (10 cases), `bellman-ford` (2) and `prim` (5) browser specs passed. VERIFIED [07]. A deliberate correctness point: Cut Vertex & Bridge skips the parent edge by edge id, so a doubled edge is not a bridge, where visualgo.net skips by vertex. DOCUMENTED (PR #28) |
| Verdict | High: algorithm work checked against independent oracles. Lead with PR #28 and the End node; use Bellman-Ford and Prim only after Q4 is answered. |

### C8. Tree operations beyond upstream

| Field | Content |
|---|---|
| Period | 2026-10-07 to 2026-10-21 |
| Where | PR #6 (`00ed4c2`, `303e50b`: extra panel, ancestor strip); pushed to `main` with no PR: `fc4172d`, `a521c13` (lazy segment tree) and `c364204`, `a6c9965`, `c56eb7b`, `e7f2fec`, `9a2f04b` (BST/AVL); PRs #22 to #27 (`499cb42`, `e55de1c`, `60ccc44`, `7d39c38`, `0a86739`, `1804565`, `3409565`, `3fec43c`, `ea37326`) [08] |
| Problem | Upstream offered five BST/AVL operations, min-heap Insert and Extract, and an eager sum segment tree. Added: Find Min/Max, Predecessor/Successor, Lower Bound, Select, three traversals and AVL Delete; a lazy segment tree with exact decimals; a Binary Heap with a Min/Max switch, 1-based indices and visualgo.net's operations (Create in O(N log N) and in O(N), Update key, Delete, Extract K times, Heap sort); LCA as two runs, with hover ancestors; edges from centre to centre. VERIFIED [08] |
| Bao's part | All first-add commits by BJoozz; the owner's requests are quoted in Vietnamese in TP-13, TP-15 and TP-30 to TP-33. VERIFIED [08], DOCUMENTED [04] |
| Kerk's part | None in these operations. TP-28 and TP-29 (Select preset, the editor look) come from his commits (owner: QUESTION). VERIFIED [04] |
| Inherited | The six workspaces and their engines, from tree-visualizer. VERIFIED [08] |
| Status now | Integrated. Not built: Range Min and Range Max; batch insert and remove (kept for later). VERIFIED [08], DOCUMENTED [04] |
| Strongest evidence | 1,881 tree vitest cases and 62 `tree.spec.ts` browser cases passed; seeded random heaps (200 lists per order). VERIFIED [07]. PR #27's value rule fixes an `Infinity` popup that a Codex review reported (reproduced before the fix). DOCUMENTED. Weak point: the BST/AVL and lazy-tree commits reached `main` with no PR. VERIFIED [01] |
| Verdict | Medium-high: broad and tested. In the report pick one deep case (the Binary Heap round, PR #25, or the lazy tree) rather than a list. |

### C9. Sorting in the shell: Study, Compare and exact seeking

| Field | Content |
|---|---|
| Period | 2026-09-23 to 2026-09-27 (PR #3); the groups version 2026-10-17; the restart rule 2026-10-30 |
| Where | PR #3 (`ee4bb72`, `42d1597`, `5ccef45`, `fed2420`, `3e62f2c`, `eeba29d`, `0a915b6`, `3c61e81`); `0e3857f` (PR #15); `9baa117` (PR #37); `design/proposals/sorting-v2-v7` [08] |
| Problem | Fit a multi-pane comparator into the shared page: Study (one pane, with Pseudocode and e-Lecture) and Compare (2 or 4 panes, Status only); a scrubber that seeks exactly by replaying the kept history; eager production capped at 60,000 operations across panes (round robin), with lazy continuation beyond it; a restart remounts the run frame. VERIFIED [06], [08] |
| Bao's part | Built here by BJoozz; SP-01 to SP-18 first written in his commits; the proposal's decisions U1 to U12 (U7 and U9 "decided by the user on 2026-09-27"). VERIFIED [04], [08]; DOCUMENTED [03] |
| Kerk's part | SP-19 and SP-20 (choices 28, 32, 34, 35 and 40; owner: QUESTION). VERIFIED [04] |
| Inherited | The eight generators, the operation model, the comparison controller and buffer, and the Canvas renderers; `engine/useSortPlayer.ts` is now unused. VERIFIED [06] |
| Status now | Integrated. Sorting has no paused motion and no step notes; four of its chrome files have drifted from the graph's (backlog item 1). VERIFIED [08]; DOCUMENTED [04] |
| Strongest evidence | `seekComparison.test.ts` ("seeking equals repeated stepping") and `eagerPriming.test.ts` passed [06]; 571 sorting cases and the 11 cases of `sorting.spec.ts` (including the SP-01 restart) passed [07]. Sorting never ran in CI before 2026-10-18. VERIFIED [03] |
| Verdict | Medium: a clean engineering example (exact seeking, a bounded eager gate), but the core is inherited; claim only the integration layer. |

### C10. Step notes and other on-canvas explanations

| Field | Content |
|---|---|
| Period | 2026-10-13 (value popups, end badges) to 2026-10-26 (legend trim) |
| Where | `ff77eca`, `28e08f8` (pushed to `main`); PR #29 (`d82aa18`), PRs #30 and #31 (`7180d81`, `277405c`, `94ec5db`), PR #32 (`08590ef`, `157d9a9`, `6b1a4fc`, `8d73c04`), PR #33 (`19aaef3`) [08] |
| Problem | Steps that change nothing on the drawing left their verdict only in the Status panel. A step note writes a short verdict over the node (green to accept, red to reject, ink when it only tells), fades within 1.6s, keeps clear of badges, and lives outside the pan and zoom transform. One layer in `src/shared` serves the tree and the graph. DOCUMENTED (TP-34, TP-36, DD-61, PR #29); the files VERIFIED [06] |
| Bao's part | All commits by BJoozz with Claude trailers (Opus 5.5 on `ff77eca`; Fable 5.1 on `d82aa18` and `08590ef`). VERIFIED [06]. The owner's requests of 2026-10-23 and 2026-10-25 quoted in Vietnamese; Codex's plan was "input only" (re-checked, DD-61, lines 2614-2617). DOCUMENTED [04] |
| Kerk's part | None found. |
| Inherited | The tree's NOW, MISS, INSERTED and DONE badges. VERIFIED [08] |
| Status now | Integrated, with partial coverage: LCA, BST, AVL, Binary Heap and Dijkstra only; none for the segment trees, Trie, sorting or the other graph algorithms. VERIFIED [08] |
| Strongest evidence | The shared tests `stepNotes`, `stepNotePlacement`, `StepNoteLayer`, `FloatingText` and `floatingTextTiming` (re-checked) passed in the full run, and so did `dijkstra.spec.ts` (8 cases) and the tree note cases. VERIFIED [07]. "20,000-scenario fuzz, 0 mismatches". DOCUMENTED (PR #32) |
| Verdict | High as a design-and-implementation case study (placement against obstacles; one layer for two visualizers). Describe the mechanism, not a learning effect. |

### C11. Motion and playback semantics

| Field | Content |
|---|---|
| Period | 2026-10-02 (edge waves) to 2026-10-30 (the shared countdown) |
| Where | `bcbed32`, `c4e597d` (PR #6); `7e92baf`, `a8c191c`, `74a4958`, `0d1f6de`, `f935bc6`, `4a54f7f`, `117975a` (pushed to `main`); PRs #10, #11 and #12 (`be570eb`); Kerk's `a074f50` and `01a1a4a`; PR #37 (`9baa117`) [08] |
| Problem | Make each step's change visible and the transport consistent: a wave shows which way an examined edge is crossed (DD-37); a paused step keeps its focus moving (DD-42, TP-17), behind a Settings switch that follows the system's reduced motion; the finished last frame keeps moving (DD-47); a step that only completes the one before is merged into it (DD-44, TP-18, SP-11); a Speed change keeps the time already spent (a shared countdown); the footer is the only transport (DD-24). DOCUMENTED [04]; the files VERIFIED [06] |
| Bao's part | The records above were first written in BJoozz commits, with dated owner choices. VERIFIED [04], [08] |
| Kerk's part | `a074f50` (Autoplay beside Stop; Next with no run starts a paused run) and `01a1a4a` (coloured chips), pushed straight to `main`. DD-24 and SP-01 call `a074f50` "the owner's commit". VERIFIED [04]; the owner: QUESTION (Q3) |
| Inherited | Typed semantic pacing (upstream DD-17) and final recap waves for BFS, Dijkstra and Max Flow. VERIFIED [08] |
| Status now | Integrated; sorting has no paused motion. VERIFIED [08] |
| Strongest evidence | `playbackCountdown.test.ts`, `e2e/graph.spec.ts:113` (DD-17), `e2e/sorting.spec.ts:107` (SP-01) and `paused-motion.spec.ts` (4 cases) passed. VERIFIED [07] |
| Verdict | Medium: good design-rationale material, but too many small items for a headline. |

### C12. Content from visualgo.net: samples, e-Lectures and the catalogue

| Field | Content |
|---|---|
| Period | 2026-09-28 (catalogue) to 2026-10-22 (traversal decks) |
| Where | PR #13 (`bc46260`, `174b417`, `32de95c`: `visualgoExamples.ts`, `positionedLayout.ts`, `layoutBoard.ts`); decks in `0073875`, `7b16bf3`, `3a429ad`, `5e9f0ef`, `88e8396`, `b88952d`; `src/site/modules.ts` [08] |
| Problem | Use the material Prof Halim teaches with: 37 of visualgo.net's example graphs with the same vertices, edges, weights and positions; e-Lecture decks written after visualgo.net's lectures; homepage cards in visualgo.net's order. DOCUMENTED [08] (PR #13, TP-14) |
| Bao's part | BJoozz commits; the owner's choices of 2026-10-16 (DD-48). VERIFIED [08], DOCUMENTED [04] |
| Kerk's part | The design system's `data.js`, the source of the card table. DOCUMENTED [08] |
| Inherited | Content copied from visualgo.net's source, held in the private repository `BJoozz/visualgo`. DOCUMENTED [08]; permission: QUESTION (Q7) |
| Status now | Integrated. Graph: 11 decks, 40 slides ("short" by choice). Tree: 7 decks, 111 slides. Sorting: 1 deck, 9 slides. Slides that drive the visualization, and quizzes, are not built. VERIFIED (counts), DOCUMENTED (the rest) [08] |
| Strongest evidence | PR #13 says every example was re-checked against the source after two extraction errors were found and fixed. DOCUMENTED |
| Verdict | Medium-low as engineering; important for credit and permission. |

### C13. Process and verification evidence

| Field | Content |
|---|---|
| Period | 2026-09-20 (the first prototype CI) to 2026-10-30 (review session 3) |
| Where | `prototypes/docs/{graph,tree,sorting}/DESIGN_DECISIONS.md` (DD-23 to DD-61, TP-01 to TP-36, SP-01 to SP-20: 95 local records), the `AGENTS.md` rules, three backlogs (24, 20 and 13 items), two acceptance records, PRs #34 to #37, the test suites and CI [04], [07] |
| Problem | Keep a fast-changing, AI-assisted codebase coherent: each decision recorded with whose choice it is (the owner, the implementer or Codex); departures from upstream listed; tests with each change; review findings reproduced before a fix. DOCUMENTED [04], [07] |
| Bao's part | 88 of the 95 local records were first written in BJoozz commits; by blame the test code is almost all his (the 14 browser specs: 4,887 of 4,952 lines); 159 of his commits touch tests (148 with a Claude trailer); the rule "upstream is a reference only" (`38c726f`). VERIFIED [04], [07] |
| Kerk's part | Seven records (DD-57, DD-58, DD-59, TP-28, TP-29, SP-19, SP-20; owner: QUESTION); `app.yml`; 62 of the 70 lines of `prototypes/AGENTS.md`, including "one fix, one place". VERIFIED [03], [04] |
| Inherited | v2's DD-01 to DD-22 and its rule "update the owning document in the same change". VERIFIED [04] |
| Status now | In use. Some docs are stale: TP-08's editor toggle, "split rails first" in the guides, the ARCHITECTURE theme and hosting sentences, "Node 20.19" in the graph guide. VERIFIED [04], [06], [07] |
| Strongest evidence | The run of 2026-11-01: typecheck clean, lint 0 errors (2 warnings), 654 + 2,619 unit cases, the build, 151/151 browser cases [07]. CI: 266 runs from 2026-09-04 to 10-30, 8 failed, each fixed by a later commit; the runs for today's `main` are green [07]. **Gaps:** no review or comment on any PR and 90 commits straight to `main` [01]; manual checklists never recorded as run; no coverage tool; Chromium only; no automated accessibility audit [07]. |
| Verdict | High as the evidence base of the evaluation chapter. It is a method, not a feature, and must be presented together with the AI-assistance facts. |

### C14. One app, CI and deployment (mostly Kerk's)

| Field | Content |
|---|---|
| Period | 2026-09-03 (Kerk's CI and Pages) to 2026-10-30 |
| Where | `.github/workflows/ci.yml`, `pages.yml`, `app.yml`; `0394b64` (PR #20), `c39b3cf` (PR #18), `c59c155` and `5235fcf` (PR #21). Bao: `37075b1` (`prototypes.yml`), PR #4 (static hosting), PR #34 (tooling), `c9e4598` and PR #5 (Vercel, closed) [01], [03], [07] |
| Problem | One app in `prototypes/`, run from the repository root (npm workspaces, port 5186); one CI job set; Pages serving the app at `/` and the engine demo at `/engine/`; no duplicated copies. DOCUMENTED (PR #20) |
| Bao's part | `prototypes.yml` (2026-09-20 to 10-17; graph and tree only); `VA_BASE`, `404.html` and `_redirects` (PR #4); the review-session tooling (Inter font guard, Node 22.12 floor, flag forwarding, CI traces; PR #34). VERIFIED [03], [07]. No Vercel deployment was found. VERIFIED [03] |
| Kerk's part | `pages.yml` (all 65 lines), `app.yml` (94/94) and `ci.yml`; `0394b64`: 3,510 files changed, the V2/V7 copies, two sites and the submodules deleted, the 40 shared files kept once in `src/shared`, the root workspace, browser specs cut from 208 files to 12; `prototypes/AGENTS.md` and the root `README.md`. VERIFIED [01], [03], [07]. "The owner's decision of 2026-10-18: V10 wins": QUESTION (Q3) |
| Inherited | None. |
| Status now | Integrated and deployed. VERIFIED [03], [07] |
| Strongest evidence | 48 Pages runs, 43 successful; the app run on `662e7b3` green with 654 + 2,619 unit and 151 browser cases. VERIFIED [03], [07] |
| Verdict | Context only: credit Kerk; give Bao's static-hosting and tooling fixes one line. |

## 3. Ranked shortlist for the interim engineering report

The ranking (INFERENCE, mine) weighs four things: clear evidence that the work is Bao's (diffs and blame, not counts); its status in today's app; engineering depth; and tests that ran green on 2026-11-01.

| Rank | Contribution | Why it ranks here | What must be said with it |
|---|---|---|---|
| 1 | **C6 V10 "Panel groups" shell** | The clearest authorship in today's app (model 1,441/1,441 lines and its tests 1,355/1,355 by blame). A real design problem (two built layouts compared, then merged into one) solved with a pure model that keeps its invariants and one resolver for every minimum. Dated records (DD-50 to DD-56 and the tree and sorting twins). Used by all three visualizers; 77 shell unit tests passed. | Claude Fable 5.1 co-author trailers. Kerk's drop-band tuning (choices 27 and 33, owner unknown) and his move into `src/shared`. Drag and split behaviour is checked by hand only. Draw no conclusion from the commit dates against the proposal's estimate. |
| 2 | **C7 Graph algorithms, led by PR #28 and the End node** | Algorithm work checked against independent oracles: seeded property tests against brute force and an independent 2-colouring; a deliberate correctness point (the parent edge is skipped by id); a Method control in the run form; 654/654 graph tests passed. | Bellman-Ford and Prim are recorded as planned and built by Codex and not reviewed (DD-38, DD-39). Keep them out of the headline until Q4 is answered. |
| 3 | **C1 with C2: the architecture of the standalone visualizers** | Explains why the app is built as it is: separate state owners, one persistent canvas, typed sequences made at run time. The session reducers are still byte-identical in the app. The standalone tests passed (276/276 and 664/664). | Present it as earlier work in Bao's own repositories; whether it is FYP work depends on Q1. v2 and tree carry Claude trailers from 09-07 and 09-12. V1 and sorting history caveats (Q10). |
| 4 | **C10 Step notes and the shared canvas layer** | The commits listed under C10 are all Bao's; one layer is shared by two visualizers (`08590ef`); records (TP-34, TP-36, DD-61) quote the dated requests; browser tests cover it. | Partial coverage; Claude trailers; no evidence of any learning benefit: describe the mechanism and its tests only. |
| 5 | **C13 Verification and process evidence** | The full green run of 2026-11-01 and the CI history are what let the report state the other claims safely; the 95 local records give the design rationale. | No PR review exists; 90 commits went straight to `main`; there is no user evaluation, coverage figure, cross-browser run or accessibility audit; the AI-assisted way of working must be stated. |

**Close runners-up.** C5, the site: strong code evidence, but the credit is shared with Kerk's design system, his UI kit and his single-theme-writer change. C8, through the Binary Heap round (PR #25). C9, through exact seeking in sorting.

**A possible report shape** (INFERENCE): the problem and the inherited base (C1, C2); the integration design (C6, with C4 as the exploration before it and C5 as the host); the algorithms (C7, with one case from C8); explanation on the canvas (C10); verification (C13); limits and next steps (the gaps in sections 2 and 5).

## 4. Uncertainties and questions for Bao

Merged from the questions in notes 01 to 08 and deduplicated. The notes that raised each one are in brackets. **P1** blocks any contribution claim; **P2** affects one section; **P3** is housekeeping.

### P1: answer before writing any contribution claim

1. **Q1 The FYP's period and scope.** When did the FYP officially start (NUS AY2026/27 Semester 1 began around 2026-08-10?), and what period does the interim report cover? Do the four standalone repositories count as FYP work, preparatory work or prior work? V1 began on 2026-07-28 under the package name `js-ts-learning`. [01, 02, brief] This decides whether C1 and C2 can be claimed.
2. **Q2 Identities.** Are `BJoozz <123baoek31@gmail.com>` and `BJoozz <83776047+BJoozz@users.noreply.github.com>` both yours? The noreply one appears only on 30 GitHub merge commits. [all notes]
3. **Q3 Kerk's role, and "the owner" in Kerk's commits.** What is Kerk's role in your FYP (fellow student, supervisor's staff, client)? Who is "the owner" in Kerk's work of 2026-10-18 to 2026-10-22: the V10 proposal's choices 27 to 48 (quoted in English), `0394b64` ("The owner's decision of 2026-10-18: V10 wins"), `40a63bd` ("The owner's request"), the PR #19 and #21 bodies, and `a074f50`, which your PR #37, DD-24 and SP-01 call "the owner's commit"? Did you agree to deleting V2/V7, two sites, the submodules and the module browser suites (208 spec files down to 12)? Who set "one fix, one place"? [01, 03, 04, 06, 07, 08] This affects C5, C6, C8, C9, C11, C13 and C14, and the records DD-52, DD-57 to DD-59, TP-23, TP-28, TP-29, SP-14, SP-19 and SP-20.
4. **Q4 AI assistance and your own role.** How should the report describe Claude Code (trailers on 199 of your 213 own commits on `main`, on 20 of 38 in v2 and 34 of 41 in tree) and Codex (DD-38 and DD-39: it planned and built Bellman-Ford and Prim, not reviewed; reviews and research notes elsewhere)? What did you do yourself in each change: direction, choices, review, acceptance? Which tools helped on the commits with no trailer (V1, sorting, `986deba`, `c458755`, `75d9760`, the 8 Bellman-Ford and Prim commits, `478174f`, `53d2ef4`, `3a6443b`)? Who wrote the `AGENTS.md` files? [01, 02, 03, 04, 05, 07, 08]
5. **Q5 Decisions that name no person, and unwritten rules.** Records marked as the implementer's (DD-23, DD-28, DD-30 to DD-33, TP-01, TP-07 to TP-09, SP-02 to SP-06, SP-08, SP-09, and DD-27's first form): your decisions, agent choices you accepted, or both? Are "docs describe the current state", "the owner decides rules" and "proportionate tests" your rules (none is written in the repository), and may the report cite them? Do the "Historical" `docs/*/AGENTS.md` rules still bind the one app? [04]

### P2: answer before writing the section concerned

6. **Q6 Review evidence.** 90 of your commits reached `main` with no merge commit (2026-09-29 to 10-15; PR #6 has an empty body), and no PR has a review or a comment. Was the work reviewed some other way (meetings, chat, Kerk, the supervisor)? Who produced the findings of the review sessions of 2026-10-26, 10-27 and 10-29, the "external review" in PR #13, and the Codex review in PR #27? [01, 07, 08]
7. **Q7 visualgo.net material and branding.** What permission covers copying 37 example graphs from visualgo.net's source (the private repository `BJoozz/visualgo`), its lecture text and its card table, and using the VisuAlgo name, the NUS Computing and Optiver logos and "adapted from Prof Halim's visualgo.net" on the public Pages site? Is Prof Halim your supervisor, and has he agreed? [03, 08]
8. **Q8 Design credit.** Did Kerk mean his wireframe (nine layouts that already name e-Lecture, Pseudocode, a legend, Save image and settings), his design system and his UI kit as the specification, or as reference? Who chose V2 and V7 from the nine, and when? Which page features are your design, and which are your build of Kerk's design? How was the design system made (its `SKILL.md`, `*.prompt.md` and `_ds_bundle.js` files look like an AI design tool's export)? [01, 03, 08]
9. **Q9 The engine study.** Was the 2026-09-17 experiment your idea, or agreed with Kerk or the supervisor? Did Kerk review it? Why the name "Kerk BFS runtime"? Why did it stop, and who decided on 2026-09-20 that "the engine integration" is outside the prototype? Is the M0 to M4 plan written anywhere? Should the report include it, and how? [01, 05]
10. **Q10 Standalone history.** Is there V1 history before 2026-07-28 (its first commit already holds about 3,000 lines)? When did the sorting work start, and does its history before the 2026-08-19 squash exist (its doc is dated 08-13)? Did tree-visualizer start from v2's code? Why was the tree submodule pinned at `1477cda` when `46ce0a7` was copied? [02]
11. **Q11 Evaluation outside the repository.** Were the manual checklists (graph 20, sorting 10 and tree 26 items, all unticked) ever run, with notes or screenshots? Is there any feedback from users, Kerk or the supervisor? Should the dated micro-profiles (sorting 2026-08-13, Bellman-Ford 10-03, Prim 10-05; their scripts are gone) be cited? Should the `wasm-arch` engine suite and the spike's 92 cases be run for the report? [05, 07]

### P3: housekeeping

12. **Q12 Local-only work at risk.** `053064f` and `53d2ef4` exist only in this local clone, and both worktree folders are empty on disk. Keep, push or archive them? Was any uncommitted work in those worktrees? [01, 05, 08]
13. **Q13 Stale docs and known debt.** Fix these before quoting them, or quote them as they stand: TP-08's editor toggle, "split rails first" in the guides, the ARCHITECTURE theme and hosting sentences, "Node 20.19" in the graph guide, the status lines of two proposals, tree backlog item 1, sorting backlog item 13? Report as debt: six sets of byte-identical files outside `src/shared`, the unused `sorting/engine/useSortPlayer.ts`, and four drifted sorting chrome files? [04, 06, 07]
14. **Q14 How to state coverage.** A card's "full" counts visualgo.net's algorithm names, not operations (BST was "full" on 09-28 with three operations), and the SSSP card does not count BFS although BFS takes the End node. [08]
15. **Q15 Vercel and the fork.** Was the fork ever deployed on Vercel (`c9e4598`, `03bfaa3`)? Why was PR #5 closed? What was the 2026-11-01 push to the fork? [01, 03]
16. **Q16 Unrelated files.** Leave out the "CDC Companion" wireframes and the "Sculpin" upload, which are not about VisuAlgo? [03]
17. **Q17 Small facts.** Choice 44's date (2026-10-18 in `HostedModule.tsx:84`, 2026-10-19 in the proposal); who answered the sorting questions U5, U7, U8 and U9; whether the vi-VN locale failure in the standalone sorting test is known; whether the other local branches (`backup/before-reword-044908`, `bj/viz-shell-v10-stage0`, `live_prototype`, `bj/vercel-spa-routing`) can be ignored. [01, 02, 03, 04]

## 5. Claims that would be unsafe to make

| # | Unsafe claim | Why it is unsafe | What can be said instead |
|---|---|---|---|
| 1 | VisuAlgo+ helps students learn, is easier to use, or is preferred to visualgo.net | No user study, participants, survey, interviews or feedback exist in the repository; there is no measure of learning. VERIFIED [07] | "It has not yet been evaluated with users." |
| 2 | It is fast, scales to large inputs, or uses little memory | No benchmark exists and none runs in CI. The only timings are dated observations of earlier builds (sorting 2026-08-13, Bellman-Ford 10-03, Prim 10-05) whose scripts are gone; Kerk's journal-versus-snapshot memory table is an estimate. VERIFIED [05], [07] | Quote a dated observation as such, with its date, build and caveat. |
| 3 | A feature is novel, the first of its kind, or unique | The evidence holds no comparison with other tools or literature; V10's drag feedback follows VS Code (PR #15); the content follows visualgo.net. | Describe the design and the reasons the records give. |
| 4 | Bao wrote N lines or N% of the code, as a measure of effort or ownership | Line counts are inflated by two or three copies of each app until 2026-10-18, by folder copies and moves, and by code brought from his own repositories; blame shows who last changed a line; most commits are AI co-authored. [01] | Name the commits and files whose diffs show the work (sections 2 and 3). |
| 5 | Bao designed and implemented Bellman-Ford and Prim | DD-38 and DD-39 say Codex planned and built them and the designs were not reviewed; their 8 stage commits carry no trailer. VERIFIED [04] (re-checked) | Wait for Q4; until then, "added to the graph module (records: planned and built with Codex)". |
| 6 | The app runs on Kerk's WebAssembly engine, or the engine integration was done | Nothing in `prototypes/src` uses the engine; the experiment was never merged. VERIFIED [05] | "An unmerged integration study (2026-09-17)." |
| 7 | The engine study's 125 or 130 tests pass, or Bao co-built Kerk's engine | The pass results are only in commit messages, with no CI run and no re-run; no commit of Bao's touches `wasm-arch/` on `main`. VERIFIED [05] | "The branch defines 125 Node tests; their results were not independently verified." |
| 8 | The work was code-reviewed, or peer-reviewed by Kerk | No PR has a review or a comment; 90 commits went straight to `main`. VERIFIED [01] | Describe the review sessions as findings reproduced and fixed (PRs #34 to #37), and say who reviewed once Q6 is answered. |
| 9 | The app is accessible or WCAG compliant | Contrast is checked only for samples (one browser spec, three unit tests); no automated audit exists; the Prim record says its sweep "is not a full accessibility certification"; graph backlog item 14 lists colours below the minimums in some themes. VERIFIED [04], [07] | "Text contrast is tested at 4.5:1 for a sample of chrome text in all nine themes." |
| 10 | It works in every browser and on phones | The browser suite runs Chromium only, at desktop viewports; the mobile design is "held pending". VERIFIED [07] | "Tested in Chromium on desktop window sizes." |
| 11 | The tests have high coverage, or any coverage percentage | No coverage tool is installed. VERIFIED [07] | "3,273 unit cases and 151 browser cases passed on 2026-11-01." |
| 12 | VisuAlgo+ covers visualgo.net, or replaces it | 12 of the 30 cards open (8 full, 4 partial; "full" counts algorithm names); 18 are "soon"; Training and quizzes are not built; PR #4 itself says "not a replacement deployment of visualgo.net". VERIFIED [08] | State the counts with the definition of "full" (Q14). |
| 13 | visualgo.net's material is used with permission | Permission is not recorded anywhere seen. [08] | Wait for Q7. |
| 14 | Choices 27 to 48, or "V10 wins", were Bao's (or were Kerk's) | Unresolved; the words sit in Kerk's commits. [01], [03], [04] | Wait for Q3; meanwhile "a choice recorded in Kerk's commit of <date>". |
| 15 | Bao made the design system, the wireframes or the homepage design | Kerk's commits added them; the site proposal calls them Kerk's. VERIFIED [03] | "Built on Kerk's design system, wireframe and UI kit." |
| 16 | The site is deployed on Vercel, or CI was always green | No Vercel deployment was found and PR #5 was closed; CI had 8 failed runs, with `main` red from 10-10 to 10-14 in the old workflow. VERIFIED [03], [07] | "Deployed by GitHub Pages; every CI failure was fixed by a later commit." |
| 17 | The browser suite tests the panel drag and split, or always covered the modules | The shell's drag, split and splitter scenarios are manual only; 208 spec files became 12 on 2026-10-18. VERIFIED [07] | Say which scenarios are automated and which are manual. |
| 18 | The test counts in the PR bodies are verified results | They are the implementer's own reports; PRs #2 to #4 say the full suites were not all re-run. DOCUMENTED [03] | Cite the 2026-11-01 run and the CI logs. |
| 19 | The V2 and V7 layouts are part of the product | They were deleted on 2026-10-18. VERIFIED [03] | "Two earlier layouts, compared and then merged into V10." |
| 20 | The sorting performance figures describe VisuAlgo+ | They were captured on 2026-08-13, on the standalone engine. VERIFIED [07] | Leave them out, or date them. |
| 21 | V10 was built in one day, against an estimate of 24 to 36 days | The commits were made in agent-run stages; dates are no basis for a productivity claim. [03] | Give the dates without a conclusion. |
| 22 | tree-visualizer was built from v2's code | This is an INFERENCE from shared lines only. [02] | Wait for Q10. |
| 23 | Kerk only set up deployment | Kerk's `0394b64`, `c59c155`, `a074f50` and `01a1a4a`, seven records and choices 27 to 48 changed the app. VERIFIED [01], [04], [06] | Credit Kerk's consolidation, chrome and footer changes. |
| 24 | "The owner decided ..." with no name | The word means Bao in his branches and an unknown person in Kerk's commits. [04] | Name the person once Q3 is answered. |

## Sources

Notes `01-inventory-timeline.md` to `08-feature-coverage.md` in this folder and `../in/prs.txt`; their evidence files are listed in each note. My re-checks are listed under "How this note was made".

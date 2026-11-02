# 04 - Decision records and working rules (evidence audit)

Audit date: 2026-11-01. Repository: `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3` (2026-10-31), working tree clean and left clean. Everything below was read with `grep -n`, `sed -n` on line ranges, `git log`, `git show`, `git blame` and `git ls-files`. No file inside the repository, the clones or the worktrees was written.

**Tests:** I ran no tests for this note. A test file named below proves only that the test exists. (INFERENCE: running vitest or Playwright would write caches and reports inside the working tree, which the brief forbids.)

## 1. How to read this note

| Label | Meaning here |
| --- | --- |
| VERIFIED | I saw it in the docs text, a commit, `git blame`, or `git ls-files` |
| DOCUMENTED | A doc or commit message says it; I did not check it against the code |
| INFERENCE | My reading |
| QUESTION | Needs Bao |

Columns in the catalogue tables:

- **ID, title, dates named, files named, line range, first commit**: VERIFIED. Titles come from the `## ` headings. "Dates named" lists every `2026-MM-DD` inside the record (shown as MM-DD). "Files named" counts back-ticked names with a file extension inside the record and shows a few.
- **Decision (one line)**: DOCUMENTED (my one-line summary of the record's own **Decision:** paragraph).
- **Status**: DOCUMENTED, taken from the record and from the "Status of the inherited/shell decisions" tables at the top of each file, unless marked otherwise.
- **Whose choice** uses these tags:
  - `Owner-B` - the record says "the owner's decision / choice / request" and the record was first written by a BJoozz commit (Bao's branch). By the brief's rule the owner there is Bao (to be confirmed by him).
  - `Owner-K?` - the owner's choice was recorded by a **Kerk Tai Heng** commit of 2026-10-18 to 2026-10-22. Whose words these are is a **QUESTION**.
  - `Impl` - the record names no person. INFERENCE: the implementer's choice (the coding agent working for the owner).
  - `Codex` - the record itself says Codex planned and built it and the owner has not reviewed the design.
  - `Upstream` - inherited from graph-visualizer-v2's DD-01 to DD-22.
  - "Details implementer's" means the record says the details were "set here within" the owner's decision.

## 2. Key findings

1. **Counts (VERIFIED).** `prototypes/docs/graph/DESIGN_DECISIONS.md` (2,886 lines) holds a status table for the inherited DD-01 to DD-22 and the records DD-23 to DD-61 (39). `prototypes/docs/tree/DESIGN_DECISIONS.md` (3,677 lines) holds TP-01 to TP-36 (36). `prototypes/docs/sorting/DESIGN_DECISIONS.md` (675 lines) holds SP-01 to SP-20 (20). Each file opens with a status table for the graph decisions it reuses.
2. **Who first wrote each record (VERIFIED,** from `git log --reverse -p -- '*DESIGN_DECISIONS.md'`, first added `## ID:` line, in the current file or an earlier copy). Every record was first written by a BJoozz commit **except seven**, all by Kerk Tai Heng on 2026-10-18: DD-57, DD-58, TP-28, SP-19 in `ae63a62`, and DD-59, TP-29, SP-20 in `c59c155`.
3. **The owner's V10 choices (VERIFIED, `git blame design/proposals/viz-shell-v10/README.md` lines 45-90).** Rows for choices 1-26 were added by BJoozz commits (2026-10-16 to 2026-10-18) and quote the owner in Vietnamese. Rows for choices 27-41 were added by Kerk's `ae63a62` and `c59c155` (2026-10-18), and 42-45 by Kerk's `3c79d36` (2026-10-19); they quote the owner in English (for example choice 29, "graph selector should say 'select preset' and not graph"). **QUESTION:** whose words are choices 27-45, Bao's or Kerk's? This affects DD-52, DD-57, DD-58, DD-59, TP-23, TP-28, TP-29, SP-14, SP-19 and SP-20.
4. **"The owner's commit of 2026-10-21"** (DD-24, SP-01, and the DD-24 rows of the tree and sorting status tables) is `a074f50` "Stepping leads the footer, Autoplay sits beside Stop", authored by **Kerk Tai Heng** and pushed straight to `main` (it is a first-parent commit; so are `01a1a4a`, `40a63bd` and `3c79d36`). The phrase was written later by Bao's `9baa117` (2026-10-30). VERIFIED. **QUESTION:** does "the owner" here mean Kerk?
5. **"V10 wins and everything else goes"** - "the owner's decision of 2026-10-18" in Kerk's `0394b64` (3,510 files changed, 2,575 deleted). It removed the split-rails and docks copies, their sites and the three upstream submodules. VERIFIED (author, date and file counts; the list of what went is DOCUMENTED in the message). **QUESTION:** whose decision was it?
6. **AI assistance (VERIFIED, trailers).** Of the 131 non-merge commits that touched any `DESIGN_DECISIONS.md` on `main`'s history (the three current files and their earlier split-rails, docks and groups copies under `prototypes/*/docs/`), Kerk's 3 all carry `Co-Authored-By: Claude ...`. Of BJoozz's 128, 118 carry it. The 10 without it are the Bellman-Ford and Prim commits of 2026-10-03 to 2026-10-05 (`aef5d0b`, `0aac567`, `6417767`, `4bd0879`, `5428ed3`, `686c06b`, `65634cf`, `490e1d1`) and `c458755`, `75d9760` (2026-09-21). DD-38 and DD-39 say the owner "had Codex plan and build" Bellman-Ford and Prim and has not reviewed those designs, apart from the choices they date (DOCUMENTED).
7. **Upstream was written by the BJoozz identities (VERIFIED; that they are Bao is to be confirmed).** All commits in the four clones (`graph-visualizer-v2`, `tree-visualizer`, `sorting-algorithm-visualizer`, `graph-algorithm-visualizer`) are by the two BJoozz identities. The graph prototype's copy was taken at `c8b14e6`, which is the clone's HEAD (2026-09-11). Its `docs/DESIGN_DECISIONS.md` (DD-01 to DD-22) has 16 commits, all by `BJoozz <123baoek31@gmail.com>`. The tree upstream has no decision file (only `docs/BACKLOG.md` and `docs/DEVELOPER_GUIDE.md`).
8. **Rules not written in the repository.** "Docs describe the current state", "the owner decides rules" and "proportionate tests" are not stated as rules in any `AGENTS.md`, guide or README (VERIFIED by `git grep`). They show only as practice in records and acceptance notes (section 6). **QUESTION** for Bao.
9. **Stale wording found (INFERENCE, details in section 9).** TP-08 says the editor header toggle still works, but TP-29 and the code (grep, VERIFIED) show the collapsible section is gone. Several guides still say "split rails first" or "mirrored into split rails", but those folders went in `0394b64`.

## 3. Catalogue - graph (`prototypes/docs/graph/DESIGN_DECISIONS.md`)

The file's opening (lines 1-15) says DD-01 to DD-22 are inherited from graph-visualizer-v2 (copy at `c8b14e6`, not copied here), DD-23 to DD-49 come from the docks build (V7), DD-50 to DD-56 are the V10 "Panel groups" shell, DD-57 and DD-58 are "the owner's changes of 2026-10-18 to the deployed build" (choices 28-32), DD-60 is the owner's choices of 2026-10-21 and DD-61 the owner's choices of 2026-10-25 (DOCUMENTED).

### 3.1 Inherited DD-01 to DD-22 (`Upstream`)

Titles are VERIFIED from the clone, `graph-visualizer-v2/docs/DESIGN_DECISIONS.md` lines 7-522. Status is DOCUMENTED, from the status table at lines 17-40.

| ID | Upstream title | Status here |
| --- | --- | --- |
| DD-01 | V1 is reference material, not a codebase to continue | Unchanged; the code it governs is a copy |
| DD-02 | One workspace and one persistent canvas | Unchanged |
| DD-03 | Topology, layout, UI, session, and presentation are separate | Unchanged |
| DD-04 | Exact IDs and canonical order are semantic | Unchanged |
| DD-05 | Topology revision is the graph-semantic invalidation boundary | Unchanged |
| DD-06 | Graph text is live and transactional without Apply | Unchanged; extended by DD-38 (any finite weight, negatives too) |
| DD-07 | Omitted weight is hidden semantic zero | **Superseded by DD-36** (an omitted weight reads as 1) |
| DD-08 | d3-force is a synchronous coordinate calculator | Unchanged as a rule; a drag with Live off moves frame by frame (DD-43); the board grows to hold a drawn sample (DD-48) |
| DD-09 | React Flow is derived renderer state | Unchanged |
| DD-10 | Generic playback, typed algorithm metadata | Unchanged |
| DD-11 | Sequences are lazy, read-only after creation, and layout-free | Unchanged; "generated only when Run is pressed" now reads as when Autoplay or Next starts a run (DD-24) |
| DD-12 | Algorithm effects are presentation overlays | Unchanged |
| DD-13 | Shared CSAcademy-inspired graph language | Unchanged, with seven notes: our Fit view button, no OS colour scheme, a see-through legend (owner, 2026-10-14), the legend shared with the tree since 2026-10-23, and a smaller 12px legend since 2026-10-25 |
| DD-14 | Preserve deliberate algorithm granularity | Extended by DD-37; **overridden by the owner** for BFS, stack DFS and Kruskal (DD-44) |
| DD-15 | Samples are typed presets, not another graph owner | Unchanged as a rule; the catalogue is DD-48's |
| DD-16 | Large graphs use a responsive virtual active board | Unchanged |
| DD-17 | Semantic operation pacing is relative and typed | Unchanged as a rule. A Speed change keeps the step's elapsed time; the tree's countdown is shared, by the owner's answer of 2026-10-29, "Đồng nhất với tree" ("make it the same as the tree") |
| DD-18 | Dijkstra's final tree preserves exact weighted arrivals | Unchanged; extended by DD-37, DD-45 and DD-47 |
| DD-19 | BFS keeps an exact tree and finishes with a level recap | Unchanged; extended by DD-37, DD-45 and DD-47 |
| DD-20 | The editor group is a run-scoped disclosure, not a mode | **Superseded by DD-23** (the editor is the Action panel's Draw graph) |
| DD-21 | A large canvas resize earns one deferred fit | Unchanged; extended by DD-27 |
| DD-22 | The inspector orders content by rate of change; one fact, one place | Unchanged. Pseudocode is its own panel (DD-25); the Dijkstra and Kruskal tables lost their inner scroll; DD-61's canvas notes are hidden from assistive technology, so Status stays the whole account |

The same status table also qualifies seven local records: DD-23 (its layout is now V10's groups), DD-26 (superseded in parts), DD-27 (narrowed by choice 24), DD-33 (DFS only), DD-34 (kept on the groups), DD-41 (button reads Select preset) and DD-46 (drag behaviour is DD-57's). These are folded into 3.2.

### 3.2 DD-23 to DD-61

| ID (lines) | Title | Dates (2026-) | Whose choice | Decision (one line) | Files named | Status | First commit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DD-23 (42-60) | The page is the wireframe; panels are placed, not owned, by the layout | - | `Impl` (follows wireframe 2 of `design/wireframes`) | Four panels, a top bar and a footer; a layout gets `renderPanel(id)` and the canvas and decides only position, visibility and size | 0 | Current as a rule; layout is V10 groups | `0073875` BJoozz 09-20 |
| DD-24 (61-131) | The footer is the only transport and speaks the session's language | 10-10, 10-11, 10-16, 10-21, 10-29 | `Owner-B` (Go folded into Play 10-10; answer 10-29 "Sửa lời theo code hiện tại", "fix the wording to match the code"); "the owner's commit of 2026-10-21" = Kerk's `a074f50`, **QUESTION** | Transport buttons map one-to-one to the session reducer; with no run, Autoplay and Next are the only starts | 0 | Current | `0073875` |
| DD-25 (132-149) | Pseudocode highlights only what the algorithm recorded | 10-13 | `Impl`; `withPrevious` tie is `Owner-B` 10-13 | The panel lights the step's typed `activeCodeLine`; a tied line lights with it | 2: `algorithmPseudocode.test.ts`, `pseudocodeHighlight.ts` | Current | `0073875` |
| DD-26 (150-210) | Docks are a pure model; a drop is the only way a panel moves | 10-15 | `Impl`; drop zones `Owner-B` 10-15 | `docksModel.ts` owned the V7 arrangement; only a release over a drop zone moves a tab | 1: `docksModel.ts` (no longer in the tree) | **Superseded in parts** by DD-51, DD-52, DD-55, DD-56; "a drop is the only pointer move" still in force | `0073875` |
| DD-27 (211-224) | A layout change asks for a fit; it never forces one | - | `Impl`; narrowed by `Owner-B` choice 24 (10-18, "Chỉ khi khung vẽ thực sự đổi kích thước", "only when the drawing really changes size"; Bao's `c0166f2`, `649f42e`) | Fits go through `useLayoutFit` and are dropped during a drag or playback; Fit view and F fit at once | 0 | **Narrowed**: a layout operation asks for a fit only when it changes the drawing's size | `37075b1` 09-20 |
| DD-28 (225-237) | The theme is html[data-theme], never the operating system | 10-18 | `Impl` | Nine themes; no `prefers-color-scheme` in `src/` | 2: `viz-page.css`, `e2e/os-colour-scheme.spec.ts` (gone 10-18) | Current | `37075b1` |
| DD-29 (238-273) | The algorithm is chosen in the top bar; Action holds graph actions and the run form | 10-10, 10-11 | `Impl`; Go removed `Owner-B` 10-10 | Switcher in visualgo.net's form; Action holds Draw graph and the run form, with no start button | 1: `algorithmNav.ts` | Current | `c458755` 09-21 (no AI trailer) |
| DD-30 (274-306) | An algorithm may read the graph its own way; the authored graph never changes | - | `Impl` | `graphInterpretation.ts`: Kruskal, Prim, Bipartite Check and Cut Vertex read it undirected; the Directed setting is kept and locked | 1: `graphInterpretation.ts` | Current (DD-60 added two readers) | `c458755` |
| DD-31 (307-329) | Inspector tables are searched by node names, separated by spaces | - | `Impl` | One search box per edge or node table; rule in `tableSearch.ts` | 1: `tableSearch.ts` | Current | `75d9760` 09-21 (no AI trailer) |
| DD-32 (330-369) | Dijkstra's distances live on the nodes; absence means unreached | 10-25 | `Impl` | Finite distance in the node badge, no infinity sign on the canvas, `old→new` on an improvement | 0 | Current | `6fc6150` 09-29 |
| DD-33 (370-403) | Two depth-first searches, named for what they hold | - | `Impl` | `dfs-recursive` and `dfs-stack` are two algorithms, recursive first | 0 | Current for DFS; other traversals take one entry and a Method (DD-60) | `4ab075c` 09-29 |
| DD-34 (404-432) | A host may open an action on mount, and it is then on screen | 10-01, 10-11 | `Owner-B` 10-01 | `initialAction: 'draw'` reveals Action for that visit; nothing is saved until the visitor changes the layout | 0 | Kept, on the groups (DD-53, DD-55) | `17e98cc` 10-01 |
| DD-35 (433-464) | Say before the run what the algorithm will make of the graph | 10-01, 10-10 | `Impl`; owner dropped a duplicate notice 10-01 | The run form lists edges an algorithm will read as 1 | 1: `inputNotices.ts` | Current | `17e98cc` |
| DD-36 (465-505) | An omitted weight reads as 1 | 10-01 | `Owner-B` (authorised 10-01) | An edge with no weight counts as 1 wherever a weight is read; it still has no label | 1: `src/graph/graph/model/weight.ts` | Current; supersedes upstream DD-07 | `0919126` 10-01 |
| DD-37 (506-587) | The step that examines an edge shows which way it crosses it | 10-02, 10-12, 10-25 | `Owner-B` (authorised 10-02) | `inspect-edge` draws a wave along the edge from the node the algorithm stands on | 2: `graphPresentation.ts`, `stepWaveTiming.ts` | Current | `bcbed32` 10-02 |
| DD-38 (588-648) | Signed weights are graph data, and Bellman-Ford is this prototype's own | 10-03, 10-04, 10-10 | `Codex` (owner asked 10-03; design "Codex's", not reviewed except 10-04 choices) | Any finite weight; each algorithm checks its own domain at start; Bellman-Ford added | 0 | Current | `aef5d0b` 10-03 (no AI trailer) |
| DD-39 (649-714) | Prim is this prototype's own, as lazy Prim over a queue of edges | 10-04, 10-05 | `Codex` (owner asked 10-04; owner chose 10-05: neutral inspection) | Lazy Prim on a min-heap of edges; a spanning forest on a disconnected graph | 0 | Current | `4bd0879` 10-04 (no AI trailer) |
| DD-40 (715-756) | A pseudocode line fits the panel | 10-05, 10-13 | `Owner-B` ("Asked for by the owner, 2026-10-05, who approved each" listing); exception 10-13 | About 36 characters a line in the 320px column; only the text changes | 0 | Current | `bff732d` 10-05 |
| DD-41 (757-814) | The picker names the graph on the canvas, and the custom graph is kept for the visit | 10-11 | `Owner-B` 10-11 | One picker button names the graph; a first edit on a sample makes the custom graph, kept for the visit | 1: `graphWorkingCopies.ts` | Current as a rule; label "Select preset" (DD-58) | `57d0144` 10-11 |
| DD-42 (815-954) | A paused step keeps its focus moving | 10-12, 10-13, 10-18, 10-19, 10-25 | `Owner-B` 10-12 | While paused, a streak runs along the step's edge and its node glows; 1.6s cycle; colours unchanged | 12: `stepEmphasis.ts`, `pausedStep.ts`, ... | Current | `7e92baf` 10-12 |
| DD-43 (955-1012) | A drag with Live force layout off follows the pointer | 10-12, 10-18, 10-25 | `Owner-B` 10-12: fix the drag in these prototypes only and record the departure from upstream | The dragged node follows the pointer frame by frame; layout only, no revision | 3: `src/graph/editor/useGraphEditor.ts`, `e2e/drag-follows-pointer.spec.ts` (gone) | Current | `74a4958` 10-12 |
| DD-44 (1013-1102) | A step that only completes the one before is merged into it | 10-13, 10-18 | `Owner-B` 10-13 (the rule, plus requests made on seeing a capture) | BFS dequeue+visit, stack DFS pop+visit and Kruskal init+sort become one step and one line | 14: `createBfsSequence.test.ts`, ... | Current; overrides upstream DD-14 for those three | `0d1f6de` 10-13 |
| DD-45 (1103-1225) | The End node changes only the last frame | 10-15, 10-18 | `Owner-B` 10-15; details implementer's, approved on review the same day | BFS, Dijkstra and Bellman-Ford get an End node that only the last frame reads; hovering previews a path | 11: `shortestPathQuery.ts`, `shortestPathPresentation.ts`, `ShortestPathRow.tsx`, ... | Current | `9e6e7bd` 10-15 |
| DD-46 (1226-1251) | Live force layout starts off | 10-15, 10-18 | `Owner-B` 10-15 ("for now, start with Live force layout off") | Live is off by default (upstream starts it on) | 2 | Current; what Live does with a drag is DD-57's | `6b953d5` 10-15 |
| DD-47 (1252-1342) | The finished run keeps its last frame moving | 10-15, 10-16, 10-18 | `Owner-B` request 10-15; details implementer's | The last frame repeats BFS's level reveal, Max Flow's cut march, Dijkstra's tree reveal, and so on | 8: `finalSpread.ts`, `edgeWaveTravel.ts`, ... | Current | `be570eb` 10-16 |
| DD-48 (1343-1515) | The samples are visualgo.net's example graphs, drawn where visualgo draws them | 10-16, 10-17, 10-18 | `Owner-B` 10-16; board quotes 10-17 ("tăng kích thước vùng canvas ... khoảng 1.2~1.4 lần", grow the canvas area about 1.2-1.4 times); details implementer's | Sample lists start with visualgo.net's examples, same vertices, edges, weights and positions; a few old samples stay | 14: `visualgoExamples.ts`, `sampleGraph.ts`, `positionedLayout.ts`, ... | Current (CLRS 22.5 deferred behind a future setting) | `bc46260` 10-16 |
| DD-49 (1516-1549) | A node's label fits its node | 10-16, 10-18 | `Owner-B` request 10-16 ("larger again"); the four sizes implementer's | Label face 30/24/18/14px by length inside a 64px node | 4: `labelSize.ts`, `labelSize.test.ts`, ... | Current | `e360df1` 10-16 |
| DD-50 (1550-1605) | The canvas is fixed; panels go around it, never over it | 10-16, 10-18 | `Owner-B` brief 10-16; choice 24 (10-18) | Left, right and bottom regions around the drawing, nothing above it; the canvas is rendered once and never remounted | 3: `groupsModel.ts`, ... | Current | `12cdf92` 10-17 |
| DD-51 (1606-1692) | Three regions, each a stack of groups | 10-16, 10-17, 10-18 | `Owner-B` choices of 10-16/17, and 26 (10-18) | `LayoutState {v:1, nextGroupId, left, right, bottom}` with invariants kept by every operation and the parser | 2: `src/shared/components/layout/groupsModel.ts`, `groupsModel.test.ts` | Current | `12cdf92` |
| DD-52 (1693-1814) | A held tab shows the area it will take; four kinds of target, tried in order | 10-16, 10-17, 10-18 | `Owner-B` choices 19-21 (10-17); choices 27 and 33 (10-18) `Owner-K?` **QUESTION** | Strip slot, then split band (a fifth of the body), then centre, then the drawing's edge band; the preview is the resolver's answer | 5: `dropTargets.ts`, `dropTargets.test.ts`, ... | Current (band 30%, then 15% capped at 32px, then a fifth) | `12cdf92` |
| DD-53 (1815-1849) | A group collapses to its tab strip; a reveal opens it | 10-17 | `Owner-B` choice 17 ("Chỉ nút chevron ở cuối thanh tab", "only the chevron at the strip's end") | A group collapses to its 31px strip from the chevron; a reveal or a tab press expands it | 1: `docs/graph/IMPROVEMENT_BACKLOG.md` | Current | `12cdf92` |
| DD-54 (1850-1919) | Tabs move by keyboard through a tab menu | 10-17, 10-27 | `Owner-B` choices 18 and 22 (10-17); review fix S2-01 (10-27) | Tab menu from a right-click, Shift+F10 or the ⋯ button: Move, New group, Split, Collapse | 1: `graph.spec.ts` | Current | `12cdf92` |
| DD-55 (1920-1947) | One versioned key; the graph's save policy | 10-01 | `Owner-B` choice 3 (versioned save); save policy from DD-34 (10-01) | Saved under `graph-visualizer-groups.layout` with `v: 1`; `parseLayout` repairs or gives the default | 2: `src/shared/app/storage.ts`, `useGroups.ts` | Current | `12cdf92` |
| DD-56 (1948-2034) | The page passes its drawing floor; one resolver holds every minimum | 10-17, 10-18 | `Owner-B` choices 9 and 10 (10-17), 25 (10-18) | `resolveLayout` with a 360x320 floor, 240px columns and bottom groups, 120px group heights | 1: `App.tsx` | Current | `12cdf92` |
| DD-57 (2035-2077) | Live force layout pushes away only the nodes a drag comes near | 10-18 | `Owner-K?` choice 31 ("the force layout is totally broken. i need it only to push neighbours away when they are close"), **QUESTION**; the 104px is the implementer's | With Live on, a drag pushes only nodes within 104px; Auto layout unchanged | 5: `src/graph/editor/pushApart.ts`, `pushApart.test.ts`, ... | Current | `ae63a62` **Kerk** 10-18 |
| DD-58 (2078-2137) | No hint lines, no small text; Select preset; Draw graph a disclosure; vector transport | 10-18, 10-25 | `Owner-K?` choices 28-32, **QUESTION**; the 12px legend exception is `Owner-B` 10-25 ("Hạ chữ legend xuống 12px", Bao's `19aaef3`) | Grey how-to lines deleted; no text under 13px; picker reads Select preset; Draw graph is a chevron disclosure; vector transport icons | 14: `typeScale.test.ts`, `ActionPanel.tsx`, ... | Current | `ae63a62` **Kerk** |
| DD-59 (2138-2179) | One font, one look for every control, one editor layout | 10-18 | `Owner-K?` choices 34-38 and 40, **QUESTION** | Inter for controls and JetBrains Mono for code; one control look in `controls.css`; one editor layout in `editor.css` | 7: `src/index.css`, `src/shared/styles/controls.css`, `src/shared/styles/editor.css`, ... | Current | `c59c155` **Kerk** 10-18 |
| DD-60 (2180-2606) | Whole-graph traversals are one entry each, their method chosen in the run form | 10-21 | `Owner-B` choices 10-21 ("thực hiện trước 3 thuật đầu tiên", "do the first three first"; one entry per algorithm); details implementer's | Topological Sort (DFS or Kahn), Bipartite Check (DFS or BFS) and Cut Vertex & Bridge; SCC and 2-SAT later | 37: `algorithmMethods.ts`, `TopologicalSortInspector.tsx`, ... | Current | `b88952d` 10-21 |
| DD-61 (2607-2885) | Dijkstra's relax step writes its verdict on the drawing | 10-25 | `Owner-B` request 10-25 ("Tôi muốn làm với dijkstra nữa ..."); Codex's plan was "input only"; four answers the same day | Each relax step writes a short note (sum and verdict), green when the distance changes, red when kept, gone within 1.6s | 27: `dijkstraStepNotes.ts`, `src/shared/visualization/stepNotes.ts`, `floating-text.css`, ... | Current | `b47d437` 10-25 |

Notes on the graph table:

- "(gone)" means the file is not in `git ls-files` at `662e7b3` (VERIFIED). The records describe these files in the past tense ("went with the standalone builds on 2026-10-18"). Other named files that are gone: DD-42 `src/app/exportImage.ts`; DD-44 four `*.spec.ts` files; DD-45 `e2e/shortest-path-end-node.spec.ts`; DD-47 `paused-step-motion.spec.ts`; DD-48 `e2e/visualgo-samples.spec.ts`; DD-49 `node-label-size.spec.ts`; DD-50 and DD-52 `groups-sandbox.spec.ts`, `layout-groups*.spec.ts`; DD-59 `graph-text-editor.css`, `graph-editor-controls.css` (VERIFIED absence).
- The graph AGENTS.md Safety list (`prototypes/docs/graph/AGENTS.md` lines 49-80) states the same attributions in one place. DD-36 and DD-37 were "authorised by the owner". DD-38 and DD-39 the owner "asked for, but their designs are Codex's and not yet reviewed by the owner". DD-43 to DD-49 are owner decisions or requests with details "set here within" them. DD-57 and DD-58 are "the owner's choices of 2026-10-18" (DOCUMENTED; for DD-57 and DD-58 this is a QUESTION, see finding 3).

## 4. Catalogue - tree (`prototypes/docs/tree/DESIGN_DECISIONS.md`)

The opening (lines 1-14) says the tree-visualizer documents are not copied (copy at `46ce0a7`; the submodule, pinned at the older `1477cda`, went on 2026-10-18). The graph's DD-23 to DD-28 and DD-50 to DD-56 apply as written, and TP-21 to TP-27 are the tree's records of DD-50 to DD-56 (DOCUMENTED).

**Status of the shell decisions (lines 16-26, DOCUMENTED):** DD-23 unchanged (the tree offers one extra panel, the ancestor table). DD-24 unchanged: Play is the start (owner, 2026-10-10), Autoplay and Next since "the owner's commit of 2026-10-21" (QUESTION, finding 4), wording per the owner's answer of 2026-10-29. DD-25 unchanged (see TP-03). DD-26 superseded in parts, as in the graph. DD-27 narrowed by choice 24, and the tree keeps upstream's own refit 360ms after a size change. DD-28 unchanged; upstream's fifteen `prefers-color-scheme` blocks were removed. DD-29 applies (seven switcher entries); DD-30 and DD-31 are graph-only.

| ID (lines) | Title | Dates (2026-) | Whose choice | Decision (one line) | Files named | Status | First commit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TP-01 (28-57) | One page frame, rendered by whichever workspace is active | 10-18 | `Impl` | Upstream's lazy workspaces each render `ModePage` into the one `VizPage` frame; page state lives in `App` | 3: `bundle.test.ts` (gone), `usePageLayout.ts`, `PageLayout.tsx` | Current | `7b16bf3` 09-22 |
| TP-02 (58-88) | An inspector renders in two halves from one set of props | 10-10, 10-11 | `Impl`; Go folded into Play by the owner (10-10) | Each inspector takes `section`, `'controls'` or `'status'`, and is rendered twice with the same props | 0 | Current | `7b16bf3` |
| TP-03 (89-111) | Which recorded field is the active pseudocode line | 10-13 | `Impl`; `withPrevious` `Owner-B` 10-13 | BST, AVL, Heap and Trie record `activeCodeLine`; Binary Lifting and Segment Tree key by `phase` | 6: `treePseudocodeView.ts`, `algorithmPseudocode.ts`, ... | Current | `7b16bf3` |
| TP-04 (112-232) | What lives in the drawing and what lives in Status | 10-07, 10-08, 10-09 | `Owner-B` 10-07 ("Decided by the owner") | Views that select with the canvas (heap array, segment array, ancestor table and its step strip) live in the drawing | 1: `describeStep.ts` | Current (some split-rails wording is historical) | `7b16bf3` |
| TP-05 (233-270) | One key listener, with upstream's ownership rules | 10-10, 10-29 | `Impl`; Space = Play `Owner-B` 10-10 | One window listener; controls that own the arrows keep them | 1: `src/shared/visualization/playbackCountdown.ts` | Current | `7b16bf3` |
| TP-06 (271-302) | The canvas keeps upstream's fit rules | 10-11 | `Impl`; amended by `Owner-B` 10-11 (control icons back) | Fit after every layout transition and 360ms after a size change; the Fit button is ours | 0 | Current (amended 10-11) | `7b16bf3` |
| TP-07 (303-316) | Tokens and state colours | - | `Impl` | Every colour is a token or the graph's state vocabulary, plus three tree roles | 2: `swatchTokens.test.ts`, `viz-page.css` | Current | `7b16bf3` |
| TP-08 (317-324) | The Edit action replaces the run-scoped editor fold | - | `Impl` | The Edit action opens and shuts the editor; a run never folds it; the issue count shows on Edit | 0 (names `drawIssueCount`) | **Partly stale?** (INFERENCE, section 9) | `7b16bf3` |
| TP-09 (325-333) | Examples are buttons, and the loaded one is named | - | `Impl` | One button per sample; the picker names the data (TP-16) | 0 | Current | `7b16bf3` |
| TP-10 (334-361) | A host may open an action on mount, and it is then on screen | 10-01, 10-11 | `Owner-B` 10-01 | `initialAction: 'draw'` reveals Action for that visit; the site's Tree Editor card passes it | 0 | Current | `17e98cc` 10-01 |
| TP-11 (362-396) | Under a host, the bar is drawn above the frames | 10-01 | `Owner-B` 10-01 ("Decided by the owner") | `renderTopBar` is called once above the frames; the parts pass through `hostBar.ts` | 2: `hostBar.ts`, `viz-page.css` | Current | `7c91fe7` 10-01 |
| TP-12 (397-439) | A pseudocode line fits the panel | 10-05, 10-13 | `Owner-B`, as DD-40 (asked for 10-05, each listing approved); exception 10-13 | About 36 characters a line; ids and indents kept | 0 | Current | `bff732d` 10-05 |
| TP-13 (440-545) | A Segment Tree with lazy propagation beside the eager one, and exact decimals in both | 10-08, 10-09, 10-10, 10-12 | `Owner-B` ("Asked for by the owner, who chose each point") | Second workspace `segment-tree-lazy` with tags and derived sums; exact decimals in both trees | 1: `src/tree/segment/decimal.ts` | Current | `fc4172d` 10-09 |
| TP-14 (546-584) | e-Lecture slides are written after visualgo.net's, in the panel | 10-09, 10-10 | `Owner-B` 10-09 | The e-Lecture stays a panel; content in visualgo.net's lecture style | 1: `electureSlides.test.ts` | Current | `3a429ad` 10-09 |
| TP-15 (585-932) | BST and AVL offer visualgo.net's remaining operations | 10-09, 10-10 | `Owner-B` chose the operations 10-09 | Adds Find Min/Max, Predecessor/Successor, Lower Bound, Select, three traversals and AVL Delete | 5: `bst/subtreeSizes.ts`, `avl/rotations.ts`, ... | Current | `c364204` 10-09 |
| TP-16 (933-994) | The picker names the data on the canvas, and the custom data is kept for the visit | 10-11 | `Owner-B` 10-11 | A picker per workspace: Custom tree/heap/words/array first, then the samples | 2: `workspaceEntries.ts`, `useWorkspaceEntries.ts` | Current (label per TP-28) | `95bf326` 10-11 |
| TP-17 (995-1133) | A paused step keeps its focus moving | 10-12, 10-13 | `Owner-B` 10-12 | As DD-42; not on the finished last step | 9: `stepEmphasis.ts`, `pausedStep.ts`, ... | Current | `a8c191c` 10-12 |
| TP-18 (1134-1296) | A step that only completes the one before is merged into it | 10-13, 10-18 | `Owner-B` 10-13 | As DD-44, for traversals, AVL, heap and others | 10: `stepFocus.test.ts`, ... | Current | `f935bc6` 10-13 |
| TP-19 (1297-1337) | A run ends on a badge that says how it ended | 10-13, 10-23, 10-24 | `Owner-B` 10-13; NONE badge 10-23 ("Thêm badge NONE trên node cuối", "add a NONE badge on the last node"); its place implementer's | MISS, DONE, INSERTED and NONE end badges | 11: `bstDeletePresentation.ts`, `heapPresentation.ts`, ... | Current | `28e08f8` 10-13 |
| TP-20 (1338-1398) | A changed number floats its change off it | 10-13, 10-23 | `Owner-B` 10-13 (the popup, four places, the cut for fast steps) | `+7` / `-3` popups on the Segment Trees, gone within 0.8s | 10: `valuePopups.ts`, `FloatingText.tsx`, `floating-text.css`, ... | Current; regression signal **narrowed** by the owner's choice of 10-23 (TP-34) | `ff77eca` 10-13 |
| TP-21 (1399-1446) | The canvas is fixed; panels go around it, never over it | 10-16, 10-18 | `Owner-B` brief 10-16 | DD-50 as written; the shell is the graph's, byte for byte | 17: `GroupsLayout.tsx`, `groupsModel.ts`, ... | Current | `d82a24c` 10-17 |
| TP-22 (1447-1518) | Three regions, each a stack of groups, the Ancestor table a tab of its own | 10-16, 10-17, 10-18 | `Owner-B` choice 5 (default, 10-16) and scrollbars (10-17) | DD-51; default: Action and e-Lecture left, Pseudocode over Status right | 4: `src/tree/app/extraPanels.ts`, `useGroups.test.tsx`, ... | Current | `d82a24c` |
| TP-23 (1519-1573) | A held tab shows the area it will take; four kinds of target, tried in order | 10-17, 10-18, 10-27 | DD-52; choices 27 and 33 `Owner-K?` **QUESTION**; choice 26 `Owner-B` | As DD-52 | 3: `dropTargets.ts`, `dropTargets.test.ts`, ... | Current | `d82a24c` |
| TP-24 (1574-1603) | A group collapses to its tab strip; a reveal opens it | 10-17, 10-18 | `Owner-B` choice 17 | DD-53 plus the tree's reveals of the Ancestor table | 2 (both specs gone) | Current | `d82a24c` |
| TP-25 (1604-1632) | Tabs move by keyboard through a tab menu | 10-17, 10-18 | `Owner-B` choice 22 | DD-54; the tree adds nothing | 1 (spec gone) | Current | `d82a24c` |
| TP-26 (1633-1665) | One versioned key; the graph's save policy | 10-16, 10-17, 10-18 | `Owner-B` choice 3 | DD-55 under `tree-visualizer-groups.layout` | 4: `src/shared/app/storage.ts`, `useGroups.ts`, ... | Current | `d82a24c` |
| TP-27 (1666-1719) | The drawing's floor is the workspace's | 10-17, 10-18 | `Owner-B` choice 10 | DD-56 with a per-workspace floor in `drawingFloor.ts` | 4: `src/tree/app/drawingFloor.ts`, `drawingFloor.test.ts`, ... | Current | `d82a24c` |
| TP-28 (1720-1769) | No hint lines, no small text; Select preset; the edit action a disclosure; vector transport | 10-18, 10-25 | `Owner-K?` choices 28-30 and 32, **QUESTION**; 12px legend `Owner-B` 10-25 | DD-58 on the tree page | 5: `typeScale.test.ts`, `ActionPanel.test.tsx`, ... | Current | `ae63a62` **Kerk** 10-18 |
| TP-29 (1770-1790) | The tree's editors are the graph's | 10-18 | `Owner-K?` choices 34-37 ("graph is the SSOT. if graph does not have a toggle dropdown for graph data, tree should not either"), **QUESTION** | DD-59: the tree editors use the graph's layout on `editor.css`; the collapsible data section, "valid" badges and Load sample go | 1: `editor.css` | Current | `c59c155` **Kerk** 10-18 |
| TP-30 (1791-1890) | Edges run between the node centres | 10-19 | `Owner-B` request 10-19 ("tôi vẫn thích những thứ truyền thống ...", an edge from the parent's centre to the child's) | Edges on the centre line, drawn rim to rim | 7: `treeEdgeGeometry.ts`, `StraightTreeEdge.test.tsx`, ... | Current | `499cb42` 10-19 |
| TP-31 (1891-1977) | Binary Lifting is two runs, Preprocessing and Query, chosen in the Action panel | 10-19 | `Owner-B` request 10-19 ("lúc chọn preprocess thì nên khóa vùng chọn u,v ...", lock u, v under Preprocessing) | Two operations, two runs; u and v dimmed and locked under Preprocessing | 10: `createBinaryLiftingSequence.ts`, ... | Current | `e55de1c` 10-19 |
| TP-32 (1978-2119) | A hovered node shows its path to the root and its 2^k-th ancestors | 10-19 | `Owner-B` request 10-19 ("tôi cần một thứ gần giống với bước cuối của dijstra ...") | On a paused or finished step, hover shows the path to the root and the 2^k ancestors; the table row lights | 11: `hoverQuery.ts`, `hoverPresentation.ts`, ... | Current | `60ccc44` 10-20 |
| TP-33 (2120-2682) | The Binary Heap: Min or Max, 1-based, and visualgo.net's operations | 10-20, 10-21 | `Owner-B` request 10-20 ("thay vì binary min heap-> chuyển thành binary heap ...") and four answers | Binary Heap with a Min/Max switch, 1-based indices, six operation groups, at most 31 items | 34: `heapOrder.ts`, `heapIndices.ts`, `heapOperationGroups.ts`, ... | Current (old `-min` file names kept as the history of a rename on 10-21) | `7d39c38` 10-20 |
| TP-34 (2683-2978) | A step writes its verdict on the drawing, Binary Lifting first | 10-13, 10-23, 10-24, 10-25 | `Owner-B` request 10-23 ("tôi muốn hiển thị những dòng chữ nổi ...", floating text; red for reject, green for accept) | Step notes float up and fade: green accept, red reject, ink when they only tell | 25: `StepNoteLayer.tsx`, `stepNotePlacement.ts`, `stepNotes.ts`, ... | Current (layer moved to `src/shared` on 10-25) | `d82aa18` 10-23 |
| TP-35 (2979-3187) | Binary Lifting's legend is on the canvas, and u and v share one colour | 10-23, 10-24, 10-25, 10-26 | `Owner-B` request 10-23 ("để u,v cùng màu ..."; "Trên canvas, góc trên phải như graph"); trimmed 10-25 | The shared canvas legend, top right; u and v one colour; the Query legend drops u = v and LCA | 20: `canvas-legend.css`, `src/shared/visualization/legend.ts`, ... | Current | `1f763dc` 10-23 |
| TP-36 (3188-3676) | The BST, AVL and heap steps write their verdicts too, AVL and Delete first | 10-23, 10-24, 10-25 | `Owner-B` request 10-23 ("bạn hãy kiểm chứng và lên plan trước khi làm", "check it and plan it before doing it") and four answers | Step notes for BST, AVL and the heap, built in three steps | 63: `walkStepNotes.ts`, `heapSifts.ts`, ... | Current | `7180d81` 10-24 |

## 5. Catalogue - sorting (`prototypes/docs/sorting/DESIGN_DECISIONS.md`)

The opening (lines 1-18) says the sorting upstream's documents are copied into the folder (`sorting-submodule-AGENTS.md`, `sorting-performance-milestone.md`; submodule pointer `9236a65` until 2026-10-18). The graph's DD-23 to DD-29 and DD-50 to DD-56 apply, and SP-12 to SP-18 are sorting's records of DD-50 to DD-56 (DOCUMENTED).

**Status of the shell decisions (lines 20-33, DOCUMENTED):** DD-23 unchanged (Compare changes which panels exist; SP-03). DD-24 kept: Play is the start (owner, 2026-10-10), Autoplay and Next since "the owner's commit of 2026-10-21" (QUESTION). DD-25 unchanged in principle and widened (all eight algorithms record lines). DD-26 superseded in parts, plus choice 17 (2026-10-17: the chevron alone collapses). DD-27 kept as a no-op, and `F` removed from the shortcut list. DD-28 unchanged and load-bearing (canvas reads tokens once per theme). DD-29 applies in Study; Compare empties the nav. DD-34: no host opens one. DD-50 to DD-56 apply as written. DD-30 and DD-31 are graph-only.

| ID (lines) | Title | Dates (2026-) | Whose choice | Decision (one line) | Files named | Status | First commit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SP-01 (35-98) | The start is a mount boundary, not a state change | 10-10, 10-21, 10-29 | `Impl` core; `Owner-B` rule 10-10 (a frozen pane does not block the start); "the owner's commit of 2026-10-21" is Kerk's `a074f50`, **QUESTION**; answer 10-29 | `IdleFrame` before a run, `RunFrame` keyed by `runKey` after; Play, or Next with no run, starts | 1: `footerFocus.ts` | Current | `613bca7` 09-27 |
| SP-02 (99-117) | The runs array's identity is load-bearing | - | `Impl` | Operation buffers hang off the runs array in a `WeakMap`; the array is replaced only on a real change | 0 | Current | `613bca7` |
| SP-03 (118-137) | Compare removes Pseudocode and e-Lecture, rather than hiding them | - | `Impl` | Compare's panel set is Status alone; the algorithm moves into each pane | 0 | Current | `613bca7` |
| SP-04 (138-158) | The drawing floor is a canvas height, with the chrome added per variant | - | `Impl` | `MIN_CANVAS_HEIGHT` 200px plus `COMPARE_PANE_CHROME` | 2: `sort-panes.css`, `drawingFloor.test.ts` | Current (compares against the V2/V7 builds, now gone) | `613bca7` |
| SP-05 (159-179) | Seeking rewinds by replaying history forward | - | `Impl` | `seekComparison` replays the kept history from a fresh state; never `reset` | 0 | Current | `613bca7` |
| SP-06 (180-202) | Eager production is decided by cap-and-bail, and keeps what it pulled | - | `Impl` | Pull until done or 60,000 operations summed across panes, round robin | 0 | Current | `613bca7` |
| SP-07 (203-232) | Line metadata rides on the operations that already exist | 10-13 | `Impl`; cites the owner's decision of 10-13 | An optional `line` on existing operations, so no extra counted step | 2: `pseudocodeHighlight.ts`, `sortingPseudocode.test.ts` | Current | `613bca7` |
| SP-08 (233-252) | The palette is floored programmatically | - | `Impl` | `sortPalette.ts` enforces contrast, distinctness and surface floors | 3: `sortPalette.ts`, `sortPalette.test.ts`, `themePalette.test.ts` | Current | `613bca7` |
| SP-09 (253-268) | A pane that cannot run is left out of the comparison | - | `Impl` | No share bar and em dashes for a pane whose algorithm rejects the data | 0 | Current | `613bca7` |
| SP-10 (269-301) | A pseudocode line fits the panel | 10-05, 10-13 | `Owner-B` ("Asked for by the owner, 2026-10-05, who approved each") | As DD-40 for `sortingPseudocode.ts` | 1: `sortingPseudocode.ts` | Current | `bff732d` 10-05 |
| SP-11 (302-374) | A step that only completes the one before it is merged into it | 10-13 | `Owner-B` rule 10-13; texts implementer's | Merged steps in radix, counting and others | 1: `src/sorting/types/sort.ts` | Current | `4a54f7f` 10-13 |
| SP-12 (375-413) | The canvas is fixed, and Study's canvas fills the drawing | 10-16, 10-17, 10-18 | `Owner-B` brief 10-16 ("phía trên canvas cố định không có panel nào", no panel above the fixed canvas) | DD-50, plus a `sort-panes.css` fix so Study's pane grid fills the drawing | 2: `sort-panes.css`, `layout-groups.spec.ts` (gone) | Current | `0e3857f` 10-17 |
| SP-13 (414-469) | The groups shell is the graph's, byte for byte; sorting's differences live in its app files | 10-16, 10-17, 10-18 | `Owner-B` (scrollbars, 10-17) | DD-51; the shell files were `cmp`-identical copies until 10-18, now one copy in `src/shared` | 15: `groupsModel.ts`, `GroupsLayout.tsx`, ... | Current | `0e3857f` |
| SP-14 (470-505) | Drop targets and the preview, with Compare's one panel | 10-17, 10-18 | DD-52; choices 27 and 33 `Owner-K?` **QUESTION**; 26 `Owner-B` | Compare's targets; a drop that would open the bottom row is judged on Compare's floor | 2 (specs gone) | Current | `0e3857f` |
| SP-15 (506-543) | Compare starts with Status alone in a collapsed bottom row | 10-17, 10-18 | `Owner-B` choice 17 | `COMPARE_LAYOUT`: all four panels in one bottom group, Status in front, row collapsed | 1 (spec gone) | Current | `0e3857f` |
| SP-16 (544-566) | Tabs move by keyboard through the tab menu, and the arrows step operations | 10-17, 10-18 | `Owner-B` choices 18 ("Một nút ⋯ mỗi thanh tab + chuột phải trên tab") and 22 | DD-54; on a tab the arrows step operations | 1 (spec gone) | Current | `0e3857f` |
| SP-17 (567-594) | One versioned key per mode | 10-16, 10-18 | `Owner-B` choice 3 | Two keys, `.layout.study` and `.layout.compare` | 3: `useGroups.ts`, `usePageLayout.test.tsx`, ... | Current | `0e3857f` |
| SP-18 (595-644) | The drawing floor is `minDrawingHeightFor`, and four panes at 1280x600 scroll | 10-17, 10-18 | `Owner-B` choice 10 | Floors 320x200 (Study), 320x278 (two panes), 320x519 (four); the grid scrolls at 1280x600 | 4: `usePageLayout.ts`, `usePageLayout.test.tsx`, ... | Current | `0e3857f` |
| SP-19 (645-669) | No hint lines, no small text, vector transport | 10-18 | `Owner-K?` choices 28 and 32, **QUESTION** | DD-58 where sorting has the same parts | 0 | Current | `ae63a62` **Kerk** 10-18 |
| SP-20 (670-674) | One font and one look for every control | 10-18 | `Owner-K?` choices 34, 35 and 40, **QUESTION** | DD-59 where sorting has the parts; no About, Team, Terms in the footer | 1: `src/shared/styles/controls.css` | Current | `c59c155` **Kerk** 10-18 |

## 6. (a) The rules that shaped the work, and where they are written

`prototypes/AGENTS.md` (70 lines) is the live rule file of the one app. Kerk's `0394b64` (2026-10-18) created it; lines 38-42 come from Kerk's `c59c155`, and later lines from Bao's commits up to `9baa117` (2026-10-30) (VERIFIED, `git blame`). Each `prototypes/docs/{graph,tree,sorting}/AGENTS.md` starts with a "Historical" note and is "kept as a record": its "folder names, ports, commands and the rule to fix split rails first no longer apply" (`prototypes/AGENTS.md` lines 53-55, DOCUMENTED). INFERENCE: their other rules are still meant to apply. **QUESTION** to confirm.

| Rule | Where it is written (file:lines) | First written | Label and notes |
| --- | --- | --- | --- |
| **One fix, one place** | `prototypes/AGENTS.md:37-44`: shared code lives in `src/shared` and is changed there; every control from `controls.css`, every editor from `editor.css` (DD-59). Repeated for the groups shell in `docs/graph/AGENTS.md:321-331`, `docs/tree/AGENTS.md:133-143`, `docs/sorting/AGENTS.md:192-202`; `docs/sorting/DEVELOPER_GUIDE.md:147-155` ("a fix that lands in one copy of the three is worse than none") | `0394b64`, Kerk, 2026-10-18 (Claude trailer) | VERIFIED text. The earlier rule of byte-identical copies checked with `cmp` was "retired" by the owner on 2026-10-28: "Rút luật, thay bằng src/shared" ("retire the rule, replace it with src/shared"), written in `02c4e12` (Bao, 2026-10-30). Different from upstream DD-22 "one fact, one place" (one fact per inspector). **QUESTION:** who set "one fix, one place"? |
| **Docs describe the current state** | No rule text in any AGENTS.md, guide or README (VERIFIED, `git grep`). Practice is recorded in `docs/graph/BELLMAN_FORD_ACCEPTANCE.md:128-132` ("The documents that described the work stage by stage now describe the current state"), `docs/graph/PRIM_ACCEPTANCE.md:201-202` ("DD-39 is a decision rather than a stage log") and `design/proposals/visualgo-web-site/README.md:1238-1242` (a review on 2026-10-04 rewrote stage-by-stage documents as the current state) | Review of 2026-10-04 (DOCUMENTED) | DOCUMENTED as practice only. The records describe removed files in the past tense ("went with the standalone builds on 2026-10-18"), which fits the practice (VERIFIED by spot checks). **QUESTION:** was this your rule, and when did you set it? |
| **Every change updates its docs** | `docs/graph/AGENTS.md:386-387`, `docs/tree/AGENTS.md:203-205`, `docs/sorting/AGENTS.md:275-277`: "Update README or the owning document here in the same change when behaviour or an invariant changes; never restate an inherited rule, link to it." | Inherited: `graph-visualizer-v2/AGENTS.md:14-15` ("Update the owning document in the same change when behavior or an invariant changes") and its `docs/DESIGN_DECISIONS.md:5` | VERIFIED text. It sits only in the three "Historical" AGENTS files; `prototypes/AGENTS.md` does not repeat it (VERIFIED). **QUESTION:** does it still bind the one app? |
| **13px floor** | DD-58 item 2 (`docs/graph/DESIGN_DECISIONS.md:2090-2099`), TP-28, SP-19; `prototypes/AGENTS.md:51-53` ("no text is set below 13px", with the canvas legend at 12px, "the owner's exception of 2026-10-25"); the test `prototypes/src/shared/styles/typeScale.test.ts` (`FLOOR_PX = 13`, `CANVAS_LEGEND_PX = 12`) | Choice 32 (2026-10-18) in Kerk's `ae63a62`; 12px exception in Bao's `19aaef3` (2026-10-26) | VERIFIED text and test file. Test not run by me. Choice 32 is `Owner-K?` (**QUESTION**, finding 3) |
| **The owner decides rules** | No single rule text (VERIFIED, `git grep`). Practice: records separate "the owner's decision / choice / request" from details "set here within it"; V10 proposal §0.2 "Implementer's defaults, not reviewed by the owner" (`design/proposals/viz-shell-v10/README.md:95`); TP-34 (`docs/tree/DESIGN_DECISIONS.md:2725-2728`): "the owner was told this changes a rule and chose the plan (2026-10-23)"; `docs/graph/AGENTS.md:329`: "The owner retired that rule on 2026-10-28"; DD-38/DD-39 flag Codex designs as not reviewed; backlog items marked "for the owner" | - | DOCUMENTED as practice. **QUESTION:** confirm this was your instruction |
| **Proportionate tests** | No rule text (VERIFIED, `git grep` for "proportionate", "can affect" and similar). The written checks are the full list in `prototypes/AGENTS.md:59-70` (`lint`, `typecheck`, `test`, `build`, `test:e2e`) and "Any change to a panel, the layout, the footer, CSS or the routing needs the browser suite" (also `docs/graph/AGENTS.md:378-379`) | - | Not written in the repository. **QUESTION:** where was this rule given, and when? |
| **Upstream is a reference only** | `docs/graph/AGENTS.md:51-58`, `docs/tree/AGENTS.md:53-62`, `docs/sorting/AGENTS.md:69-76` (each "the owner's decision of 2026-10-12": nothing changed upstream, nothing synced either way, every fix in the prototypes); `docs/graph/DEVELOPER_GUIDE.md:303-313`; `docs/tree/DEVELOPER_GUIDE.md:703-707`; `docs/sorting/README.md:38-41`; `docs/tree/DESIGN_DECISIONS.md:875` | `38c726f`, Bao, 2026-10-12, "Record that upstream is a reference only, never changed or synced" (Claude trailer) | VERIFIED text and commit. The upstream repositories were written by the BJoozz identities (finding 7) |

Other written rules seen while reading (VERIFIED text): **Every page is a route** (`prototypes/AGENTS.md:45-46`). **Feature-scoped CSS, design-system tokens, theme in `html[data-theme]`** (`prototypes/AGENTS.md:56-57`, DD-28). **Target screens**: desktop and laptop windows about 1366x657 to 1920x960; smaller windows are not defects (`docs/*/AGENTS.md` "Target screens", for example `docs/graph/AGENTS.md:36-45`). **The design decisions stand** (`prototypes/AGENTS.md:47-53`).

## 7. (b) Backlog items that record open limitations

All three files say none of their items is implemented (graph line 3, tree line 3, sorting line 2). Items are DOCUMENTED; I checked none against the code. "Owner" marks an item the file leaves for the owner to decide.

### 7.1 Graph (`prototypes/docs/graph/IMPROVEMENT_BACKLOG.md`, 166 lines, items 1-24)

| # | Open limitation (one line) |
| --- | --- |
| 1 | e-Lecture slides are placeholders; they need VisuAlgo's text |
| 2 | Owner: a collapsed group can still be expanded in a column too short for it (drawn under its minimums) |
| 3 | Owner: whether a visit without a reveal should save its arrival on mount |
| 4 | A panel moved to another group remounts, so caret, selection or draft held in the panel itself is lost |
| 5 | At 1280px wide the drawing is 646px, so the legend starts as a chip |
| 6 | Bundle size: the build warns above 500 kB |
| 7 | `App` still wires many props through one wide `PagePanelContext` |
| 8 | No wave on recursive DFS's return step (the step carries no edge) |
| 9 | Wave glow is always sky blue whatever the wave's colour |
| 10 | Recursive DFS briefly paints a skipped tree edge grey and dashed |
| 11 | The Flow/Residual switch replays a wave |
| 12 | Bellman-Ford on large graphs: whole timeline generated at start (about 25,700 frames, 32 MiB for 40 nodes, 160 edges); no cap |
| 13 | Prim on very large inputs: quadratic snapshot references; O(E) name lookups per row |
| 14 | Shared colours below contrast minimums in some themes (muted text 3.46:1 to 4.48:1, and others) |
| 15 | Kruskal prints raw JavaScript sums (0.30000000000000004) and a hyphen for minus |
| 16 | Owner: drop-feedback details set by the implementer (DD-52) await confirmation |
| 17 | The Graph Traversal e-Lecture decks are short (four or five slides) |
| 18 | Owner: one opening graph per algorithm, as visualgo.net's lecture does |
| 19 | Strongly Connected Components and 2-SAT not built (later round, owner's choice of 2026-10-21) |
| 20 | Step notes only for Dijkstra; Bellman-Ford, Kruskal and Kahn have none |
| 21 | Dijkstra prints raw decimal sums; the engine's exact compare can read wrong in arithmetic |
| 22 | Sums past the largest number print infinity, and that step writes no note |
| 23 | A step note does not keep off React Flow's controls, edges or arrowheads |
| 24 | Owner: crowded samples at fit zoom (Large and MRT nodes 19-23px across under notes) |

### 7.2 Tree (`prototypes/docs/tree/IMPROVEMENT_BACKLOG.md`, 267 lines, items 1-20)

The file says the graph's layout items apply here too (lines 3-8).

| # | Open limitation (one line) |
| --- | --- |
| 1 | Extract the shell into a package (the item still speaks of copies; see section 9) |
| 2 | At 1280px wide the drawing is 646px; wide trees and the heap array get small |
| 3 | The run header shows a phase but no tracked figure (comparisons, swaps) |
| 4 | Classic theme: white `--text-on-sunken` on a light surface makes summary tiles hard to read |
| 5 | Heap Insert legend: a node both current and new paints as new |
| 6 | No interactive e-Lecture mode (slides that drive the visualization, quizzes) |
| 7 | Only Binary Lifting's legend is on the canvas; every other operation's is still in Status |
| 8 | Focus falls to the page when a step removes a focused chip |
| 9 | Legends that disagree with the canvas (from stylesheet order; not checked in a browser) |
| 10 | BST/AVL features of visualgo.net left out (batch insert/remove and others), kept for later by the owner on 2026-10-09 |
| 11 | Owner: the arrays under the tree grow 2px when Range Update starts |
| 12 | TP-04's smallest drawing and TP-12's row counts not measured again in this build |
| 13 | A drop during automatic playback: the test went on 2026-10-18 and the tree's case was never checked |
| 14 | Binary Lifting two runs: with no run the table and strip are empty under Query (an owner's call) |
| 15 | Binary Lifting hover: pointer only, no keyboard or touch equivalent |
| 16 | Binary Heap open points (hover does not light parent and children, and others) |
| 17 | Step notes beyond Binary Lifting: open points of the shared layer |
| 18 | Sorting's stylesheet still declares tree swatch tokens no sheet reads |
| 19 | A click selects the node clicked before it (`/lca`, `/bst`, no run), seen 2026-10-23, not fixed |
| 20 | Found while writing BST/AVL notes, not fixed: the paused glow restarts on a frame that repeats the one before, and more |

Also under "Outside the target screens" (line 99, for the later phone design): chips in a narrow strip; the strip at very large fonts in a short drawing; the canvas legend in one column (windows 761-1100px). VERIFIED structure note: items 11-20 come after this heading with no heading of their own. INFERENCE: they are general items, not small-screen ones.

### 7.3 Sorting (`prototypes/docs/sorting/IMPROVEMENT_BACKLOG.md`, 118 lines, items 1-13)

The file says the graph's shell items and the tree's shell and legend items apply too (lines 2-11).

| # | Open limitation (one line) |
| --- | --- |
| 1 | Four chrome files (`FooterBar.tsx`, `pageCommands.ts`, `playbackSpeed.ts`, `usePageUi.ts`) have drifted from the graph's; no back-port |
| 2 | Compare mode has no colour legend |
| 3 | Seven renderer colours cannot be rebound by the floored palette (tuned for the old dark theme) |
| 4 | Nothing announces to a screen reader that a pane has finished |
| 5 | The setup strip's collapse state is not saved |
| 6 | Structural pseudocode lines (signatures, `mid = ...`, recursive calls) never light |
| 7 | Operation history is unbounded (17-28 MiB worst case over four panes); no checkpoint seeking |
| 8 | Seventeen readouts call `toLocaleString()` with no locale |
| 9 | The browser suite's environment needs (artifacts outside OneDrive, `--workers=2`) are recorded mostly in commits |
| 10 | A compared value that has left its slot is shown nowhere |
| 11 | Owner: Compare's bottom row opens by its chevron where a drop could not open it |
| 12 | Compare's Status table needs a 616px group; it scrolls sideways in a side column |
| 13 | The Study canvas-fill fix is "in this copy only" (see section 9) |

Open questions U5, U7, U8 and U9 (lines 107-118) are all marked answered: U5 unreachable, U7 "Decided: no" (the cap stays 240), U8 worked around (`CODE_OVERRIDES`), U9 "Decided: yes, confirmed" (four panels). The table does not say who answered them. **QUESTION.**

## 8. (c) The DEVELOPER_GUIDE "departures from upstream" lists

### 8.1 Graph

`prototypes/docs/graph/DEVELOPER_GUIDE.md:303-313` "Upstream is a reference" points to the list in `prototypes/docs/graph/AGENTS.md` Safety (lines 49-272). DOCUMENTED content of that list:

- **What upstream keeps that the prototype changed** (lines 78-82): DD-07's 0 for an omitted weight; its recap waves; its non-negative-only text parser; no Bellman-Ford or Prim; Live force layout on at start; a node dragged with Live off moving only on release; its own samples laid out by force.
- **Inherited files deliberately changed** (lines 83-110; the record ids in brackets are mine where the list gives none, INFERENCE): the five inspectors (pseudocode removed, to its own panel, DD-25); `MaximumFlowInspector` (controlled edge filter); `GraphEditorControls` (Directed can be locked with a reason, DD-30); `GraphTextEditor` (no hint lines, DD-58); the Dijkstra, Kruskal and Max Flow inspectors (table search, DD-31); `GraphCanvas.module.css` (no OS colour scheme, DD-28; Dijkstra badges, DD-32); `canvas-legend.css` (see-through, DD-13 note); `dijkstraPresentation.ts` (DD-32); the inspector sheets (inner scroll removed, DD-22); the listings of BFS, stack DFS, Dijkstra, Kruskal and Max Flow (shortened, DD-40; merged lines, DD-44); `dfs` renamed `dfsStack`, with `dfsRecursive` new (DD-33).
- **Later changes, each with its record as the reason** (lines 110-272): DD-36 (weight 1), DD-37 (waves), DD-42 (paused loop), DD-47 (final frames), DD-49 (label size), DD-43, DD-46 and DD-57 (drag and Live layout), DD-44 (merged steps), DD-38 (signed parser, Bellman-Ford), DD-39 (Prim), DD-30, DD-29, DD-45 (End node), DD-48 (visualgo samples, `layoutBoard.ts`), DD-60 (traversals) and DD-61 (Dijkstra notes).
- **Why, in one line:** "The owner's decision, 2026-10-12": every fix is made in the prototypes, never upstream, and the departures are recorded (lines 51-58). Each item's own reason is its DD record.

### 8.2 Tree

`prototypes/docs/tree/DEVELOPER_GUIDE.md:703-909` "Departures from upstream, and graph shell fixes" is one long inventory, "a record ... not a checklist for a sync" (DOCUMENTED):

- **Changed inherited files** (lines 708-765; record ids in brackets are mine, INFERENCE, except TP-12 and TP-13, which the list names): every inspector (split into controls and status, TP-02; no Run button, TP-02 and DD-24); `BinaryLiftingTable` (view state by prop, a sheet or panel variant, TP-04); `TreeCanvas` (`showControls`, `showHint`, TP-06); `TreeTextEditor`; the four modes; `App`; `LazyWorkspace`; every sheet under `src/tree/styles` and `TreeCanvas.module.css` (tokens, no OS colour scheme, TP-07, DD-28); the listings shortened to fit (TP-12); the Segment Tree's exact decimals (TP-13).
- **Deleted:** `TreeWorkspace`, `TreeToolbar`, `TreeInspector`, `ModeToolbar`, `WorkspacePlayer`, `VisualizationPlayer`, `SamplePicker`, `usePlaybackShortcuts` and their sheets, and `BinaryLiftingTable.toggle.test.tsx` (INFERENCE: replaced by TP-01's frame, TP-05's one listener and TP-09's buttons).
- **Added inside upstream's folders:** the Binary Lifting strip files (TP-04), the lazy Segment Tree (TP-13), the BST and AVL operations (TP-15).
- **Changed for later records:** TP-15, TP-17, TP-18, TP-03/TP-12/TP-19, TP-20, TP-30, TP-33, TP-34, TP-35 and TP-36, each listing its files (lines 766-906).
- It ends: "Shell files are listed in ARCHITECTURE.md; copy a graph shell fix over verbatim unless the table there names the file" (lines 907-909).

### 8.3 Sorting

`prototypes/docs/sorting/DEVELOPER_GUIDE.md:147-155` "Keeping in step with the shell" points to `prototypes/docs/sorting/ARCHITECTURE.md:56-84` "Shell files that differ from the graph prototype, and why" (DOCUMENTED):

- `FooterBar.tsx` counts operations, not frames (a growing total, Replay at the end); `playbackSpeed.ts` is operations per second on a 15x ladder; `PseudocodePanel.tsx` gets `hasRun` ("No line" at operation 0); `pageCommands.ts` and `keyboardShortcuts.ts` add `Alt+1/2/4` and drop `F` (no Fit); `usePageUi.ts` holds setup-strip state and the Compare panel set; `usePageShortcuts.ts` is the tree's copy; `footer-bar.css` and `viz-page.css` style the scrubber and pane grid; `usePageLayout.ts` and `PageLayout.tsx` hold the per-mode layout. `TopBar.tsx`, `exportImage.ts` and the local `panelRegistry.ts` are gone (2026-10-18, 2026-10-19).
- The domain code (eight algorithms, operation model, lazy pipeline, three Canvas renderers) is "forked" from sorting-algorithm-visualizer at `9236a65`, not imported (`prototypes/docs/sorting/README.md:34-41`).

## 9. Places where the docs may not describe the current state

These are found while reading, not a full sweep. I fixed nothing (read-only).

| Where | What it says | Evidence | Label |
| --- | --- | --- | --- |
| TP-08, `docs/tree/DESIGN_DECISIONS.md:317-323` | "the user's own toggle of the editor header still works" | TP-29 (lines 1770-1790) says the collapsible data section (`CollapsibleSection`, `useEditorCollapse`) is gone, and `grep` finds neither name in `prototypes/src`. `drawIssueCount`, the other half of TP-08, is still in `src/tree/app/ModePage.tsx` | VERIFIED code; INFERENCE that the sentence is stale |
| `docs/graph/DEVELOPER_GUIDE.md:306-309`; also `docs/tree/AGENTS.md:60-61` | Fixes are made "in graph-visualizer-split-rails first and then in graph-visualizer-docks and graph-visualizer-groups" | Those folders were deleted by `0394b64`. `prototypes/AGENTS.md:53-55` says the split-rails-first rule no longer applies, but the DEVELOPER_GUIDE is not marked historical | VERIFIED; INFERENCE stale |
| `docs/sorting/README.md:38-39`; `docs/sorting/AGENTS.md:66-68` | Domain fixes are "mirrored into the split-rails prototype" | Same deletion | INFERENCE stale |
| Tree backlog item 1 | "share ... by copy. A workspace package would remove four copies" | TP-21: "nothing of it is forked here"; the groups shell is one copy in `src/shared` since 2026-10-18. Sorting's guide says the other shell files are still one copy each (`docs/sorting/DEVELOPER_GUIDE.md:151-153`) | INFERENCE: partly stale. **QUESTION** |
| Sorting backlog item 13 | "Split rails and docks still put Study's pane grid in the region's auto row" | Those builds are gone (`0394b64`) | INFERENCE: obsolete |
| Tree status table, DD-23 row (`docs/tree/DESIGN_DECISIONS.md:20`); TP-04, TP-10 | Speak of "split rails" as a current build | Same deletion | INFERENCE: historical wording |
| `docs/sorting/AGENTS.md:140-143` and `148-150` | The bullet "A control that is not implemented is disabled, never inert" appears twice, in two versions | Read both | VERIFIED |

## 10. Questions for Bao

1. Are `BJoozz <123baoek31@gmail.com>` and `BJoozz <83776047+BJoozz@users.noreply.github.com>` both you?
2. Whose words are V10 choices 27-45? They are quoted in English and were added by Kerk's commits `ae63a62`, `c59c155` and `3c79d36`; PR #19 by kerktaiheng calls them "The owner's six fixes". The answer decides the "owner" in DD-52, DD-57, DD-58, DD-59, TP-23, TP-28, TP-29, SP-14, SP-19 and SP-20.
3. "The owner's commit of 2026-10-21" (DD-24, SP-01) is Kerk's `a074f50`, pushed straight to `main`. Is "the owner" Kerk there, or did you direct that change?
4. Whose decision was "V10 wins and everything else goes" (Kerk's `0394b64`, 2026-10-18)? Who set "One fix, one place", which first appears in the same commit?
5. "Docs describe the current state", "the owner decides rules" and "proportionate tests" are not written in the repository. Where and when did you give them, and may the report cite them as your working rules?
6. The three `docs/*/AGENTS.md` files are marked "Historical". Do their rules still bind the one app, beyond the parts `prototypes/AGENTS.md` says no longer apply (the doc-update rule above all)?
7. DD-38 and DD-39 say the Bellman-Ford and Prim designs are Codex's and not reviewed by the owner. Is that still true? How should the report credit that work? (Those commits carry no AI trailer, but the records name Codex.)
8. For records that name no person (DD-23, DD-28, DD-30 to DD-33, TP-01, TP-07 to TP-09, SP-02 to SP-06, SP-08, SP-09, and the first form of DD-27): were they your decisions, agent choices you accepted, or both?
9. Who answered the sorting questions U5, U7, U8 and U9?
10. Should the stale items in section 9 be fixed before the report quotes the docs, or quoted as they stand?

## 11. Method (to reproduce)

- Headings: `grep -n '^#' prototypes/docs/{graph,tree,sorting}/DESIGN_DECISIONS.md`.
- First 12 lines of each record: an `awk` pass printing lines 1-12 after each `## ` heading, into a scratch file read in parts.
- Per-record dates, files and owner mentions: an `awk` pass that collects `2026-MM-DD`, back-ticked names with an extension, and lines containing "owner".
- First commit per record: `git log --reverse -p --format='@@C %h %ad %an' -- '*DESIGN_DECISIONS.md'`, keeping the first `+## ID:` line for each id.
- Choice rows: `git blame -L 45,90 design/proposals/viz-shell-v10/README.md`.
- AI trailers: `git log --no-merges --format='%h%x09%an%x09%(trailers:key=Co-Authored-By,valueonly)' -- '*DESIGN_DECISIONS.md'`.
- Files gone: each named basename checked against `git ls-files` at `662e7b3`.
- Rule texts: `git grep -n -i` over `*.md` for each rule's wording; `git log -S'<phrase>' --reverse` for the commit that first wrote it.
- Scratch files (records index, first-commit table, trailers) are in `C:/Users/123ba/AppData/Local/Temp/claude/c--Users-123ba-nuss-OneDrive---National-University-of-Singapore-workplace-vstudio-learn-code-visualgo-plus-design/dd1448ed-3ceb-4759-a934-c360d565fa8f/scratchpad/fyp/work04/`.

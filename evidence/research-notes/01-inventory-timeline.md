# 01 - Repository inventory and timeline (visualgo-plus-design)

Repository: `kerktaiheng/visualgo-plus-design` (private on GitHub), local clone on `main` at `662e7b3` (2026-10-31). Audit made on 2026-11-01.

**How this note was made.** Read-only commands only: `git log / show / ls-tree / diff / blame / cherry / merge-base`, and read-only GitHub API calls (`gh api`). Nothing was written inside the repository, the four clones or the two worktrees. **No tests were run** for this note (an inventory needs none).

**Labels.** VERIFIED = seen in git objects, a diff, a log or a GitHub API answer. DOCUMENTED = a commit message, PR body or doc says it (not checked against code). INFERENCE = my reading. QUESTION = Bao must answer.

**Dates.** Commit dates are the author's local time as recorded (+0800 or +0700). PR merge times from the GitHub API are UTC, so a PR can look one day earlier than its merge commit (PR #1: `2026-09-20T19:40Z` = `2026-09-21 03:40 +0800`).

## 1. Key facts

| # | Fact | Label |
| --- | --- | --- |
| 1 | Kerk created the GitHub repository on 2026-09-03 (API `created_at` 03:39Z) and made the first commit `634b5be` the same day. | VERIFIED |
| 2 | `main` has 267 commits. Bao: 246 = 213 own commits + 33 merges. Kerk: 21 = 17 own commits + 4 merges. | VERIFIED |
| 3 | Identities: `BJoozz <123baoek31@gmail.com>` = 216 commits (213 own + 3 merges); `BJoozz <83776047+BJoozz@users.noreply.github.com>` = 30 commits, all GitHub PR merge commits; `Kerk Tai Heng <taihengkerk@gmail.com>` = 17; `kerktaiheng <42596694+kerktaiheng@users.noreply.github.com>` = 4 PR merge commits. | VERIFIED (that both BJoozz identities are Bao's: QUESTION) |
| 4 | Bao's first commit is `986deba` (2026-09-13 22:40 +0800): it adds two git submodules. It reached `main` through PR #1. | VERIFIED |
| 5 | Bao has **write** permission on the origin repository (not admin); all his PR branches except #5's lived in Kerk's repository. | VERIFIED (API `collaborators/BJoozz/permission` = write) |
| 6 | 37 PRs: 36 merged, 1 closed without merge (#5). Bao opened 33 (#1-#17, #22-#37), Kerk 4 (#18-#21). Bao merged 31; Kerk merged 5 (#17, which is Bao's, and his own #18-#21). | VERIFIED (API `merged_by`) |
| 7 | No PR has a review, a review comment or a comment, and the repository has no issues. | VERIFIED (API, 2026-11-01) |
| 8 | Submodule era: 2026-09-13 to 2026-10-18. Three submodules, all pointing at Bao's own GitHub repositories; their pins never moved. | VERIFIED |
| 9 | Three generations of app folders: V2 "split rails" and V7 "docks" prototypes (from 2026-09-20), V2/V7 websites (2026-09-28), V10 "groups" copies (2026-10-17). Kerk's `0394b64` (PR #20, 2026-10-18) deleted all but V10 and turned V10 into one app in `prototypes/`. | VERIFIED |
| 10 | 90 of Bao's commits reached `main` with no merge commit (2026-09-29 to 2026-10-15); GitHub recorded 29 of them as PR #6. From PR #7 (2026-10-14 UTC) on, all of Bao's work came by PR. Kerk pushed 4 commits straight to `main` on 2026-10-19 to 2026-10-22. | VERIFIED |
| 11 | Not merged: `origin/bj/engine-v2-experiment` (4 commits) and the local `bj/engine-package-spike` (1 more), all inside `wasm-arch/`. The one "extra" commit of `bj/viz-shell-v10` is already in `main` under another hash. | VERIFIED |
| 12 | Bao's fork `BJoozz/visualgo-plus-design` holds 7 branches; each has the same commit as the same-named branch on origin. | VERIFIED |

## 2. Creation and the first commits (Kerk, 2026-09-03 to 2026-09-14)

All VERIFIED from `git show --stat` (sizes are git's shortstat; the trailer column is the `Co-Authored-By` line in the message).

| Commit | Date (+0800) | Size | What it holds | AI trailer |
| --- | --- | --- | --- | --- |
| `634b5be` | 09-03 11:46 | 388 files, +8,593 | "init": the VisuAlgo design system in `design/design-system/` (component `.jsx` / `.d.ts` / `.prompt.md` files, guideline cards, tokens, two UI kits, `ui_kits/test-mode/` and `ui_kits/visualgo-web/` (with `HomeScreen.jsx`), fonts, icons, a 3,684-line `_ds_bundle.js`), plus Windows `Zone.Identifier` files | none |
| `b3e86ba` | 09-03 23:11 | 57 files, +6,099 | Graph RPC prototype at the repository root: protobuf messages, a C++20 engine compiled to WASM (the message lists BFS, DFS, Dijkstra, Kruskal, Edmonds-Karp, Kahn, CC/SCC, red-black insert), a Vite page, Node tests, Docker, CI and Pages workflows | Claude Fable 5.1 |
| `8a59115` | 09-04 11:48 | 58 files, +40 -31 | moves the engine prototype into `wasm-arch/` (renames) | Claude Fable 5.1 |
| `e396e06` | 09-04 12:29 | 35 files, +1,848 -118 | array message type and a Python engine that traces unmodified sorts (`sys.settrace`), run in the browser through Pyodide | Claude Fable 5.1 |
| `69aa8e4` | 09-04 13:36 | 3 files, +1,455 | "wireframs": `design/wireframes/` - wireframe 1, its user flow, and "wireframe 2 viz desktop" with nine layouts V1-V9; **V2 = "Split rails", V7 = "Docks, draggable"** | none |
| `aa541a1` | 09-04 13:55 | 29 files, +878 -89 | one log stream across C++, Python, workers and page (`wasm-arch/`) | Claude Fable 5.1 |
| `598193b` | 09-13 21:32 | 205 files, +35 -14 | deletes the `Zone.Identifier` files, adds `.vscode/settings.json` (the next commit says it also moved `wasm-arch/scripts` by mistake) | none |
| `df99dac` | 09-14 13:03 | 8 files, +8 -8 | moves `wasm-arch/scripts` back; bumps the GitHub Actions versions | Claude Opus 5 |

- VERIFIED: before Bao's work, `main` (`df99dac`) tracked 279 files: `design/` 197, `wasm-arch/` 78, plus `.github`, `.gitignore`, `.vscode`. There was no `prototypes/` folder.
- VERIFIED: on `main`, `wasm-arch/` was only ever changed by Kerk (last change `df99dac`, 2026-09-14). VERIFIED: `prototypes/src` has no reference to the engine (grep for `wasm-arch`, `@vgp`, `graph.v1`, `RpcPeer`: 0 hits). Its only link to the app is the Pages job, which builds the engine demo at `/engine/` (`.github/workflows/pages.yml`).
- DOCUMENTED: `design/design-system/readme.md` says it was "read from source code" of `kerktaiheng/visualgo` (a fork of `stevenhalim/visualgo`), commit `bd1756cd1d7b`.
- VERIFIED: the layouts Bao later built (V2, V7) are named frames in Kerk's wireframe 2. DOCUMENTED: `0073875` says the graph prototypes were built "from design/wireframes/wireframe 2 viz desktop.html".
- DOCUMENTED: `87db4a3` calls the website "Kerk's recreation of visualgo.net", and `design/proposals/visualgo-web-site/README.md` says "Kerk's UI kit is a click-through recreation of visualgo.net" (line 59) and sets the goal "a visitor lands on Kerk's homepage" (line 16). VERIFIED: the homepage today says the site is "by Kerk and Bao" (`prototypes/src/site/HomePage.tsx:153`, added in `ae2f31f`).

## 3. Bao joins; the submodule era (2026-09-13 to 2026-10-18)

### 3.1 How Bao's first commit reached main (VERIFIED)

`986deba` (2026-09-13, parent `598193b`) adds `.gitmodules` and two gitlinks on branch `bj/visualization-work`. `4bd9ca9` (2026-09-16) merges `origin/main` (`df99dac`) into that branch. PR #1's branch starts from `4bd9ca9`, so the submodules entered `main` with PR #1's merge `6a621df` (2026-09-20T19:40Z).

### 3.2 The three submodules (VERIFIED)

| Path | URL | Pin (never changed) | Pin in Bao's repo | Added | Reached main | Removed |
| --- | --- | --- | --- | --- | --- | --- |
| `prototypes/graph-visualizer-v2` | github.com/BJoozz/graph-visualizer-v2 | `c8b14e6` | 2026-09-11 "fix: align inspector edge identity and flow filters" | `986deba` 09-13 | PR #1 | `0394b64` 10-18 (Kerk, PR #20) |
| `prototypes/tree-visualizer` | github.com/BJoozz/tree-visualizer | `1477cda` | 2026-09-12 "feat: animate binary lifting initialization by level" | `986deba` 09-13 | PR #1 | `0394b64` |
| `prototypes/sorting-algorithm-visualizer` | github.com/BJoozz/sorting-algorithm-visualizer | `9236a65` | 2026-08-19 "Initial sorting algorithm visualizer" (that repo's only commit) | `e7a44f9` 09-23 | PR #3 | `0394b64` |

- `.gitmodules` history has exactly three commits: `986deba` (created), `e7a44f9` (sorting added), `0394b64` (deleted). The gitlinks are the same at `e7a44f9` and at `0394b64^`. VERIFIED.
- DOCUMENTED (`7b16bf3`): the tree prototypes took tree-visualizer's code at `46ce0a7` (2026-09-17), while the submodule pin stayed at `1477cda`.
- VERIFIED: Bao's earliest repository, `BJoozz/graph-algorithm-visualizer` (55 commits, 2026-07-28 to 2026-08-19 in the clone), was never a submodule. Clone tips: graph-visualizer-v2 `c8b14e6` (2026-09-11), tree-visualizer `46ce0a7` (2026-09-17), sorting `9236a65` (2026-08-19); all commits in the four clones are by the two BJoozz identities.

### 3.3 The prototype folders (VERIFIED)

"Added" = the commit that first added the folder's `package.json` on `main`'s history. Ports from each folder's `vite.config.ts` / `package.json` at `f286712`. All 12 were added by Bao and deleted or moved by Kerk's `0394b64` (2026-10-18, PR #20).

| Folder | Layout | Port | Added | Reached main by | Files at `f286712` |
| --- | --- | --- | --- | --- | --- |
| `graph-visualizer-split-rails` | V2 | 5174 | `0073875` 09-20 | PR #1 | 385 |
| `graph-visualizer-docks` | V7 | 5175 | `0073875` 09-20 | PR #1 | 392 |
| `tree-visualizer-split-rails` | V2 | 5176 | `7b16bf3` 09-22 | PR #2 | 532 |
| `tree-visualizer-docks` | V7 | 5177 | `7b16bf3` 09-22 | PR #2 | 540 |
| `sorting-visualizer-split-rails` | V2 | 5178 | `ee4bb72` 09-25 | PR #3 | 168 |
| `sorting-visualizer-docks` | V7 | 5179 | `ee4bb72` 09-25 | PR #3 | 171 |
| `visualgo-web-split-rails` (site) | V2 | 5181 | `87db4a3` 09-28 | PR #4 | 55 |
| `visualgo-web-docks` (site) | V7 | 5182 | `8aeb543` 09-28 | PR #4 | 55 |
| `graph-visualizer-groups` | V10 | 5183 | `de7b1fe` 10-17 | PR #15 | 402 |
| `tree-visualizer-groups` | V10 | 5184 | `d82a24c` 10-17 | PR #15 | 548 |
| `sorting-visualizer-groups` | V10 | 5185 | `0e3857f` 10-17 | PR #15 | 184 |
| `visualgo-web-groups` (site) | V10 | 5186 | `d445364` 10-17 | PR #15 | 55 |

- VERIFIED: no folder called plain `prototypes/visualgo-web` ever existed on any ref.
- DOCUMENTED (commit messages): the V2/V7 folders began as copies of Bao's standalone repositories (`0073875` "clones of graph-visualizer-v2"; `ee4bb72`/PR #3 "fork its domain code"); `8aeb543` says the V7 site's `src/` and `e2e/` are byte-identical to the V2 site's; the four groups folders are copies of the docks folders (`de7b1fe`, `d82a24c`, `0e3857f`, `d445364`).

### 3.4 Snapshots of main (VERIFIED, `git ls-tree`)

| Commit | Event | Tracked files | Entries in `prototypes/` (* = submodule) |
| --- | --- | --- | --- |
| `df99dac` 09-14 | before Bao | 279 | none |
| `6a621df` 09-21 | PR #1 | 796 | graph-visualizer-v2*, tree-visualizer*, graph split-rails, graph docks |
| `495fa73` 09-23 | PR #2 | 1,579 | + tree split-rails, tree docks |
| `ca56cef` 09-27 | PR #3 | 1,907 | + sorting-algorithm-visualizer*, sorting split-rails, sorting docks |
| `9cc009f` 09-28 | PR #4 | 2,002 | + visualgo-web-split-rails, visualgo-web-docks (11 entries) |
| `ae2f31f` 10-08 | after PR #6 | 2,223 | same 11 |
| `f510477` 10-15 | last direct push | 2,547 | same 11 |
| `c899b69` 10-17 | PR #15 | 3,777 | + the four groups folders (15 entries) |
| `94cdaf3` 10-18 | PR #18 | 3,779 | same 15 (prototypes/ = 3,492 files) |
| `8d7a63a` 10-18 | PR #20 | 1,216 | one app: `src`, `e2e`, `docs`, `scripts`, `public` + config (927 files); no submodules; new root `README.md`, `package.json`, `package-lock.json` |
| `662e7b3` 10-31 | now | 1,355 | same layout (prototypes/ = 1,066 files; `src` = 1,010) |

### 3.5 The end of the era: `0394b64` (Kerk, 2026-10-18 21:37 +0800, PR #20)

- VERIFIED: 3,510 files, +824 -346,532: 2,575 deleted, 924 renamed, 7 added, 4 modified. The renames move the V10 code into `prototypes/src/{site,graph,tree,sorting,shared}` and the docs into `prototypes/docs/{graph,tree,sorting}`; because the docks and groups copies held identical files, git paired many files with the docks copy (for example 372 renames from `tree-visualizer-docks/src`). Added: `.github/workflows/app.yml`, `README.md`, `package.json`, `prototypes/AGENTS.md`, `prototypes/playwright.config.ts`, `prototypes/vite.config.ts`, `prototypes/src/shared/styles/typeScale.test.ts`. Removed: `.gitmodules`, the three gitlinks, `.github/workflows/prototypes.yml`. Trailer: Claude Opus 5.5.
- DOCUMENTED (PR #20 body): "V10 wins; everything else is gone"; npm workspaces run from the root on port 5186; the 40 byte-identical shell files now live once in `src/shared`; "Bao's open branches against the deleted folders will not merge".
- QUESTION: who decided to keep V10 only and delete V2/V7 - Kerk alone, Bao, or both?

## 4. Branches

### 4.1 Every branch on origin (38, plus `origin/HEAD` = `main`)

VERIFIED: the GitHub API branch list of origin equals the local remote-tracking refs (same 38 names, same commits, 2026-11-01). "In main" = `git merge-base --is-ancestor <branch> main`; "direct push" = the branch tip sits on `main`'s first-parent line with no merge commit. Purposes come from the PR titles and commit subjects (DOCUMENTED). All are Bao's except `deploy-v10-pages` (Kerk).

| Branch | Tip | Last commit | PR | In main? | How it landed | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `bj/visualization-work` | `4bd9ca9` | 09-16 | none | yes | base of PR #1 | submodules + merge of main |
| `bj/engine-v2-experiment` | `ffb9274` | 09-17 | none | **no (4 commits)** | - | engine milestones M0-M3 in `wasm-arch/` (4.2) |
| `bj/graph-wireframe-v2-v7` | `75d9760` | 09-21 | #1 | yes | merge `6a621df` | graph V2/V7 prototypes, CI |
| `bj/tree-wireframe-v2-v7` | `1af2c72` | 09-23 | #2 | yes | merge `495fa73` | tree V2/V7 prototypes |
| `bj/sorting-wireframe-v2-v7` | `4a8f1f2` | 09-27 | #3 | yes | merge `ca56cef` | sorting V2/V7 + sorting submodule |
| `bj/visualgo-web-site` | `ad20f0d` | 09-28 | #4 | yes | merge `9cc009f` | V2/V7 websites |
| `bj/visualgo-web-editors` | `ae2f31f` | 10-08 | #6 | yes | fast-forward (API: "merge commit" = PR head `b0d099b`; `ae2f31f` pushed after) | Graph/Tree Editor cards, Bellman-Ford, Prim, LCA table |
| `bj/segment-tree-lazy` | `a521c13` | 10-09 | none | yes | direct push (4 commits) | lazy segment tree, tree e-Lectures |
| `bj/bst-avl-operations` | `c620145` | 10-10 | none | yes | direct push (7) | BST/AVL operations and decks |
| `bj/uiux-pass-1` | `c3f6508` | 10-15 | none | yes | direct push (44) | Play replaces Go, canvas controls, paused motion, step merges, see-through legend |
| `bj/dock-drop-zones` | `f510477` | 10-15 | none | yes | direct push (2) | V7 dock drop zones |
| `bj/fix-traversal-ci` | `3a6443b` | 10-15 | #7 | yes | merge `fb0b6a9` | tree traversal CI test across fonts |
| `bj/sssp-end-node` | `b596101` | 10-15 | #8, #9 | yes | merges `240b688`, `504fcab` | End node for BFS/Dijkstra/Bellman-Ford |
| `bj/live-layout-off` | `6b953d5` | 10-15 | #10 | yes | merge `6470083` | Live force layout starts off |
| `bj/footer-centre-transport` | `d6ce97b` | 10-16 | #11 | yes | merge `36086f3` | centred footer transport |
| `bj/final-frame-motion` | `fced77a` | 10-16 | #12 | yes | merge `420c202` | last frame keeps moving (DD-47) |
| `bj/visualgo-samples` | `32de95c` | 10-16 | #13 | yes | merge `8bb2720` | visualgo.net's sample graphs |
| `bj/node-label-fit` | `96f85e2` | 10-16 | #14 | yes | merge `acbf138` | node label sizes |
| `bj/viz-shell-v10` | `46234cd` | 10-17 | #15 | yes, but 1 commit not by hash | merge `c899b69` | V10 panel-groups layout |
| `bj/faint-scrollbars-trim-hints` | `867b428` | 10-17 | #16 | yes | merge `f286712` | faint scrollbars, fewer hints, bigger board |
| `bj/v10-review-fixes` | `b8f1c1a` | 10-18 | #17 | yes | merge `b9ec8fa` **by Kerk** | V10 shell review fixes |
| `deploy-v10-pages` (Kerk) | `c39b3cf` | 10-18 | #18 | yes | merge `94cdaf3` | Pages: V10 site at root, engine at `/engine/` |
| `bj/tree-centre-edges` | `1119740` | 10-19 | #22 | yes | merge `15c0cc7` | tree edges centre to centre (TP-30) |
| `bj/lca-two-runs` | `409a200` | 10-19 | #23 (into `bj/tree-centre-edges`) | yes | `1119740`, then `15c0cc7` | LCA Preprocessing/Query runs (TP-31) |
| `bj/lca-hover-ancestors` | `60ccc44` | 10-20 | #24 | yes | merge `48e58d9` | LCA hover ancestors (TP-32) |
| `bj/heap-operations` | `908f8a3` | 10-21 | #25 | yes | merge `e267352` | Binary Heap, Min/Max (TP-33) |
| `bj/heap-rename-ids` | `3fec43c` | 10-21 | #26 | yes | merge `a436873` | heap extract naming |
| `bj/heap-value-rule` | `ea37326` | 10-21 | #27 | yes | merge `7380025` | heap value rule |
| `bj/graph-traversal-ts-bgc-cvb` | `0fc105c` | 10-22 | #28 | yes | merge `4621b1f` | Topological Sort, Bipartite Check, Cut Vertex and Bridge |
| `bj/step-notes` | `a1a6f28` | 10-25 | #29, #31 | yes | merges `eb4c4d8`, `163688c` | tree step notes |
| `bj/step-notes-2` | `1df8a0c` | 10-25 | #30 (into `bj/step-notes`) | yes | `a1a6f28`, then `163688c` | step notes for BST/AVL/heap (TP-36) |
| `bj/dijkstra-step-notes` | `b309309` | 10-25 | #32 | yes | merge `b5506e9` | Dijkstra relax notes (DD-61) |
| `bj/legend-trim` | `1671990` | 10-26 | #33 | yes | merge `c984e63` | smaller canvas legend |
| `bj/review-session-1` | `a5bb08f` | 10-28 | #34 | yes | merge `ad5e119` | tooling review findings |
| `bj/tab-strip-reveal` | `fd9ff5c` | 10-29 | #35 | yes | merge `4dedee1` | tab strip keeps its tab in view |
| `bj/docs-graph-sorting` | `876ed0d` | 10-30 | #36 | yes | merge `f58ed5f` | docs paths; shell copy rule retired |
| `bj/review-session-3` | `6fa4981` | 10-30 | #37 | yes | merge `662e7b3` | playback review findings |
| `main` | `662e7b3` | 10-31 | - | - | - | - |

- VERIFIED: Kerk's PR branches `v10-owner-fixes` (#19), `v10-single-app` (#20) and `v10-polish` (#21) are no longer on origin; their commits are in `main`. INFERENCE: deleted after merging.

### 4.2 Unmerged work and what is unique in it

**(a) `origin/bj/engine-v2-experiment`** - base `4bd9ca9`; 4 commits, 48 files, +4,312 -179, all under `wasm-arch/`. VERIFIED: `git cherry main` marks all 4 "+" (no equivalent patch in `main`).

| Commit | Date (+0800) | Subject | Size | Trailer |
| --- | --- | --- | --- | --- |
| `478174f` | 09-17 01:12 | feat(engine): add stable edge identity across runtime and playback | 25 files, +717 -125 | none (one-line message) |
| `e348a6d` | 09-17 05:38 | refactor(engine): extract reusable browser engine client | 15 files, +657 -54 | Claude Opus 5 (1M context) |
| `ee65bef` | 09-17 12:21 | test(engine): dispatch a Node-safe error event in the client worker test | 1 file, +2 -1 | Claude Fable 5.1 |
| `ffb9274` | 09-17 12:21 | feat(engine): add experimental Kerk BFS runtime | 15 files, +2,939 -2 | Claude Fable 5.1 |

- DOCUMENTED (messages and `wasm-arch/docs/KERK_BFS_RUNTIME.md`, `EDGE_IDENTITY.md` on the branch): milestones M0 baseline, M1 stable edge ids, M2 `GraphEngineClient`, M3 `KerkBfsRuntime` - "an experimental backend" that lets a Graph V2-style host run BFS on Kerk's C++ engine with its own string ids. The messages report Docker test runs (e.g. "125 Node + 9 Python tests"); I did not re-run them. VERIFIED: `EDGE_IDENTITY.md` is partly written in Vietnamese.
- INFERENCE: nothing from this branch is used by the app (no engine reference in `prototypes/src`, see section 2).

**(b) `bj/viz-shell-v10`'s extra commit `46234cd`** (2026-10-17 22:12 +0700, "Draw every scrollbar thin and faint until the pointer is in the area it scrolls"). VERIFIED: `git cherry` marks it "-": the same patch is in `main` as `9bf60f6` (same author time), the first commit of PR #16. Nothing unique.

**(c) local `bj/engine-package-spike` `053064f`** (2026-09-17 13:09 +0800), a child of `ffb9274`: "wip(package): M4a packaging spike for @visualgo/kerk-bfs-runtime", 23 files, +681 -179 in `wasm-arch/` (`package/`, `examples/package-consumer/`, `docs/PACKAGE.md`, `web/src/runtime/types.ts`, a package-surface test). Trailer: Claude Fable 5.1. VERIFIED: never pushed (not on origin, not on the fork). The message reports "130 Node + 9 Python tests" in Docker (DOCUMENTED, not re-run).

**Worktrees.** VERIFIED: both worktrees' folders hold **0 files on disk** (`git status` lists 314 deletions in `visualgo-engine-v2-experiment` and 2,544 in `visualgo-traversal-ci`); the commits are intact in the object store. Local `bj/fix-traversal-ci` = origin's `3a6443b` (merged by PR #7). QUESTION: was there uncommitted work in these worktrees?

### 4.3 Other local-only branches (not in branches.tsv)

| Branch | Tip | Date | Unique content (VERIFIED with `git cherry main`) |
| --- | --- | --- | --- |
| `backup/before-reword-044908` | `d3ab325` | 09-28 | 5 commits; all 5 patches are in `main` (PR #4's commits before their messages were reworded) |
| `bj/bfs-wasm-spike` | `53d2ef4` | 09-17 | 1 unique commit "currently paused": 14 files, +509 -49 in `wasm-arch/` (an engine client). INFERENCE: this is probably the "engine-client spike" that the experiment's `EDGE_IDENTITY.md` says, in Vietnamese, it took no code from. |
| `bj/vercel-spa-routing` | `c9e4598` | 09-29 | 1 unique commit: `vercel.json` in the two V2/V7 sites (+10). It was on the fork's `main` behind PR #5 (section 10). |
| `bj/viz-shell-v10-stage0` | `8d4c15f` | 10-17 | 2 commits; both patches are in `main` |
| `live_prototype` | `4bd9ca9` | 09-16 | same commit as `bj/visualization-work`; in `main` |

## 5. How work reached main

| Route | Bao | Kerk |
| --- | --- | --- |
| Own commits on `main`'s first-parent line (pushed straight to `main` or fast-forwarded) | 90 (2026-09-29 to 2026-10-15) | 12 (8 from 09-03 to 09-14, before any PR; 4 from 10-19 to 10-22) |
| Own commits brought in by a merge commit | 123 | 5 (PRs #18-#21) |
| Merge commits made | 33 (30 GitHub PR merge commits + 3 merges of `main` into his branches: `4bd9ca9`, `876ed0d`, `6fa4981`); PR #6 was merged with no merge commit | 4 (#17, #18, #20, #21) |

All VERIFIED. The 90 direct commits of Bao, in order: 3 on 2026-09-29 (`6fc6150`..`65766cc`; already on origin `main` by 2026-09-29 12:51Z, because the fork's sync merge `4179c7e` has `65766cc` as a parent); 29 that GitHub records as PR #6 (`65766cc..b0d099b`, merged_by BJoozz 2026-10-08T04:08Z with no merge commit); then `ae2f31f` and 57 more up to `f510477` (2026-10-15 07:00 +0800) - the branches `bj/segment-tree-lazy`, `bj/bst-avl-operations`, `bj/uiux-pass-1`, `bj/dock-drop-zones`. INFERENCE: fast-forward pushes of those branches to `main`. QUESTION: Bao to confirm these were pushed to `main` without a PR or review.

Stacked PRs (VERIFIED from merge parents and API bases): #23 into `bj/tree-centre-edges`, then #22 to `main`; #30 into `bj/step-notes` after #29 had merged, then #31 to `main`; #19's commit `ae63a62` came in with #20 (API: #19 merged 15:19:58Z, #20 15:19:56Z); #21 was stacked on #20 (DOCUMENTED in its body); #10 had 4 commits on GitHub but only 1 beyond #9.

## 6. Timeline of main

Counts are VERIFIED from `git log main` by author date (local time). "Commits" = own (non-merge) commits; merges are counted apart. The "what happened" text is from commit subjects and PR titles (DOCUMENTED).

### 6.1 Month by month

| Month | Bao commits | Bao merges | Kerk commits | Kerk merges | PRs merged | Main events |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09 | 46 | 5 | 8 | 0 | #1-#4 | Kerk: repository, design system, engine prototype, wireframes (09-03/04). Bao: submodules (09-13), graph, tree and sorting V2/V7 prototypes, V2/V7 websites (09-20 to 09-28); fork created; PR #5 opened (09-29). |
| 2026-10 | 167 | 28 | 9 | 4 | #6-#37 (not #5) | Bao: Graph/Tree editors, Bellman-Ford, Prim, LCA table, lazy segment tree, BST/AVL operations, UI/UX pass, V10 groups; then the unified app's features and reviews. Kerk: V10 deploy and one-app consolidation (10-18), footer/landing tweaks (10-19 to 10-22). |
| 2026-11 (to 11-01) | 0 | 0 | 0 | 0 | - | none |

### 6.2 Week by week (Monday to Sunday)

| Week | Bao commits (+merges) | Kerk commits (+merges) | What happened |
| --- | --- | --- | --- |
| 08-31 to 09-06 | 0 | 6 | Repository created; `634b5be` design system; `b3e86ba` engine RPC prototype; `8a59115` move to `wasm-arch/`; `e396e06` Python array engine; `69aa8e4` wireframes; `aa541a1` logging |
| 09-07 to 09-13 | 1 | 1 | Kerk `598193b` removes Zone.Identifier files; Bao's first commit `986deba` (graph and tree submodules), on a branch |
| 09-14 to 09-20 | 3 (+1) | 1 | Kerk `df99dac` fixes CI/Pages; Bao merges main into his branch (`4bd9ca9`); engine experiment (09-17, not merged); graph V2/V7 clones `0073875`, `37075b1`, `fab4005` (09-20) |
| 09-21 to 09-27 | 32 (+3) | 0 | PR #1 graph V2/V7 (merge commit 09-21 03:40 +0800, i.e. 09-20 UTC); PR #2 tree V2/V7 (09-23); sorting submodule `e7a44f9`; PR #3 sorting V2/V7 (09-27) |
| 09-28 to 10-04 | 30 (+1) | 0 | PR #4 V2/V7 websites (09-28); fork created; PR #5 opened; direct pushes: Dijkstra distances on nodes, recursive DFS (09-29); Graph and Tree Editor cards (10-01); edge direction waves DD-37 (10-02); Bellman-Ford (10-03/04); Prim begins (10-04) |
| 10-05 to 10-11 | 39 | 0 | Prim done, shorter pseudocode lines (10-05); extra dock panel and LCA ancestor table (10-07); PR #6 fast-forward and homepage credit line `ae2f31f` (10-08); lazy segment tree and tree e-Lectures (10-09); BST/AVL operations (10-09/10); Play replaces Go, canvas controls, Action-panel picker (10-10/11) |
| 10-12 to 10-18 | 69 (+10) | 5 (+4) | Paused-step motion DD-42/TP-17, drag fix DD-43 (10-12); step merges DD-44/TP-18/SP-11 (10-13); see-through legend (10-14); dock drop zones, the last direct push (10-15); PRs #7-#16 incl. #15 V10 groups (10-17); 10-18: #17 (Bao's, merged by Kerk), Kerk's #18 Pages, #19 owner fixes, #20 one app, #21 polish |
| 10-19 to 10-25 | 33 (+10) | 4 | Kerk's direct pushes: hotfix `3c79d36` (10-19), landing tips removed `40a63bd` (10-20), footer stepping/Autoplay `a074f50`, `01a1a4a` (10-21/22). Bao's PRs #22-#31: tree centre edges, LCA two runs and hover, Binary Heap (3 PRs), graph traversal TS/BGC/CVB, step notes |
| 10-26 to 11-01 | 6 (+8) | 0 | PRs #32 Dijkstra notes, #33 legend trim, #34 tooling review, #35 tab strip, #36 docs, #37 playback review; last commit `662e7b3` (10-31 local) |

### 6.3 PR milestones (all 37)

VERIFIED from the GitHub API (merge time UTC, merged_by, commits, additions/deletions as GitHub counts them) and the merge commits on `main`. Author is Bao unless marked **Kerk**. The "what" column is the PR title, shortened (DOCUMENTED).

| PR | Merged (UTC) | Merged by | Merge commit | Commits | +/- (GitHub) | What |
| --- | --- | --- | --- | --- | --- | --- |
| #1 | 09-20 19:40 | BJoozz | `6a621df` | 7 | +65,204 | graph V2/V7 prototypes, two submodules, prototype CI |
| #2 | 09-23 07:06 | BJoozz | `495fa73` | 7 | +75,560 -108 | tree V2/V7; shell fixes in all four apps |
| #3 | 09-27 08:42 | BJoozz | `ca56cef` | 23 | +53,094 | sorting V2/V7 + sorting submodule |
| #4 | 09-28 06:20 | BJoozz | `9cc009f` | 7 | +13,660 -167 | VisuAlgo+ V2 and V7 websites |
| #5 | closed 10-25 10:39, not merged | - | - | 0 now | 0 | from the fork's `main`: "Configure Vercel SPA routing for both websites" |
| #6 | 10-08 04:08 | BJoozz | none (= head `b0d099b`) | 29 | +36,188 -1,755 | "Bj/visualgo web editors" (no body) |
| #7 | 10-14 23:55 | BJoozz | `fb0b6a9` | 1 | +120 -14 | tree traversal CI test across platform fonts |
| #8 | 10-15 01:29 | BJoozz | `240b688` | 1 | +2,688 -44 | End node for BFS, Dijkstra, Bellman-Ford |
| #9 | 10-15 02:38 | BJoozz | `504fcab` | 3 | +42 -108 | End node review follow-up |
| #10 | 10-15 02:47 | BJoozz | `6470083` | 4 | +140 -134 | Live force layout starts off |
| #11 | 10-15 23:43 | BJoozz | `36086f3` | 1 | +364 -262 | centred footer transport |
| #12 | 10-15 23:43 | BJoozz | `420c202` | 2 | +1,722 -74 | finished last frame keeps moving (DD-47) |
| #13 | 10-16 11:33 | BJoozz | `8bb2720` | 3 | +5,427 -1,557 | visualgo.net's sample graphs |
| #14 | 10-17 00:10 | BJoozz | `acbf138` | 2 | +266 -4 | node label fits its node |
| #15 | 10-17 09:34 | BJoozz | `c899b69` | 20 | +170,900 -34 | V10 panel groups: third layout, four new folders |
| #16 | 10-17 16:25 | BJoozz | `f286712` | 4 | +424 -550 | faint scrollbars, fewer hints, larger board |
| #17 | 10-18 10:57 | **kerktaiheng** | `b9ec8fa` | 3 | +2,313 -533 | V10 shell review fixes |
| #18 **Kerk** | 10-18 11:13 | kerktaiheng | `94cdaf3` | 1 | +37 -4 | deploy V10 to GitHub Pages, engine at `/engine/` |
| #19 **Kerk** | 10-18 15:19 | kerktaiheng | via #20 (`ae63a62`) | 1 | +1,367 -792 | V10 fixes, choices 27-32 |
| #20 **Kerk** | 10-18 15:19 | kerktaiheng | `8d7a63a` | 2 | +38,223 -383,356 | keep V10 only: one app in `prototypes/` |
| #21 **Kerk** | 10-18 15:23 | kerktaiheng | `fae8418` | 2 | +1,062 -3,132 | V10 polish, choices 33-41 |
| #22 | 10-19 14:50 | BJoozz | `15c0cc7` | 4 | +1,456 -342 | tree edges centre to centre (TP-30) |
| #23 | 10-19 13:22 | BJoozz | `1119740` (into #22's branch) | 2 | +847 -325 | LCA as two runs (TP-31) |
| #24 | 10-19 17:57 | BJoozz | `48e58d9` | 1 | +909 -15 | LCA hover: path to root, 2^k ancestors (TP-32) |
| #25 | 10-20 19:16 | BJoozz | `e267352` | 8 | +8,933 -587 | Binary Heap: Min/Max, 1-based, operations (TP-33) |
| #26 | 10-20 19:18 | BJoozz | `a436873` | 2 | +257 -246 | heap extract named by its extreme |
| #27 | 10-20 20:02 | BJoozz | `7380025` | 1 | +328 -77 | heap values follow the decimal rule |
| #28 | 10-22 18:32 | BJoozz | `4621b1f` | 3 | +9,085 -158 | Topological Sort, Bipartite Check, Cut Vertex and Bridge |
| #29 | 10-24 17:14 | BJoozz | `eb4c4d8` | 3 | +3,763 -524 | tree step notes (Binary Lifting first) |
| #30 | 10-24 19:51 | BJoozz | `a1a6f28` (into `bj/step-notes`) | 6 | +5,408 -980 | step notes for BST, AVL, heap (TP-36) |
| #31 | 10-24 20:27 | BJoozz | `163688c` | 7 | +5,408 -980 | #30's work onto `main` |
| #32 | 10-26 02:56 | BJoozz | `b5506e9` | 6 | +3,058 -778 | Dijkstra relax notes (DD-61) |
| #33 | 10-26 07:27 | BJoozz | `c984e63` | 2 | +503 -268 | Binary Lifting legend trim, 12px legend |
| #34 | 10-30 14:58 | BJoozz | `ad5e119` | 1 | +38 -11 | tooling: Inter, Node 22.12 floor, flags, CI traces |
| #35 | 10-30 14:59 | BJoozz | `4dedee1` | 1 | +196 -14 | tab strip keeps its front tab in view |
| #36 | 10-30 17:04 | BJoozz | `f58ed5f` | 2 | +681 -508 | graph/sorting docs; shell copy rule retired |
| #37 | 10-30 17:04 | BJoozz | `662e7b3` | 4 | +1,146 -615 | playback: Speed timer, sorting restarts, Autoplay/Next |

Note: GitHub's +/- for #20 differs from git's (`0394b64`: +824 -346,532; VERIFIED both). INFERENCE: GitHub counted many moved files as deleted and re-added, where git's rename detection paired them.

## 7. Kerk's 21 commits on main

Sizes VERIFIED (`git show --shortstat`, folders from `--numstat`); the description is from the diff stat and the message. 17 own commits and 4 GitHub merge commits.

| # | Commit | Date (+0800) | Size | One line from the diff stat | Route | Trailer |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `634b5be` | 09-03 11:46 | 388 files, +8,593 | design system in `design/design-system/` | first commit | none |
| 2 | `b3e86ba` | 09-03 23:11 | 57 files, +6,099 | C++/WASM graph engine, protobuf RPC, web page, tests, Docker, CI and Pages workflows | direct | Fable 5.1 |
| 3 | `8a59115` | 09-04 11:48 | 58 files, +40 -31 | engine moved into `wasm-arch/` | direct | Fable 5.1 |
| 4 | `e396e06` | 09-04 12:29 | 35 files, +1,848 -118 | array protobuf + Python tracing engine (`wasm-arch/pyengine`) | direct | Fable 5.1 |
| 5 | `69aa8e4` | 09-04 13:36 | 3 files, +1,455 | three wireframe HTML files in `design/wireframes/` | direct | none |
| 6 | `aa541a1` | 09-04 13:55 | 29 files, +878 -89 | logging across the engine chain (`wasm-arch/`) | direct | Fable 5.1 |
| 7 | `598193b` | 09-13 21:32 | 205 files, +35 -14 | `Zone.Identifier` files deleted; `.vscode/settings.json` | direct | none |
| 8 | `df99dac` | 09-14 13:03 | 8 files, +8 -8 | `wasm-arch/scripts` restored; 2 workflow files | direct | Opus 5 |
| 9 | `b9ec8fa` | 10-18 18:57 | merge (Bao's content: 35 files, +2,313 -533) | merges Bao's PR #17 | GitHub merge | - |
| 10 | `c39b3cf` | 10-18 18:58 | 1 file, +37 -4 | `.github/workflows/pages.yml`: V10 site at the Pages root, engine at `/engine/` | PR #18 | Opus 5.5 |
| 11 | `94cdaf3` | 10-18 19:13 | merge, 1 file | merges PR #18 | GitHub merge | - |
| 12 | `ae63a62` | 10-18 20:33 | 149 files, +1,367 -792 | the three `*-groups` copies' `src`, `e2e`, `docs` + V10 proposal: "owner's" choices 27-32 | PR #19 | Opus 5.5 |
| 13 | `0394b64` | 10-18 21:37 | 3,510 files, +824 -346,532 | deletes V2/V7 folders, sites and submodules; moves V10 into one app; root workspace, `app.yml` CI (section 3.5) | PR #20 | Opus 5.5 |
| 14 | `c59c155` | 10-18 23:08 | 100 files, +1,039 -3,015 | `prototypes/src/{tree,graph,sorting,shared,site}`, graph docs, 2 design-system files: one font, one control look, dead code removed | PR #21 | Opus 5.5 |
| 15 | `5235fcf` | 10-18 23:19 | 6 files, +23 -117 | Settings menu item styles in `src/shared` | PR #21 | Opus 5.5 |
| 16 | `8d7a63a` | 10-18 23:19 | merge (3,508 files) | merges PR #20 (and so #19) | GitHub merge | - |
| 17 | `fae8418` | 10-18 23:23 | merge (105 files) | merges PR #21 | GitHub merge | - |
| 18 | `3c79d36` | 10-19 00:07 | 41 files, +139 -338 | LCA indentation, Save image removed, Full screen and Shortcuts moved to the top bar, longer speed slider ("owner's choices 42 to 45") | direct push | Opus 5.5 |
| 19 | `40a63bd` | 10-20 15:36 | 6 files, +12 -35 | tips removed from the landing page (`src/site`, 2 e2e specs) | direct push | Opus 5.5 |
| 20 | `a074f50` | 10-21 23:32 | 17 files, +212 -75 | footer: stepping first, Play becomes Autoplay beside Stop, e-Lecture nav pinned | direct push | Opus 5.5 |
| 21 | `01a1a4a` | 10-22 00:31 | 16 files, +235 -253 | Autoplay/Stop as green and red chips; step buttons one size | direct push | Opus 5.5 |

- VERIFIED: the V10 proposal's choice rows 27-48 (`design/proposals/viz-shell-v10/README.md`, lines 72-93) were written in Kerk's commits (`ae63a62`, `c59c155`, `3c79d36`, `a074f50`, `01a1a4a`); rows 1-26 were written in Bao's commits (rows 24-26 in `c0166f2`, PR #17). VERIFIED: where rows 1-26 quote the owner, the quotes are Vietnamese with an English translation ("Quoted words are the owner's; the English after them is a translation", line 41); rows 27-48 quote informal English directly.
- QUESTION: who is "the owner" in Kerk's commits and PRs of 2026-10-18 to 2026-10-22 (choices 27-48; `40a63bd` "The owner's request, 2026-10-20")? Note also that Bao's own PR #37 calls `a074f50` "The owner's commit". INFERENCE (to confirm, not to assume): the English quotes may be Kerk's own requests.

## 8. AI-assistance facts (no judgement)

- VERIFIED: 213 of the 230 own commits on `main` carry a `Co-Authored-By: Claude ...` trailer: Bao 199 of 213, Kerk 14 of 17. No merge commit carries one.

| Trailer name | Bao | Kerk |
| --- | --- | --- |
| Claude Fable 5.1 | 91 | 4 |
| Claude Opus 5.5 | 73 | 9 |
| Claude Opus 5 (1M context) | 30 | 0 |
| Claude Opus 5 | 4 | 1 |
| Claude Fable 5 | 1 | 0 |

- VERIFIED: own commits without a trailer - Bao (14): `986deba`, `c458755`, `75d9760`, `1af2c72`, `e7a44f9`, `aef5d0b`, `0aac567`, `6417767`, `4bd0879`, `5428ed3`, `686c06b`, `65634cf`, `490e1d1`, `3a6443b`; Kerk (3): `634b5be`, `69aa8e4`, `598193b`. INFERENCE: a missing trailer does not show that no AI tool was used.
- DOCUMENTED: 30 of the 37 PR bodies contain the line "Generated with [Claude Code]". 8 commit messages on `main` and 3 PR bodies mention reviews or research by Codex. QUESTION: how Bao wants the report to describe the tools (Claude Code, Codex) and his own role in each change.
- VERIFIED: three of the four unmerged engine commits and the local spike commit carry trailers (section 4.2).

## 9. Lines changed per author (a crude measure, context only)

**Read this first.** Line counts do not measure effort, design or quality. In this repository they are inflated by copies: until 2026-10-18 most changes were made in two or three copies of each app (DOCUMENTED, e.g. PR #17: the shell fix "copied byte for byte into the tree and sorting copies"; PR #19: each fix "carried into the tree and sorting copies"), the big folder-copy commits count whole apps again, and lines Bao brought from his own earlier repositories count as added here. Most commits are AI-assisted (section 8). Kerk's large deletion count is one consolidation commit.

**Method (VERIFIED, my own run on 2026-11-01).** `git log main --no-merges --numstat` with rename detection (git 2.50 default), summed by a small Python script. Excluded: `package-lock.json`, `yarn.lock`, `node_modules/`, the generated `_ds_bundle.js`, profiler output `*-profile.json`, minified files, `dist/`/`build/`. Binary files have no line counts (not counted: 1,147 binary file-changes in Bao's commits, 646 in Kerk's).

### 9.1 Numstat totals

| Variant | Bao added | Bao deleted | Kerk added | Kerk deleted |
| --- | --- | --- | --- | --- |
| A. All own commits on `main` (Bao 213, Kerk 17) | 517,278 | 35,601 | 18,195 | 321,081 |
| B. A without the 8 folder-copy commits (`0073875`, `7b16bf3`, `ee4bb72`, `8aeb543`, `de7b1fe`, `d82a24c`, `0e3857f`, `d445364`) and Kerk's consolidation `0394b64` | 189,517 | 35,571 | 17,619 | 4,882 |
| C. Unified-app era only: the 45 commits after `0394b64` (Bao 39, Kerk 6) | 36,215 | 5,752 | 1,660 | 3,826 |

Excluded lines, for the record: Bao `package-lock.json` +24,060 and profiler JSON +8,289; Kerk `_ds_bundle.js` +3,684, `yarn.lock` +717, `package-lock.json` +248 -22,051, profiler JSON -8,289.

Variant A by area (VERIFIED):

| Area | Bao | Kerk |
| --- | --- | --- |
| old prototype folders (`prototypes/<name>/`, before 10-18) | +475,480 -29,199 | +1,354 -316,656 |
| unified app `prototypes/src` | +26,369 -3,453 | +1,670 -3,811 |
| unified app `prototypes/e2e` | +3,425 -242 | +67 -134 |
| unified app `prototypes/docs` | +6,392 -2,039 | +136 -20 |
| `prototypes/` config and scripts | +27 -14 | +194 -18 |
| `design/` | +5,417 -638 | +6,408 -10 |
| `wasm-arch/` | 0 | +2,796 -223 |
| repository root files (for Kerk mostly `b3e86ba`'s engine code before `8a59115` moved it into `wasm-arch/`) | +17 -4 | +5,360 -39 |
| `.github/` | +151 -12 | +210 -170 |

### 9.2 Lines in today's tree, by last author (`git blame -w` at `662e7b3`)

Method (VERIFIED, my own run): blame of 1,292 text files (59 binary files skipped; lockfiles, `_ds_bundle.js` and profiler JSON excluded). Blame follows whole-file renames, so code moved by `0394b64` keeps its earlier author. It shows who last changed a line, not who designed it; Bao's lines include code first written in his standalone repositories.

| Area at `662e7b3` | Bao | Kerk |
| --- | --- | --- |
| `prototypes/src/tree` | 61,710 | 527 |
| `prototypes/src/graph` | 46,521 | 574 |
| `prototypes/src/sorting` | 18,268 | 218 |
| `prototypes/src/shared` | 8,932 | 634 |
| `prototypes/src/site` | 1,898 | 56 |
| `prototypes/src` other (`index.css`, `main.tsx`) | 594 | 50 |
| `prototypes/e2e` | 5,235 | 71 |
| `prototypes/docs` | 13,442 | 305 |
| `prototypes/` config and scripts | 310 | 185 |
| **all of `prototypes/` (the app)** | **156,910** | **2,620** |
| `design/` (Bao: proposals 4,622, the V10/V11 frames added to Kerk's wireframe 2: 150, design-system `TopBar` 11; Kerk: design system, wireframes) | 4,783 | 6,394 |
| `wasm-arch/` | 0 | 7,862 |
| `.github/` | 0 | 179 |
| root files | 5 | 40 |
| **total** | **161,698** | **17,095** |


## 10. The BJoozz fork (`BJoozz/visualgo-plus-design`)

- VERIFIED (API): a private fork of `kerktaiheng/visualgo-plus-design`, created 2026-09-28T06:27Z; last push 2026-11-01T14:53Z.
- VERIFIED: its 7 branches all point at the same commits as the same-named branches on origin, and GitHub's compare of `kerktaiheng:main...BJoozz:main` says "identical" (ahead 0, behind 0).

| Fork branch | Commit | Same on origin? |
| --- | --- | --- |
| `bj/engine-v2-experiment` | `ffb9274` | yes |
| `bj/graph-wireframe-v2-v7` | `75d9760` | yes |
| `bj/sorting-wireframe-v2-v7` | `4a8f1f2` | yes |
| `bj/tree-wireframe-v2-v7` | `1af2c72` | yes |
| `bj/visualgo-web-site` | `ad20f0d` | yes |
| `bj/visualization-work` | `4bd9ca9` | yes |
| `main` | `662e7b3` | yes |

- VERIFIED (events and commits API): the fork's `main` used to differ. It carried GitHub "Sync fork" merges ("Merge branch 'kerktaiheng:main' into main": `4179c7e` 09-29, `e3c56bf` and `c31fe29` 10-08, `ab20022` 10-15, `14f1f70`, `0f00e33`, `822ea8a` 10-17) and two Vercel commits: `c9e4598` (2026-09-28T22:09Z, `vercel.json` in the V2/V7 sites; also kept on the local branch `bj/vercel-spa-routing`) and `03bfaa3` (2026-10-17, "chore: add Vercel SPA routing for V10", `vercel.json` in `visualgo-web-groups`). PR #5 (fork `main` to origin `main`) was opened 2026-09-29T03:09Z. On 2026-10-25T10:39:43Z the fork's `main` was pushed to `163688c` (origin `main` at that time) and PR #5 closed one second later, unmerged.
- INFERENCE: resetting the fork's `main` to origin's emptied PR #5, so GitHub closed it; the Vercel commits are now on no fork branch (`03bfaa3` is not in the local object store either). VERIFIED: no `vercel.json` was ever in origin `main`'s history.
- The 2026-11-01 push is not yet in the events feed; INFERENCE: it moved the fork's `main` from `163688c` to `662e7b3` (a sync). QUESTION.
- DOCUMENTED (`README.md`): the app is deployed to GitHub Pages from origin `main` at https://kerktaiheng.github.io/visualgo-plus-design/ (not checked live). QUESTION: was there a Vercel deployment from the fork, and is it still live?

## 11. Questions for Bao

1. Are both `BJoozz <123baoek31@gmail.com>` and `BJoozz <83776047+BJoozz@users.noreply.github.com>` yours? (The noreply one appears only on the 30 GitHub PR merges.)
2. Who is "the owner" in Kerk's commits and PRs of 2026-10-18 to 2026-10-22 (V10 choices 27-48, `40a63bd`'s "owner's request")? Your PR #37 calls Kerk's `a074f50` "the owner's commit".
3. Who decided "V10 wins" and the deletion of the V2/V7 folders, sites and submodules (Kerk's PR #20)?
4. Were the 90 commits of 2026-09-29 to 2026-10-15 pushed straight to `main` (fast-forward) without review? GitHub shows no reviews or comments on any PR: did Kerk review your work in another way (meetings, chat)?
5. What is the status of the engine work (`bj/engine-v2-experiment`, local `bj/engine-package-spike`, local `bj/bfs-wasm-spike`)? Was the "Kerk BFS runtime" agreed with Kerk? Should the report mention it as unmerged exploration?
6. The two worktree folders are empty on disk. Was any uncommitted work in them?
7. Vercel: was there a deployment from the fork (`c9e4598`, `03bfaa3`), with what URL, and is it still up? What was the 2026-11-01 push to the fork?
8. The site proposal calls the homepage "Kerk's homepage" and the kit "Kerk's UI kit"; the site uses Kerk's design system; the V2/V7 layouts are frames in Kerk's wireframe 2. Is that how you want the report to credit them? How was the design system produced (it holds `SKILL.md` and `*.prompt.md` files)?
9. How should the report describe the AI tools (Claude trailers on 199 of your 213 commits; Codex named in 8 commit messages and 3 PR bodies) and your own role?
10. Do the other local branches (`backup/before-reword-044908`, `bj/viz-shell-v10-stage0`, `live_prototype`, `bj/vercel-spa-routing`) matter for the report, or can they be ignored?

## 12. Evidence trail

Main commands (all read-only, run 2026-11-01 from the repository root):

- `git log main --reverse --format=...`, `git shortlog -sne main`, `git log --first-parent --no-merges main`
- `git show --stat / --shortstat / -M --name-status <commit>` for every commit named above
- `git log --all -- .gitmodules`, `git ls-tree <commit> prototypes/`, `git ls-tree -r --name-only <commit>` at the snapshot commits
- `git log main --diff-filter=A|D -- prototypes/<folder>/package.json`
- `git merge-base --is-ancestor`, `git rev-list --count main..<branch>`, `git cherry -v main <branch>` for every branch
- `git log main --no-merges --numstat` (section 9.1) and `git blame --line-porcelain -w 662e7b3 -- <file>` over 1,292 files (section 9.2)
- `gh api`: `repos/{kerktaiheng,BJoozz}/visualgo-plus-design` (repo, branches, events, commits, compare), `pulls/<n>`, `pulls/<n>/reviews`, `pulls/<n>/comments`, `issues/<n>/comments`, `issues`, `collaborators/BJoozz/permission`
- `git -C <worktree> status --short`, `find <worktree> -type f` (counts only)

Working files (outside the repository): `C:/Users/123ba/AppData/Local/Temp/claude/c--Users-123ba-nuss-OneDrive---National-University-of-Singapore-workplace-vstudio-learn-code-visualgo-plus-design/dd1448ed-3ceb-4759-a934-c360d565fa8f/scratchpad/fyp/work/` - `numstat.txt`, `blame-out.tsv`, `merges.tsv`, `prs-api.tsv`, `branches-check.tsv`, `0394b64-ns.txt`, and the scripts in `scripts/`.

Tests: none run for this note.

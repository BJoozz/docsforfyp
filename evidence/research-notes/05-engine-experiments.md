# 05 — Engine and WASM experiments

Evidence note for Bao's FYP report. Audit of 2026-11-01, read-only.

## How to read this note

- Repository: kerktaiheng/visualgo-plus-design, `main` at `662e7b3` (2026-10-31). The working tree was clean before and after this audit (VERIFIED, `git status`).
- Paths are relative to the repository root. Commit hashes have 7 characters.
- Labels: **VERIFIED** (I saw it in code, a diff, a log, a live probe or a test run), **DOCUMENTED** (a doc, commit message or PR body says it; not checked against code), **INFERENCE** (my reading), **QUESTION** (Bao must answer).
- What I ran myself on 2026-11-01:
  1. The deployed engine demo's own self-test, `https://kerktaiheng.github.io/visualgo-plus-design/engine/?selftest=1`, in headless Chromium (Playwright from the repo's `node_modules`; the probe script lives in the scratchpad, not the repo). Result at 15:47 UTC: **SELFTEST PASS, 15 of 15 checks "ok"**, no page errors, no failed requests. VERIFIED.
  2. HTTP probes of the demo page and its `.wasm` file (section 2.5). VERIFIED.
- What I did not run: the `wasm-arch` test suite and any test on Bao's branches. They need the Docker/Emscripten toolchain; the Docker daemon was not running and `emcc` and `protoc` are not installed on this machine. Test results for `main` come from the GitHub Actions log (2.4). Results for the branches are only what their commit messages say.

## 1. At a glance

| Item | Author identity (git) | Dates | Where | Status | In today's app? |
|---|---|---|---|---|---|
| Engine prototype: protobuf RPC, C++ engine compiled to WASM, Python engine, journal and Delta | Kerk Tai Heng | 2026-09-03 to 09-14 (deploy change 10-18) | `wasm-arch/` on `main` | On `main`; CI tests pass; deployed at `/engine/` | No (separate project; not imported, not linked) |
| Engine experiment M0 to M3 (edge identity, browser client, BFS runtime) | BJoozz `<123baoek31@gmail.com>` | 2026-09-17 | `wasm-arch/` on `origin/bj/engine-v2-experiment` (4 commits) | Never merged, no PR, no CI run | No |
| M4a packaging spike | BJoozz (same) | 2026-09-17 | local branch `bj/engine-package-spike` (1 commit) | Local only, never pushed | No |
| Earlier client draft, "currently paused" | BJoozz (same) | 2026-09-17 | local branch `bj/bfs-wasm-spike` (1 commit) | Local only, never pushed | No |

All rows VERIFIED (git log, `git merge-base --is-ancestor`, `git ls-remote`, `gh run list`, search of `HEAD`). That "BJoozz <123baoek31@gmail.com>" is Bao: QUESTION (please confirm).

## 2. Kerk's engine prototype (`wasm-arch/`)

### 2.1 Authorship and dates

| Commit | Date (+08:00) | Author | AI co-author trailer | What it did |
|---|---|---|---|---|
| `b3e86ba` | 2026-09-03 23:11 | Kerk Tai Heng | Claude Fable 5.1 | "Graph RPC: monotype protobuf between a web page and a C++ WASM engine": schema, C++ engine, page, Node tests, Docker, CI and Pages workflows (57 files, +6,099 lines), then at the repository root |
| `8a59115` | 2026-09-04 11:48 | Kerk Tai Heng | Claude Fable 5.1 | Moves the prototype into `wasm-arch/` |
| `e396e06` | 2026-09-04 12:29 | Kerk Tai Heng | Claude Fable 5.1 | Second monotype `arrays.v1.Array` and the Python engine that traces unmodified sorts (+1,848) |
| `aa541a1` | 2026-09-04 13:55 | Kerk Tai Heng | Claude Fable 5.1 | One log stream for every hop of a call (+878) |
| `598193b` | 2026-09-13 21:32 | Kerk Tai Heng | none | Removes `Zone.Identifier` files; also moves `wasm-arch/scripts/` under `pyengine/tests/` and edits a few files |
| `df99dac` | 2026-09-14 13:03 | Kerk Tai Heng | Claude Opus 5 | Moves `scripts/` back (its message: CI and Pages had failed on every push since `598193b`); bumps the GitHub actions |
| `c39b3cf` (PR #18) | 2026-10-18 18:58 | Kerk Tai Heng | Claude Opus 5.5 | Pages: the engine demo moves to `/engine/` |

VERIFIED (`git log -- wasm-arch`, `git show --stat`, trailers), except the CI-failure remark (DOCUMENTED in `df99dac`). The repository's first commit `634b5be` "init" (Kerk, 2026-09-03) holds design files only (VERIFIED). Every commit on `main` that touches `wasm-arch/` is Kerk's; Bao's first commit on `main` is `986deba` (2026-09-13), after the engine existed (VERIFIED). No person's choice ("the owner") is recorded in the engine commits or in PR #18; the word appears only in its technical sense ("ownership") (VERIFIED, grep).

Size on `main` today (tracked files, `wc -l`, VERIFIED): C++ engine 2,630 lines; proto 239; Python engine 860 plus 199 lines of unittest; demo page 2,020; Node tests 643; scripts 269; README and architecture doc 544.

### 2.2 The problem it addresses

DOCUMENTED (`wasm-arch/docs/ARCHITECTURE.md`, "Goals"):

1. One message type on the wire: every RPC takes a `graph.v1.Graph` and returns one.
2. Two symmetric peers: the page and the engine both serve methods and both make calls.
3. The engine owns history: the page is a stateless view; every response is the full state at the new step plus a `Delta` of what changed; `Prev` never re-runs an algorithm.
4. Deployable as static files, built reproducibly inside Docker.

INFERENCE: it is an architecture prototype for running algorithm engines outside the UI code (C++ compiled to WebAssembly, or Python inside Pyodide) behind one protocol, so that the page only draws states.

### 2.3 Approach and components

| Component | What it does | Evidence |
|---|---|---|
| "Monotype" schema | Every `GraphEngine` RPC takes a `graph.v1.Graph` and returns one; parameters and results ride inside it. A second monotype, `arrays.v1.Array`, serves the Python engine. A `Frame` envelope carries `id`, `kind` (REQUEST, RESPONSE, ERROR), `method`, a `payload` oneof (graph or array) and `error`. proto3 `optional` keeps "absent" and "zero" apart. | VERIFIED `wasm-arch/proto/graph/v1/graph.proto:106-147`, `wasm-arch/proto/arrays/v1/array.proto:84-90` |
| Symmetric RPC | The engine serves `Echo`, `Bfs`, `Dfs`, `Dijkstra`, `Mst`, `MaxFlow`, `TopoSort`, `Components`, `RbInsert`, `Next`, `Prev`, `Seek`, `RunToEnd`; the page serves `GraphView/Layout` and `GraphView/Progress`. JS `RpcPeer` uses promises, the C++ `Peer` uses coroutines, the Python `Peer` is synchronous with no outbound calls. | VERIFIED (services in the proto, files exist); DOCUMENTED (peer styles) |
| Transport | The worker only forwards bytes. The WASM exports `vgp_alloc`, `vgp_free`, `vgp_receive` and `vgp_set_log_level`, and calls JS through two `EM_JS` functions (`vgp_js_send`, `vgp_js_log`). | VERIFIED `wasm-arch/engine/src/exports.cc`; DOCUMENTED: no threads, no SharedArrayBuffer, no special headers |
| C++ engine | Emscripten with protobuf-lite 3.21.12 and C++20 coroutines. `Task<T>` is an eager coroutine; each algorithm is a generator over a `Session` that `co_yield`s once per step. Algorithms: BFS, DFS, Dijkstra, Kruskal, Edmonds-Karp, Kahn, connected and strongly connected components, red-black insertion. | VERIFIED `wasm-arch/engine/src/algorithms/common.cc:7-8`, `wasm-arch/engine/include/vgp/task.h`; DOCUMENTED (toolchain versions) |
| Journal and Delta | Every mutation appends a `Record` (the changed fields before and after; creation or deletion has one side absent). A `Step` is the records plus a narration. `step_forward()` replays a stored step or resumes the generator (so execution is lazy); `step_backward()` applies the records in reverse with before and after swapped; `seek(k)` walks with both. A transaction captures each touched element's pre-image and diffs it at the end to build the wire `Delta`, so a long `Seek` becomes one change per element. Field lists are X-macros. | VERIFIED `wasm-arch/engine/include/vgp/session.h:95-154`, `wasm-arch/engine/include/vgp/fields.h`; behaviour VERIFIED by the passing CI test "Prev and Seek replay the journal exactly, forwards and backwards" (2.4) |
| Python engine | Runs unmodified textbook sorts (bubble, selection, insertion, merge, quick, counting) under `sys.settrace`, passing a `TracedList` (a `list` subclass that reports index reads and writes). Builds the same kind of journal, eagerly. Runs in Pyodide (from jsDelivr) in the browser and under CPython over stdio in tests. | VERIFIED `wasm-arch/pyengine/vgp/tracer.py:28-48,121`, `wasm-arch/pyengine/vgp/programs/sorts.py`, `wasm-arch/web/src/engine/py-worker.ts:10,56-57` |
| Demo page | Vite and TypeScript: a graph canvas that tweens Deltas, a bar chart for arrays, a force-directed layout served to the engine, a JSON editor, and a log panel with levels frames, engine and trace. | VERIFIED (files); DOCUMENTED (behaviour) |

### 2.4 Tests and results

| Suite | Tests | Result | Evidence |
|---|---|---|---|
| `wasm-arch/tests/engine.test.ts` (node:test over the Node build of the WASM, through the same `RpcPeer` as the page) | 20 | pass | VERIFIED: GitHub Actions `ci` run 41095633621 on `662e7b3`, 2026-10-30 17:04 UTC. Its log shows `RUN yarn test` executing (not cached) and "tests 25, pass 25, fail 0" |
| `wasm-arch/tests/pyengine.test.ts` (the Python engine over stdio) | 5 | pass | same run |
| `wasm-arch/pyengine/tests/test_engine.py` (unittest) | 9 | pass | same run: "Ran 9 tests … OK" |
| `wasm-arch/scripts/smoke.mjs` (headless Chrome opens `?selftest=1`) | 15 checks | not part of CI: the Docker `test` stage runs only `yarn test` (`wasm-arch/Dockerfile:47-48`) | VERIFIED (Dockerfile). My own run of the same self-test on the deployed site: PASS, 15 of 15 (VERIFIED, 2026-11-01) |

The test names cover framing and field presence, error frames, logging per hop, BFS deltas, journal replay forwards and backwards, `Seek`, the `Layout` and `Progress` callbacks, every algorithm's result and red-black invariants (VERIFIED, test names in the CI log). `.github/workflows/ci.yml` runs this Docker build on every push to `main` and on every pull request, with no path filter (VERIFIED). INFERENCE: every PR of the project also re-checked Kerk's engine; I read only the latest run's log.

### 2.5 The deployed demo and PR #18

- Before PR #18, Pages served the `wasm-arch` demo at the site root (`dest=site`, `VITE_BASE=/<repo>/`). VERIFIED (the lines `c39b3cf` removes).
- PR #18, "Deploy V10 to GitHub Pages, with the engine demo at /engine/" (Kerk; one commit `c39b3cf`; merged by kerktaiheng as `94cdaf3` on 2026-10-18): the demo is built with `VITE_BASE=/<repo>/engine/` into `site/engine`, the V10 site goes to `/`, and a PR that changes `pages.yml` builds without deploying. VERIFIED (diff); DOCUMENTED (PR body).
- Today `.github/workflows/pages.yml` still builds the engine demo into `/engine/`; the root now comes from the unified app (`0394b64`, Kerk, 2026-10-18). VERIFIED.
- Live on 2026-11-01: `https://kerktaiheng.github.io/visualgo-plus-design/engine/` returns HTTP 200 with the title "VisuAlgo+ graph engine" and `Last-Modified` 2026-10-30 17:06:48 GMT, which matches the successful Pages run 41095633645 for `662e7b3`. Its WASM file `assets/graph_engine-B2BmsNSd.wasm` is served as `application/wasm`, 408,202 bytes (131,908 bytes after `gzip -9` on my machine). VERIFIED.
- The deployed self-test has none of the edge-identity checks that Bao's branch adds, so it is `main`'s (Kerk's) build. VERIFIED (check names against `wasm-arch/web/src/selftest.ts`).
- The app does not link to `/engine/`. VERIFIED (search of `prototypes/src`).

### 2.6 Small differences between Kerk's doc and code (check before quoting)

| `wasm-arch/docs/ARCHITECTURE.md` says | The code says | Label |
|---|---|---|
| The X-macro field lists are "at the top of `src/session.cc`" (line 145) | They are in `engine/include/vgp/fields.h`, which `engine/src/session.cc:7` includes | VERIFIED |
| The WASM "exports three C functions … and imports one JS callback" (Transport) | Four exports, including `vgp_set_log_level`, and two `EM_JS` callbacks since `aa541a1` (the Observability section does name the log export) | VERIFIED |
| "The wasm is 325 KB (110 KB gzipped)" (Costs) | The deployed binary is 408,202 bytes (131,908 with `gzip -9`) | VERIFIED; INFERENCE: the figure was written before later additions such as logging |
| A table of journal versus snapshot memory (Costs) | Not measured by me | DOCUMENTED only; do not cite it as a measurement |

### 2.7 Known limits stated by Kerk

DOCUMENTED (`wasm-arch/docs/ARCHITECTURE.md:314-327`): parallel edges cannot be addressed by `(u, v)` ("an optional `Edge.id` would be the fix"); side structures are text in `attributes`; one session per engine instance; a worker crash is only shown in the status line; the Python peer cannot call the page; Pyodide (about 10 MB) comes from a CDN.

The first limit is real in the code. `Session` indexes edges by their endpoint pair, `eidx_.emplace(key(e.u(), e.v()), i);  // first occurrence wins for parallel edges` (`wasm-arch/engine/src/session.cc:154`), and Dijkstra stores each parent edge as an endpoint pair (`wasm-arch/engine/src/algorithms/dijkstra.cc:14`). VERIFIED. This is the gap Bao's M1 works on (3.3).

## 3. Bao's engine experiment (2026-09-17)

### 3.1 Branches, commits and status

| Ref | Tip | Commits | On GitHub? | Merged into `main`? | CI or PR |
|---|---|---|---|---|---|
| `origin/bj/engine-v2-experiment` (the local branch of the same name is identical) | `ffb9274` | 4 ahead of `main`: `478174f`, `e348a6d`, `ee65bef`, `ffb9274` | yes (`git ls-remote`) | no | no Actions run on the branch, 0 check runs on `ffb9274`, no PR in `prs.txt` |
| `bj/engine-package-spike` (worktree) | `053064f` | 1 on top of `ffb9274` | no remote branch contains it | no | none |
| `bj/bfs-wasm-spike` | `53d2ef4` | 1 on the same base as `478174f` | no remote branch contains it | no | none |

All VERIFIED. "Never merged": `git merge-base main origin/bj/engine-v2-experiment` is `4bd9ca9` (Bao's merge of `origin/main` into `bj/visualization-work`, 2026-09-16), and `git merge-base --is-ancestor <commit> main` is false for `ffb9274`, `053064f` and `53d2ef4`. `ci.yml` runs only on pushes to `main` and on PRs (VERIFIED); INFERENCE: that is why the pushed branch never ran CI. The base `4bd9ca9` has exactly today's `wasm-arch/` (`git diff 4bd9ca9 main -- wasm-arch` is empty; VERIFIED).

Timeline, all on 2026-09-17 (+08:00; author time equals committer time):

| Time | Commit | Message | AI co-author trailer |
|---|---|---|---|
| 01:12 | `478174f` | feat(engine): add stable edge identity across runtime and playback (M0 and M1) | none |
| 03:56 | `53d2ef4` | currently paused (`bj/bfs-wasm-spike`, a sibling of `478174f`) | none |
| 05:38 | `e348a6d` | refactor(engine): extract reusable browser engine client (M2) | Claude Opus 5 (1M context) |
| 12:21:15 | `ee65bef` | test(engine): dispatch a Node-safe error event in the client worker test | Claude Fable 5.1 |
| 12:21:15 | `ffb9274` | feat(engine): add experimental Kerk BFS runtime (M3) | Claude Fable 5.1 |
| 13:09 | `053064f` | wip(package): M4a packaging spike for @visualgo/kerk-bfs-runtime | Claude Fable 5.1 |

VERIFIED. `ee65bef` and `ffb9274` carry the same second (INFERENCE: committed together).

**Where it sits.** Every one of these commits changes files only under `wasm-arch/`, Kerk's engine folder (0 files elsewhere; VERIFIED). In that era `prototypes/` held only two submodules, `graph-visualizer-v2` at `c8b14e6` and `tree-visualizer` at `1477cda`, both BJoozz repositories (VERIFIED, `.gitmodules` at `4bd9ca9`). The host that the runtime targets, "Graph V2", is `graph-visualizer-v2` (VERIFIED: its clone has `GraphDocument`, `GraphPresentation`, `src/algorithms/bfs/createBfsSequence.ts`, `topologyRevision` and the `@xyflow/react` dependency that the docs call React Flow). The branch never changed that submodule (VERIFIED).

**Size**, branch tip `053064f` against the base (`git diff --shortstat`, VERIFIED): C++ engine and proto 16 files, +154/−103 (all in `478174f`); `web/` 18 files, +1,371/−67; `tests/` 11 files, +2,227; `docs/` 5 files, +752/−9; `package/` and `examples/` 9 files, +287; Python engine unchanged.

**Language.** `docs/EDGE_IDENTITY.md` and `docs/ENGINE_CLIENT.md` mix Vietnamese and English; `docs/KERK_BFS_RUNTIME.md` and `docs/PACKAGE.md` are in English. The summaries below are my translation. VERIFIED.

### 3.2 The milestone plan and the name "M4a"

No separate plan file exists: searching the whole `053064f` tree and every remote branch finds the milestone names only in the branch's own docs (VERIFIED). The plan is spread across them:

| Milestone | Content | Defined in | Commit | Label |
|---|---|---|---|---|
| M0 | Baseline: write down Kerk's existing BFS behaviour and pin it with tests before changing anything | `wasm-arch/docs/EDGE_IDENTITY.md`, section M0 | `478174f` | DOCUMENTED |
| M1 | Stable edge identity | same doc, section M1 | `478174f` | DOCUMENTED |
| M2 | Reusable browser engine client | `wasm-arch/docs/ENGINE_CLIENT.md` | `e348a6d` | DOCUMENTED |
| M3 | Runtime for hosts with string IDs: validation, ID mapping, one request at a time, stale-response protection, normalized frames | `ENGINE_CLIENT.md` ("Reserved for M3 and M4") and `wasm-arch/docs/KERK_BFS_RUNTIME.md` | `ffb9274` | DOCUMENTED |
| M4 | Presentation side: a BFS presenter from `KerkBfsFrame` to `GraphPresentation`, an async shared player, and Graph V2's persistent React Flow canvas | the same two docs ("What remains for M4") | not started | DOCUMENTED (`PACKAGE.md`: "M4 proper … has not started") |
| M4a | Packaging spike `@visualgo/kerk-bfs-runtime` | `wasm-arch/docs/PACKAGE.md` | `053064f` | DOCUMENTED |

INFERENCE: "M4a" is a first sub-step of M4 (package the boundary that M4 would consume), done before M4 proper. QUESTION: was the M0 to M4 plan written anywhere else (notes, an AI session plan, a meeting with Kerk or the supervisor)?

### 3.3 M0 and M1: stable edge identity (`478174f`)

**Problem.** Kerk's engine identifies an edge by its two endpoints. When two edges join the same vertices (parallel edges), the second cannot be addressed: lookups, journal records and Delta entries all reach the first (code in 2.7, VERIFIED). M0 states the effect: "the base handles simple graphs correctly, but endpoint lookup can read or modify the wrong parallel edge", for example Dijkstra's parent edge (DOCUMENTED).

**Approach.** Give every edge an ID that stays the same for the whole session and use it everywhere instead of the endpoints. The ID's path (DOCUMENTED, section M1): `Graph.edges[].id` → worker → WASM → `Engine::start` → the session's edge index → adjacency entries `{to, edge_id}` → algorithm mutations → journal → transaction Delta → full `Graph` and Delta → the page pulses edges by ID.

**Components** (VERIFIED in the diff unless marked):
- Proto: `Edge.id` (optional uint32, field 12; 0 is a valid ID) and `Vertex.parent_edge` (optional uint32, field 13: the exact tree edge from BFS, DFS and Dijkstra). A Delta always carries `Edge.id`, `u` and `v`; other fields only when they changed.
- `assign_edge_ids()` in `engine/src/algorithms/common.cc`, called by `Engine::start`: reserve every explicit ID, reject duplicates (even between different endpoints), give each missing ID the smallest unused number in input order. Example in the doc: `[absent, 0, 4294967295, absent, 21]` becomes `[1, 0, 4294967295, 2, 21]` (DOCUMENTED).
- `Session` by ID (`engine/include/vgp/session.h`): `edge(id)`, `update_edge(id, …)`, `remove_edge(id)`, `set_edge_state(id, …)`, and `add_edge()` returns `optional<EdgeId>`. The index is an `unordered_map<EdgeId,int>`. `used_edge_ids_` keeps every ID ever used, so a deleted or undone ID is never handed out again. Journal records keep the array position (`edge_index`), so undo and replay restore both identity and order without allocating.
- All eight algorithm files move from endpoint keys to IDs (16 engine and proto files in all). For example, Kruskal now sorts edge IDs by weight (`mst.cc`); MaxFlow's residual arcs point back to the original edge (DOCUMENTED).
- Page: `web/src/edge-identity.ts` adds `withEdgeIds()` (the engine's normalisation, for the demo) and `edgeLanes()` (groups edges by endpoint pair for drawing only). `web/src/view/canvas.ts` pulses `e<id>` instead of `e<u>-<v>`, and draws parallel and reciprocal edges as separate curves and self-loops as loops.

**Tests added.**
- `wasm-arch/tests/baseline.test.ts`, 3 tests (one generated twice in a loop): pins lazy BFS steps, neighbour order and orientation, that a directed incoming edge is not followed, and that an undirected self-loop is visited twice. The doc says they passed on the unchanged WASM first (DOCUMENTED).
- `wasm-arch/tests/edge-identity.test.ts`, 16 tests (5 generated in loops): zero, mixed, missing and maximum IDs; duplicate rejection that keeps the old session; parallel, reciprocal and self-loop edges through replay; reversed undirected endpoints; Dijkstra with parallel weights and ties; Kruskal; MaxFlow parallel capacities and residual cancellation; TopoSort parallel arcs; DFS and Components navigation; red-black rotations keeping IDs; demo lanes. Each trace rebuilds the state from the sparse Deltas and checks Next, Prev, Next and a Seek to every step in both directions (DOCUMENTED).
- The browser self-test gains 4 checks (parallel BFS and Dijkstra, worker replay, Seek keeps the IDs).

Test names and counts VERIFIED; what each asserts DOCUMENTED.

**Result claimed.** "44 Node + 9 Python pass", Chrome smoke PASS, and the screenshot was inspected (DOCUMENTED, `EDGE_IDENTITY.md`, "Verification"). My count of test definitions at `478174f`, loops included, is also 44 Node tests (VERIFIED count; that they pass is not verified). The worktree's `.smoke/` folder, where the screenshot would be, is empty now (VERIFIED).

**Limits stated** (DOCUMENTED): this fixes identity, it does not certify every multigraph input; red-black input still rejects parallel parent/child edges, self-loops and cycles; NaN and Infinity validation is unchanged; the red-black vertex allocator `max(id)+1` is not fixed; the single-session lifecycle is unchanged; labels of dense parallel edges can overlap.

### 3.4 M2: reusable browser engine client (`e348a6d`, `ee65bef`)

**Problem.** On `main`, the demo's `connect()` builds the worker, the `WorkerTransport` and the `RpcPeer` next to DOM status code (`wasm-arch/web/src/main.ts:65-94`). A worker error only rejects the "ready" promise and sets the status line (`main.ts:81-86`). `RpcPeer` cannot be closed and rejects a pending call only when an ERROR frame arrives (`wasm-arch/web/src/rpc/peer.ts:106-115`); `WorkerTransport` does not listen for `error` or `messageerror`. VERIFIED (code). INFERENCE: a call in flight when the worker dies never settles, and another host cannot reuse the engine without the demo's DOM code.

**Approach and components** (VERIFIED in code; the React note is DOCUMENTED). `wasm-arch/web/src/engine/client.ts`, class `GraphEngineClient`:
- owns exactly one worker, its `WorkerTransport` and its `RpcPeer`, and no DOM, renderer or playback state;
- one-way lifecycle `new → initializing → ready`, with `failed` and `disposed` as end states; the constructor creates nothing (so it is safe inside React Strict Mode effects); repeated `initialize()` calls share one promise;
- methods `call`, `start(method, graph)`, `next`, `prev`, `seek`, `runToEnd`, `setLogLevel`; calls are refused unless the state is `ready`;
- any worker `error`, `messageerror`, failed status, decode failure or send failure closes the peer, rejects every pending call and terminates the worker; `dispose()` can be called many times safely.
- Supporting changes: `RpcPeer.close()` and `onError`; `WorkerTransport.onError` and `dispose()`; DOM-free log types in `web/src/engine/log-types.ts`; the demo itself now uses the client (`main.ts:2,93` at `e348a6d`).

**Tests added** (VERIFIED names and diff).
- `wasm-arch/tests/engine-client.test.ts`, 11 tests (8 generated): a real worker thread with the Node WASM build runs BFS Next, Prev, Seek and RunToEnd with no `document` or `window`; initialisation is lazy and shared; each of `error`, `messageerror`, failed status and `dispose` rejects outstanding work, both while initialising and while ready; constructor and send failures do not hang.
- `wasm-arch/tests/engine-client-worker.ts`: the worker harness.
- `wasm-arch/tests/rpc-lifecycle.test.ts`, 4 tests: closing rejects pending calls and ignores late frames; a send failure is reported once; malformed protobuf rejects instead of becoming an unhandled rejection; an async inbound handler cannot send after close.
- `ee65bef` fixes the harness: Node 24 has no global `ErrorEvent`, so the test dispatches a plain `Event` with `message`, `filename` and `lineno`.

**Result claimed.** "59 Node + 9 Python tests … Chrome smoke PASS" (DOCUMENTED, `e348a6d` message). My count of test definitions is 59 (VERIFIED count). The same commit corrects, on the branch only, the two stale notes of 2.6 and 2.7 (X-macro location, edge-identity limit) (VERIFIED diff).

### 3.5 M3: Kerk BFS runtime (`ffb9274`)

**Problem.** Graph V2 keeps string IDs: a `GraphDocument` has `nodes {id, label}`, `edges {id, source, target, weight?}`, `directed` and `topologyRevision` (VERIFIED in the clone, `src/graph/model/graph.ts`). Kerk's engine uses numeric IDs, writes vertex names into its narration and its queue text, holds one session, and has no guard against overlapping requests: `Start` can wait on `GraphView/Layout` and `RunToEnd` waits on `Progress` every 16 steps, and a request that arrives meanwhile "could wipe its transaction" (DOCUMENTED, `KERK_BFS_RUNTIME.md`, "Request serialization").

**Approach and components** in `wasm-arch/web/src/runtime/` (files and names VERIFIED; behaviour DOCUMENTED in `KERK_BFS_RUNTIME.md` unless marked):
- `kerk-graph-input.ts`: validates a `GraphDocument`-shaped input; builds frozen string-to-number maps (the array index is the numeric ID; nodes and edges are separate namespaces); sends every edge ID explicitly so parallel, reciprocal and self-loop edges stay distinct; checks weights but does not send them (BFS ignores weights); names vertices `v<n>` so the engine's queue text can be parsed back strictly.
- `kerk-bfs-runtime.ts`: `KerkBfsRuntime` sends one engine call at a time. A generation counter moves on at `start()`, `invalidate()` and `dispose()`; a response for an older generation is never published and its caller gets `stale-run` or `disposed`. A failed start leaves no run to navigate; a client failure turns the runtime `failed`. The generation code is VERIFIED at `kerk-bfs-runtime.ts:66,129-142,231-242,286-294`.
- `kerk-bfs-frame.ts`: turns the engine's full `Graph` and `Delta` into a deeply frozen `KerkBfsFrame` that uses only the original IDs (distance, parent node and edge with direction, Kerk's highlight state, queue, current node, active edge, step kind). The step kind comes from `delta.code_line`, and the pseudocode text is pinned (`KERK_BFS_PSEUDOCODE`), so a renumbered engine fails loudly.
- `errors.ts` (`KerkRuntimeError` codes: `invalid-input`, `no-active-run`, `stale-run`, `protocol`, `engine-failed`, `disposed`), `frozen-map.ts`, and `index.ts` (`createKerkBfsRuntime`).
- It keeps Kerk's BFS as it is and does not imitate Graph V2's BFS. The doc lists the differences: neighbour order, step granularity, which edge an inspect step names, an undirected self-loop inspected twice, the meaning of "visited", a queue parsed from text, and an end that is known only after one extra call. It adds that the Graph V2 column "is taken from Graph V2's source, not tested here".

**Tests added** (VERIFIED names and counts): `kerk-graph-input.test.ts` 9 (pure); `kerk-bfs-frame.test.ts` 15 (hand-built responses); `kerk-bfs-runtime.test.ts` 31 (a fake engine: serialization, generations, stale responses, failures, disposal, no retention of old responses); `kerk-bfs-runtime-wasm.test.ts` 11 (the real Node WASM behind `GraphEngineClient` in a worker: pinned step sequences, ID mapping, navigation, end discovery, reverse callbacks, failed start); helper `kerk-runtime-support.ts`.

**Result claimed.** "125 Node + 9 Python tests … Chrome smoke PASS" (DOCUMENTED). My count of test definitions is 125 (VERIFIED count). The doc notes that test files are not type-checked (DOCUMENTED).

### 3.6 M4a: packaging spike (`053064f`, local only)

**Problem.** Let another frontend use the runtime by importing one package, without seeing protobuf, the RPC layer, the worker or the WASM (DOCUMENTED, `PACKAGE.md`).

**Components** (VERIFIED): `wasm-arch/package/` (`@visualgo/kerk-bfs-runtime` 0.1.0, `"private": true`; it exports only `createKerkBfsRuntime`, `KerkRuntimeError` and types) with a Vite library build; the public types move to `web/src/runtime/types.ts`; `wasm-arch/examples/package-consumer/` is a Vite app that imports only the package; `wasm-arch/tests/package-surface.test.ts` has 5 tests (exact exports, no bare imports, a worker chunk with the WASM inlined, loads without a DOM, the declaration files hide the internals).

**Result claimed** (DOCUMENTED): "130 Node + 9 Python tests … consumer and demo Chrome smoke PASS"; the worker chunk is about 1.1 MB because the WASM is inlined as a `data:` URL, "about 35% more bytes than the 414 kB binary". My count of test definitions is 130 (VERIFIED count). I did not check the sizes.

**Limits stated** (DOCUMENTED): not installed or published (the consumer reaches it through a Vite alias); it can be built only inside `wasm-arch`'s Docker and Emscripten toolchain; BFS only; no React and no presenter.

**Status.** The message calls it "wip … Temporary checkpoint for review" (DOCUMENTED). The commit exists only in this clone (VERIFIED). Its worktree `C:/Users/123ba/AppData/Local/Temp/visualgo-engine-v2-experiment` has no files left on disk: 314 tracked files show as deleted and only empty folders remain (VERIFIED with `git --no-optional-locks status`, which does not write the index). Everything above was read from git objects. The other worktree, `bj/fix-traversal-ci` (not engine work, 0 commits ahead of `main`), is in the same state: 2,544 tracked files deleted on disk, but no unique commit is at risk there (VERIFIED). INFERENCE: if this clone is lost, `053064f` and `53d2ef4` are lost too. QUESTION: keep, push or archive them?

### 3.7 The earlier draft on `bj/bfs-wasm-spike` (`53d2ef4`)

VERIFIED: a local-only commit "currently paused" at 03:56 whose parent is `4bd9ca9` (so it is a sibling of `478174f`, not an ancestor of M2). It changes 14 files under `wasm-arch/`: a first `GraphEngineClient` (115 lines), the same three test files as M2, and README and architecture notes. No AI trailer. `e348a6d` later redid this work on top of M1 (`client.ts` and its test differ by +111/−46 lines). `EDGE_IDENTITY.md` says no code was taken from "the engine-client spike" (DOCUMENTED). INFERENCE: this branch is that spike, saved as a checkpoint. QUESTION: is that right?

### 3.8 Did any of it reach the current app?

No.

- A literal search of `HEAD` outside `wasm-arch/` finds none of `GraphEngineClient`, `KerkBfs…`, `createKerkBfsRuntime`, `kerk-bfs`, `edgeLanes`, `withEdgeIds`, `RpcPeer`, `WorkerTransport`, `graph_pb` or `@bufbuild`; `prototypes/src` uses no `.wasm`, `WebAssembly` or Pyodide. `main`'s `wasm-arch/` is the branch's base, unchanged. VERIFIED.
- The `parentEdge…` names in `prototypes/src` (85 hits) are unrelated: the graph's `parentEdge` and `parentEdgesByNodeId` already existed in Bao's `graph-visualizer-v2` from `a8c3e00` (2026-09-02), and the tree's `parentEdgeByNodeId` in `tree-visualizer` from `e687099` (2026-09-03), both before the experiment. VERIFIED.
- In `prototypes/src` the word "engine" names the app's own TypeScript step builders, such as `src/sorting/engine/operations.ts` and `src/graph/algorithms/prim/primEngine.ts`. VERIFIED.
- Graph V2 already gave every edge a string ID (`GraphEdge.id` in the clone's `src/graph/model/graph.ts`), and the app's graph code descends from it (`0073875` is titled "Add split-rails (V2) and docks (V7) clones of graph-visualizer-v2"). So the app never needed M1's fix. VERIFIED (the type, the commit title); INFERENCE (the consequence).
- Three days after the experiment, `0073875` (BJoozz, 2026-09-20, the first V2 and V7 viz-page clones) wrote that "the engine integration" is "outside this prototype"; the sentence survives in today's docs (section 4). VERIFIED (`git log -S`). QUESTION: why did the engine work stop on 2026-09-17, and who decided that integration was out of scope?

## 4. Engine mentions in the current docs

`grep -rn -i -E 'engine|wasm' prototypes/docs README.md` returns 156 lines (VERIFIED, 2026-11-01). Seven of them are about the WASM engine. The other 149 use "engine" for the app's own TypeScript algorithm code, for example `prototypes/docs/graph/ARCHITECTURE.md:363`, "**Engine.** `src/graph/algorithms/bellmanFord/createBellmanFordSequence.ts` builds …" (VERIFIED).

| Place | What it says | Label |
|---|---|---|
| `README.md:6` | "`wasm-arch/`: the C++/WebAssembly engine prototype, a project of its own." | VERIFIED |
| `prototypes/docs/graph/AGENTS.md:50`, `prototypes/docs/tree/AGENTS.md:54`, `prototypes/docs/sorting/AGENTS.md:65` | Do not modify `../wasm-arch` from here. | VERIFIED |
| `prototypes/docs/graph/README.md:451` | "the separate Wasm engine integration [is] outside this prototype" | VERIFIED |
| `prototypes/docs/tree/README.md:301` | "any engine (WASM) integration [is] outside this prototype" | VERIFIED |
| `prototypes/docs/graph/PRIM_ACCEPTANCE.md:6` | the "WASM experiment [is] outside this change" | VERIFIED |
| Outside the grep: `prototypes/AGENTS.md:19-20` | "`../wasm-arch` is the engine prototype, a separate project." | VERIFIED |
| Outside the grep: `design/proposals/prim-v2-v7/README.md:16,174` (in Vietnamese) | the Prim work does not touch the WASM experiment | VERIFIED |
| Backlogs (`prototypes/docs/*/IMPROVEMENT_BACKLOG.md`) | no WASM item; their "engine" lines are about the TypeScript engines | VERIFIED |
| Bodies of PRs #1, #2 and #3 (2026-09-20 to 09-27) | the engine experiment (and, in #1 and #3, `wasm-arch`) is unchanged; #1: "`wasm-arch` and the separate engine experiment are unchanged" | DOCUMENTED (`prs.txt`) |

## 5. Statements the report can make safely

Each statement rests on the labelled evidence above.

- Kerk built the engine prototype in `wasm-arch/` between 2026-09-03 and 09-14, with Claude co-author trailers on five of its six commits: one protobuf message type per service, a symmetric RPC between page and engine, a C++ engine compiled to WebAssembly whose reversible journal answers every step with a Delta, and a Python engine that traces unmodified sorts in Pyodide. Its 25 Node and 9 Python tests pass in CI on `662e7b3` (2026-10-30), and the deployed demo's self-test passed when I ran it on 2026-11-01.
- On 2026-09-17 Bao explored connecting that engine to his Graph V2 host in steps M0 to M4a: stable edge IDs inside the engine, a reusable browser client, a BFS runtime for hosts with string IDs, and a packaging spike, each with its own tests. Claude co-author trailers are on four of his six commits. None of it was merged or used by the app, and the viz-page work that followed put engine integration out of scope.
- Do not claim: performance or memory gains (only Kerk's estimates exist); that the app uses the engine; that the branch tests passed (only the commit messages say so, and no CI ran); that Bao co-wrote Kerk's engine (no commit of his touches `wasm-arch/` on `main`).

## 6. Questions for Bao

1. Is `BJoozz <123baoek31@gmail.com>` you? All six engine commits use it.
2. Was the experiment your own idea, or agreed with Kerk or the supervisor? Did Kerk review it (no PR exists)? Why is the runtime named "Kerk BFS runtime"?
3. Why did the work stop after M4a on 2026-09-17 ("currently paused"), and was the 2026-09-20 line "the engine integration [is] outside this prototype" your decision?
4. Is the M0 to M4 plan written anywhere else (notes, an AI session, a meeting)?
5. Four of your six engine commits carry Claude trailers; `478174f` and `53d2ef4` carry none. Was AI used there too, and how do you want to present AI assistance in the report?
6. `053064f` and `53d2ef4` exist only in this clone, and the spike worktree's files are gone from disk. Keep, push or archive them?
7. Do you want the report to present this unmerged exploration, and under which framing (for example "integration study")?
8. Does Kerk plan more engine work, and is the `/engine/` demo meant to stay on the project site?

## 7. How this was checked

- `git log --format=… -- wasm-arch`; `git show --stat <hash>`; `git show <hash> -- <path>`; `git show <ref>:<path>` into `$TEMP` and `grep -n` / `sed -n` on ranges.
- `git merge-base main origin/bj/engine-v2-experiment`; `git merge-base --is-ancestor <hash> main`; `git branch -r --contains <hash>`; `git ls-remote origin`.
- `git diff --shortstat 4bd9ca9 053064f -- <area>`; `git diff --stat 4bd9ca9 main -- wasm-arch`.
- Test counts: `grep -c` of top-level `test(` calls per file at each commit, plus the loops that generate tests, read by hand.
- `git grep -F` over `HEAD` for the branch's names; `grep -rn -i -E 'engine|wasm' prototypes/docs README.md`; `git log --all -S 'engine integration'`.
- `gh run list` and `gh run view 41095633621 --log` (CI), `gh api …/commits/ffb9274…/check-runs` (none), `gh run list --branch bj/engine-v2-experiment` (none).
- `curl` of `/engine/` and its `.wasm`; Playwright headless Chromium on `/engine/?selftest=1`.
- `git --no-optional-locks -C <worktree> status` for the spike worktree.

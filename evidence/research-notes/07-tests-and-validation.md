# 07 Tests, CI and validation evidence

Audit of the repository `kerktaiheng/visualgo-plus-design` at `main` = `662e7b3`
(2026-10-31 +08:00), done on 2026-11-01. The working tree was clean before and
after the audit (`git status --short` printed nothing, both times).

Labels used on every claim:

| Label | Meaning |
| --- | --- |
| VERIFIED | Seen in code, a diff, a log, the GitHub API, or a command run during this audit |
| DOCUMENTED | A doc, commit message, PR body or comment says it; not checked against code |
| INFERENCE | My reading of the evidence |
| QUESTION | Needs Bao's answer |

The note keeps two things apart: **what exists as a file** (Section 3) and
**what ran during this audit, with its result** (Section 2). A test file proves
that a test exists, not that it passes.

## 1. Key facts

- VERIFIED: every check ran green during this audit on 2026-11-01:
  typecheck, lint (0 errors, 2 warnings), 654 `node:test` cases, 2,619 vitest
  cases in 235 files, the production build, and the full browser suite with
  151 of 151 cases passing in 1.8 minutes.
- VERIFIED: the code holds 328 unit test files (93 graph, 187 tree, 15
  shared, 32 sorting, 1 site) and 14 Playwright specs (151 cases, Chromium
  only).
- VERIFIED: GitHub Actions ran 266 workflow runs from 2026-09-04 to
  2026-10-30. 8 failed, and each failing workflow passed again on a later
  commit. The last 60 runs include 1 failure (a one-pixel font-metric pin on
  2026-10-25, fixed 11 minutes later). The runs for the current `main` all
  passed.
- VERIFIED: browser coverage was cut on 2026-10-18 (Kerk's `0394b64`): 208
  spec files across 12 app copies became 12. The kept layout alone had 74
  spec files. The suite has since grown back to 14 specs and 151 cases.
- VERIFIED: there is no user study, no usability test, no participant data,
  no benchmark suite, no code-coverage tool and no automated accessibility
  audit tool in the repository. Timing numbers exist only as dated
  development observations: three micro-profiles (2026-08-13, 2026-10-03,
  2026-10-05) and a few single readings in the design proposals. The
  profiling scripts are no longer in the app.
- VERIFIED: other validation exists as documents: two graph acceptance
  records, three manual checklists (none recorded as done), three review
  sessions (2026-10-26 to 2026-10-29) whose findings became PRs #34 to #37,
  and many pixel measurements in the DD/TP/SP records.

## 2. Ran during this audit (audit-time evidence)

Machine: Windows 11, Node v24.17.0, npm 11.13.0, Playwright 1.64.1. Clock
shown as the machine's (UTC+07:00); UTC = minus 7 hours. Run from the
repository root on `main` at `662e7b3`, one step after another by a script.
All results below are VERIFIED from the logs of these runs.

| Step | Command | Start (UTC+07:00) | Time | Exit | Result |
| --- | --- | --- | --- | --- | --- |
| Types | `npm run typecheck` (`tsc -b`) | 2026-11-01 22:34:58 | 24 s | 0 | No diagnostics |
| Lint | `npm run lint` (`oxlint`) | 22:35:22 | 2 s | 0 | 0 errors, 2 warnings: `react(only-export-components)` at `src/site/ModuleBar.tsx:46` and `:66` |
| Unit | `npm test` | 22:35:24 | 50 s | 0 | Graph `node --test`: 654 tests, 654 pass, 0 fail, 0 skipped (3.3 s). Vitest: 235 files passed, 2,619 tests passed (42.8 s) |
| Build | `npm run build` | 22:36:14 | 19 s | 0 | Vite 8.3.4, 874 modules; postbuild wrote `dist/404.html` and `dist/_redirects`; a warning that some chunks are over 500 kB after minification, also named in the Prim record (largest `index-*.js` 704.99 kB, gzip 206.24 kB) |
| Browser | `cd prototypes && VA_PORT=5950 npx playwright test --output C:/Users/123ba/AppData/Local/Temp/pw-fyp-audit` | 22:36:33 | 112 s | 0 | **151 passed (1.8 m)**, 3 workers, Chromium, 0 failed, 0 flaky |
| Unit, again | `npx vitest run --reporter=json` (output to my scratch folder), from `prototypes/` | 22:38:59 | 39 s | 0 | Same 235 files and 2,619 tests, all passed; 578 suites. Used for the per-folder counts in Section 3 |

Also run, before the steps above: `npx playwright test --list`, which
reported "Total: 151 tests in 14 files" (VERIFIED).

Notes on the browser run (all VERIFIED from its log):

- Playwright started its own Vite server on 127.0.0.1:5950 and stopped it at
  the end; nothing listened on 5950 afterwards. Port 5186 had no listener when
  checked before the runs and again after them, and was not touched.
- The run needed the network: `e2e/ready.ts:40-47` fails a test when no Inter
  face could be fetched from Google Fonts. It did not fail, so the fonts
  loaded.
- The dev server logged browser console noise that did not fail any test:
  4 "ResizeObserver loop completed with undelivered notifications" errors
  (at 22:37:10, around the `graph.spec.ts` editor cases; with 3 workers the
  exact test is not known), 3 React Flow
  warnings that a parent container had no width and height, and 53 React Flow
  attribution warnings.
- Calling `npx playwright test` directly skips the `pretest:e2e` asset sync;
  the build step just before it had run the same sync (`04-build.log`).

Side effects of these commands (VERIFIED): the build rewrote the ignored
folder `prototypes/dist`; `scripts/sync-assets.mjs` overwrote the ignored
`prototypes/public/ds` in place; `tsc -b` rewrote the three ignored
`prototypes/node_modules/.tmp/*.tsbuildinfo` files; Playwright wrote only to
`C:/Users/123ba/AppData/Local/Temp/pw-fyp-audit`. `git status` stayed empty.

Not run during this audit:

- The engine suite in `wasm-arch` (`yarn test` inside Docker, which `ci.yml`
  runs). Docker is installed, but the task did not ask for it.
- The 9 test files (92 cases by grep) on the local-only branch
  `bj/engine-package-spike`. That branch has no CI runs (VERIFIED: 0 runs).
- The four standalone repositories' tests (graph-algorithm-visualizer: 24
  test files; graph-visualizer-v2: 55 including 13 specs; tree-visualizer: 90;
  sorting-algorithm-visualizer: 18; counted by file name only).
- `npm run screenshots` and the manual checklists (Section 5.2).

Deployed site, probed with `curl` at 2026-11-01 22:46 (UTC+07:00), VERIFIED:
`https://kerktaiheng.github.io/visualgo-plus-design/` answered 200 (title
"VisuAlgo+"), `/engine/` answered 200, and the deep link `/bst/avl`
answered HTTP 404 with a body identical to the index page (same MD5). That is
the `404.html` fallback the build writes on purpose (`scripts/static-fallback.mjs`).
I did not open the deployed site in a browser.

## 3. What exists as files (inventory)

### 3.1 Unit tests per folder

Files are counted with `git ls-files` (VERIFIED). "Cases at run time" come
from the audit runs in Section 2 (VERIFIED). The graph uses Node's built-in
`node:test`, run through `node --experimental-strip-types --test
"src/graph/**/*.test.ts"`; the other folders use vitest 4 (`vite.config.ts`
includes `src/**/*.test.{ts,tsx}` and excludes `src/graph/**`).

| Folder | Runner | Test files | Cases at run time | Passed in the audit |
| --- | --- | ---: | ---: | ---: |
| `src/graph` | node:test | 93 | 654 | 654 |
| `src/tree` | vitest | 187 | 1,881 | 1,881 |
| `src/shared` | vitest | 15 | 143 | 143 |
| `src/sorting` | vitest | 32 | 571 | 571 |
| `src/site` | vitest | 1 | 24 | 24 |
| **Total** | | **328** | **3,273** | **3,273** |

A grep finds 647 `test(` calls in the graph files; 7 of them sit inside
loops over `directed` in `[true, false]`, so they run twice, which gives the
654 cases (VERIFIED by reading the
loops, for example `src/graph/algorithms/signedWeightInput.test.ts:26`).

Biggest subfolders (vitest, from the JSON run; graph by grep):

| Subfolder | Files | Cases |
| --- | ---: | ---: |
| `src/graph/algorithms` | 51 | 391 (static) |
| `src/graph/graph`, `app`, `components`, `editor`, `visualization`, `tests` | 8 / 10 / 9 / 7 / 7 / 1 | 59 / 53 / 47 / 43 / 45 / 9 (static) |
| `src/tree/algorithms` | 86 | 913 |
| `src/tree/components` | 35 | 260 |
| `src/tree/app` | 11 | 238 |
| `src/tree/samples` | 1 | 124 |
| `src/tree/editor` | 21 | 113 |
| `src/tree/segment` | 7 | 98 |
| other tree (`tree`, `heap`, `trie`, `visualization`, `styles`) | 26 | 135 |
| `src/sorting/algorithms` / `app` / `comparison` / `visualization` | 3 / 9 / 7 / 6 | 178 / 151 / 85 / 78 |
| other sorting (`animation`, `components`, `engine`, `input`) | 7 | 79 |
| `src/shared/components` / `app` / `styles` / `visualization` | 7 / 2 / 2 / 4 | 92 / 20 / 16 / 15 |

What kind of tests these are (VERIFIED by grep, counts approximate):

- 271 `.test.ts` and 57 `.test.tsx` files; 47 files run in a fake DOM
  (`// @vitest-environment happy-dom`), so component tests do not use a real
  browser.
- 13 test files generate seeded random inputs (graph 4, shared 1, tree 8).
  Example: `src/tree/algorithms/heap/createHeapCreateSequence.test.ts:166`
  builds 200 random lists per order.
- Some tests compare an engine with an independent oracle: an all-pairs
  oracle for Bellman-Ford (`createBellmanFordSequence.test.ts:224-254`) and an
  exhaustive search for Prim (`primEngine.test.ts:278`). 8 test files mention
  a brute force, oracle or naive check.
- Type-level contract test: `src/graph/tests/primContracts.typecheck.ts`,
  checked by `tsc -b` (included by `tsconfig.app.json` and `tsconfig.test.json`).
- TypeScript is `strict` with `noUnusedLocals` and `noUnusedParameters`
  (`tsconfig.app.json:22-24`); the test config extends it and also checks
  `e2e/**/*.ts` and `playwright.config.ts`.
- Lint is oxlint with the `react`, `typescript` and `oxc` plugins on top of
  its defaults; `.oxlintrc.json` sets two React rules: `rules-of-hooks`
  as an error and `only-export-components` as a warning.
- No coverage tool: no `@vitest/coverage-*`, `c8`, `nyc` or `istanbul`
  entry in `package-lock.json`, and no `coverage` setting. So there is no code
  coverage figure anywhere.
- No property-testing library (no `fast-check`); the randomized tests are
  hand-written.

### 3.2 Browser specs (Playwright, `prototypes/e2e`)

One project, `chromium` (Desktop Chrome, 1280 x 900 viewport), against the
dev server (`playwright.config.ts`). "grep" is `grep -c "^test("`; "listed"
is what `playwright test --list` reported; loops and one `test.describe`
make the difference. All VERIFIED.

| Spec | grep | Listed | Lines | What the titles cover |
| --- | ---: | ---: | ---: | --- |
| `bellman-ford.spec.ts` | 0 | 2 | 32 | `/sssp` and `/graph-editor` deep-link to Bellman-Ford and run the signed sample |
| `chrome.spec.ts` | 4 | 4 | 93 | Search text in every theme, the Privacy panel, a modal by keyboard, footer and bar contents |
| `dijkstra.spec.ts` | 8 | 8 | 309 | Dijkstra step notes on `/sssp` (DD-61): text, colour, placement, 1366 x 768 with the legend open |
| `drawing.spec.ts` | 4 | 4 | 114 | The tree, the graph and the sorting canvas really draw; React Flow follows the site theme |
| `graph-traversal.spec.ts` | 10 | 10 | 421 | Topological Sort (DFS, Kahn), Bipartite Graph Check, Cut Vertex & Bridge on CP4 samples |
| `graph.spec.ts` | 10 | 15 | 397 | Each graph card's route, switching, a run under the site chrome, Speed timer (DD-17), legend pass-through (DD-13), Graph Editor through eleven algorithms, tab strip in view (DD-54) |
| `home.spec.ts` | 12 | 12 | 226 | The homepage grid, editor cards, search, links, unknown routes, theme persistence |
| `journey.spec.ts` | 8 | 8 | 245 | Every card in one session, back and forward, full screen, build base for assets, favicon, card pictures |
| `paused-motion.spec.ts` | 3 | 4 | 75 | The "Animate paused steps" setting, reduced motion, sorting without it |
| `play.spec.ts` | 1 | 1 | 81 | Autoplay starts a run in each visualizer; a refused start shows the Action panel |
| `prim.spec.ts` | 3 | 5 | 172 | Prim routes, MST defaults to Kruskal, runs cancelled cleanly, nav reachable at desktop widths |
| `sorting.spec.ts` | 11 | 11 | 213 | Mount, nav, deep links, Compare panes, run lifecycle, restart plays (SP-01), theme on the canvas |
| `themes.spec.ts` | 2 | 5 | 283 | Text contrast at least 4.5:1 (WCAG ratio computed in the page) on three pages and the homepage in every theme; partner logos |
| `tree.spec.ts` | 51 | 62 | 2,291 | BST, AVL, Binary Heap (TP-33), LCA / Binary Lifting, Segment Tree, Trie, Tree Editor routes; step notes (TP-36) |
| **Total** | **127** | **151** | **4,952** | |

Helpers, not specs: `canvasLegend.ts`, `helpers.ts`, `ready.ts` (waits for
the page and for Inter), `settings.ts`, `stepNotes.ts`. All 151 titles are in
Appendix A.

Limits of the suite (VERIFIED from the config): Chromium only, no Firefox or
WebKit; desktop viewports only; no retries configured; locally 3 workers and
no traces; on CI default workers (the last run used 1), an HTML report,
traces kept on failure and screenshots on failure (`playwright.config.ts`,
changed by Bao in `a5bb08f`, 2026-10-28).

### 3.3 CI workflows (`.github/workflows`)

All VERIFIED by reading the files and `git log --follow`.

| Workflow | Runs on | What it runs | Node | Written by |
| --- | --- | --- | --- | --- |
| `app.yml` | Push to `main`/`master` and pull requests that touch `prototypes/**`, `design/design-system/**`, the root `package*.json` or the file itself | Job "Lint, types, unit tests, build": `npm ci`, `npm run lint`, `npm run typecheck`, `npm test`, `npm run build`, and on PRs `git diff --check` against the base. Job "Browser suite": `npm ci`, a cached `npx playwright install --with-deps chromium`, `npm run test:e2e`, and on failure an upload of `test-results` and `playwright-report` | 22 (the last run got v22.23.4) | Kerk, `0394b64` (2026-10-18). It replaced `prototypes.yml`, which Bao created in `37075b1` (2026-09-20) and extended in `7b16bf3`, `238f603`, `d82a24c` |
| `ci.yml` | Push to `main`/`master` and every PR | Docker build of `wasm-arch` up to the `test` stage, which runs `yarn test` (Node tests, then Python tests) for Kerk's engine | inside Docker | Kerk, `b3e86ba` (2026-09-03), `8a59115`, `df99dac` |
| `pages.yml` | Push to `main`/`master`, PRs that change the file, manual dispatch | Builds the engine demo in Docker into `site/engine`, builds the app with `VA_BASE=/<repo>/`, copies `prototypes/dist` to the site root, uploads it, and deploys to GitHub Pages (not on PRs) | 22 | Kerk, all five commits: `b3e86ba` (2026-09-03), `8a59115`, `df99dac`, `c39b3cf`, `0394b64` (2026-10-18) |

No workflow runs `npm run screenshots`, a benchmark, a profiler, an
accessibility scanner or a coverage report (VERIFIED). The app's minimum
Node is 22.12 (`package.json` `engines`); CI asks for "22", so CI does not
pin the floor itself (INFERENCE: any 22.x at or above 22.12 passes it).

### 3.4 Scripts (`prototypes/scripts`)

| Script | What it does | When it runs |
| --- | --- | --- |
| `sync-assets.mjs` | Copies the design system's static assets into the ignored `public/ds` | Before `dev`, `build` and `test:e2e` (npm `pre` scripts) |
| `static-fallback.mjs` | Writes `dist/404.html` and `dist/_redirects` so deep links work on static hosts | After `build` |
| `screenshots.mjs` | Takes review captures into `docs/screenshots`, with the dev server already running | By hand only (`npm run screenshots`); no captures are committed (0 image files tracked under `prototypes/docs`) |

All VERIFIED. There is no profile, benchmark or mutation script in the app
today (VERIFIED: the `scripts` block of `prototypes/package.json` and
`git ls-files prototypes/scripts`).

### 3.5 Who wrote the test code

Line attribution by `git blame -w -M` at `662e7b3` (follows file renames;
VERIFIED). Blame shows the author of the last commit that changed each line.
It cannot show pairing, review or AI help.

| Test code | Lines by BJoozz (123baoek31@gmail.com) | Lines by Kerk Tai Heng |
| --- | ---: | ---: |
| 14 e2e specs | 4,887 | 65 |
| `src/graph` tests | 17,479 | 146 |
| `src/tree` tests | 25,955 | 136 |
| `src/sorting` tests | 6,615 | 12 |
| `src/shared` tests | 2,611 | 103 |
| `src/site` tests | 366 | 5 |

Non-merge commits on `main` that touch a test or spec file (VERIFIED from
the `Co-Authored-By` trailers): BJoozz 159 (148 with a Claude co-author
trailer, 11 without), Kerk Tai Heng 10 (all 10 with a Claude trailer). The
models named are Claude Fable 5.1 (69), Claude Opus 5.5 (63), Claude Opus 5
(1M context) (23), Claude Opus 5 (2) and Claude Fable 5 (1). The 11 without
a trailer are the Bellman-Ford and Prim stages of 2026-10-03 to 2026-10-05
(`aef5d0b`, `0aac567`, `6417767`, `4bd0879`, `5428ed3`, `686c06b`,
`65634cf`, `490e1d1`), two commits of 2026-09-21 (`c458755`, `75d9760`) and
`3a6443b` (2026-10-15).

QUESTION: the blame shows only the `123baoek31@gmail.com` identity for Bao;
please confirm that both BJoozz identities are yours.

## 4. CI history (GitHub Actions)

Source: `gh run list` (limit 60, then limit 1000) and `gh run view` on
2026-11-01. All VERIFIED. Times are UTC.

### 4.1 All runs, 2026-09-04 to 2026-10-30 (266 runs)

| Workflow | Success | Failure | Cancelled | Active period |
| --- | ---: | ---: | ---: | --- |
| `ci` (engine) | 112 | 1 | 0 | 2026-09-04 to 2026-10-30 |
| `pages` | 43 | 2 | 3 | 2026-09-04 to 2026-10-30 |
| `prototypes` (old, per app copy) | 41 | 4 | 5 | 2026-09-20 to 2026-10-18 |
| `app` (current) | 49 | 1 | 5 | 2026-10-18 to 2026-10-30 |

The last 60 runs (2026-10-22 18:32 to 2026-10-30 17:04): `app` 23 success,
1 failure, 2 cancelled; `ci` 26 success; `pages` 6 success, 2 cancelled.
26 were pushes to `main`, 34 were pull requests. There were no runs after
2026-10-30 17:04.

Every cancelled run in the last 60 is a `main` push replaced within a minute
by the next merge (`concurrency: cancel-in-progress`): `ad5e119` by `4dedee1`
and `f58ed5f` by `662e7b3`.

### 4.2 Every failed run

| Date | Workflow, ref | Failed job / step | Cause and fix |
| --- | --- | --- | --- |
| 2026-09-04 | `pages`, `main` `69aa8e4` (Kerk) | deploy, `actions/deploy-pages@v4` | Not checked further; `pages` passed again at `df99dac` (2026-09-14) |
| 2026-09-13 | `ci` and `pages`, `main` `598193b` (Kerk) | The Docker build step of each | Both passed at `df99dac` (Kerk, "Restore wasm-arch/scripts and update workflow actions for Pages") |
| 2026-09-23 | `prototypes`, PR `bj/tree-wireframe-v2-v7` `05b4b4a` (Bao) | "Whitespace errors introduced by this change" | Passed on the next push `1af2c72`, 7 minutes later |
| 2026-10-10 | `prototypes`, `main` `c620145` (Bao) | Tree browser suites (split-rails and docks) | "BST Traversal at 864x768 with long values" failed with its retry |
| 2026-10-14 | `prototypes`, `main` `c3f6508` (Bao) | Same | Same test |
| 2026-10-14 | `prototypes`, `main` `f510477` (Bao) | Same | Same test. Fixed by PR #7 (`3a6443b`): the test assumed a 20-character label must overflow, but it fits with CI's Linux fonts. `main` passed again at `fb0b6a9` |
| 2026-10-25 | `app`, PR `bj/dijkstra-step-notes` `b47d437` (Bao) | Browser suite: 1 failed, 147 passed (6.4 m) | `tree.spec.ts:1112` (an LCA note over the open legend, TP-36). Fixed in `b309309` 11 minutes later: "Inter's metrics differ by a pixel between Windows and CI's Linux", so the pin became a bound |

So `main` was red in the old `prototypes` workflow for three pushes in a row
(2026-10-10 to 2026-10-14). Both browser-suite failure episodes (the traversal
chip test, three runs on `main`; the LCA note pin, one PR run)
came from text metrics that differ between Windows and Linux. The failing
tests are VERIFIED from the logs; the cause is DOCUMENTED in `b309309` and PR #7.

### 4.3 Pull requests

`gh pr list --state all` shows the final check state of each PR's last
commit. All 36 merged PRs (#1 to #37 except #5, closed without checks) show
no failed check; the Pages deploy job shows as skipped on #18 and #20, as
`pages.yml` intends for PRs (VERIFIED). This view hides earlier failures inside a PR;
for example the `b47d437` failure in PR #32 is visible only in the run list.

The current `main`, `662e7b3`: `app` run 41095633732 passed, with 654
node:test cases, 235 vitest files / 2,619 tests, and "151 passed (7.5m)" in
the browser job using 1 worker on Node v22.23.4; `pages` run 41095633645
built and deployed (deploy finished 2026-10-30 17:06:54); `ci` run
41095633621 passed (VERIFIED from the run logs).

### 4.4 Test counts the PR bodies record (DOCUMENTED)

These numbers are what each PR author wrote about local runs. They were not
re-run here, but the CI runs of those PRs passed (VERIFIED, Section 4.3).

| PR (author) | Merged | Unit: graph + vitest | Browser suite | Notes in the PR |
| --- | --- | --- | --- | --- |
| #20 (Kerk) | 2026-10-18 | 545 + 2,217 | 83/83 | "The first runs had 12-16 failures from `net::ERR_NETWORK_CHANGED`... All of them passed on rerun." |
| #21 (Kerk) | 2026-10-18 | 545 + 2,203 | 83/83 | "Two sorting tests timed out under load and passed when rerun alone." |
| #23 (Bao) | 2026-10-19 | 543 + 2,226 | 90/90, twice | |
| #24 | 2026-10-19 | 543 + 2,241 | 92/92 | |
| #25, #26 | 2026-10-20 | 543 + 2,411 | 106/106 | |
| #27 | 2026-10-20 | not stated | 107/107 | |
| #28 | 2026-10-22 | 626 + 2,421 | 117/117 | "seeded property tests" against independent checks |
| #29 | 2026-10-24 | 626 + 2,462 | 123/123 | |
| #30, #31 | 2026-10-24 | 626 + 2,603 | 140/140 | |
| #32 | 2026-10-26 | 650 + 2,615 | 148/148 | |
| #33 | 2026-10-26 | 650 + 2,616 | 148/148 | |
| #34 | 2026-10-30 | 650 + vitest | 83/83, three specs only | |
| #35 | 2026-10-30 | 650 + 2,616 | 149/149 | |
| #37 | 2026-10-30 | 654 + 2,619 | 150/150 | |
| This audit | 2026-11-01 | 654 + 2,619 | 151/151 | VERIFIED |

Every PR from #22 onward is Bao's (VERIFIED). The audit's 151 against #37's 150:
the head of #37 (`9baa117`) had 126 top-level `test(` calls and `main` has
127; the extra case is the tab-strip test of PR #35 (`graph.spec.ts:299`),
which joined #37's line in the merge `6fa4981` (VERIFIED by counting at both
commits). The two lint warnings in `src/site/ModuleBar.tsx` are named as
"existing" in #20, #21, #28 and #29 and were still there in this audit.

Older records also show partial passes. `37075b1` (Bao, 2026-09-20) says
"288/293 unit tests, and 34/36 Playwright tests. Existing dock layout issues
remain outside this change." PR #11 says five tree tests failed while the
machine's network was suspended and passed on a rerun. (DOCUMENTED)

### 4.5 The browser coverage cut of 2026-10-18

Counted with `git ls-tree` (VERIFIED):

| Commit | App copies | Spec files | `test(` lines in specs | Unit test files |
| --- | ---: | ---: | ---: | ---: |
| `0394b64^` (before) | 12 (3 layouts x graph, tree, sorting, plus 3 sites) | 208 | 1,162 | 843 |
| the kept layout only, before | 4 (`*-groups`, `visualgo-web-groups`) | 74 | | 285 |
| `0394b64` (Kerk, 2026-10-18) | 1 | 12 | 70 | 274 |
| `662e7b3` (now) | 1 | 14 | 135 | 328 |

The unit tests of the kept layout survived: 285 files became 274, which fits
the commit message's "one copy of their tests" for the 40 shared files
(INFERENCE). The browser
specs did not: the graph's 41, the tree's 11 and the sorting's 10 specs were
deleted, and only the site's 12 specs stayed (VERIFIED: the same 12 file
names as `visualgo-web-groups/e2e`). Since then Bao added
`graph-traversal.spec.ts` (`b88952d`, 2026-10-21) and `dijkstra.spec.ts`
(`6b1a4fc`, 2026-10-25). The commit message says:
"Their standalone pages, entry points, the graph sandbox and their browser
suites are gone; the site's suite, which drives every route, stays."
(DOCUMENTED). The guides list what the deleted suites covered, for example
`docs/graph/DEVELOPER_GUIDE.md:194` onward ("The graph prototype's own suite
went with the standalone builds on 2026-10-18. Until then it also covered:
...").

QUESTION: `0394b64` opens with "The owner's decision of 2026-10-18: V10 wins
and everything else goes." Whose decision was it, Bao's or Kerk's? Was
dropping the module browser suites part of that decision?

## 5. Validation beyond the automated tests

### 5.1 Acceptance records (`prototypes/docs/graph/*_ACCEPTANCE.md`)

Only two exist, both for the graph; there are none for the tree or sorting
modules (VERIFIED). Both were written by Bao in the standalone builds and
moved into the app by Kerk's `0394b64` (VERIFIED with `git log --follow`:
Bellman-Ford from `6417767` 2026-10-04, Prim from `490e1d1` 2026-10-05; last
edited by Bao in `02c4e12`, 2026-10-30). Their content is DOCUMENTED:

| Record | What it records | Can it be re-run today? |
| --- | --- | --- |
| `BELLMAN_FORD_ACCEPTANCE.md` (stage E, 2026-10-04) | Checks "the original A-E plan, Codex's, which the owner asked for but has not reviewed" against the code. Gates: unit 392 (V2) / 408 (V7), browser 78 / 86, hosted route checks 2 / 2. "Timeline measurements" (2026-10-03, Node 24.17.0, median of 3): 4 cases of 40 nodes, 243 to 25,684 frames, 1.94 to 139.16 ms to generate, 0.30 to 32.05 MiB retained heap. Its own caveat: "These are observations, not guarantees or supported limits." | No. `scripts/bellman-ford-profile.mjs` "went with the standalone builds on 2026-10-18" (the record says so; VERIFIED absent from the app) |
| `PRIM_ACCEPTANCE.md` (2026-10-05) | Final gates: graph V2 450 unit / 90 browser, V7 466 / 98, the two sites 22 / 75 each. A nine-theme sweep: inspector text and node labels at least 4.5:1, strokes and swatches at least 3:1, with one exception (Classic's accepted stroke, 2.84:1, left in the backlog). A core and timeline profile (4 fixtures, warm medians, i9-13900H, Node 24.17.0; for example "Dense" timeline 27.495 / 26.717 ms) and an inspector profile (React render medians 0.7 to 26.6 ms). "The eight engine mutants were caught again using the V2 mutation tool." | No. `prim-profile.mjs`, `prim-inspector-profile.mjs`, `prim-mutations.mjs` and `e2e/prim-acceptance.spec.ts` went with the standalone builds (VERIFIED: the mutation script exists only in deleted app copies in history) |

The oracle unit tests these records rely on are still in the app and passed
in this audit (VERIFIED: `createBellmanFordSequence.test.ts`,
`primEngine.test.ts`, `minHeap.test.ts` and the other files that
`docs/graph/DEVELOPER_GUIDE.md:314-363` names all exist).

QUESTION: the Bellman-Ford record says the A-E plan was Codex's, and the 8
Bellman-Ford and Prim stage commits (3 + 5, listed in 3.5) carry no co-author
trailer. Which tools, if any, helped
with these commits? (Fact only, for the report's AI-use statement.)

### 5.2 Manual checklists

| Guide | Section | Items |
| --- | --- | ---: |
| `docs/graph/DEVELOPER_GUIDE.md` | "Manual checklist for the page", line 266 | 20 check boxes |
| `docs/sorting/DEVELOPER_GUIDE.md` | "Manual checklist for the page", line 111 | 10 check boxes |
| `docs/tree/DEVELOPER_GUIDE.md` | "Checklist for a page change", line 493 | 26 bullets |

VERIFIED: every box is unticked (`- [ ]`; no `- [x]` anywhere in the repo),
and no file records a dated run of these checklists. The groups shell's drag,
split and splitter scenarios are manual on purpose: "the owner, 2026-10-28:
guides only, no new shell e2e - review S2-02" (DOCUMENTED, PR #36).

QUESTION: did you go through these checklists, and when? If so, is there a
record (notes, screenshots) outside the repository?

### 5.3 Review sessions of 2026-10-26 to 2026-10-30

The repository keeps no review documents; the findings are known from the
PR bodies and commit messages (DOCUMENTED), and the fixes and their tests
are in the code (VERIFIED). PRs #34, #35 and #37 say the findings were "reproduced
before the fix".

| Session (review date) | Findings | PR, commit | Tests that hold the fix (VERIFIED to exist and pass) |
| --- | --- | --- | --- |
| 1 (2026-10-26) | F01 a browser case fails without Google Fonts; F02 Node floor; F03 root scripts swallowed flags; F04 CI uploaded traces that were never written | #34, `a5bb08f` | `e2e/ready.ts:40-47`, the Inter guard (10 of the 14 specs import `ready.ts`); config only for F02 to F04 |
| 2 (2026-10-27) | S2-01 a side strip hid its front tab when narrowed; S2-02 no new shell e2e, guides only (owner 2026-10-28); docs sweep and the shell copy rule retired | #35 `fd9ff5c`; #36 | `e2e/graph.spec.ts:299` (DD-54) |
| 3 (2026-10-29) | S3-01 the graph stalled while Speed kept changing; S3-02 a sorting restart did not always play; S3-03 stale records | #37, `9baa117` | `src/graph/visualization/playbackCountdown.test.ts`, `e2e/graph.spec.ts:113` (DD-17), `e2e/sorting.spec.ts:107` (SP-01) |

The code cites these reviews at `e2e/graph.spec.ts:104` and `:294`,
`src/graph/visualization/playbackCountdown.test.ts:17`,
`src/shared/components/layout/GroupView.tsx:100` and
`docs/graph/DESIGN_DECISIONS.md:29` (VERIFIED by `git grep "review of 2026-10"`).

QUESTION: who produced the findings of these three reviews (a person or a
tool)? The repository does not say.

QUESTION: PR #37 (finding S3-03) calls `a074f50` "the owner's commit
(2026-10-21)". Its author is Kerk Tai Heng (VERIFIED). Who is "the owner"
there?

### 5.4 Measured numbers in the DD / TP / SP records

The design records hold many measurements taken in the page; the ones I read
are layout geometry in pixels, not timings (counts VERIFIED by `grep -c`):

| Record | Lines with "measur..." | Lines with a px number (designed and measured sizes together) |
| --- | ---: | ---: |
| `docs/graph/DESIGN_DECISIONS.md` (DD) | 14 | 110 |
| `docs/tree/DESIGN_DECISIONS.md` (TP) | 16 | 184 |
| `docs/sorting/DESIGN_DECISIONS.md` (SP) | 6 | 27 |

Examples (DOCUMENTED): graph DD-61, line 2734: "Measured on the page default
at 1440 x 900, every note is centred over its vertex within 0.01px"; sorting,
line 397: "Measured in this copy with the rule removed, on 2026-10-17: 403 of
798 on load"; tree, line 3420: "measured 70.1 to 78.3px". Several of these
numbers are pinned in the browser suite as bounds, because Windows and Linux
fonts differ by about a pixel (DOCUMENTED in `b309309`). The millisecond
values in the records (for example "each wave at most 420ms", graph line 547)
are chosen design durations, not measurements (VERIFIED by reading them).

Contrast is measured, not assumed: `e2e/themes.spec.ts` computes the WCAG
ratio of a small sample of chrome text against the first ancestor with an
opaque background, in all nine themes, and needs 4.5:1
(VERIFIED in code, lines 5-58; it passed in this audit). Unit
tests on colour contrast: `src/shared/styles/floatingTextTones.test.ts`,
`src/sorting/visualization/sortPalette.test.ts`,
`src/sorting/visualization/themePalette.test.ts`. There is no axe-core or
other automated accessibility audit, and the Prim record says its sweep "is
not a full accessibility certification".

### 5.5 `docs/sorting/sorting-performance-milestone.md`

VERIFIED: this file is a copy, identical except for line endings, of
`docs/performance-milestone.md` in Bao's standalone repository
sorting-algorithm-visualizer (one commit, `9236a65`, 2026-08-19). Its tables
were "captured on 2026-08-13 with Node v24.17.0" and are called "development
diagnostics" that "do not measure browser FPS, Canvas rasterization, React
commit time, or GPU work" (DOCUMENTED). Line 70 says to run
`npm run profile`; the app has no such script, and `scripts/profile-sorting.mjs`
exists only in the standalone repository (VERIFIED). So these numbers describe
the standalone sorting engine before it joined this project (INFERENCE from
the dates: the capture is three weeks older than this repository's first
commit of 2026-09-03).

## 6. What does not exist

Searched with `git grep -i -F` over every tracked file of the main repository
at `662e7b3` (not the standalone clones or other branches), except
`package-lock.json`, on 2026-11-01 (VERIFIED):

| Term | Hits | What the hits are |
| --- | ---: | --- |
| `benchmark` | 10 | Non-goals and future work only: "No checkpoints, bounded-history policy, Web Workers, benchmark mode" (sorting note, line 155); "Do not implement advanced benchmarking until explicitly requested" (`docs/sorting/sorting-submodule-AGENTS.md:629`); a wireframe note that the page "never puts a stopwatch" next to a count |
| `user study`, `user studies` | 0 | |
| `participants` | 17 | AVL "rotation participants" (tree nodes) in the tree records and code; no people |
| `ms per` | 1 | A false match inside "algorithms persist" (`design/proposals/sorting-v2-v7/README.md:469`) |
| `usability`, `questionnaire`, `think-aloud`, `user test` | 0 | |
| `survey` | 2 | "Surveyed from visualgo.net" (the module list), not a survey of people |
| `lighthouse`, `web vitals`, `frames per second` | 0 | |
| `fps` | 2 | The sorting note says it does not measure FPS; a design-system wireframe file |
| `performance` | 22 | The dated profiles of Sections 5.1 and 5.5, design notes about performance debt, a few code comments and e-Lecture slide text |
| `feedback` | 25 | UI feedback components (alerts, overlays) and drag-and-drop feedback; none is feedback from people |
| `teacher`, `supervisor`, `classroom`, `learning outcome`, `student feedback`, `students said` | 0 | |
| `lecturer` | 11 | The design system's description of visualgo.net's lecturer-only features and a test-mode UI kit |
| `pilot` | 2 | A paused-step design "after a pilot on BFS, Kruskal and Max Flow" (graph DD line 883), then used in the tree (line 1070): a trial implementation, not a pilot study with people |

So, in the repository today:

- no user study, usability test, interview, survey of users or participant
  data; no feedback from students or teachers; no measure of learning or
  educational benefit;
- no benchmark suite and no performance test in CI; no measurement of frame
  rate, load time or memory in a browser for the current app;
- no code-coverage figure (no coverage tool is installed);
- no automated accessibility audit; contrast is checked for a sample of
  text only (Section 5.4);
- no cross-browser testing (Chromium only) and no mobile viewport testing
  ("desktop and laptop screens" are the stated target, DOCUMENTED in
  `docs/graph/AGENTS.md:36-43` and its tree and sorting twins; the literal
  viewports in the specs run from 720 x 900 to 1920 x 1080, VERIFIED).

Timing numbers exist only as dated development observations (VERIFIED):
the micro-profiles of 2026-08-13 (sorting, standalone repo), 2026-10-03
(Bellman-Ford) and 2026-10-05 (Prim), each called an observation and not a
limit, none of whose scripts is in the app any more; and a few single
readings in the design proposals, for example Prim stage B's single samples
(`design/proposals/prim-v2-v7/README.md:160`, in Vietnamese), a canvas refit
"measured 382 to 401ms" (`design/proposals/viz-shell-v10/README.md:608`) and
"about 5 ms warm" for the default sorting set
(`design/proposals/sorting-v2-v7/README.md:349`).

## 7. Discrepancies found during the audit

All VERIFIED by reading the files at `662e7b3`:

| Where | What it says | What is true |
| --- | --- | --- |
| `docs/graph/DEVELOPER_GUIDE.md:28` | "Use Node.js 20.19 or newer" | `package.json` `engines` is `>=22.12`; `README.md:8` and `prototypes/AGENTS.md:24` say 22.12. The graph tests need `--experimental-strip-types` |
| `docs/tree/DEVELOPER_GUIDE.md:30-31` | The groups shell files "must stay identical" and the `cmp` loop is in `AGENTS.md` | `docs/tree/AGENTS.md:142` says the owner retired that rule; the shell lives once in `src/shared` |
| `docs/tree/DEVELOPER_GUIDE.md:25` | "every spec waits for it [Inter] in `ready()`" | 10 of the 14 specs import `ready.ts`; `bellman-ford`, `chrome`, `graph-traversal` and `prim` never call it, directly or through a helper (INFERENCE: they may not measure text, so this may not matter) |
| `docs/sorting/sorting-performance-milestone.md:70` | "Run: `npm run profile`" | The app has no `profile` script (Section 5.5) |
| PR #37 body | "full browser suite 150/150" | True for its branch head; `main` has 151 cases after the merge (Section 4.4) |

Other caveats for the report (VERIFIED unless marked):

- Local runs and CI differ: locally 3 workers, list reporter, no traces; on
  CI default workers (1 in the last run), traces and an HTML report on
  failure. Local runs are on Windows, CI on Ubuntu.
- The browser suite needs internet access to Google Fonts (`e2e/ready.ts`).
- Several PR bodies report flaky local failures caused by the machine
  (network changes, a suspended network, load). These are DOCUMENTED
  (PRs #11, #20, #21), and none happened in this audit's run.

## 8. Questions for Bao

1. Both BJoozz identities: please confirm both are yours. Blame of the test
   code shows only `123baoek31@gmail.com` (Section 3.5).
2. `0394b64` (Kerk, 2026-10-18): "The owner's decision of 2026-10-18: V10
   wins and everything else goes." Whose decision, and did it include
   deleting the module browser suites (74 spec files in the kept layout
   became 12)? (Section 4.5)
3. PR #37 calls Kerk's `a074f50` (2026-10-21) "the owner's commit". Who is
   the owner there? (Section 5.3)
4. Who produced the review findings of 2026-10-26, 2026-10-27 and
   2026-10-29? (Section 5.3)
5. The 8 Bellman-Ford and Prim stage commits (2026-10-03 to 2026-10-05) carry
   no co-author trailer, and the Bellman-Ford record calls the plan Codex's.
   Which tools helped, if any? (Section 5.1)
6. Were the manual checklists ever run, and is there a record? (Section 5.2)
7. Should the report cite the dated micro-profiles? Their scripts are gone,
   so nobody can re-run them on the current app. (Sections 5.1, 5.5)
8. Should the engine suite (`wasm-arch`, Kerk's, run by `ci.yml`) and the 92
   cases on the local-only `bj/engine-package-spike` be run for the report?
   Neither was run in this audit. (Section 2)

## Appendix A. The 151 browser cases

As listed by `npx playwright test --list` on 2026-11-01 (VERIFIED), in the
form `spec:line:column  title`. All 151 passed in this audit's run.

```text
bellman-ford.spec.ts:6:3  sssp deep-links to Bellman-Ford and runs the signed sample
bellman-ford.spec.ts:6:3  graph-editor deep-links to Bellman-Ford and runs the signed sample
chrome.spec.ts:25:1  what you type into search is visible in every theme
chrome.spec.ts:51:1  the Privacy panel says what the site keeps, and no more
chrome.spec.ts:68:1  a modal can be opened and dismissed without a mouse
chrome.spec.ts:85:1  the footer offers only the privacy note, and the bar no Login
dijkstra.spec.ts:122:1  /sssp: a first reach writes its sum in green over the vertex it reaches, and the start, a selection, a settle and an inspection write none (DD-61)
dijkstra.spec.ts:149:1  /sssp: a settled target says so in red, an update says its comparison in green clear of the flashing badge and the weight it quotes, and Previous writes none while the flash replays (DD-61)
dijkstra.spec.ts:198:1  /sssp: on CP4 4.2 an equal candidate keeps its distance in red, saying its sum (DD-61)
dijkstra.spec.ts:206:1  /sssp: on CP4 4.2 a note whose places above and on the right hold weights goes below its vertex, not beside it nearer the next one (DD-61)
dijkstra.spec.ts:217:1  /sssp: on Large, fitted small, a note lies on no other vertex and sits nearest its own (DD-61)
dijkstra.spec.ts:234:1  /sssp: Parallel-edge improvement's update keeps off the 3 it quotes as it pops in, and off every mark over its life (DD-61)
dijkstra.spec.ts:248:1  /sssp: a theme picked and a vertex dragged while an update's note shows keep the same note, which moves with its vertex (DD-61)
dijkstra.spec.ts:282:1  /sssp at 1366 × 768: with D panned under the open legend, D's notes stay centred over D, drawn over the legend, and rise their whole 20px (DD-61)
drawing.spec.ts:26:1  the tree is drawn as a tree, not as a column of unpositioned nodes
drawing.spec.ts:50:1  the graph is drawn with positioned nodes too
drawing.spec.ts:60:1  sorting actually paints its canvas
drawing.spec.ts:89:1  React Flow follows the site theme, not the prototype default
graph-traversal.spec.ts:32:1  Topological Sort opens on its DFS method and swaps the listing for Kahn
graph-traversal.spec.ts:56:1  CP4 4.3 DAG ends on every vertex badged with its place, under both methods
graph-traversal.spec.ts:94:1  CP4 4.7 has no order: DFS ends on the cycle its back edge closed, Kahn on the vertices it left
graph-traversal.spec.ts:122:1  an undirected graph is refused when Autoplay starts the run, and the Directed box stays free
graph-traversal.spec.ts:170:1  Bipartite Graph Check opens on its DFS method, reads the graph undirected and swaps the listing for BFS
graph-traversal.spec.ts:214:1  CP4 4.20 ends bipartite under both methods, both sides badged A and B on solid faces, a root ringed once dequeued
graph-traversal.spec.ts:257:1  CP4 4.1 is not bipartite: each method ends on the odd cycle it found, drawn and listed
graph-traversal.spec.ts:316:1  Cut Vertex & Bridge opens with no Method, reads the graph undirected, and keeps its page on reload
graph-traversal.spec.ts:354:1  CP4 4.7 ends with its cut vertices ringed and its bridges marked, both listed in Status
graph-traversal.spec.ts:402:1  CP4 4.22: the second edge between 1 and 2 is a back edge to the parent, so the doubled edge is no bridge
graph.spec.ts:29:3  /graph-editor opens on Breadth-First Search
graph.spec.ts:29:3  /dfsbfs opens on Breadth-First Search
graph.spec.ts:29:3  /sssp opens on Dijkstra
graph.spec.ts:29:3  /mst opens on Kruskal
graph.spec.ts:29:3  /maxflow opens on Edmonds-Karp
graph.spec.ts:41:1  a card shows its own algorithms and not the whole visualizer
graph.spec.ts:53:1  switching within a card moves the URL and the selection together
graph.spec.ts:67:1  the old DFS id still lands on the stack variant, at its current URL
graph.spec.ts:80:1  a graph run plays under the site chrome
graph.spec.ts:113:1  /dfsbfs: Speed moved every 150ms keeps the run moving, and a resume after Pause waits a whole step (DD-17)
graph.spec.ts:151:1  /dfsbfs: the canvas legend lets the pointer through to the graph, a pan and a press started under it, and only Hide and the chip take it (DD-13)
graph.spec.ts:166:1  the theme chosen on the grid survives opening a graph card
graph.spec.ts:193:1  the Graph Editor keeps an edited graph through all eleven algorithms and runs each on it
graph.spec.ts:258:1  an editor shows its editor even when the visitor hid the Action panel on another card
graph.spec.ts:299:1  /dfsbfs: a side strip keeps its front tab in view when a splitter or the window narrows it, and leaves a strip the wheel moved (DD-54)
home.spec.ts:8:1  the homepage shows every module, and says which are not built
home.spec.ts:20:1  the editors have a section of their own above the grid, and only they are marked New
home.spec.ts:50:1  an editor card is one real link, and opens on its editor
home.spec.ts:84:1  a modified click on an editor card is left to the browser, so it opens a new tab
home.spec.ts:96:1  search finds a card by an algorithm it runs, and keeps only the sections with a match
home.spec.ts:141:1  exactly one top bar, one footer and one settings control
home.spec.ts:155:1  a coming-soon card does not open
home.spec.ts:165:1  the wordmark is the way home
home.spec.ts:173:1  a module URL is direct, and names the module after the language picker
home.spec.ts:181:1  an unknown module goes back to the grid rather than to an apology
home.spec.ts:189:1  the theme reaches the whole page and survives a reload
home.spec.ts:203:1  the theme survives a navigation into a module, and the menu agrees
journey.spec.ts:26:1  every card opens correctly in one session, whatever the order
journey.spec.ts:80:1  the grid and the modules survive repeated back and forward
journey.spec.ts:99:1  an algorithm from another card falls back to this one
journey.spec.ts:127:1  full screen hides the site bar and leaving restores it
journey.spec.ts:142:1  the module assets follow the build base rather than the domain root
journey.spec.ts:172:1  the favicon is in this build too
journey.spec.ts:183:1  every card has its picture, including the two the site draws itself
journey.spec.ts:215:1  the visualizer keeps its layout controls, and only inside the settings menu
paused-motion.spec.ts:23:1  the graph and tree pages share one choice, on until the visitor turns it off
paused-motion.spec.ts:44:3  when the system asks for reduced motion › the choice starts off, and the visitor can still turn it on
paused-motion.spec.ts:56:1  with no choice made, the item follows the system setting while the page is open
paused-motion.spec.ts:69:1  sorting, which has no paused motion, shows no such item
play.spec.ts:27:1  Autoplay starts a run from idle in each visualizer, and a refused start brings the Action panel back
prim.spec.ts:17:3  /mst/prim runs a signed forest under one host bar and unmounts cleanly
prim.spec.ts:17:3  /graph-editor/prim runs a signed forest under one host bar and unmounts cleanly
prim.spec.ts:50:1  MST is complete, defaults to Kruskal, and Prim stays within its module boundary
prim.spec.ts:72:1  Prim, Kruskal, Cut Vertex & Bridge and Dijkstra keep the authored graph and host theme while cancelling the previous run
prim.spec.ts:136:1  the hosted eleven-algorithm nav keeps Prim, HOME and site controls reachable at desktop widths, focus ring whole
sorting.spec.ts:13:1  the real visualizer mounts, with exactly one of each piece of chrome
sorting.spec.ts:27:1  the nav spells out the selected algorithm and abbreviates the rest
sorting.spec.ts:36:1  a deep link opens that algorithm
sorting.spec.ts:43:1  choosing an algorithm moves the URL with it
sorting.spec.ts:51:1  the pane control sits beside the algorithm nav, not across the bar
sorting.spec.ts:66:1  Compare takes the pane grid and drops the algorithm from the bar
sorting.spec.ts:79:1  the run plays, and leaving mid-run does not leave it running
sorting.spec.ts:107:1  a new pane count restarts the run playing, after Next then Autoplay, after Autoplay, and from the end (SP-01)
sorting.spec.ts:147:1  the site owns the theme, and it reaches the canvas
sorting.spec.ts:159:1  a deep link into a saved Compare set keeps every pane
sorting.spec.ts:181:1  the settings control does not cover the footer
themes.spec.ts:125:3  every theme keeps /sorting readable
themes.spec.ts:125:3  every theme keeps /bst readable
themes.spec.ts:125:3  every theme keeps /dfsbfs readable
themes.spec.ts:181:1  the homepage stays readable in every theme
themes.spec.ts:239:1  both partner logos show, and follow the theme
tree.spec.ts:28:3  /tree-editor opens on Binary Lifting, with one frame
tree.spec.ts:28:3  /bst opens on Binary Search Tree, with one frame
tree.spec.ts:28:3  /heap opens on Binary Heap, with one frame
tree.spec.ts:28:3  /segmenttree opens on Range Sum, with one frame
tree.spec.ts:28:3  /trie opens on Trie, with one frame
tree.spec.ts:28:3  /lca opens on Binary Lifting, with one frame
tree.spec.ts:51:1  a card shows its own algorithms and not the whole visualizer
tree.spec.ts:67:1  /segmenttree switches to Range Sum (lazy), its own workspace, and back, each keeping its own array
tree.spec.ts:151:1  moving between cards through the grid lands on each card own algorithm
tree.spec.ts:183:1  the theme chosen on the grid survives opening a tree card
tree.spec.ts:212:1  leaving a tree module mid-run leaves nothing running
tree.spec.ts:244:1  the Tree Editor keeps an edited tree across LCA, BST and AVL, and runs each on it
tree.spec.ts:284:1  /lca runs Preprocessing to its end, then Query on the u and v chosen, each as its own run (TP-31)
tree.spec.ts:329:1  /lca: a hovered node shows its path to the root and its 2^k-th ancestors while the run rests (TP-32)
tree.spec.ts:463:1  /lca: the hover needs no run, ignores Animate paused steps and reduced motion, and starts no easing (TP-32)
tree.spec.ts:565:1  /lca: a step's note floats over the drawing as the step arrives, red over the ancestor u and v share, none on Previous (TP-34)
tree.spec.ts:628:1  /lca: a depth check says keep in red and lift in green over the deeper cursor, then how far it went (TP-34)
tree.spec.ts:659:1  /lca: on Balanced · 31 nodes a note keeps its 14px while the drawing is at 0.43 (TP-34)
tree.spec.ts:680:1  /lca: with no room above a root drawn near the canvas's top, its note goes beside it and the column's note keeps off it (TP-34)
tree.spec.ts:715:1  /lca: Preprocessing says a filled column at the canvas's top centre, and a theme change replays no note (TP-34)
tree.spec.ts:797:1  /bst/avl: AVL Inspection writes a node's height and balance factor in ink, then its verdict in green or red (TP-36)
tree.spec.ts:823:1  /bst/avl: AVL Delete's note over the heavy child keeps clear of its parent's badge below, at rest and rising (TP-36)
tree.spec.ts:851:1  /bst/avl: on the Min AVL tree, where the row above's badge leaves no room, the heavy child's note settles clear of it and stays (TP-36)
tree.spec.ts:872:1  /bst: BST Delete says each comparison, the target's case and the removal, with no Comparison row in Status (TP-36)
tree.spec.ts:938:1  /bst: Search says each comparison in ink and the hit in green, a miss in red on MISS, with no Comparison row (TP-36)
tree.spec.ts:978:1  /bst: Lower Bound says the candidate in green over the node it leaves, and an end with no key ≥ v in red on NONE (TP-36)
tree.spec.ts:1017:1  /bst: Select writes each turn over the node that decided it, with the k the walk carries on (TP-36)
tree.spec.ts:1043:1  /bst: Predecessor of the smallest value climbs past the root and ends on NONE over v, in red (TP-36, TP-19)
tree.spec.ts:1071:1  /bst: a traversal writes the empty children and the end of a call in ink, nothing on a visit (TP-36)
tree.spec.ts:1103:1  /lca: at 1366 × 768 a note over a node panned under the open legend keeps its place, drawn over the legend, and a column's note the top centre (TP-36)
tree.spec.ts:1159:1  /lca: a note settling under the open legend stays over its node and rises its 20px into it, and the column's note keeps the top centre (TP-36)
tree.spec.ts:1219:1  /lca: the legend is on the canvas, top right, for the operation chosen, u and v in its one colour, and Status has none (TP-35)
tree.spec.ts:1315:1  /lca: the legend lets the pointer through to the tree, a pan and a hover started under it, and only Hide and the chip take it (TP-35)
tree.spec.ts:1333:1  the Segment Tree's +7 floats off its node as before, the number form unchanged (TP-20)
tree.spec.ts:1351:1  a tree card keeps its bar, and a menu open in it, while its workspace loads
tree.spec.ts:1381:1  a heap is not an algorithm of the Tree Editor, even by its URL
tree.spec.ts:1389:1  the Tree Editor shows its editor even when the visitor hid the Action panel on another card
tree.spec.ts:1484:3  /bst draws each edge between its nodes' centres, rim to rim (TP-30)
tree.spec.ts:1484:3  /trie draws each edge between its nodes' centres, rim to rim (TP-30)
tree.spec.ts:1500:1  the Tree Editor laid out left to right still draws edges centre to centre (TP-30)
tree.spec.ts:1535:3  /bst: no edge runs under [class*="collapseButton"] (TP-30)
tree.spec.ts:1535:3  /heap: no edge runs under [class*="indexBadge"] (TP-30)
tree.spec.ts:1535:3  /tree-editor laid out left to right: no edge runs under [class*="collapseButton"] (TP-30)
tree.spec.ts:1549:1  a faded Segment Tree node stays opaque over the edges under its range label and rim (TP-30)
tree.spec.ts:1588:1  /heap: the order switches the first heap to its max twin, the labels with it, and the indices are 1-based (TP-33)
tree.spec.ts:1622:1  /heap: a custom heap is rearranged into the other order, silently, and the run ends (TP-33)
tree.spec.ts:1643:1  /heap: Insert and Extract Max run on the max twin and Apply (TP-33)
tree.spec.ts:1685:1  /heap/binary-heap is the route, and an old /heap/min-heap link lands on it (TP-33)
tree.spec.ts:1705:1  /heap: Create O(N log N) builds visualgo.net's list from an empty heap, and Apply makes it the heap (TP-33)
tree.spec.ts:1760:1  /heap: Create O(N) builds the Diagonal entry into a max heap in 26 swaps, the Values kept across Method (TP-33)
tree.spec.ts:1802:1  /heap: Create blocks Play on an empty or an over-long Values list, saying why (TP-33)
tree.spec.ts:1823:1  /heap: Update key sifts a value up and one down under Min, each applied as the editor's text (TP-33)
tree.spec.ts:1879:1  /heap: Delete a middle index of the max twin, its badge trail, then Apply deletion (TP-33)
tree.spec.ts:1922:1  /heap: Update key and Delete block Play on an index outside 1..N or an empty heap, saying why (TP-33)
tree.spec.ts:1955:1  /heap: Extract 3 times under Min, the Extracted rail growing a round at a time, then Apply (TP-33)
tree.spec.ts:2002:1  /heap: Heap sort In-place under Max fades the sorted tail, ends sorted, and Stop leaves the heap (TP-33)
tree.spec.ts:2049:1  /heap: the output rail of a 31-item Heap sort scrolls back to its first values, by the wheel and the keys (TP-33)
tree.spec.ts:2086:1  /heap: a value past 15 digits is refused by Update key and by the editor, saying why (TP-33, TP-13)
tree.spec.ts:2114:1  /heap: Play is blocked on K = 0 and on a 32nd value, the editor and Insert saying why (TP-33)
tree.spec.ts:2190:1  /heap: a climb writes its comparison in green over the climbing item, clear of its parent's i=, its sign by the order (TP-36)
tree.spec.ts:2225:1  /heap: a sift that stops writes no swap · order satisfied in the ink, and equal children the left one's tie (TP-36)
tree.spec.ts:2263:1  /heap: Update key with the value an item holds writes 3 = 3 · no sift in the ink, where no number floats (TP-36)
```

## Appendix B. Evidence files kept from this audit

In `C:/Users/123ba/AppData/Local/Temp/claude/c--Users-123ba-nuss-OneDrive---National-University-of-Singapore-workplace-vstudio-learn-code-visualgo-plus-design/dd1448ed-3ceb-4759-a934-c360d565fa8f/scratchpad/fyp/work/07/`:

| File | Content |
| --- | --- |
| `runs/summary.txt`, `runs/00-env.txt` | Start time, exit code and duration of each step; Node, HEAD and `git status` before and after |
| `runs/01-typecheck.log` to `runs/05-e2e.log` | Full output of the five audit steps |
| `runs/vitest.json` | The second vitest run, per file and per test |
| `e2e-list.txt` | `playwright test --list` output |
| `runsall.json`, `runs60.json`, `runs60.txt`, `failures.txt` | GitHub Actions run history |
| `faillog-*.txt`, `ci-main-662e7b3.log` | Logs of the failed runs and of the current `main` app run |
| `prchecks.json` | Final check state per PR |
| `blame-agg.txt` | Line attribution per spec and folder |
| `scripts/` | The small scripts used for the runs and the counts |

Playwright's per-test output folder from the audit run:
`C:/Users/123ba/AppData/Local/Temp/pw-fyp-audit`.

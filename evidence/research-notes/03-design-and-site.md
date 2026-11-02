# 03. The design side and the site integration

An evidence audit for Bao's FYP report. It covers `design/` (design system, wireframes, proposals), the V2/V7 prototype era, the V10 "Panel groups" shell, the site in `prototypes/src/site`, and deployment.

- Repository: `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3` (2026-10-31). The working tree was clean before and after this audit. Paths are relative to the repository.
- Dates: a commit date is the author's local date. A "PR" date comes from GitHub (`prs.txt`). The two can differ by one day.
- Identities: "Bao" means commits by `BJoozz <123baoek31@gmail.com>`. GitHub's merge commits use `BJoozz <83776047+BJoozz@users.noreply.github.com>` (30 on `main`). Bao still has to confirm both (QUESTION). "Kerk" means `Kerk Tai Heng <taihengkerk@gmail.com>` (17 commits on `main`) and `kerktaiheng` (4 merge commits).
- "Who wrote" means the commit author. Almost every commit here also has an AI co-author trailer (section 6).

**Labels.** VERIFIED: I saw it in code, a diff, a log, a blob comparison or a run. DOCUMENTED: a doc, commit message, PR body or code comment says it, and I did not check it against the code. INFERENCE: my own reading. QUESTION: Bao needs to answer it.

**What I ran myself, on 2026-11-01**
- Unit tests, vitest 4.1.11, at 15:47 UTC. I ran them on a `git archive` copy of `662e7b3` extracted under `%TEMP%`, with the dependencies linked read-only. Nothing was written into the repository. Three files ran: `src/shared/components/layout/groupsModel.test.ts` (62 tests), `src/shared/components/layout/dropTargets.test.ts` (15) and `src/site/modules.test.ts` (24). **Result: 3 files, 101 tests, all passed, exit 0.** [VERIFIED]
- Read-only GitHub API calls with `gh`: the Pages settings and the workflow run lists (section 5). [VERIFIED]
- I imported `src/site/modules.ts` with Node to count the homepage cards (section 4). [VERIFIED]
- Not run: lint, typecheck, build, the graph `node --test` suite, the tree and sorting vitest files, and the Playwright browser suite. Every other test number in this note is quoted from a PR body. [DOCUMENTED]

## Key findings

| # | Finding | Label |
|---|---|---|
| 1 | Kerk's first commit `634b5be` "init" (2026-09-03) brought in the whole design system (`design/design-system`: nine themes, 26 components, two UI kits). Only two small commits have edited it since: Bao's `57912e8` (TopBar `onHomeClick`, +12/−3) and Kerk's `c59c155` (TopBar `account={false}`, +5/−3). Kerk's `598193b` deleted Windows `Zone.Identifier` files. | VERIFIED |
| 2 | Kerk's `wireframe 2 viz desktop.html` (`69aa8e4`, 2026-09-04) drew nine desktop layouts, V1 to V9. From them Bao built V2 (split rails) and V7 (docks, with the V8/V9 drag states) for graph, tree and sorting, and later added frames V10/V11 to the same file (`55f3387`, 2026-10-16). | VERIFIED |
| 3 | The other two wireframe files are "CDC Companion Draft 1": 390px mobile screens about vouchers and merchants. They never mention VisuAlgo. | VERIFIED (content); whether they belong in the FYP is a QUESTION |
| 4 | Bao's commits started all four proposals. Kerk's commits added rows to two of them between 2026-10-18 and 2026-10-22. The status lines at the top of two proposals are out of date. | VERIFIED |
| 5 | The V10 groups model (`prototypes/src/shared/components/layout/groupsModel.ts`, 1,441 lines) is 100% Bao's lines by `git blame`. Kerk's changes to the shell code are the drop-band tuning in `dropTargets.ts` (41 of its 388 lines) and moving the files into `src/shared` (PR #20, no line changes). | VERIFIED |
| 6 | Kerk's PR #20 (`0394b64`, 2026-10-18) deleted the V2 and V7 copies, their sites and the three upstream submodules (2,573 files deleted). The groups copies became one app. `prototypes/` went from 3,492 tracked files to 927. | VERIFIED |
| 7 | The site (`prototypes/src/site`, 12 code files) is 97% Bao's lines by blame (1,854 of 1,910). Kerk's 56 lines are small edits (bar buttons, the account flag, the tips removal). Lines Kerk deleted cannot show up in blame. | VERIFIED |
| 8 | GitHub Pages deploys `main` through `.github/workflows/pages.yml` (all lines Kerk's): the app at `/`, the wasm-arch engine demo at `/engine/`. The run at `662e7b3` succeeded. Pages never deployed the V2/V7 sites. The Vercel attempt (PR #5) was closed without merging. | VERIFIED |
| 9 | Nearly every Bao commit here has a `Co-Authored-By: Claude ...` trailer. The eight Bellman-Ford and Prim stage commits have none, and the docs say Codex planned and built them. | VERIFIED (trailers), DOCUMENTED (Codex) |

## 1. The `design/` folder

### 1.1 Design system (`design/design-system`)

| Item | Fact | Label |
|---|---|---|
| Arrival | Kerk's commit `634b5be` "init" (2026-09-03 11:46 +0800) added the whole folder: 388 files, of which 194 are `*:Zone.Identifier` files. No other path changed. | VERIFIED |
| Source | `readme.md`, "Sources": it was read from `github.com/kerktaiheng/visualgo` (a fork of `stevenhalim/visualgo`) at commit `bd1756cd1d7b`. "No design file, Figma library or brand guideline exists for VisuAlgo. Every value in this system was measured out of CSS and JS." | DOCUMENTED |
| Made before the repository | `github.md` says "Last sync 2026-08-27T03:08:45Z" and "Built the design system from scratch: tokens, 26 components, 18 foundation cards". It also says three themes ship, but the readme and the tokens have nine. | DOCUMENTED; the nine themes are VERIFIED in `tokens/colors.css`, both at `634b5be` and now |
| Format | A `SKILL.md` (name `visualgo-design`: "Use this skill to generate well-branded interfaces..."). For each component a `.jsx`, a `.d.ts` and a `.prompt.md`, plus `*.card.html` files. Also `_ds_bundle.js` (header `@ds-bundle`, format 4), `_ds_manifest.json` (namespace `VisuAlgoDesignSystem_7518b0`), `_adherence.oxlintrc.json` and `.thumbnail`. | VERIFIED (files) |
| What the format suggests | It looks like the export of an AI design tool, made outside this repository and then committed. | INFERENCE. Which tool, and how much Kerk wrote by hand, is a QUESTION |
| `Zone.Identifier` files | Windows "downloaded from the internet" markers. They fit files downloaded on Windows and copied into a Linux/WSL checkout. Kerk removed them in `598193b` (2026-09-13). | VERIFIED (files), INFERENCE (meaning) |
| Tokens | `tokens/`: base, colors, elevation, fonts, modern-skin, spacing, typography, viz. `styles.css` imports all eight. Themes: `light` (the default, written as no attribute), `midnight`, `tide`, `abyss`, `forest`, `pine`, `clay`, `ember`, `classic`, set by `data-theme` on `<html>`. | VERIFIED |
| Components and kits | 26 components (chrome 4, content 5, feedback 4, forms 7, viz 6). Two UI kits: `ui_kits/visualgo-web` (Home, Viz, Training, Login) and `ui_kits/test-mode` (Dashboard, TakeTest, Result). | VERIFIED (files); the counts are DOCUMENTED in the readme index |
| `uploads/` | `Sculpin Wireframes (standalone).html` (a 700 KB bundle) is titled "Sculpin — SEP research workspace". It is not VisuAlgo. | VERIFIED (content); its purpose is a QUESTION |
| Later edits | `57912e8`, Bao, 2026-09-28: `TopBar` gets an optional `onHomeClick`. The message says "This is the only change to Kerk's design system in the VisuAlgo+ site work." `c59c155`, Kerk, 2026-10-18: `TopBar` takes `account={false}` (no Login). | VERIFIED |
| Drift since `init` | `git diff --stat 634b5be HEAD -- design/design-system`: 196 files, +16/−5. That is the 194 removed `Zone` files plus the two TopBar edits. | VERIFIED |

### 1.2 Wireframes (`design/wireframes`)

| File | Commits | Content | Label |
|---|---|---|---|
| `wireframe 2 viz desktop.html` | `69aa8e4` "wireframs", Kerk, 2026-09-04 (812 lines). `55f3387`, Bao, 2026-10-16 (+150/−6). | "VisuAlgo visualisation page. Draft 2. Low fidelity. 1440px desktop. AVL tree." It has an element inventory and nine versions: V1 left stack, V2 split rails, V3 controls and reading, V4 rails and drawers, V5 docked code, V6 bottom dock, V7 docks draggable, V8 docks mid-drag, V9 docks after the drop. Then the V1 states, a footer bar "identical in all nine versions", the rules "true in every version", and "Mobile. Held pending further instructions". Bao's commit added V10 "Panel groups" and V11 "Panel groups, mid-drag", and changed "nine" to "eleven". | VERIFIED |
| `wireframe 1.html`, `wireframe 1 user flow.html` | `69aa8e4`, Kerk | "CDC Companion Draft 1": 390px mobile screens and user flows UF1 to UF6 (first use, find somewhere to spend, pay at a merchant, act on expiry...). There is no VisuAlgo content. | VERIFIED; relevance is a QUESTION |
| `design/proposals/sorting-v2-v7/wireframe-sorting-v2-v7.html` | `ee4bb72`, Bao, 2026-09-25 | Sorting V2/V7 frames, "in the same form as" Kerk's file | VERIFIED |

Who picked V2 and V7 out of the nine for building, and when, is not recorded in the files I read. QUESTION.

### 1.3 Proposals (`design/proposals`)

| Proposal | Size, language | Commits (authors), first to last | What it holds | Label |
|---|---|---|---|---|
| `prim-v2-v7/README.md` | 210 lines, **Vietnamese** | 7 (all Bao), `4bd0879` 2026-10-04 to `6fec0d3` 2026-10-10 | The plan and the stage records A to E for Prim in graph V2/V7 and the two sites. §8: "Codex thực hiện Stages A/B..." (Codex carried out stages A/B). The owner then gave C, D and E to Codex, with sub-agents on separate files. §15: a Claude review of A to E on 2026-10-05, which says the owner had not approved the choices in §2/§9 and only asked Codex to plan and build. §9 lists four choices: lazy edge priority queue, a spanning forest on disconnected graphs, an undirected view as Kruskal's, prototype plus both sites ("PRI"). | VERIFIED (log), DOCUMENTED (content) |
| `sorting-v2-v7/README.md` + wireframe | 969 + 1,182 lines, English | 19 (all Bao), `ee4bb72` 2026-09-25 to `38c726f` 2026-10-12 | §0 "Decisions taken" covers U1 to U12: keep Stop; a Go button (replaced by Play on 2026-10-10); a full restart when the pane count changes; eager production when the run fits 60,000 operations; no Zoom/Fit; a Status ranking only in V7; Pseudocode and e-Lecture absent from Compare; and more. U7 and U9 were "decided by the user on 2026-09-27". §1 to §12 cover the clashes with the shell, the layout floors, accessibility and the stages. | VERIFIED (log), DOCUMENTED (content) |
| `visualgo-web-site/README.md` + `RUNNING.md` | 1,296 + 222 lines, English | 38 (36 Bao, 2 Kerk: `ae63a62`, `0394b64`), `a972917` 2026-09-28 to `0394b64` 2026-10-18 | "Status: built." Five decisions: separate builds (V2, V7, later V10); the DS `TopBar` is the one bar; the footer differs by page; the kit's `VizScreen` is a reference, not code; 12 of 30 cards are real. §2 says who owns what (table below). §11 has stages 1 to 6 with what each cost. §12 lists the target screens ("owner, 2026-10-08": desktop and laptop windows, 1280×600 up to 1920×960). §13 has questions Q1 to Q10. It calls the homepage "Kerk's homepage" and the DS components "Kerk's components". | VERIFIED (log), DOCUMENTED (content) |
| `viz-shell-v10/README.md` | 779 lines, English; the owner's words are quoted in Vietnamese (choices 1 to 26) or English (27 to 48) | 13 (7 Bao, 6 Kerk), `55f3387` 2026-10-16 to `01a1a4a` 2026-10-22 | 10 revisions. §0.1 is the owner's choices (48 rows now). §0.2 is the "Implementer's defaults, not reviewed by the owner". Then the draft records DD-50 to DD-56, measurements for graph/tree/sorting, the milestones and stages (estimate: "Milestone 1 is about 24 to 36 days"), and open questions. | VERIFIED (log, blame), DOCUMENTED (content) |

The site proposal's ownership table (§2) [DOCUMENTED]:
- The **site** owns the top bar, wordmark, language and account, routing, the theme (one `html[data-theme]`) and the homepage.
- The **visualizer** owns the panel layout, the domain and algorithm state, and the playback transport (its `FooterBar`).
- Module nav is drawn by the module into the DS `TopBar`'s left slot.
- The proposal says it is a loss "worth naming" that Kerk's `MediaControls`/`SpeedControl` go unused.

Out-of-date status lines at `HEAD` [VERIFIED]:
- `sorting-v2-v7/README.md` line 3 still says "Revision 5, 2026-09-24. Status: design only, awaiting review... The two prototypes do not exist yet."
- `viz-shell-v10/README.md` line 3 still says "Stage 0, 2026-10-16. Status: design only, awaiting the owner's review."
- Both prototypes were built (PRs #3 and #15). Only the revision tables describe the later state.

### 1.4 The owner's choices in `viz-shell-v10` §0.1

Numbered rows counted at each commit [VERIFIED]:
- 21 at `e66fbba` (revision 5)
- 23 at the PR #15 merge `c899b69`
- 26 after PR #17
- 32 after PR #20 (which carried #19)
- 41 after PR #21
- 45 after `3c79d36`
- 47 after `a074f50`
- 48 after `01a1a4a` (unchanged at `HEAD`)

| Choices | Dates | Written into the file by (blame) | Quoted words | Who "the owner" is |
|---|---|---|---|---|
| Brief, 1 to 8 | 2026-10-16 | `55f3387` Bao | Vietnamese | INFERENCE: Bao (his commits, his language). QUESTION: confirm |
| 9 to 23 | 2026-10-17 | `cdbc18b`, `7a3b4e8`, `af828eb`, `e66fbba`, `2397826` (Bao) | Vietnamese | same |
| 24 to 26 | 2026-10-18 | `c0166f2` (Bao, PR #17) | Vietnamese | same |
| 27 to 32 | 2026-10-18 | `ae63a62` (Kerk, PR #19, merged through #20) | English ("drag pane only works when i drag beyond the center...") | QUESTION: Kerk? |
| 33 to 41 | 2026-10-18 | `c59c155` (Kerk, PR #21) | English ("i didn't ask for the valid ...", "remove login button") | QUESTION |
| 42 to 45 | 2026-10-19 | `3c79d36` (Kerk, pushed to `main`, no PR) | English | QUESTION |
| 46 to 47 | 2026-10-21 | `a074f50` (Kerk, no PR) | English | QUESTION |
| 48 | 2026-10-22 | `01a1a4a` (Kerk, no PR) | English | QUESTION |

More "owner" wording in Kerk's work, all QUESTION:
- `40a63bd` (2026-10-20): "The owner's request, 2026-10-20".
- PR #19: "The owner's six fixes".
- PR #21: "The owner's ten requests".
- Bao's PR #37 also calls Kerk's `a074f50` "The owner's commit".

A small date mismatch [VERIFIED]: `prototypes/src/site/HostedModule.tsx:84` says Full screen and Shortcuts sit beside Settings "(the owner's choice, 2026-10-18)". The proposal's choice 44 is dated 2026-10-19, and commit `3c79d36` is dated 2026-10-19 00:07 +0800.

## 2. The V2 (split rails) and V7 (docks) era, 2026-09-13 to 2026-10-18

### 2.1 What each PR built

All five branches show 0 commits ahead of `main`, so they are fully merged. Each prototype is "a standalone copy of graph-visualizer-v2 [or the tree/sorting repo] laid out as wireframe V2/V7", copied from Bao's own earlier repos (`BJoozz/graph-visualizer-v2`, `tree-visualizer`, `sorting-algorithm-visualizer`; all their commits are BJoozz's). [VERIFIED]

| PR (branch) | PR date | Merge | Commits (with AI trailer) | Diff of the merge | What it built | Label |
|---|---|---|---|---|---|---|
| #1 `bj/graph-wireframe-v2-v7` | 2026-09-20 | `6a621df` | 6 (3) | 517 files, +65,204 | `graph-visualizer-split-rails` (V2: left/right accordion rails) and `graph-visualizer-docks` (V7: movable tabs, resizable docks, persistence, reset). Registers the graph and tree submodules. Algorithm picker moved to the top bar; DS themes through the `@ds` alias; `.github/workflows/prototypes.yml`. | VERIFIED (stat), DOCUMENTED (features) |
| #2 `bj/tree-wireframe-v2-v7` | 2026-09-23 | `495fa73` | 7 (6) | 841 files, +75,560/−108 | `tree-visualizer-split-rails` and `-docks` (LCA, BST, AVL, Min Heap, Trie, Segment Tree) in the graph shell. Shell fixes in all four prototypes; CI extended to four apps. | VERIFIED, DOCUMENTED |
| #3 `bj/sorting-wireframe-v2-v7` | 2026-09-27 | `ca56cef` | 23 (22) | 329 files, +53,094 | `sorting-visualizer-split-rails` and `-docks` (Study mode, and Compare with 2 or 4 panes). Sorting submodule pinned at `9236a65`. `design/proposals/sorting-v2-v7`. | VERIFIED, DOCUMENTED |
| #4 `bj/visualgo-web-site` | 2026-09-28 | `9cc009f` | 7 (7) | 119 files, +13,660/−167 | Two sites: `visualgo-web-split-rails` (port 5181) and `visualgo-web-docks` (5182). A homepage with search, tag filters, tips and partner logos, mounting the real visualizers under one top bar. Host-chrome adapters (`a8dd634`), DS `TopBar` `onHomeClick` (`57912e8`), the `visualgo-web-site` proposal. | VERIFIED, DOCUMENTED |
| #6 `bj/visualgo-web-editors` | 2026-10-08 | no merge commit: a fast-forward, `9cc009f..ae2f31f` | 33 (25) | 622 files, +39,549/−2,176 | Graph Editor and Tree Editor cards marked New (`cc38942`); recursive DFS (`4ab075c`) and the old DFS URL redirect (`65766cc`); Dijkstra's distances on the nodes (`6fc6150`); edge waves DD-37 (`bcbed32`, `c4e597d`); Bellman-Ford stages A to E (`aef5d0b` to `e6ce1ac`); Prim stages A to E (`4bd0879` to `6b1791a`); an extra dock panel (`00ed4c2`); the LCA ancestor strip (`303e50b`); the homepage credit (`ae2f31f`). The PR body is empty. | VERIFIED |

All the test counts in PR bodies #1 to #4 are reported by the implementer. Example: #3 has "537/571 unit, 68 browser". PRs #3 and #4 themselves say "the complete final suites were not independently rerun". [DOCUMENTED]

The old `prototypes.yml` matrix covered only graph and tree (split rails, docks, later groups). Sorting and the sites never ran in CI. [VERIFIED at `94cdaf3`]

### 2.2 How the copies were kept the same

The rules [DOCUMENTED]:
- `prototypes/graph-visualizer-split-rails/AGENTS.md` at `94cdaf3`: every fix is made "in graph-visualizer-split-rails first and then in graph-visualizer-docks".
- The tree and sorting `AGENTS.md`: "the shell sheets stay byte-identical to the graph prototype". The tree has marked exceptions in `viz-page.css`. Sorting lists four files that had drifted as "outstanding debt".
- The site proposal, §11 stage 4: "`diff -rq` of the two `src/` and `e2e/` trees is EMPTY".
- V10: the shell files (`src/components/layout/*`, `src/styles/groups.css`) were byte-identical in the three groups copies, checked with a `cmp` loop written in each `AGENTS.md` (e.g. `94cdaf3:prototypes/tree-visualizer-groups/AGENTS.md:192-195`).
- PR #36 (2026-10-30) retired the copy rule: "the owner, 2026-10-28: 'Rút luật, thay bằng src/shared'".

My check: file-by-file git blob hashes at `94cdaf3`, the last `main` commit before PR #20 [VERIFIED]

| V2 vs V7 pair | Identical | Differ | Only in V2 | Only in V7 |
|---|---|---|---|---|
| graph | 340 | 38 | 7 | 14 |
| tree | 495 | 30 | 7 | 15 |
| sorting | 138 | 25 | 5 | 8 |
| sites | 43 | 12 | 0 | 0 |

Graph detail:
- The files found in only one copy are each layout's own: `SplitRailsLayout.tsx`, `splitRailsModel.ts`, `useSplitRails.ts` and `split-rails.css` in V2; `DocksLayout.tsx`, `docksModel.ts`, `useDocks.ts`, `useTabDrag.ts`, `Splitter.tsx`, `docks.css` and four e2e files in V7.
- Apart from screenshots, the files that differ are the docs, five e2e specs, configs and `src/app/App.tsx`.

The sites differed only in `package.json`, `package-lock.json`, `tsconfig.app.json`, `vite.config.ts` and 8 screenshots. The V10 shell at `c899b69` and `94cdaf3`: all 9 non-test shell files were identical across the graph, tree and sorting groups copies. The two test files differ because graph's use `node:test`.

### 2.3 What remains of V2/V7 now

- No V2/V7 code at `HEAD`: `git ls-files prototypes | grep -iE 'dock|split-?rails'` finds nothing. [VERIFIED]
- PR #20 (`0394b64`) deleted 2,573 files, renamed 921, added 10 and modified 4. [VERIFIED]
  - Deleted, per folder: tree split rails 514, tree groups 496, graph groups 364, graph split rails 363, sorting split rails 166, sorting groups 155, tree docks 153, graph docks 146, sorting docks 85, the sites (split rails 54, groups 41, docks 31).
  - Also gone: the three submodules and `.gitmodules`.
- Git often reports the renames as coming "from `*-docks`". That is git's rename detection choosing one of several identical source files. The PR body says the groups copies became the app. [INFERENCE + DOCUMENTED]
- Still there [VERIFIED]:
  - the remote branches and all the history
  - the `sorting-v2-v7`, `prim-v2-v7` and `visualgo-web-site` proposals (now history)
  - frames V1 to V9
  - many mentions in the records (for example 29 in `prototypes/docs/graph/DESIGN_DECISIONS.md`)
  - comments in `groupsModel.ts` naming V7's `docksModel.ts` as the source of its region maths (DD-26)
- PR #20, "Not done": "Bao's open branches against the deleted folders will not merge." [DOCUMENTED]
- Revision 9 of the V10 proposal records "V10 kept, the rest removed" without an owner choice number. Who decided it, and whether Bao agreed, is a QUESTION.

## 3. The V10 "Panel groups" shell

### 3.1 Who did what

The diff sizes below are VERIFIED. Feature details come from the PR bodies [DOCUMENTED] unless a file is named.

| PR / commit | Author | Date | Size | What it did |
|---|---|---|---|---|
| #15 `bj/viz-shell-v10`, 20 commits | Bao | 2026-10-16 to 17 | 1,196 files, +170,900/−34 (mostly the three copied prototypes) | Proposal stage 0 and frames V10/V11 (`55f3387`). Groups model and drop geometry (`72450e1`). Shell: `GroupsLayout`, tab menu, drag overlay, sandbox (`a876206`). Graph page in groups (`950ab6f`). DD-50 to DD-56 (`12cdf92`). Sorting copy (`0e3857f`), tree copy (`d82a24c`), site `visualgo-web-groups` on 5186 (`d445364`). Wheel-scrolled tab strip (`5902020`). CI (`238f603`). |
| #16 | Bao | 2026-10-17 | 104 files, +424/−550 | Faint scrollbars in all nine prototypes, hint lines removed, a layout board 1.3 times larger. Its first commit `9bf60f6` is the same patch as `46234cd` (same patch-id). That commit was pushed to #15's branch after #15 merged, and the branch is still 1 commit ahead of `main`. |
| #17 | Bao | 2026-10-18 | 35 files, +2,313/−533 | Choices 24 to 26: fit the drawing only on a size change, bottom groups keep 240px, hidden groups keep their space (`649f42e`, then copied in `b8f1c1a`). |
| #18 `deploy-v10-pages` | Kerk | 2026-10-18 | 1 file, `pages.yml` +37/−4 | The site at the Pages root, the engine at `/engine/` (`c39b3cf`). |
| #19 `v10-owner-fixes` (`ae63a62`, merged as part of #20) | Kerk | 2026-10-18 | 149 files, +1,367/−792 | Choices 27 to 32: thin split bands (15%, at most 32px), vector `TransportIcon.tsx` (26/26 lines Kerk's), "Select preset", Draw graph as a disclosure, push-only Live layout (`pushApart.ts`), no text under 13px. |
| #20 `v10-single-app` (`0394b64`) | Kerk | 2026-10-18 | 3,510 files, +824/−346,532 | Keep V10 only. One app, npm workspaces, `app.yml` CI, Pages built from the root. The 40 shared files moved into `src/shared`. |
| #21 `v10-polish` (`c59c155`, `5235fcf`) | Kerk | 2026-10-18 | 105 files, +1,062/−3,132 | Choices 33 to 41. The visualizers' dead standalone `TopBar`/`SettingsMenu`/theme writer removed. New `src/shared/styles/controls.css` (143 of its 153 lines are Kerk's) and `editor.css` (122/122 Kerk's). |
| `3c79d36` (no PR) | Kerk | 2026-10-19 | 41 files, +139/−338 | Choices 42 to 45: LCA indentation, no Save image, Full screen and Shortcuts beside Settings, a 340px speed slider. |
| `40a63bd` (no PR) | Kerk | 2026-10-20 | 6 files, +12/−35 | The tips removed from the homepage. |
| `a074f50` (no PR) | Kerk | 2026-10-21 | 17 files, +212/−75 | Choices 46 and 47: stepping leads the footer, Autoplay sits beside Stop, the e-Lecture nav is pinned. |
| `01a1a4a` (no PR) | Kerk | 2026-10-22 | 16 files, +235/−253 | Choice 48: Autoplay and Stop become coloured chips. |

The four Kerk commits marked "no PR" sit on `main`'s first-parent chain, and no PR in `prs.txt` contains them. [VERIFIED]

Merge commits [VERIFIED]:
- Bao's GitHub identity merged #15 and #16.
- `kerktaiheng` merged #17, #18, #20 and #21.
- This shows who pressed merge, not who wrote the code.

### 3.2 The groups model

What it is [DOCUMENTED, from the file's header comment, which also says "Everything here is pure"]: "three regions around a canvas that is not in the model". The left and right regions are columns of tab groups; the bottom region is a row. A group collapses to its tab strip. A tab moves into a group, splits one, or opens an empty region. `resolveLayout` fits the stored sizes to the page and the drawing floor, and `canDrop` uses the same maths, "so every limit lives in this file".

Code facts [VERIFIED]:
- Exported functions include `moveTab`, `pressTab`, `revealTab`, `setGroupCollapsed`, `offerExtraPanel`, `presentLayout`, `resizeRegion`, `resizeGroup`, `serializeLayout`/`parseLayout`, `resolveLayout`, `maxRegionSize`, `maxGroupSize`.
- Its constants match choices 9, 10 and 12: `GROUP_MIN_WIDTH = 240`, `GROUP_MIN_HEIGHT = 120`, `BOTTOM_ROW_MIN_HEIGHT = 120`, `DEFAULT_MIN_DRAWING = 360 x 320`.
- History by `git log --follow --numstat`:
  - `72450e1` +1,179 (Bao)
  - `a876206` +192/−81 (Bao)
  - `649f42e` +243/−92 (Bao)
  - `0394b64` +0/−0 (Kerk, a pure move)

`git blame` at `HEAD`, lines by commit author [VERIFIED]:

| File in `prototypes/src/shared/components/layout` | Lines | Bao | Kerk |
|---|---|---|---|
| `groupsModel.ts` | 1,441 | 1,441 | 0 |
| `groupsModel.test.ts` | 1,355 | 1,355 | 0 |
| `dropTargets.ts` | 388 | 347 | 41 (`ae63a62`, `c59c155`) |
| `dropTargets.test.ts` | 328 | 274 | 54 |
| `GroupsLayout.tsx` | 639 | 637 | 2 |
| `GroupView.tsx`, `TabMenu.tsx`, `Splitter.tsx`, `useGroups.ts` | 658 | 658 | 0 |
| `useGroupDrag.ts` | 138 | 135 | 3 |
| `../../styles/groups.css` | 453 | 447 | 6 |

Tests:
- I ran `groupsModel.test.ts` (62) and `dropTargets.test.ts` (15) on 2026-11-01. All passed. [VERIFIED]
- The shell's drag, split and splitter scenarios have no browser test; they "stay manual (the owner, 2026-10-28: guides only, no new shell e2e)". [DOCUMENTED, PR #36]

Plan versus dates [VERIFIED dates, DOCUMENTED estimate]: the proposal estimated milestone 1 at "about 24 to 36 days". The commits for stages 1 to 6 are all dated 2026-10-17. I draw no conclusion from that.

## 4. The site now (`prototypes/src/site`)

### 4.1 Who wrote which parts

Lineage: Bao created the site in `87db4a3` (V2 site) and `8aeb543` (V7 copy), both on 2026-09-28. He copied it into `visualgo-web-groups` in `d445364` (2026-10-17). Kerk moved it into `src/site` in `0394b64`. [VERIFIED]

The groups site differed from the docks site in 4 files (+12/−11). Of the moved files, 10 kept identical content and 4 got small edits (+15/−15). [VERIFIED]

`git blame -w -M HEAD`, lines by commit author [VERIFIED]:

| File | Lines | Bao | Kerk | Kerk's commits that touched it (`git log --follow`) |
|---|---|---|---|---|
| `App.tsx` (routes) | 75 | 75 | 0 | `0394b64` (move only) |
| `useTheme.ts` | 96 | 95 | 1 | `0394b64` (+1/−1) |
| `ModulePage.tsx` | 101 | 93 | 8 | `0394b64` (+8/−8, paths) |
| `ModuleBar.tsx` | 169 | 165 | 4 | `3c79d36` (+4) |
| `HomePage.tsx` | 240 | 226 | 14 | `c59c155` (+15/−102), `40a63bd` (+5/−17) |
| `HostedModule.tsx` | 119 | 106 | 13 | `3c79d36` (+13) |
| `SiteTopBar.tsx` | 74 | 64 | 10 | `c59c155` (+4/−45), `3c79d36` (+9/−3) |
| `SettingsMenu.tsx` | 94 | 94 | 0 | `c59c155` (−3) |
| `SiteOverlay.tsx` | 70 | 70 | 0 | none |
| `EditorCard.tsx` | 53 | 52 | 1 | `40a63bd` |
| `modules.ts` (card table) | 448 | 448 | 0 | `40a63bd` (−7) |
| `modules.test.ts` | 371 | 366 | 5 | |
| **Total** | **1,910** | **1,854** | **56** | |

Around the site:
- `scripts/static-fallback.mjs` (29/29 lines Bao's) and `scripts/sync-assets.mjs` (20 lines Bao, 7 Kerk) [VERIFIED].
- `prototypes/vite.config.ts` (72/72 lines Kerk's, rewritten in `0394b64`). It keeps Bao's `VA_BASE` subpath setting (first in `87db4a3`) and the `@ds` alias [VERIFIED].
- `prototypes/e2e` (19 files): 5,236 lines Bao's, 70 Kerk's [VERIFIED].
- `prototypes/AGENTS.md`: 62 of 70 lines Kerk's. Root `README.md`: 15 of 17 lines Kerk's [VERIFIED].

### 4.2 How it works

Facts [VERIFIED, from the code]:
- **Routes** (`App.tsx`): `BrowserRouter basename={import.meta.env.BASE_URL}`, with `/` (home), `/:slug` and `/:slug/:algorithm`. Anything else goes back to `/`. Old algorithm URLs redirect (`findFormerAlgorithm`).
- **Cards** (`modules.ts`, counted by importing it): 30 cards.
  - 8 "full": graph-editor, tree-editor, sorting, bst, heap, mst, trie, lca.
  - 4 "partial": segmenttree, dfsbfs, sssp, maxflow.
  - 18 "soon", which do not open.
  - The 24 tests in `modules.test.ts` pass (my run).
- **Themes**: `useTheme.ts` `THEMES` lists the design system's nine ids. `light` is written as no `data-theme` attribute, and the site is the only writer: outside tests, only `src/site/useTheme.ts` sets or removes `data-theme` (grep). Since `c59c155` the visualizers only follow it. `src/shared/app/themes.ts` (33/33 lines Bao's) came from `0073875`; Bao's upstream `graph-visualizer-v2` had no theme list.
- **Design-system use**:
  - `src/main.tsx` imports `@ds/styles.css` (all the tokens).
  - The site imports 5 of the 26 components: `TopBar`, `BottomBar`, `LessonCard`, `TextInput`, `Overlay`.
  - `scripts/sync-assets.mjs` copies `icons`, `logo` and `modules` into `public/ds`, which git ignores.
- **Credit line**: `HomePage.tsx:152` says "This site is an experimental version adapted from Prof Halim's visualgo.net, built by Kerk and Bao." (`ae2f31f`, Bao, 2026-10-08).

Design, from the doc comments [DOCUMENTED]: `ModulePage`, `HostedModule` and `ModuleBar` serve all three visualizers, "so the three cannot drift apart". A visualizer hands the site its bar's parts. The transport stays the visualizer's own `FooterBar`.

### 4.3 How Kerk's designs map to the site

| Kerk's piece | Where it is now | Changes since | Label |
|---|---|---|---|
| DS tokens and nine themes | `@ds/styles.css` in `src/main.tsx`; the ids in `useTheme.ts` and `src/shared/app/themes.ts` | none to the tokens | VERIFIED |
| DS `TopBar` | `SiteTopBar.tsx` | Bao: `onHomeClick` (`57912e8`). Kerk: `account={false}` (`c59c155`), Full screen and Shortcuts beside Settings (`3c79d36`) | VERIFIED |
| DS kit `ui_kits/visualgo-web/HomeScreen.jsx` (TopBar, TextInput search, FilterTag, TipBox, LessonCard grid, BottomBar, Overlay) | `HomePage.tsx`. Bao's first version (`87db4a3`) imported FilterTag, TipBox, LessonCard, TextInput, BottomBar and Overlay. | FilterTag removed (Kerk `c59c155`, choice 41). TipBox removed (Kerk `40a63bd`). Footer reduced to Privacy policy (choice 40). Editors section added (Bao `5e745b2`). | VERIFIED (imports). INFERENCE: the page started as a port of the kit (the proposal says the visitor "lands on Kerk's homepage") |
| DS kit `VizScreen.jsx` | not used; "reference, not code" | | DOCUMENTED |
| DS `MediaControls`, `SpeedControl` | not imported; the visualizers' `FooterBar` is used instead | | VERIFIED (no import), DOCUMENTED (reason) |
| DS PNG transport icons | replaced by vector `TransportIcon.tsx` (Kerk, `ae63a62`); `icons/` is still passed to `LessonCard` | | VERIFIED |
| DS module PNGs and logos | card thumbnails; NUS Computing and Optiver logos on the homepage | | VERIFIED |
| Wireframe 2, V1 to V9 | V2/V7 built, then deleted; V10 (Bao's frames) is the shell today | | VERIFIED |
| Wireframe: e-Lecture as a panel, action inputs in the Action panel | done | | DOCUMENTED (PR #1, proposal) |
| Wireframe: "Mode switcher: Exploration, Training, Test" | not built (`HomePage.tsx`: "Training is not built") | | VERIFIED |
| Wireframe: footer "identical in all nine versions" (with Save image and About/Team/Terms) | changed by choices 40, 43, 44, 46 and 48, all in Kerk's commits | | DOCUMENTED (§0.1), VERIFIED (bar buttons in `HostedModule.tsx`) |
| Wireframe: mobile "held pending" | not built; the target is desktop/laptop windows (site proposal §12, "owner, 2026-10-08") | | DOCUMENTED |

QUESTION: did Kerk mean the wireframes and the design system as the specification for the site, or only as reference material?

## 5. Deployment

### 5.1 GitHub Pages (`.github/workflows/pages.yml`, all 65 lines Kerk's)

| Commit | Date | Author | What Pages served | Label |
|---|---|---|---|---|
| `b3e86ba`, `8a59115`, `df99dac` | 2026-09-03 to 09-14 | Kerk | the wasm-arch engine demo at the root (`VITE_BASE=/<repo>/`) | VERIFIED |
| `c39b3cf` (PR #18) | 2026-10-18 | Kerk | `visualgo-web-groups` at `/` (built with `VA_BASE`, `npm ci` in four folders), the engine at `/engine/`. A PR that changes `pages.yml` builds but does not deploy. | VERIFIED |
| `0394b64` (PR #20) | 2026-10-18 | Kerk | the app built from the repository root (`npm ci`, `npm run build`, `VA_BASE=/<repo>/`), copied to the site root; the engine at `/engine/` | VERIFIED |

GitHub API, read on 2026-11-01 [VERIFIED]:
- Pages `build_type: workflow`, URL `https://kerktaiheng.github.io/visualgo-plus-design/` (the root README says the same).
- 48 runs of `pages.yml`: 43 succeeded, 3 were cancelled, 2 failed. The two failures were `69aa8e4` (2026-09-04) and `598193b` (2026-09-13), both before `df99dac` fixed the workflow.
- The first run with the V10 site at the root was at `94cdaf3` (2026-10-18 11:13 UTC): success.
- The latest was at `662e7b3` (2026-10-30 17:04 UTC): success.
- I did not open the live site.

The V2/V7 sites were never deployed through Pages, because before `c39b3cf` the workflow built only wasm-arch. [VERIFIED]

Static-host support (Bao, PR #4) [VERIFIED (scripts), DOCUMENTED (hosts)]:
- `VA_BASE` sets the asset URLs, the router basename and the icon prefix.
- `postbuild` writes `404.html` (GitHub Pages) and `_redirects` (Netlify).
- `RUNNING.md` gives the one-line rules for `serve`, nginx, Apache and Vercel.

### 5.2 CI

- `prototypes.yml` (Bao: `37075b1` 2026-09-20 to `d82a24c` 2026-10-17) ran a matrix of the graph and tree prototypes. Sorting and the sites were never in it. [VERIFIED]
- PR #20 replaced it with `app.yml` (94/94 lines Kerk's): lint, typecheck, unit tests, build, a whitespace check, the Playwright suite, and uploaded traces on failure. Its latest run on `main` (`662e7b3`) succeeded. [VERIFIED via `gh`]
- `ci.yml` (Kerk) only builds and tests wasm-arch in Docker. [VERIFIED]

### 5.3 The Vercel attempt (PR #5)

- PR #5 "Configure Vercel SPA routing for both websites", by BJoozz, created 2026-09-29. CLOSED, not merged. Head `main` into base `main`. The body is empty. [VERIFIED, `prs.txt`]
- Commit `c9e4598` (Bao, 2026-09-29 06:09 +0800, parent `9cc009f`) adds a 5-line `vercel.json` (rewrite everything to `/index.html`) to `visualgo-web-split-rails` and `visualgo-web-docks`. It exists only on the local branch `bj/vercel-spa-routing` and never reached `main`. [VERIFIED]
- I found no evidence of any Vercel deployment. QUESTION.

## 6. AI-assistance facts in this area

Commits with a `Co-Authored-By: Claude ...` trailer [VERIFIED]:

| Range | Commits | With trailer | Models named in the trailers |
|---|---|---|---|
| PR #1 | 6 | 3 | Claude Fable 5.1. The three without are `986deba`, `c458755`, `75d9760`. |
| PR #2 | 7 | 6 | Fable 5.1 (5), Opus 5 (1M context) (1) |
| PR #3 | 23 | 22 | Opus 5 (1M context) |
| PR #4 | 7 | 7 | Opus 5 (1M context) |
| PR #6 | 33 | 25 | Opus 5.5 (20), Fable 5.1 (4), Fable 5 (1). The 8 without are the Bellman-Ford and Prim stage commits `aef5d0b`, `0aac567`, `6417767`, `4bd0879`, `5428ed3`, `686c06b`, `65634cf`, `490e1d1`. |
| PR #15 | 20 | 20 | Fable 5.1 (18), Opus 5.5 (2) |
| PR #16, #17 | 4, 3 | 4, 3 | Opus 5.5, plus one Fable 5.1 |
| Kerk: PR #18, #19/#20, #21, and `3c79d36`, `40a63bd`, `a074f50`, `01a1a4a` | 9 | 9 | Opus 5.5 |

Docs that name Codex (INFERENCE: OpenAI's coding agent) [DOCUMENTED]:
- `design/proposals/prim-v2-v7/README.md` §8 and §15: Codex did Prim stages A to E, and Claude reviewed them.
- `design/proposals/visualgo-web-site/README.md` line 932 ("A review by Codex") and line 1055 ("from a plan Codex drew up").
- `prototypes/docs/graph/DESIGN_DECISIONS.md` (DD-38, DD-39: "had Codex plan and build it").
- So Codex's share does not show in the commit trailers.

Other facts:
- The site proposal (`a972917`, with a Claude trailer) is written in the first person ("the module I know best"). INFERENCE: an AI agent drafted that prose.
- The local branch `backup/before-reword-044908` (`d3ab325`) holds the PR #4 commits from before a message reword. The trees are identical. Only one message changed (`a3d777b` became `a8dd634`), in its sentence about test counts, and no trailer was removed. [VERIFIED]

## 7. Questions for Bao

1. **Identities.** Are `BJoozz <123baoek31@gmail.com>` and `BJoozz <83776047+BJoozz@users.noreply.github.com>` both you? The second appears only on GitHub merge commits.
2. **The design system's origin.** Its format (`SKILL.md`, a `.prompt.md` per component, `_ds_bundle.js`, `_ds_manifest.json`) looks like an AI design-tool export, and `github.md` dates it 2026-08-27, before the repository existed.
   - Which tool made it?
   - How much did Kerk write or edit by hand?
   - Did you add anything to it apart from `57912e8`?
3. **Unrelated files.** `design/wireframes/wireframe 1.html` and `wireframe 1 user flow.html` ("CDC Companion", vouchers and merchants) and `design/design-system/uploads/Sculpin Wireframes (standalone).html` ("SEP research workspace") are not about VisuAlgo. Should the report leave them out?
4. **Picking V2 and V7.** Who chose V2 and V7 out of Kerk's nine wireframe versions, and when? I found no dated record.
5. **"The owner" in Kerk's commits.** Who is the owner in choices 27 to 48 of `viz-shell-v10` §0.1 (2026-10-18 to 2026-10-22, English quotes), in `40a63bd` ("The owner's request, 2026-10-20"), in the PR #19 and #21 bodies, and in your PR #37's "The owner's commit `a074f50`"? Is it Kerk? Choices 1 to 26 (Vietnamese quotes, your commits) look like yours: please confirm.
6. **Keep V10 only.** Who decided to delete V2 and V7 (PR #20, 2026-10-18), and were you asked? The proposal's revision 9 gives no owner choice for it.
7. **Vercel.** Why was PR #5 closed? Was the site ever deployed on Vercel? Why was it opened `main` into `main` (from a fork)?
8. **Commits with no AI trailer.** Who wrote `986deba`, `c458755` and `75d9760` (PR #1)? The docs say Codex built Bellman-Ford and Prim (8 commits with no trailer). Did Codex write any other commits?
9. **A date.** `HostedModule.tsx:84` says choice "2026-10-18", but the proposal's choice 44 says 2026-10-19 (`3c79d36` is 00:07 +0800 on 10-19). Which date should the report use?
10. **Branding.** The site uses the VisuAlgo name, the NUS Computing and Optiver logos, and says it is "adapted from Prof Halim's visualgo.net". Is that agreed with your supervisor, for the report and the public Pages site?

## 8. How this note was built

Commands I used, all read-only:
- `git log`, `git show --stat`, `git diff --stat` and `--name-status`
- `git ls-tree` blob hashes, for the V2/V7 and V10 copy comparisons
- `git blame -w -M --line-porcelain` (line counts by commit author)
- `git grep` at fixed commits, mainly `94cdaf3` (the last commit before PR #20) and `HEAD`
- `gh run list` and `gh api .../pages`
- the vitest run described at the top

The repository stayed clean (`git status --short` was empty afterwards). Nothing was written inside the repository, the clones or the worktrees.

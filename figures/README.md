# Figures: what each capture shows and how to make it again

Audit date: 2026-11-01/02\
Repository: `kerktaiheng/visualgo-plus-design`, `main` at `662e7b3`\
Evidence labels: VERIFIED / DOCUMENTED / INFERENCE / QUESTION\
The owner's answers of 2026-11-01 are applied. Each PNG is described as it appears (I viewed every one). The steps are a reconstruction, because the capture script was lost. Which figures to use, and their captions, are in `../04_figures_and_validation.md` §1.

## Common facts

- **Captured:** on 2026-11-01 between 23:52:47 and 23:53:07 (UTC+07:00, the machine's clock that day; 16:52–16:53 UTC; file times), by a Playwright script in headless Chromium. The viewport was 1440 × 900 at device scale 1, and the commit was `662e7b3`. The script was lost when its agent was cut off. VERIFIED (file times and sizes); the commit is what the capture run reported.
- **Capture plan:** the steps listed under each file, as reconstructed. On 2026-11-02 the script at the end of this file ran them against the Pages build of `662e7b3`, and every one reached the same frame and texts. F1 matched pixel for pixel; the others differed in 0.01–0.35% of their pixels, only in animated marks, in the pointer's hover state or in where the ghost sits. VERIFIED. That run's own PNGs are not in this folder.
- **Every capture needs:** a fresh browser profile, so no theme, layout or dataset is restored. Use an English locale; with this PC's default `vi`, F7's counter reads 1.825. The page needs network access to load the Inter font.
- **Server:** either `https://kerktaiheng.github.io/visualgo-plus-design` (deployed from `662e7b3`; no workflow has run since 2026-10-30), or a local `npm run dev` at the repository root, served at http://127.0.0.1:5186 (`README.md`).
- **Transport:** the footer buttons are First, Previous, Next, Last, Autoplay and Stop. With no run, Next starts a paused run on Frame 1, and each further Next adds one frame.
- **By hand:** use a new guest window. Turn on the DevTools device toolbar, choose "Responsive", set 1440 × 900 with a device pixel ratio of 1, and save with its menu's "Capture screenshot" or, for F1's long version, "Capture full size screenshot". Two kinds of capture are awkward by hand. F3 needs the mouse held down during the capture, so use a screenshot tool with a delay timer or the script. F4–F6 need the capture within about a second, because the step note fades: it is gone by about 1.9 s, and Previous then Next brings it back (VERIFIED). For these three, use the script, or first slow the page's animations to 10% in the DevTools Animations panel (an untested suggestion).

| File | Pixels | File time (2026-11-01, UTC+07:00) | Route | Frame |
|---|---|---|---|---|
| `F1-home-catalogue.png` | 1440 × 900 | 23:52:47 | `/` | none |
| `F1-home-catalogue-fullpage.png` | 1440 × 3076 | 23:52:47 | `/` | none |
| `F2-dfsbfs-bfs-frame8.png` | 1440 × 900 | 23:52:50 | `/dfsbfs` | 8 / 22 |
| `F3-tab-drag-preview.png` | 1440 × 900 | 23:52:52 | `/dfsbfs` | no run |
| `F4-sssp-dijkstra-frame24-note.png` | 1440 × 900 | 23:52:56 | `/sssp` | 24 / 31 |
| `F5-lca-query-6-2-frame2-note.png` | 1440 × 900 | 23:52:59 | `/lca` | 2 / 6 |
| `F6-heap-insert-climb-note.png` | 1440 × 900 | 23:53:02 | `/heap` | 3 / 9 |
| `F7-sorting-compare-4-panes.png` | 1440 × 900 | 23:53:04 | `/sorting` | operation 150 / 1,825 |
| `F8-cut-vertex-bridge-cp4-4-7-last.png` | 1440 × 900 | 23:53:07 | `/dfsbfs/cut-vertex-bridge` | 51 / 51 |

## The files

### `F1-home-catalogue.png` and `F1-home-catalogue-fullpage.png`

- **Shows:**
  - The site bar: the VisuAlgo wordmark, the language picker "en" and Settings.
  - The title "VisuAlgo" with a small ".net/en", the tagline "Visualising data structures and algorithms through animation", and a Search box.
  - The NUS Computing and Optiver logos and the line "VisuAlgo is funded by Optiver, from mid 2023 to mid 2026 and possibly beyond."
  - The credit line: "This site is an experimental version adapted from Prof Halim's visualgo.net, built by Kerk and Bao. Modules marked Coming soon are not built yet; the two editors, marked New, are VisuAlgo+'s own and not on visualgo.net."
  - An "Editors" section with two cards, Graph Editor and Tree Editor, each marked New.
  - In the viewport file, the top of the "Algorithms & Data Structures" grid, cut off at the bottom edge.
  - The full-page file shows the whole grid, four columns wide, and a "Privacy policy" footer.
    - 10 cards open: Sorting; Binary Search Tree, AVL Tree; Binary Heap; Segment Tree ("1 of 3"); Graph Traversal ("5 of 7"); Single-Source Shortest Paths ("2 of 3"); Min Spanning Tree; Max Flow ("1 of 4"); Trie (Prefix Tree); Lowest Common Ancestor.
    - 18 greyed cards are marked "Coming soon": Array, Bitmask, Linked List/Stack/Queue/DLL/Deque, Hash Table, Graph Data Structures, Union-Find Disjoint Sets, Fenwick Tree, Recursion Tree and DAG, Cycle Finding, Suffix Array, Suffix Tree, Convex Hull, Polygon, Graph Matching, Min Vertex Cover, Steiner Tree, Travelling Salesman Problem and NP-hard/complete Reductions.
- **Sample:** none (the default light theme).
- **Capture plan:** open `/`, wait for the Inter font, and capture the viewport; then take a full-page capture.
- **By hand:** use "Capture screenshot" for the first file and "Capture full size screenshot" for the second.

### `F2-dfsbfs-bfs-frame8.png`

- **Shows:** a BFS run paused at frame 8 of 22. It is not an idle page.
  - **Bar:** the route "/dfsbfs"; HOME; the card's algorithms, with "Breadth-First Search" spelled out, then DFS·R, DFS·S, TOPO, BIP and CVB, and SCC and 2SC struck through; Full screen, Shortcuts and Settings.
  - **Left group:** the tabs ACTION (front) and E-LECTURE. The Action panel shows Select preset "Custom graph", Start node A, End node "All vertices" and "Draw graph".
  - **Canvas:** the default graph, vertices A–F with eight weighted directed edges. A is green (visited), B is blue with a glow (current) and C is yellow and dashed (in the queue); edges A→B and A→C are red (BFS tree). The legend is open at the top right and the zoom buttons are at the bottom left.
  - **Right column:** the Pseudocode group (BFS, line 4 "u = dequeue(); visit u" lit) above the Status group, which shows "Visit", Visited 2 / 6, "Dequeue B and visit it." and a queue holding C.
  - **Footer:** Frame 8 / 22, Speed 0.50s ("Slow · 0.75s"), the transport, Autoplay and Stop.
  - There is no step note: BFS has none.
- **Sample:** `INITIAL_GRAPH` (`prototypes/src/graph/graph/samples/initialGraph.ts`), BFS from A.
- **Capture plan:** open `/dfsbfs` and press Next 8 times.

### `F3-tab-drag-preview.png`

- **Shows:** `/dfsbfs` with no run. The footer reads "No run", Status says "No active run", and the canvas shows the default graph with no marks and the legend open.
  - The ACTION tab in the left strip is faded, because it is being held.
  - The body of the Pseudocode group (top right) is framed in the accent colour and tinted. At its top left is a label "ACTION", and in its strip an accent caret stands right after the PSEUDOCODE tab.
  - Just below and to the right of the pointer, near (1330, 330), is a ghost label "ACTION".
  - A dashed band runs along the bottom edge of the drawing (y ≈ 718–838): the empty bottom region offered as a target.
- **Sample:** the default graph, no run.
- **Capture plan:** open `/dfsbfs` and press the ACTION tab. Holding the button, move to the middle of the Pseudocode group's body (x ≈ 1280, y ≈ 316) and wait 0.4 s. Capture while still holding; Escape cancels.
- **By hand:** a screenshot tool with a delay timer, cropped to the page area, or the script.

### `F4-sssp-dijkstra-frame24-note.png`

- **Shows:** `/sssp`, with "Dijkstra" spelled out in the bar, then BF, and BU struck through.
  - **Action panel:** Custom graph, Start node A, End node "All vertices".
  - **Canvas:** the default graph with distance badges A 0, C 2, D 3, B 4 and F 5, and E showing "8→7". A, C and D are green (settled), B is blue (current), and E and F are yellow and dashed (frontier). B → E is dotted green, with its weight 3 in red.
  - **The note:** "4 + 3 < 8 · update" in green, between the 3 and E.
  - **Legend:** open.
  - **Pseudocode:** line 7, "if d[u] + w < d[v]: update v".
  - **Status:** "Relax edge", Settled 4 / 6, "Relax B → E: 4 + 3 = 7 is shorter than 8, so update E's distance to 7." The priority frontier holds F 5 and E 7.
  - **Footer:** Frame 24 / 31 ("Emphasis · 1.00s").
- **Sample:** the default graph, Dijkstra from A.
- **Capture plan:** open `/sssp`, press Next 24 times, and capture about 0.35 s after the last press.

### `F5-lca-query-6-2-frame2-note.png`

- **Shows:** `/lca`, with "Binary Lifting" in the bar.
  - **Action panel:** Custom tree; Preprocessing | Query, with Query on; Node u 6 and Node v 2.
  - **Canvas:** the tree 8 (ROOT) → 12 (14, 10) and 4 (6, 2). Nodes 6 and 2 are blue, with "u" and "v" marks; 8 is yellow and dashed, with an "ancestor" label.
  - **The note:** "same ancestor · keep u, v" in red above 8.
  - **Legend:** open (Query).
  - **Step strip:** under the drawing, "k = 2: up[6][2] = 8, up[2][2] = 8, equal: keep", with an "Ancestor table" button.
  - **Pseudocode:** line 4, "for k desc: up[u][k] ≠ up[v][k]?".
  - **Lower right group:** two tabs, STATUS (front) and ANCESTOR TABLE. Status reads "k = 2: both ancestors are 8, so u and v stay.", with current u 6 (depth 2), current v 2 (depth 2) and active k 2 (2^k = 4).
  - **Footer:** Frame 2 / 6 ("Normal · 0.50s").
- **Sample:** the default tree (the "Balanced BST" text, root 8), Query(6, 2) by default.
- **Capture plan:** open `/lca`, press Next twice, and capture about 0.35 s later.

### `F6-heap-insert-climb-note.png`

- **Shows:** `/heap`, with "Binary Heap" in the bar.
  - **Action panel:** Custom heap; Min heap (on) | Max heap; the operations Create, Insert (on), Extract, Update key, Delete and Heap sort; the hint "Switching the heap order or the operation discards this preview. Apply at the final step to save it."; Value to insert 1.
  - **Canvas:** a tree with index badges i=1 to i=10: 2 (ROOT), 5, 3, 9, 7, 6, 8, 12, 10, and the new 1 at i=10, green with a NOW badge. Its parent 7 at i=5 is yellow and dashed, and the edge between them is red and dashed.
  - **The note:** "1 < 7 · swap up" in green.
  - **Array strip:** under the drawing, "Array representation" with the 10 items, 7 and 1 marked.
  - **Pseudocode:** line 4, "p = i div 2; compare A[i], A[p]".
  - **Status:** "Compare parent", then "1 at index 10 is smaller than parent 7 at index 5, so swap upward."
  - **Footer:** Frame 3 / 9 ("Fast · 0.35s").
- **Sample:** the default min heap 2, 5, 3, 9, 7, 6, 8, 12, 10; Insert 1.
- **Capture plan:** open `/heap`, press Next 3 times, and capture about 0.35 s later.

### `F7-sorting-compare-4-panes.png`

- **Shows:** `/sorting`, with HOME and a pane control 1 | 2 | 4 (4 on) in the bar.
  - **Dataset row:** Distribution Random, Size 48, Seed `sorting-room-01`, Generate, and "48 values · Generate caps at 160".
  - **Four panes in a 2 × 2 grid, each "Paused":**
    - MER — Merge Sort: Ops 150 · Compare 120 · Swaps 0 · Writes 150.
    - BUB — Bubble Sort: Ops 150 · Compare 82 · Swaps 67 · Writes 134.
    - QUI — Quick Sort: Ops 150 · Compare 110 · Swaps 18 · Writes 36.
    - RAD — Radix Sort: Ops 150 · Counts 96 · Pass 2 · Writes 53. It shows a "Current array" strip and the digit buckets 0–9, under "Collect buckets in digit order · Pass 2 · Tens".
  - **Bottom:** a collapsed Status strip. There is no Action, Pseudocode or e-Lecture panel.
  - **Footer:** Op 150 / 1,825, a "Go to operation" box holding 150, Target 12 ops/s ("One At A Time"), the transport, Autoplay and Stop.
- **Sample:** the defaults; panes Merge, Bubble, Quick and Radix.
- **Capture plan:** open `/sorting` and press 4 in the bar. Press Next, which gives Op 0 / 1,825. Type 150 into "Go to operation", press Enter, and wait 0.8 s.

### `F8-cut-vertex-bridge-cp4-4-7-last.png`

- **Shows:** the bar has "Cut Vertex & Bridge" spelled out.
  - **Action panel:** Select preset "CP4 4.7", with its list open under "Example graphs for CVB": Custom graph, CP4 4.1, CP4 4.2, CP4 4.3 DAG, CP4 4.7 (highlighted), CP4 4.16*, CP4 4.20 DAG, Bipartite, CP4 4.22 Bipartite, Large Graph, and Large, Cycles.
  - **Canvas:** vertices 0–7, all green (finished), each with a num,low badge: 0 (0,0), 1 (1,1), 3 (2,1), 2 (3,1), 4 (4,4), 5 (5,4), 7 (6,4), 6 (7,4).
    - Vertices 1, 3 and 4 have a double ring (cut vertices).
    - Edges 0–1 and 3–4 are green (bridges).
    - Edges 1–3, 3–2, 4–5, 5–7 and 7–6 are red (DFS tree edges).
    - Edges 1–2 and 4–6 are blue and dashed (back edges).
  - **Legend:** open (CVB).
  - **Pseudocode:** line 3, "if r has 2+ children: r is a cut vertex".
  - **Status:** "Complete", Cut vertices · Bridges 3 · 2, then "dfs(0) is complete: the call stack is empty, and the root 0 has 1 DFS child, so it is not a cut vertex. Done: 3 cut vertices (4, 3, 1) and 2 bridges (3 — 4, 0 — 1)." An empty call stack follows.
  - **Footer:** Frame 51 / 51.
- **Sample:** "CP4 4.7", which is visualgo.net's example `CP3_4_9` (`prototypes/src/graph/algorithms/visualgoExamples.ts`), read as undirected.
- **Capture plan:** open `/dfsbfs/cut-vertex-bridge`. Press Select preset, then CP4 4.7; the list stays open. Press Next, then Last, and wait 1.2 s.

## Not in this folder

The two diagrams, D1 (architecture) and D2 (the groups model), are not captured. D1 extends doc 03's Diagram 1; D2 is drawn from the list in doc 04 §1.4, since no Mermaid shows it yet. Nothing here shows them.

## Replay script (tested on 2026-11-02)

It writes the nine PNGs above, under the same names, into a folder you choose; pick one outside the repository. The base URL is the Pages site or `http://127.0.0.1:5186`. Run it from Git Bash:

`NODE_PATH="<repository>/node_modules" node replay-figures.cjs https://kerktaiheng.github.io/visualgo-plus-design <out-dir>`

In PowerShell, set `$env:NODE_PATH` first.

```js
// node replay-figures.cjs <base-url> <out-dir>, with NODE_PATH=<repository>/node_modules
const { chromium } = require('playwright')
const [BASE, OUT] = process.argv.slice(2)
const press = async (page, name, times = 1) => {
  for (let i = 0; i < times; i++) {
    await page.locator('footer.footer-bar').getByRole('button', { name, exact: true }).click()
    await page.waitForTimeout(150)
  }
}
const open = async (page, route) => {
  await page.goto(BASE + route)
  await page.waitForFunction(() => document.querySelector('.viz-page') || document.body.innerText.includes('Algorithms & Data Structures'))
  await page.waitForFunction(() => !document.querySelector('.workspace-loading__message'))
  await page.evaluate(async () => { await document.fonts.load('700 14px Inter'); await document.fonts.ready })
  await page.waitForTimeout(800)
}
const figures = {
  'F1-home-catalogue': async (page) => {
    await open(page, '/')
    await page.screenshot({ path: `${OUT}/F1-home-catalogue-fullpage.png`, fullPage: true })
  },
  'F2-dfsbfs-bfs-frame8': async (page) => { await open(page, '/dfsbfs'); await press(page, 'Next', 8) },
  'F3-tab-drag-preview': async (page) => {
    await open(page, '/dfsbfs')
    const tab = await page.locator('[data-panel-tab="action"]').boundingBox()
    const body = await page.locator('section.group:has([data-panel-tab="pseudocode"]) [role="tabpanel"]').boundingBox()
    await page.mouse.move(tab.x + tab.width / 2, tab.y + tab.height / 2)
    await page.mouse.down()
    await page.mouse.move(body.x + body.width / 2, body.y + body.height / 2, { steps: 25 })
    await page.waitForTimeout(400)
  },
  'F4-sssp-dijkstra-frame24-note': async (page) => { await open(page, '/sssp'); await press(page, 'Next', 24) },
  'F5-lca-query-6-2-frame2-note': async (page) => { await open(page, '/lca'); await press(page, 'Next', 2) },
  'F6-heap-insert-climb-note': async (page) => { await open(page, '/heap'); await press(page, 'Next', 3) },
  'F7-sorting-compare-4-panes': async (page) => {
    await open(page, '/sorting')
    await page.locator('[aria-label="Panes"]').getByRole('button', { name: '4', exact: true }).click()
    await press(page, 'Next')
    await page.getByLabel('Go to operation').fill('150')
    await page.getByLabel('Go to operation').press('Enter')
    await page.waitForTimeout(800)
  },
  'F8-cut-vertex-bridge-cp4-4-7-last': async (page) => {
    await open(page, '/dfsbfs/cut-vertex-bridge')
    await page.locator('button[aria-expanded]', { hasText: 'Select preset' }).click()
    await page.getByRole('button', { name: 'CP4 4.7', exact: true }).click()
    await press(page, 'Next')
    await press(page, 'Last')
    await page.waitForTimeout(1200)
  },
}
;(async () => {
  const browser = await chromium.launch()
  for (const [name, steps] of Object.entries(figures)) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-US' })
    const page = await context.newPage()
    await steps(page)
    await page.waitForTimeout(350)
    await page.screenshot({ path: `${OUT}/${name}.png` }) // a note shows for about 1 s after its step
    await context.close()
  }
  await browser.close()
})()
```

# VisuAlgo+ CA Presentation: master script and structure

Working rehearsal draft • 16 November 2026 • 33 minutes plus 12 minutes for Q&A and buffer.

## How to use this version

The talk uses two PowerPoint files. `VisuAlgo_CA_Presentation.pptx` contains 22 timed slides and the Q&A slide (23). `VisuAlgo_CA_QA_Backup.pptx` contains four backup slides, B1 to B4; the recursive DFS recap comes first because it is the fallback for the live demo. Slides 14–18, B1 and B2 embed real-app clips; see [the media map](CA_PRESENTATION_MEDIA_USAGE.md). English speaking text, demo cues and source links are also embedded in speaker notes. Timing includes transitions and demonstrations; it is a rehearsal budget, not measured delivery time. Slides 7–12 are an evidence-based draft for Kerk to confirm and replace with his current details where necessary. No fabricated benchmarks or completed engine integration are claimed.

Script format, 16 November, at Bao's request: every slide has a main message, three to five talking points, a script in plain spoken English, cues and a transition to the next slide. The talking points are there so the speaker can say it in their own words; the script is not meant to be learned by heart. The slide text, clip timings and sources are folded under each script. The same text is in the speaker notes of both PowerPoint files, and [the cheat sheet](VisuAlgo_CA_Cheat_Sheet.md) has the short version. The word counts assume about 130 words per minute and are a guide, not a measurement. Kerk's slides, 7 to 12, were reworded in the same style with their technical content kept; they are his to confirm.

Owner confirmations: editing, playback and comparison were early goals discussed with Prof. Halim; LCA is the main Tree example; Bao recalls frequent Status reading among newer learners, especially for LCA, as motivation for floating text. The intended benefit has not been measured.

Order and test case, 16 November, at Bao's request: Sorting (slide 16) now comes before LCA (slide 17), because it stands apart from the two explanation slides. The LCA slide uses the Balanced · 10 nodes preset. Its clip first moves the root from 10 to 16 on camera, which also shows the re-root operation, then runs the query LCA(8, 20). The slide stresses what floating text is for.

Finalised on 16 November, at Bao's request: the captions under captures say only "Real app capture"; dates, commits and play instructions stay in the speaker notes and the media map. The two dated captions that remain, on slide 21 and backup B3, mark a snapshot of 1 November. Slide 20 says only "Live demo"; the text and cue in section 20 below are a working plan to settle in rehearsal. The backup slides moved to their own file.

Added on 16 November, on Bao's account: Prof. Halim also encouraged widening the range of algorithms VisuAlgo+ supports. There is no written record of this, and no specific topic is attributed to him. LCA with Binary Lifting and Trie were built in the standalone Tree prototype in September 2026 and are in the current app. Heavy-Light Decomposition and Centroid Decomposition are possible later extensions; they are not implemented and are not Semester 2 commitments.

## Run of show

| Section | Speaker | Time | Slides |
|---|---|---:|---|
| Introduction | Bao | 4:00 | 1–4 |
| Early Design | Bao | 3:00 | 5–6 |
| UI/UX Evolution | Kerk | 3:00 | 7–8 |
| Engine & Website | Kerk | 8:00 | 9–12 |
| Algorithm Visualizers | Bao | 8:00 | 13–19 |
| Demo & Evaluation | Both | 5:00 | 20–21 |
| Future Work | Both | 2:00 | 22 |
| Q&A and buffer | Both | 12:00 | 23, then the backup file (B1–B4) |

## Slide-by-slide script

### 01. VisuAlgo+

**Bao · Introduction · 00:00–00:30**

*Script: 62 words, about 29 s at 130 words per minute; the slot is 30 s.*

**Main message:** We are rebuilding VisuAlgo, and we keep what it is for: learning and exploring algorithms.

**Talking points**

- We are Bao and Kerk; the project is VisuAlgo+
- Rebuild the platform, keep its purpose
- Three parts today: how the design evolved, what each of us built, what the prototype taught us

**Script**

> Good afternoon. We are Bao and Kerk, and our project is VisuAlgo+.
>
> We are rebuilding VisuAlgo, and we keep its purpose: helping people learn and explore data structures and algorithms.
>
> Today we will cover three things: how the design evolved, what each of us built, and what we learned from the working prototype.

**Cues**

- The picture is the home page of the current prototype. No click is needed.

**Transition:** Let me start with why we are doing this.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- VisuAlgo+
- Rebuilding interactive algorithm visualization
- Truong Van Quoc Bao and Kerk Tai Heng · Supervisor: A/P Steven Halim
- NUS School of Computing · CP4101 Continuous Assessment · 16 November 2026

**Visual:** The current app's home page beside the title (app 346e84b): the VisuAlgo logo, the credit line, the Editors row and the top of the catalogue. Bao chose it on 16 November in place of a Dijkstra step, which slide 2 also shows.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/main.tex

</details>

### 02. Motivation

**Bao · Introduction · 00:30–01:40**

*Script: 129 words, about 60 s at 130 words per minute; the slot is 70 s.*

**Main message:** We keep VisuAlgo's strengths, and we follow Prof. Halim's directions: better interaction and a wider range of algorithms.

**Talking points**

- VisuAlgo already has custom input and step-by-step runs; we keep them
- Prof. Halim's directions: easier graph editing, clearer parallel and curved edges, richer canvas interaction, side-by-side sorting
- He also encouraged a wider range of algorithms; LCA and Trie are topics I added
- My own focus, from competitive programming and teaching: explain why a step happens

**Script**

> VisuAlgo already lets students try their own inputs and follow an algorithm step by step. We want to keep these strengths.
>
> In our early meetings, Prof. Halim suggested several directions. First, easier graph editing, with clearer parallel and curved edges. Second, richer interaction on the canvas. Third, comparing sorting algorithms side by side. He also encouraged us to cover a wider range of algorithms. The two examples on the last card, LCA and Trie, are topics I added.
>
> These directions were our starting point, and the prototypes helped us explore them.
>
> I come from competitive programming and teaching, so I care about one more thing. Students should understand why a step happens, not only see the final answer.

**Cues**

- Point at one card for each direction, left to right; the fourth card is the wider range of algorithms.
- The images come from the current prototype.

**Transition:** So why not just add these features to the existing site?

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- More convenient graph editing: draw and change the graph you are studying, with parallel and curved edges handled clearly
- Richer interaction on the canvas: inspect a step, move things and see why a decision happens
- Sorting comparison on the same input: several algorithms on one dataset, side by side
- A wider range of algorithms: more topics, such as LCA with Binary Lifting and Trie, on foundations that make later ones easier to add

**Visual:** Four cards, each with a crop of today's prototype; the fourth shows the current Trie page (Insert "care", frame 5/7). Footer: directions proposed by Prof. Halim in early weekly meetings.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

</details>

### 03. Why rebuild the foundation?

**Bao · Introduction · 01:40–02:50**

*Script: 131 words, about 60 s at 130 words per minute; the slot is 70 s.*

**Main message:** In the original code, one common change touches several topics, so we reorganised the foundation.

**Talking points**

- The platform grew over many years; some parts are shared, such as the graph widget
- But each topic has its own input handling and state building
- So one editing change means changes and checks in several topics
- Sorting comparison: each pane needs its own state, with shared controls
- Decision: reorganise the foundation, and keep tools that fit, such as D3

**Script**

> The original platform has grown over many years, with many contributors. It already shares some parts, such as the graph widget in this diagram.
>
> But a lot of logic still lives inside each topic. In the graph modules we looked at, each topic handles its own input and builds its own visual state. So one change to graph editing means changes and checks in several topics.
>
> Sorting comparison raises a different problem. Each pane needs its own state, but one set of controls must drive all of them. Splitting the screen is not enough.
>
> So we decided to reorganise the foundation. We chose boundaries that support these interactions, and we keep useful tools, such as D3, where they fit.

**Cues**

- Point at the three topic boxes, then the shared widget, then the amber box.

**Transition:** With that reason in mind, here is what we aim to deliver.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Shared components already exist: for example, a graph widget used by several topics
- Module-specific logic complicates common changes: input handling and visual-state building live inside each topic
- New interactions need clearer state boundaries: comparison panes need their own state but shared controls

**Visual:** Simplified diagram: three original graph topics, each with its own input handling and state building, over one shared graph widget; consequence: one editing change means coordinated changes and checks across several topics.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

</details>

### 04. Objectives and current scope

**Bao · Introduction · 02:50–04:00**

*Script: 142 words, about 66 s at 130 words per minute; the slot is 70 s.*

**Main message:** We have three objectives and a working prototype; connecting the engine and a first release come next.

**Talking points**

- Three objectives, one per card: a reusable visualization and interaction layer; a renewed website and execution foundation; a working prototype to validate
- Now: Graph, Tree and Sorting share one shell; students tried the prototype in Week 10
- Boundary: the visualizers run TypeScript in the browser; Kerk's C++ and WebAssembly engine is separate; connecting them is Semester 2 work
- Target: a first public release around March 2027; the original VisuAlgo stays online

**Script**

> We have three objectives, one on each card. First, a reusable layer for visualization and interaction, with clear boundaries, so that new algorithms are easier to add. Second, a renewed website and execution foundation. Third, a working prototype that we can validate.
>
> Where are we now? We have a working prototype. Graph, Tree and Sorting share one shell, and students tried it in Week 10.
>
> One boundary is important. Today, the visualizers run TypeScript algorithms in the browser. Kerk has built a separate engine in C++ and WebAssembly. Connecting the two is Semester 2 work.
>
> Our target is a first public release around March 2027, if integration and validation go well. The plan is to keep the original VisuAlgo online, and to link from it to the finished topics in VisuAlgo+.

**Cues**

- Each card has NOW and NEXT.
- Point at the band at the bottom when you reach the boundary.

**Transition:** Let me go back to where it started: the early prototypes.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- A reusable visualization and interaction layer · now: Graph, Tree and Sorting share one shell; LCA and Trie already run on it · next: stabilize the shown workflows; add topics on the same foundations
- A renewed website and execution foundation · now: site with catalogue and routes; separate C++/WebAssembly engine foundation · next: connect them to the visualizers
- A working prototype with further integration ahead · now: students tried the prototype in Week 10 · next: validate, then an initial release around March 2027 (target)
- Current boundary: the visualizers run TypeScript algorithms in the browser; the engine is separate and connecting it is Semester 2 work

**Visual:** Three objective cards with NOW and NEXT chips, and a boundary band.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PREP.md

</details>

### 05. Early visualizer prototypes

**Bao · Early Design · 04:00–05:30**

*Script: 178 words, about 82 s at 130 words per minute; the slot is 90 s.*

**Main message:** Each early prototype tested one requirement that the final design had to meet.

**Talking points**

- The prototypes were experiments toward the goals we discussed with Prof. Halim
- Graph: first separate edit and run views, then one canvas; input, positions and playback are separate, so moving a vertex keeps the same step
- Tree: new topics (LCA with Binary Lifting, Trie); an ancestor table under the tree; preview before Apply
- Sorting: the same array in every pane; each pane has its own state; one playback bar
- Naming: the standalone Graph rewrite is not the layout called V2

**Script**

> These early prototypes were experiments toward the goals we discussed with Prof. Halim. Each one tested a different requirement.
>
> Start with Graph, on the left. My first prototype had separate views for editing and running. In the rewrite, I kept one canvas, and I separated the input, the positions and the playback. So a learner can move a vertex and stay on the same step of the algorithm.
>
> In the middle is the Tree prototype. It added new topics: LCA with Binary Lifting, and Trie. LCA needs an ancestor table under the tree. For operations that change the tree, I tried a preview: you inspect the result before you apply it.
>
> On the right is Sorting. Several algorithms get the same array. Each pane keeps its own state, and one playback bar moves them all.
>
> One note on names. This standalone Graph rewrite is not the layout we later call V2. I will keep the two names apart.

**Cues**

- Point left to right: Graph prototype 1 (the dark one), the Graph rewrite, the Tree prototype, Sorting Room.
- These are the old standalone builds, not the current app.

**Transition:** While I was building the Graph rewrite and the Tree prototype, Kerk was designing the look of the new site.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Graph: editing and playback on one canvas
- Tree: structural operations and ancestor information
- Sorting: independent runs with shared controls

**Visual:** Real stills of the standalone builds, rebuilt at their last documented commits (5fc06a0, c8b14e6, 46ce0a7, 9236a65) and captured on 16 Nov 2026: Graph prototype 1 run view, the Graph rewrite with one canvas, the Tree prototype's Binary Lifting table, and Sorting Room with two panes. Not the current app. The Tree card reads: LCA: ancestor table under the tree; Trie: insert and search along a prefix; Changes previewed before Apply. The prototype's Trie workspace (Insert and Search) is not pictured.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

</details>

### 06. Two parallel foundations

**Bao · Early Design · 05:30–07:00**

*Script: 145 words, about 67 s at 130 words per minute; the slot is 90 s.*

**Main message:** Two foundations grew side by side: my working visualizers and Kerk's design system.

**Talking points**

- From late August, Kerk and I worked in parallel
- Mine: working algorithms, editors and playback, but separate apps with their own controls
- Kerk's: a design system from restyling visualgo.net (nine themes, twenty-six components) and a UI kit; also the first version of his engine
- Three requirements carried forward: keep the drawing available; keep playback familiar; show topic information beside the drawing

**Script**

> From late August, Kerk and I worked in parallel.
>
> On my side, the visualizers already worked. Their algorithms, editors and playback became the base of the later builds. But each one was a separate app, with its own bars and controls. They needed one page and one look.
>
> On Kerk's side, he restyled visualgo.net into a design system, with nine themes and twenty-six components. His UI kit recreates the home page and the visualisation page in the new style, and the site I built later follows his home page. Around the same time, he also committed the first version of his C++ and WebAssembly engine, which he will present later.
>
> From the prototypes, we took three requirements. Keep the drawing available. Keep playback familiar across topics. And show topic-specific information beside the drawing.

**Cues**

- Left card: my standalone Graph rewrite. Right card: Kerk's UI kit, home page and visualisation page.
- Read the three requirements from the bottom of the slide.
- Hand over to Kerk.

**Transition:** Kerk will now show how he laid out the new visualisation page.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Bao · standalone visualizers, Jul–Sep 2026: TypeScript algorithms, editors and playback, reused later; Separate apps, each with its own bars and controls; Showed what each topic needs from a shared page
- Kerk · design system and UI kit, Aug–Sep 2026: Restyled visualgo.net: purple and gold, Inter, nine themes; 26 components, from the top bar to lesson cards; UI kit recreating visualgo.net's home and visualisation pages
- Requirements we carried forward: Keep the drawing available · Familiar playback across topics · Topic-specific information alongside

**Visual:** Left card: a still of Bao's standalone Graph rewrite (slide 5 showed all three prototypes). Right card: the home and visualisation screens of Kerk's design-system UI kit, which recreate visualgo.net's pages in the new style, rendered from commit 634b5be (3 Sep 2026). Both captured on 16 Nov 2026.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/design-history/README.md

</details>

### 07. From nine wireframes to two working layouts

**Kerk · UI/UX Evolution · 07:00–08:30**

*Script: 164 words, about 76 s at 130 words per minute; the slot is 90 s.*

**Main message:** We narrowed nine wireframes to two layouts, and Bao built both, so we could compare real runs.

**Talking points**

- Low-fidelity wireframes of the visualisation page, with an AVL tree as the example
- Same top bar and footer everywhere; the versions differ in where panels live and how they open
- Nine versions: seven layouts and two drag states of V7
- An early layout survey with students: formative, separate from the Week 10 trial
- Bao and I chose V2 (split rails) and V7 (draggable docks); Bao built Graph, Tree and Sorting in both

**Script**

> Alongside the design system, I drew low-fidelity wireframes of the visualisation page. I used an AVL tree as the example.
>
> Every version has the same top bar and footer. e-Lecture is a panel, and the footer holds a scrubber, zoom and shortcuts. The versions differ only in where the panels live and how they open. There are nine versions: seven layouts, and two that show V7 during a drag and after the drop.
>
> I then organised an early layout survey with students. It was formative input, and it is separate from the Week 10 trial.
>
> After that, Bao and I chose two layouts together: V2, with split rails, and V7, with draggable docks.
>
> Bao then built Graph, Tree and Sorting in both layouts, on top of his prototypes and my design tokens and themes. Both builds had the same features. So when we compared them, we were comparing the layouts themselves, on real runs and not on drawings.

**Cues**

- Left: the nine wireframes, with V2 and V7 outlined. Middle: the two chosen wireframes. Right: Bao's working builds.
- Kerk to confirm the wording.

**Transition:** So what did the comparison show?

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Kerk's wireframes, V1–V9: One top bar and footer; seven panel layouts and two drag states of V7
- V2 and V7 chosen together: By Kerk and Bao, after an early layout survey of students that Kerk organised
- Bao's six working builds: Graph, Tree and Sorting in both layouts: his prototypes on Kerk's tokens and themes
- Same features in both builds, so our discussions compared the layouts on real runs, not just as drawings

**Visual:** Left: the "At a glance" grid of Kerk's wireframe page (commit 69aa8e4, 4 Sep 2026), nine frames V1–V9 with V2 and V7 outlined on the slide. Middle: the V2 and V7 wireframes. Right: Bao's working Graph builds in V2 (split rails) and V7 (docks). He made them on 20–27 September; the stills show them as they stood on 17 October, at commit ae63a62, the last one that still had them.

**Team review:** Kerk to confirm this slide: the wireframes, the student feedback he organised (no numbers are on record) and how the choice is described. The script was rewritten on 16 November from the records and Bao's account.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/design-history/README.md

</details>

### 08. From V2 and V7 to V10

**Kerk · UI/UX Evolution · 08:30–10:00**

*Script: 154 words, about 71 s at 130 words per minute; the slot is 90 s.*

**Main message:** V10 keeps the strengths of both: visible stacked panels from V2 and draggable tabs from V7, around a canvas that is never covered.

**Talking points**

- Trade-off: V2 has fixed places with several panels open; V7 has movable panels but one tab per dock
- Bao and I discussed it, with Prof. Halim's feedback; we arrived at V10 in Week 9
- V10: panels stacked and visible together, tabs dragged between areas, several tab groups per area, the canvas in the centre
- Bao built the panel-group model and the shell
- Kerk implemented the agreed refinements and, on 18 October, merged the site and the visualizers into one application

**Script**

> Comparing the two builds showed a trade-off. V2 keeps every panel in a fixed place, and several can be open at once. V7 lets you move panels, but each dock shows only one tab.
>
> Bao and I discussed this, with feedback from Prof. Halim. In Week 9, we arrived at V10, which keeps both strengths.
>
> Panels stay stacked and visible together, as in V2. You can drag tabs between areas, as in V7. Each area can hold several tab groups. And the canvas stays in the centre and is never covered.
>
> Bao built the panel-group model and the shell. I then implemented refinements we agreed on, such as drag sensitivity, controls and fonts. On 18 October, I merged the site and the visualizers into one application, so we now fix the shell in one place.

**Cues**

- Left: what V10 keeps from V2 and from V7. Right: the current app, with its regions outlined.
- The band at the bottom says who did what.
- Kerk to confirm the wording.

**Transition:** Bao will show the shell in detail later. Next, I will turn to the website and the execution architecture.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- From V2 · split rails: Panels stacked and visible together; Its panel positions as V10's default
- From V7 · draggable docks: Panels moved by dragging their tabs; A bottom area and splitters to resize
- V10 · panel groups: The canvas stays central and uncovered; Tab groups around the drawing; One playback bar for every topic
- Discussed together: Kerk and Bao, with Prof. Halim's feedback
- Bao: built V10's panel-group model and shell (16–18 Oct)
- Kerk: refined V10's dragging, controls and fonts; made its site and visualizers one app (18–22 Oct)

**Visual:** Left: Bao's working Tree builds in V2 (split rails) and V7 (docks), as of 17 October, with what V10 keeps from each. Right: the current app (Tree Editor, app 346e84b) with coloured outlines for the tab groups, the canvas and the shared playback bar.

**Team review:** Kerk to confirm this slide: his refinements, the consolidation and how the discussion with Prof. Halim is described. The script was rewritten on 16 November from the records and Bao's account.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/design-history/README.md

</details>

### 09. Application boundaries

**Kerk · Engine & Website · 10:00–12:00**

*Script: 131 words, about 60 s at 130 words per minute; the slot is 120 s.*

**Main message:** The prototype is one application with clear owners, and today the engine is still separate from it.

**Talking points**

- One React and TypeScript application, built with Vite
- The site host owns routing, the top bar and the theme; it mounts Graph, Tree or Sorting
- Each visualizer owns its input and playback; a shared layer supplies the panel layout and presentation utilities
- Drawing: React Flow for Graph and Tree, D3 for some layout calculations, Canvas 2D for Sorting
- Boundary: the visualizers run TypeScript in the page; the WebAssembly engine is a separate project

**Script**

> The prototype is one React and TypeScript application, built with Vite.
>
> The site host owns the routing, the top bar and the theme. It mounts Graph, Tree or Sorting. Each visualizer owns its own input and playback. A shared layer supplies the panel layout and some reusable presentation utilities.
>
> Why separate them this way? The shell should know where the Status panel sits. The algorithm decides what that panel means.
>
> For drawing, Graph and Tree use React Flow, with D3 for some layout calculations. Sorting uses Canvas 2D.
>
> There is one important boundary in the current build. These visualizers run TypeScript algorithms in the page. The WebAssembly engine is a separate project. This lets us develop interaction and execution independently, while we work toward integration.

**Cues**

- Walk down the diagram: the site host, the three visualizers, the shared layer. The engine is the dashed box at the side.
- Kerk to confirm against the current implementation.

**Transition:** Let me now describe that engine.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Site host: routes, top bar and theme
- Visualizers: input, execution and playback (TypeScript in the page)
- Shared layer: layout and presentation utilities
- Separate engine foundation awaiting integration

**Visual:** Layered diagram: site host over three visualizer boxes (Graph and Tree: React Flow with D3 layout; Sorting: Canvas 2D) over the shared layer; the engine is a dashed box to the side.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

</details>

### 10. Engine foundation

**Kerk · Engine & Website · 12:00–14:30**

*Script: 156 words, about 72 s at 130 words per minute; the slot is 150 s.*

**Main message:** The engine runs algorithms in a worker; the plan is that it describes their state and the visualizer explains it to the learner.

**Talking points**

- C++ algorithms compiled to WebAssembly, running inside a worker
- The page and the engine talk through protocol messages, not direct calls
- Protobuf messages with graph and array representations; a Python path through Pyodide for tracing sorting algorithms
- Design question: expose enough state without tying the engine to the page layout
- Plan: the engine describes state and changes; the visualizer decides the note and the pseudocode line

**Script**

> The engine foundation explores running C++ algorithms, compiled to WebAssembly, inside a worker.
>
> The page and the engine talk through protocol messages, not through direct calls into the visual components. The worker gives execution its own context. The page stays responsible for interaction and drawing.
>
> The documented engine uses protobuf messages, with graph and array representations. It also has a Python path, through Pyodide, for tracing sorting algorithms.
>
> The main design question is this. How do we expose enough state for visualization, without making the engine depend on the page layout?
>
> Our answer is a division of work. The engine should describe the algorithm's state and its changes. The visualizer still has to explain them to the learner. For example, when the engine updates a distance, it does not decide where a note appears, or which pseudocode line to highlight. That belongs to the integration boundary.

**Cues**

- Follow the flow on the diagram: the page, the protocol messages, the worker.
- Optional engine demonstration: one forward step in the separate engine build, then its state output. Keep it within 45 seconds, and skip it if time is short.
- Kerk to confirm against the current implementation.

**Transition:** The harder part is connecting the engine to the visualizers.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- C++20 compiled to WebAssembly
- Execution inside a worker
- Protocol messages connect the page and engine
- Python tracing explored through Pyodide

**Visual:** Flow diagram: page ⇄ protocol messages ⇄ worker (WebAssembly engine, Pyodide); band with the design question about exposing state without depending on page layout.

**Delivery cue:** Kerk: confirm against your current engine build. Optional 45-second separate-engine demonstration is included in this time slot.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

</details>

### 11. Reversible execution and integration

**Kerk · Engine & Website · 14:30–16:30**

*Script: 162 words, about 75 s at 130 words per minute; the slot is 120 s.*

**Main message:** The engine and the visualizers keep history differently, so connecting them needs an explicit translation, one Graph algorithm first.

**Talking points**

- Engine: a reversible journal, one record per step, and it can move backward
- Visualizers: Graph and Tree build all steps when a run starts; Sorting pulls from generators and keeps history
- Three things must stay consistent: node and edge identity, run identity, and the meaning of a step
- Bao's earlier integration experiment stays separate from the delivered visualizers
- Next step: one complete Graph integration, checked against the TypeScript behaviour

**Script**

> The engine and the visualizers keep history in different ways.
>
> The documented engine keeps a reversible journal: a record for each step, and it can move backward through those records. The current Graph and Tree visualizers build all their steps when a run starts. Sorting pulls operations from generators and keeps history for seeking.
>
> So connecting them needs an explicit translation. We cannot simply replace one algorithm function with another.
>
> Three things must stay consistent. First, the identity of nodes and edges, especially parallel edges. Second, the identity of a run, when the user changes the input or starts again. Third, the meaning of a step: the drawing, the pseudocode and the text must agree.
>
> Bao did an earlier integration experiment, with stable edge identities and a browser client. It remains separate from the delivered visualizers.
>
> Our proposed next step is one complete Graph integration, checked against the current TypeScript behaviour, before we expand.

**Cues**

- Left card: the engine's history. Right card: the visualizers' history. The three chips below are what integration must keep.
- Kerk to confirm against the current implementation.

**Transition:** Finally, the website that hosts all of this.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Engine history: reversible records per step
- Current visualizers: sequences or operation history
- Integration must preserve identity and step meaning

**Visual:** Two cards marked ≠, over a band with three chips: node and edge identity, the same run across edits and restarts, state/pseudocode/notes agree on a step.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

</details>

### 12. Website integration

**Kerk · Engine & Website · 16:30–18:00**

*Script: 132 words, about 61 s at 130 words per minute; the slot is 90 s.*

**Main message:** The site hosts the visualizers without duplicating their controls, and this boundary is where our contributions meet.

**Talking points**

- The site owns the top bar and the theme; each visualizer supplies its topic-specific parts
- Bao built the working catalogue, the routes and the host adapters on the design system
- Kerk's consolidation and refinements made it a single application
- The wider website infrastructure and the engine still have to join the visualization layer
- Clear responsibilities avoid a second set of playback controls and conflicting theme state

**Script**

> The website has to host the visualizers without duplicating their controls.
>
> In the prototype, the site owns the top bar and the theme. Each visualizer supplies the topic-specific parts, such as the algorithm choices or the sorting pane controls. The host then presents them inside one site.
>
> Bao built the working catalogue, the routes and the host adapters, on top of the design system. My consolidation and refinements made it a single application. So this boundary is where our contributions meet.
>
> The wider website infrastructure and the engine still need to come together with the visualization layer.
>
> Keeping these responsibilities explicit helps us avoid two problems: a second set of playback controls, and conflicting theme state.

**Cues**

- Point at the site frame, then the three visualizer slots, then the attribution line.
- Kerk to confirm against the current implementation.
- Hand back to Bao.

**Transition:** Bao will now explain how the visualization layer uses these boundaries for editing, comparison and explanations.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- One site controls navigation and theme
- Visualizers supply topic-specific controls
- Shared infrastructure supports further integration

**Visual:** Site frame with three visualizer slots and an infrastructure card; attribution line: Bao built the functional catalogue, routes and host adapters; Kerk consolidated and refined.

**Team review:** Kerk to confirm current implementation and add his own technical detail. The script uses the documented architecture, not a fresh engine audit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

</details>

### 13. My visualization contributions

**Bao · Algorithm Visualizers · 18:00–18:40**

*Script: 81 words, about 37 s at 130 words per minute; the slot is 40 s.*

**Main message:** I built the visualizer foundations, the algorithms, the shell and the step explanations; I will show a few decisions you can see on screen.

**Talking points**

- Foundations for Graph, Tree and Sorting
- Algorithms: each needs its own steps, pseudocode and inspector, for example LCA with Binary Lifting, and Trie
- The V10 shell and the integration into the site
- How each step explains itself, and how the behaviour is tested
- Next: a few selected decisions

**Script**

> This slide sums up my part. I built the foundations for Graph, Tree and Sorting, the V10 shell, and the integration into the site.
>
> I also implemented the algorithms. Each one needs its own steps, pseudocode and inspector. Two examples are LCA with Binary Lifting, and Trie.
>
> Finally, I worked on how each step explains itself, and on how we test the behaviour.
>
> I will show a few decisions that you can see on screen.

**Cues**

- Four cards. Do not read them; name each area in one sentence.

**Transition:** The first one is the shell.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Graph, Tree and Sorting foundations
- Algorithm and operation extensions
- V10 shell and site integration
- Step explanations and validation

**Visual:** 2×2 cards with a short detail and a small current-app thumbnail each. Card 02 reads: implemented: LCA (Binary Lifting), Trie, recursive DFS, Bellman-Ford, Prim, bridges, AVL, heap, lazy segment tree; each with its own steps, pseudocode and inspector. Its thumbnail is the current Trie page.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

</details>

### 14. A shared shell with clear constraints

**Bao · Algorithm Visualizers · 18:40–19:50**

*Script: 143 words, about 66 s at 130 words per minute; the slot is 70 s.*

**Main message:** You can move panels around without losing the drawing or the run.

**Talking points**

- The layout has state: moving a panel must keep the canvas and the panel's input
- One model keeps the groups (left, right, bottom) and enforces size limits
- One resolver computes both the real layout and the drop preview, so the preview matches the result
- Saved layouts are versioned and checked; a broken one is repaired or reset
- Trade-off: less freedom than a fully general split layout, for a stable drawing and predictable drops

**Script**

> In the V10 shell, the layout has state. When you move a panel, the canvas and the panel's input must survive.
>
> [Press → to play the clip.] Watch the Status tab. It splits the right column. The counter still says 12. Now it joins the left group. The drawing does not reload. Now it docks under the drawing. Still frame 12.
>
> Behind this is one layout model. It keeps the groups on the left, right and bottom, and it enforces size limits. One resolver computes both the real layout and the drop preview. So the preview matches the result.
>
> Saved layouts are versioned and checked when they load. A broken one is repaired or reset.
>
> The trade-off is this. We give up a fully free split layout, and we get a stable drawing and predictable drops.

**Cues**

- Press → after the first two sentences. The clip is 16 seconds and plays once.
- Name each move as it lands: the split (4 s), the left group (9 s), under the drawing (14 s).
- The footer counter stays at 12 of 21. It is small on Zoom, so say the number.

**Transition:** The same care for the run applies when the user edits the graph.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- The canvas stays mounted: moving Status does not reload the drawing or the run
- One model governs sizes and valid drops: split, join or dock: the preview uses the same geometry as the result
- Saved layouts recover safely: versioned and checked, repaired or reset

**Visual:** Clip `02b_v10_split_left_bottom.mp4` (16.3 s, app 346e84b), paused at frame 12/21 throughout. The Status tab, set up beside Pseudocode, is dragged down to split the right column in two, then into the left group, then to the bottom row under the drawing. The first take, `02_v10_move_panel.mp4`, is kept as an alternative.

**Delivery cue:** Clip, 16.3 s, frame 12/21 throughout.
- 1.5–4.4 s: Status is dragged down its own group (the preview moves from the upper to the lower half).
- 4.4 s: the right column splits into two equal groups.
- 6.3–9.2 s: Status is dragged to the left group.
- 11.1–14.0 s: Status is dragged to the bottom row.
- 14.0 s: Status docks under the drawing; the drawing re-fits and the left group shows E-Lecture.

Live alternative only if time allows.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/02b_v10_split_left_bottom.mp4

</details>

### 15. Input, layout and playback

**Bao · Algorithm Visualizers · 19:50–20:55**

*Script: 124 words, about 57 s at 130 words per minute; the slot is 65 s.*

**Main message:** Moving a vertex changes the drawing; changing a weight changes the problem. So they are stored separately.

**Talking points**

- Four things stored separately: the graph document, the layout, the playback session, the presentation
- Drag a vertex: only the layout changes, so the run continues
- Change a weight: the document changes, so the old run is no longer valid
- A parallel edge is a separate edge, with its own identity and weight
- Result: consistent interaction, because each piece of state has one owner

**Script**

> Moving a vertex changes the drawing. Changing a weight changes the problem. So I store four things separately: the graph document, the layout, the playback session and the presentation.
>
> [Press → to play the clip.] I drag B. Still frame 12. Now the weight of B to A: 1 becomes 5. The run is gone. Now a second edge from B to A, with weight 2.
>
> Dragging changed only the layout. The new weight changed the document. And the two parallel edges are separate edges: each has its own identity and its own weight, in the editor, in the drawing and in the algorithms.
>
> So the interaction stays consistent, because each piece of state has one clear owner.

**Cues**

- Press →. The clip is 16 seconds.
- Say each action as it happens: drag B (2 s), weight 1 to 5 and NO RUN (5 s), the second edge (8 s), its weight 2 (11 s).
- End on the final frame: two B → A edges, labelled 5 and 2.

**Transition:** That was one run. Sorting comparison needs several runs side by side.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Move a vertex: preserve the run (changes Layout only)
- Change an edge weight: invalidate the run (changes the Document)
- Add a parallel edge: a separate edge (its own identity and weight: 5 and 2)
- Who owns which state: Document (nodes, edges, weights) · Layout (positions) · Session (run and selected step) · Presentation (derived highlights)

**Visual:** State-ownership diagram and three outcome cards beside clip `03b_graph_drag_edit_parallel.mp4` (16.2 s): B dragged at frame 12/21; B → A changed from 1 to 5 in Draw graph → Edges, giving NO RUN; a second B → A edge drawn on the canvas and given weight 2. The first take, `03_graph_drag_then_edit.mp4`, is kept as an alternative.

**Delivery cue:** Clip, 16.2 s.
- 0–1.0 s: paused at 12/21, relaxing B → A.
- 1.0–3.5 s: B dragged; still 12/21.
- 3.5–7.2 s: Draw graph → Edges, "B A 1" becomes "B A 5": label 5, NO RUN, NO ACTIVE RUN.
- 7.2–9.2 s: a new edge is dragged on the canvas from B's handle to A's handle.
- 9.2–10.8 s: two B → A edges, curved apart; the new one has no weight yet, the Edges text gains "B A", and the app notes that it counts as 1.
- 10.8–12.2 s: typing " 2" on that line gives the second edge its label 2; the notice goes away.
- 12.2–16.2 s: both edges carry their own weights, 5 and 2; still NO RUN.

Live layout was off. The app has no on-canvas weight edit.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_GRAPH_CASE.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/03b_graph_drag_edit_parallel.mp4

</details>

### 16. Sorting comparison

**Bao · Algorithm Visualizers · 20:55–21:55**

*Script: 124 words, about 57 s at 130 words per minute; the slot is 60 s.*

**Main message:** The panes share one input and one clock, but each keeps its own state; the counters are operations, not runtime.

**Talking points**

- Every pane gets the same input and keeps its own state
- One shared clock moves all panes, one logical operation at a time; they can finish at different times
- Operations come from generators; history is kept for stepping back, which costs memory on long runs
- The counters count operations in the visualization, not CPU time

**Script**

> Sorting comparison gives every pane the same input, but each pane keeps its own state.
>
> One shared clock moves all the panes forward, one logical operation at a time. They can show different actions, and they can finish at different times.
>
> [Press → to play the clip.] Here, Bubble Sort and Selection Sort get the same twelve values. They pause together at operation 48, then continue, and I jump to the end.
>
> Each pane's operations come from a generator. We keep the history, so you can step backward. On long runs, that history costs memory.
>
> One caution. These counters count operations in the visualization. They are not CPU time. So the comparison shows behaviour, not speed.

**Cues**

- Press →. The clip is 10 seconds.
- Say 'both at 48' when the panes pause.
- Last is a jump to the end, not a speed result.

**Transition:** The next two slides are about a different question: how one step explains itself.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- The same dataset in every pane: 12 values, Bubble and Selection
- One clock, independent operation streams: both panes pause at operation 48
- Retained history supports seeking: the clip ends with Last, a seek to the final operation
- Operation counts are not CPU time

**Visual:** Codex clip `02_sorting_shared_clock.mp4` (10.4 s), poster at operation 48.

**Delivery cue:** Codex clip, 10.4 s: Bubble and Selection on 8, 3, 10, 1, 6, 4, 12, 2, 9, 5, 11, 7 at 12 operations/s; both pause at operation 48 (Bubble 27 compares, 19 swaps; Selection 40 compares, 4 swaps); Last ends at 92 and 86 operations. Live alternative: step back once with Prev, only if time allows.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16/02_short_clips/02_sorting_shared_clock.mp4

</details>

### 17. LCA: explaining a decision to stay

**Bao · Algorithm Visualizers · 21:55–23:50**

*Script: 214 words, about 99 s at 130 words per minute; the slot is 115 s.*

**Main message:** Floating text puts the reason beside the node, so a step with no movement still explains itself.

**Talking points**

- Binary Lifting is a topic I added; a query has several stages and reads an ancestor table
- Clip: the root moves from 10 to 16, then LCA(8, 20): 8 lifts to 4; both stay at ancestor 16; both lift at k = 0; the answer is 16
- During the query no node moves, and 5 of the 12 steps only decide to stay
- With floating text the reason sits beside the node; Status keeps the full sentence
- Why: as I remember the Week 10 trial, newer learners often had to read Status; the benefit is not measured yet

**Script**

> Binary Lifting is one of the topics I added. A query has several stages, and it reads an ancestor table.
>
> [Press → to play the clip.] I move the root from 10 to 16. Then I ask for the LCA of 8 and 20. 8 is deeper, so it lifts two levels, to 4. Now both ancestors are 16, so u and v stay. At k = 0, the ancestors 10 and 18 differ, so both lift. Their parent, 16, is the answer.
>
> Notice what happened. During the query, no node moved. And five of the twelve steps only decided to stay: two while 8 was catching up, and three at ancestor 16. Without a note, those steps look the same.
>
> With floating text, the reason sits beside the node. The learner can read it without leaving the tree. Status still keeps the full sentence.
>
> I added this after the Week 10 trial. As I remember it, newer learners often had to read Status for algorithms with several stages, such as LCA. We have not yet measured whether floating text helps.
>
> The same rooted tree and ancestor queries also prepare the ground for more advanced tree topics later.

**Cues**

- Press → after the first two sentences. The clip is 28 seconds; keep pace with it.
- Clip: the root moves to 16 (3 s), the query starts (5 s), 8 lifts to 4 (10 s), both stay at 16 (14 to 20 s), both lift (20 s), the answer 16 (25 s).
- After the clip, point at the three note crops on the left.
- Say clearly that the benefit is not measured yet.
- If you are late, skip the last sentence, on advanced tree topics.

**Transition:** LCA shows a note when a step arrives. The next slide adds two more tools: motion while paused, and hover on the result.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Floating text puts the reason beside the node: 9 of this query's 12 steps carry a note; no node moves during the query
- Query: LCA(8, 20) = 16 (Balanced · 10 nodes; root moved 10 → 16)
- Depth gap 2: lift u from 8 to 4
- Same ancestor 16: keep u and v
- Ancestors 10 and 18 differ: lift both

**Visual:** Clip `01d_lca_reroot_on_camera_8_20.mp4` (27.9 s, app 346e84b): the root is moved from 10 to 16 on camera, then the query runs. The left column shows three of the run's notes, cropped from stills of frames 4, 8 and 9: "gap 2 ≥ 2 · lift u", "same ancestor · keep u, v" and "differ · lift both". Earlier clips, kept as alternatives: `01c_lca_reroot_8_20.mp4` (the same query without the re-root on camera), `01b_lca_keep_then_jump.mp4` (LCA(6, 10) = 8) and `01_lca_equal_ancestors.mp4` (LCA(6, 2) = 4), both on the default tree.

**Delivery cue:** Clip, 27.9 s; keep talking over it. Set up before recording: preset Balanced · 10 nodes (root 10), u = 8, v = 20. The re-root is in the clip.
- 0.0–1.5 s: the preset with root 10. Root under Structure reads 10 and Depth reads 3.
- 2.4–3.3 s: typing 16 in the Root control moves the root. The ROOT badge moves to 16, the tree is laid out again and the view re-fits. Depth reads 4; u and v are kept.
- Frame 1/12 (5.0 s): depths 4 and 2.
- Frames 2–3 (6.2 s, 8.2 s): k = 3 and k = 2, the gap 2 is smaller than 8 and 4, so u stays ("gap 2 < 8 · keep u", "gap 2 < 4 · keep u").
- Frame 4 (10.2 s): k = 1, "gap 2 ≥ 2 · lift u". Frame 5 (12.2 s): u moves from 8 to 4, "↑ 2 levels".
- Frames 6–8 (14.3 s, 16.3 s, 18.3 s): k = 3, 2, 1, both ancestors are 16, "same ancestor · keep u, v".
- Frame 9 (20.3 s): k = 0, ancestors 10 and 18 differ, "differ · lift both". Frame 10 (22.3 s): u = 10, v = 18.
- Frame 11 (24.2 s): same parent, 16. Frame 12 (25.4 s): LCA(8, 20) = 16.

Say that floating text is a design response to a formative observation; its effect is not measured.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/week10_user_trial_addendum.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/01d_lca_reroot_on_camera_8_20.mp4 (stills in https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/stills/)

</details>

### 18. Pause and inspect the result

**Bao · Algorithm Visualizers · 23:50–25:10**

*Script: 153 words, about 71 s at 130 words per minute; the slot is 80 s.*

**Main message:** Emphasis and progress are separate: motion while paused, a note when a step arrives, and hover on the result never advance or rerun the algorithm.

**Talking points**

- Dijkstra from vertex 0 on visualgo.net's nine-vertex 'Big' example
- Paused at frame 17: the light on edge 2 to 3 keeps moving, the counter does not (Kerk's suggestion, my implementation)
- Next: a note beside 3 says 12 + 14 < 33, so update; 33 becomes 26
- Final frame: hover 8 gives 0, 2, 3, 8 with distance 42; hover 4 gives distance 46; read from the stored result
- The motion can be turned off and respects the reduced-motion setting

**Script**

> I also separate visual emphasis from algorithm progress. This is Dijkstra from vertex 0, on the nine-vertex 'Big' example from visualgo.net.
>
> [Press → to play the clip, and name each step as it happens.] Still 17: watch edge 2 to 3. Next: a note. Last. Hover 8. Hover 4.
>
> While the run was paused, the light on the edge kept moving, but the counter stayed at 17. This motion shows what we are looking at, without advancing the algorithm. Kerk suggested it, and I implemented it.
>
> When I pressed Next, a short note appeared beside 3: 12 plus 14 is less than 33, so update. The distance changed from 33 to 26.
>
> At the final frame, hovering 8 showed its shortest path: 0, 2, 3, 8, with distance 42. Hovering 4 gave distance 46. The app reads this from the stored result; it does not run Dijkstra again.
>
> The motion can be turned off, and it respects the reduced-motion setting.

**Cues**

- Press →. The clip is only 14 seconds: paused at 17 (0 s), Next (3 s), Last (6 s), hover 8 (8 s), hover 4 (11 s).
- During the clip, only name the steps. Explain after it stops.
- The paused motion is subtle on Zoom: say 'still 17' and point at the edge from 2 to 3.

**Transition:** The editors bring these features together.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Paused motion keeps the current relationship visible: the counter stays at frame 17 while edge 2 → 3 is emphasised
- A short note explains the step on arrival: frame 18, 12 + 14 < 33 · update
- Final Dijkstra hover reveals a computed path: 8: 0 → 2 → 3 → 8, distance 42 · 4: distance 46

**Visual:** Clip `04b_dijkstra_big_note_pause_hover.mp4` (14.0 s): Dijkstra from 0 on the nine-vertex Big preset (visualgo.net's TESSELLATION). The first take, on the four-vertex S, A, B, T graph, `04_dijkstra_note_pause_hover.mp4`, is kept as an alternative.

**Delivery cue:** Clip, 14.0 s.
- 0–3.0 s: paused at 17/53 (inspect 2 → 3, weight 14); the streak and glow move.
- 3.0 s: Next to 18/53; "12 + 14 < 33 · update" beside 3, whose badge reads 33→26.
- 6.0 s: Last, 53/53, 9 nodes settled.
- 7.6 s: hover 8: 0 → 2 → 3 → 8, distance 42.
- 10.6 s: hover 4: 0 → 2 → 3 → 4, distance 46.

Point at the 2 → 3 edge while the counter reads 17. Edge weights are small at slide size.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/04b_dijkstra_big_note_pause_hover.mp4

</details>

### 19. Editors for exploring an example

**Bao · Algorithm Visualizers · 25:10–26:00**

*Script: 105 words, about 48 s at 130 words per minute; the slot is 50 s.*

**Main message:** The editors start from the user's own example, and let them ask several questions about it.

**Talking points**

- Two entry points on the home page: the Graph Editor and the Tree Editor
- Start from an example you already have in mind, then try compatible algorithms on it
- Fits competitive programming practice: a small test, an observation, a counterexample
- The original VisuAlgo already accepts custom input; ours is a more explicit entry point
- An intended use; adoption is not measured

**Script**

> On the home page, there are two editors: the Graph Editor and the Tree Editor. They support a workflow that starts from an example.
>
> A user may already have a graph in mind, and want to investigate it. This fits competitive programming practice: build a small test, check an observation, or look for a counterexample.
>
> The original VisuAlgo already accepts custom input. What we add is a more explicit entry point, and a workflow built around that input. The Tree Editor currently covers Binary Lifting, BST and AVL.
>
> This is the use we intend. We have not measured adoption.

**Cues**

- The picture is the Editors section of the home page.
- Press → to show the Live demo slide, then switch to the browser.

**Transition:** Let us look at this live.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Begin with a graph or tree
- Try compatible algorithms
- Build small tests and investigate conjectures

**Visual:** Current Editors section of the home page (app 346e84b) above a three-step flow; limits line: custom input already exists in VisuAlgo, this is a more explicit entry point; adoption not measured.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

</details>

### 20. Live demo

**Both · Demo & Evaluation · 26:00–29:00**

*Script: 230 words, about 106 s at 130 words per minute; the slot is 180 s.*

**Main message:** One example, several questions: the same input drives different algorithms, in one interface.

**Talking points**

- This is the running app, not a recording
- Graph Editor: one small graph; eleven graph algorithms on the same input
- Question 1, Dijkstra from A: hover E gives A, B, E with distance 7; hover D gives A, C, D with distance 3
- Question 2, recursive DFS on the same graph: the last frame replays the DFS tree (A, B, D, F, E, C)
- Kerk: one interface for every structure
- Tree Editor: pause on a step and hover a node to see its path to the root, its ancestors and its table row

**Script**

> **Bao:** This is the running app, not a recording. I start from the Graph Editor.
>
> **Bao:** This small graph is the input. The editor offers eleven graph algorithms on this same input.
>
> **Bao:** Question one: what are the shortest paths from A? I run Dijkstra and jump to the end. Hovering E shows its path: A, B, E, with distance 7. D goes through C, with distance 3. Nothing runs again; the app reads the finished result.
>
> **Bao:** Question two, on the same graph: in what order does recursive DFS visit the vertices? I switch to DFS and let it play. At the last frame, the drawing replays the DFS tree in visit order: A, B, D, F, then E, then C. So one input answered two questions.
>
> **Kerk:** The site gives these activities one interface. You go back to the editors and choose another structure, with the same bar, panels and footer.
>
> **Bao:** In the Tree Editor, one tree is shared by Binary Lifting, BST and AVL. I pause on a step and hover node 6. The app shows its path to the root, marks its ancestors one and two levels up, 4 and 8, and highlights row 6 of the ancestor table. The hover does not move the step.
>
> **Bao:** That is the workflow we aim for: one example, several questions.

**Cues**

- A proposed plan, checked on app 346e84b on 16 November. Settle it in rehearsal.
- Before the talk: open the app, load both editors once, choose Settings → Reset panel layout, check that 'Animate paused steps' is on, and return to the home page.
- 0:00 Home page → click the Graph Editor card. It opens on Breadth-First Search with the default graph: vertices A to F, eight directed edges.
- 0:10 Click Algorithms ▾ to show the list (11 algorithms in 5 groups), then press Esc.
- 0:20 Click DIJ. Click Next (frame 1 of 31), then Last. Hover E: A → B → E · distance 7. Hover D: A → C → D · distance 3.
- 0:50 Click DFS. The graph stays and the footer says NO RUN. Click Autoplay (31 frames, about 15 seconds). Final frame: Visited A, B, D, F, E, C.
- 1:30 Kerk speaks. Bao clicks HOME, then the Tree Editor card.
- 1:45 It opens on Binary Lifting, Query, root 8, u = 6, v = 2. Click the Ancestor table tab. Click Next twice (frame 2 of 6, note 'same ancestor · keep u, v'). Hover 6, then 14.
- 2:40 Return to PowerPoint and press → for slide 21.
- If a step fails, do not debug: use the clips on slides 15, 17 and 18, or B1 in the backup file. If time is short, stop after the DFS recap.

**Transition:** So how did we evaluate all this?

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Live demo
- A short demo of VisuAlgo+

**Visual:** A navy divider slide with only those two lines. At Bao's request (16 November), what the demo shows is settled here in the script, not on the slide. The text and cue below are a working plan to settle in rehearsal.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

</details>

### 21. Evaluation and design response

**Both · Demo & Evaluation · 29:00–31:00**

*Script: 189 words, about 87 s at 130 words per minute; the slot is 120 s.*

**Main message:** We tested the software and ran a formative trial in Week 10; floating text is a design response, and its effect is not yet measured.

**Talking points**

- Bao: tests, a snapshot of 1 November: 3,273 unit tests and 151 browser cases passing
- Bao: an example of an independent check: cut vertices and bridges
- Kerk: Week 10: NUS students used V10 on their own for 15 to 20 minutes; sessions recorded; a short post-use test and feedback
- Bao: as I remember it, newer learners often had to read Status, so I added floating text, with legend and Status changes
- Not measured yet; a follow-up study needs defined tasks

**Script**

> **Bao:** We evaluated in two ways: software tests, and formative feedback from users.
>
> **Bao:** On testing, our report snapshot from 1 November records 3,273 passing unit tests and 151 passing browser cases in Chromium. Here is one example. For cut vertices and bridges, a separate check removes each vertex or edge and counts the connected components again. So the result is checked by a different method.
>
> **Kerk:** In Week 10, NUS students with different levels of algorithm experience used V10 on their own, for 15 to 20 minutes. We recorded the sessions, then collected a short post-use test and feedback. This was separate from the earlier layout survey.
>
> **Bao:** As I remember it, newer learners still often had to read Status, especially for algorithms with several stages, such as LCA. So I added floating text near the objects on the canvas, together with changes to the legend and Status.
>
> **Bao:** These are design responses to formative observations. We have not measured whether floating text improves learning or reduces attention switching. A follow-up study needs defined tasks, with the revised interface.

**Cues**

- The two numbers are a snapshot of 1 November, not a rerun today. Say the date.
- Order: Bao, Kerk, Bao.

**Transition:** That brings us to the plan for Semester 2.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- 1 Nov 2026: 3,273 unit tests and 151 Chromium cases (snapshot, app 662e7b3; not a rerun today)
- Week 10: independent use, post-use test and feedback
- Frequent Status reading motivated floating text
- Learning impact remains unmeasured

**Visual:** Two stat callouts, a Week 10 card, a design-response band and an amber limits band.

**Delivery cue:** Historical test snapshot: app commit 662e7b3, 1 November 2026. LCA-specific observation is Bao’s recollection clarified on 16 November, not a coded analysis of reviewed footage.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/week10_user_trial_addendum.md

</details>

### 22. Semester 2 priorities

**Both · Future Work · 31:00–33:00**

*Script: 216 words, about 100 s at 130 words per minute; the slot is 120 s.*

**Main message:** Next: one Graph algorithm through the engine end to end, a stable and evaluated prototype, and a first release around March 2027.

**Talking points**

- Kerk: the integration milestone is one Graph algorithm across the full application, checked against the TypeScript version
- Bao: stabilise the workflows we showed; evaluate the explanations with defined tasks; measure startup, seeking and memory
- Kerk: target a first public release around March 2027; the original platform stays available
- Bao: the wider ambition is the original range, then advanced topics; Heavy-Light and Centroid Decomposition are possibilities, not commitments
- Today we have the foundation and a working prototype

**Script**

> **Kerk:** Our next integration milestone is one Graph algorithm working across the full application. The input, the engine and the playback must agree on three things: node and edge identity, the meaning of each step, and cancellation. We can check the result against the current TypeScript version before we go further.
>
> **Bao:** In parallel, I want to stabilise the workflows we showed today, and evaluate the new explanations. For example, we can ask a learner to explain why an LCA step keeps both nodes in place, and observe how they use the canvas, the ancestor table and Status. We also need measurements for startup, seeking, and memory on long runs.
>
> **Kerk:** We are targeting a first public release around March 2027, depending on integration and validation. The current plan keeps the original platform available, and links to the completed topics.
>
> **Bao:** Our wider ambition is to cover the original range of algorithms and, later, to add advanced topics. For example, LCA already uses rooted trees and ancestor queries. That work could later support Heavy-Light Decomposition or Centroid Decomposition. These are possibilities, not Semester 2 commitments. Integration, validation and stability come first.
>
> **Bao:** What we have today is the foundation: working visualizers, and a prototype to build that release on.

**Cues**

- Four steps on the roadmap. Kerk takes integration and the release; Bao takes validation and coverage.
- The release paragraph was marked 'Both' before; this split is a proposal for Kerk to confirm.
- March 2027 is a target, not a promise.

**Transition:** That is the end of our talk.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Integrate one Graph algorithm end to end
- Validate interaction, correctness and resource use
- Evaluate revised explanations with defined tasks
- Target an initial release around March 2027

**Visual:** Four-step roadmap, each with a one-line detail. Limits lines: March 2027 is a target; possible later extensions, not Semester 2 commitments: advanced tree topics such as Heavy-Light Decomposition and Centroid Decomposition.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

</details>

### 23. Questions

**Backup / Q&A, outside timed talk**

*Script: 21 words, about 10 s at 130 words per minute.*

**Main message:** Thank the audience and open the floor.

**Talking points**

- Thank you
- Questions on the design decisions, the implementation or the evaluation plan
- The backup slides are in the second file

**Script**

> Thank you for listening. We are happy to take your questions, on the design decisions, the implementation, or the evaluation plan.

**Cues**

- Leave this slide up during questions. Switch to the backup file when a backup slide helps.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Questions
- Interactive visualization foundations
- A working prototype and a defined integration path
- Evidence and media: github.com/BJoozz/docsforfyp

**Backup file:** open `VisuAlgo_CA_QA_Backup.pptx` before the talk. It holds four slides for Q&A: B1 recursive DFS recap (also the fallback for the live demo), B2 preview before Apply (BST), B3 correctness and limitations, B4 evidence and ownership.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/report/main.tex

</details>

## Backup file

`VisuAlgo_CA_QA_Backup.pptx` holds the four backup slides, pages B1 to B4. They are outside the timed talk. The recursive DFS recap is first because it is the fallback for the live demo.

### B1. Backup: recursive DFS recap (demo fallback)

**Backup / demo fallback, outside timed talk**

*Script: 61 words, about 28 s at 130 words per minute.*

**Main message:** If the live Graph demo fails, this clip shows the recursive DFS recap.

**Talking points**

- The same S, A, B, T graph as the clips on slides 14 and 15
- The final frame replays the DFS tree in visit order: S, A, T, then S, B
- Different from Dijkstra's final frame, where you hover a vertex to see its path

**Script**

> This is recursive DFS on the same S, A, B, T graph as the clips on slides 14 and 15.
>
> [Press → to play the clip.] On the final frame, the drawing replays the DFS tree in visit order, every few seconds: S to A to T, then S to B.
>
> This is different from Dijkstra's final frame, where you hover a vertex to see its path.

**Cues**

- Use this slide only if the Graph Editor part of the live demo fails.
- Press → to play. The clip is 8.5 seconds.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Same graph, another question: recursive DFS from S on the S, A, B, T graph of slides 14–15
- The final frame replays the DFS tree: glow and streak in visit order, S → A → T, then S → B
- Different from Dijkstra's hover: a recap of the traversal, not a path query

**Visual:** Clip `06_dfs_recursive_recap.mp4` (8.5 s): Last to 21/21, visited S, A, T, B; the final frame replays the DFS tree about every 3 s.

**Delivery cue:** Press → to play the clip.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_INTERACTIVE_DEMO.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/06_dfs_recursive_recap.mp4

</details>

### B2. Backup: preview before Apply

**Backup / Q&A, outside timed talk**

*Script: 95 words, about 44 s at 130 words per minute.*

**Main message:** An operation that changes the tree runs as a preview first; only Apply commits it.

**Talking points**

- A changing operation needs a different contract from a read-only query such as LCA
- BST Insert 5 runs as a preview: the search path and the new node are visible, and I can step backward
- The tree and its text do not change until Apply
- Apply commits the result: the text gains the edge 6 5 and the run ends
- Heap insertion follows the same contract

**Script**

> An operation that changes the tree needs a different contract from a read-only query such as LCA.
>
> Here, BST Insert 5 runs as a preview. You can see the search path and the new node. But the tree itself, and its text input, do not change yet. [Press → to play the clip.] Two steps back. Forward again. Now Apply. The tree text gains the edge 6 5, and the run ends.
>
> So only Apply commits the result. If I switch to another operation, the preview is discarded.
>
> Heap insertion follows the same contract, with an array view beside the tree.

**Cues**

- Explain the preview first, on the poster. Then press →: the clip is 8.6 seconds: two steps back, forward again, then Apply.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Inspect intermediate structures: BST Insert(5), the new node is a preview
- Step backward through the preview: the committed tree is unchanged
- Apply the completed result to the input: the tree text gains the edge 6 5

**Visual:** Clip `05_bst_preview_apply.mp4` (8.6 s).

**Delivery cue:** Clip, 8.6 s: preview complete at 8/8 (text still 6 lines); Previous to 7/8 and 6/8; Next back to 8/8; 5.2 s Apply insertion, NO RUN; 6.2 s Edit tree shows "6 5" (8 nodes, 7 edges).

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

**Media:** https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/clips/05_bst_preview_apply.mp4

</details>

### B3. Backup: correctness and limitations

**Backup / Q&A, outside timed talk**

*Script: 100 words, about 46 s at 130 words per minute.*

**Main message:** We check results with an independent method, and we are open about the limits.

**Talking points**

- Cut vertices and bridges: an independent check removes each candidate and counts the components again
- Exact edge identity matters: removing one of two parallel edges keeps the connection
- Limits: sorting history is not bounded; Graph and Tree build all their steps up front
- Passing tests do not prove full correctness, performance or learning benefit
- AI tools assisted under my requirements; the design choices, acceptance and validation are mine

**Script**

> For cut vertices and bridges, an independent check removes each candidate and counts the connected components again.
>
> Exact edge identity matters here. Removing one of two parallel edges keeps the connection, so it is different from removing the connection altogether.
>
> There are limits. Sorting keeps a history that is not bounded, and Graph and Tree build all their steps up front.
>
> Passing tests cover the tested cases. They do not prove complete correctness, performance, or learning benefit.
>
> AI tools assisted the implementation and the review, under my requirements. I remained responsible for the design choices, the acceptance and the validation.

**Cues**

- The capture is from 1 November 2026.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- Independent oracle for cut vertices and bridges
- Stable edge identity for parallel edges
- Long sorting histories still cost memory

**Visual:** Historical still (app 662e7b3, 1 Nov 2026), now larger.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_CONTRIBUTION_MAP.md

</details>

### B4. Backup: evidence and ownership

**Backup / Q&A, outside timed talk**

*Script: 44 words, about 20 s at 130 words per minute.*

**Main message:** The main evidence is in the public repository, and each slide's notes link to its sources.

**Talking points**

- Repository: BJoozz/docsforfyp
- The CA report and the architecture records
- The contribution map and the prototype history
- The Week 10 trial addendum
- Each slide's notes link to its sources and media

**Script**

> Our main evidence is in the public repository, BJoozz/docsforfyp. It holds the CA report, the architecture records, the contribution map, the prototype history and the Week 10 addendum.
>
> Each slide's notes link to its sources and media. The application repository itself is private.

**Cues**

- The details are in the REFERENCE block below.

<details>
<summary>Slide text, clip details and sources</summary>

**On slide**

- CA report and architecture records
- Contribution map and prototype history
- Week 10 trial addendum
- Source links in each slide’s notes

**Visual:** Four evidence cards with repository paths.

**Source:** https://github.com/BJoozz/docsforfyp/blob/main/docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md

</details>

## Demo preparation and remaining work

Slides 14–18 now play real-app clips embedded in the deck (app `346e84b`, recorded 15–16 November), so no window switching is needed during the technical section. The live demo stays on slide 20. Each clip has a poster frame on the slide as its static fallback; press → or click to play. Details: [media map](CA_PRESENTATION_MEDIA_USAGE.md) · [changelog](CA_DECK_CHANGELOG.md).

| Clip or live action | Slide | Length | Fallback |
|---|---:|---:|---|
| V10: split, join and dock Status while paused | 14 | 16.3 s clip | Poster: Status docked under the drawing at 12/21 |
| Vertex drag, weight edit and a parallel edge | 15 | 16.2 s clip | Poster: both B → A edges, labelled 5 and 2 |
| Sorting shared input and clock | 16 | 10.4 s clip (Codex) | Poster: both panes at operation 48 |
| Root moved from 10 to 16, then LCA(8, 20) | 17 | 27.9 s clip | Poster: frame 9/12, "differ · lift both" |
| Dijkstra on the nine-vertex Big graph: paused motion, note and final hover | 18 | 14.0 s clip | Poster: frame 18/53 with the 2 → 3 update note |
| Joint editor workflow | 20 | 3 min live | Clips on slides 15, 17 and 18; backup B1 for the DFS recap |

### Demo input: the editors' defaults

The proposed demo in section 20 needs no typing. It was run step by step on app `346e84b` on 16 November; these are the values the app showed.

- **Graph Editor.** It opens on Breadth-First Search with a directed graph: vertices A to F and the eight edges below. The Algorithms menu lists 11 algorithms in 5 groups.
- **Dijkstra (DIJ), start A.** 31 frames. Final distances: A 0, B 4, C 2, D 3, E 7, F 5. Hover E: A → B → E · distance 7. Hover D: A → C → D · distance 3. Hover F: A → C → D → F · distance 5.
- **Recursive DFS (DFS), same graph.** The graph text is unchanged and the footer says NO RUN until the run starts. 31 frames. Final frame: Visited A, B, D, F, E, C, with 5 tree edges; the drawing then replays the DFS tree.
- **Tree Editor.** It opens on Binary Lifting, Query, with a seven-node tree rooted at 8, u = 6 and v = 2. Frame 2 of 6 shows the note "same ancestor · keep u, v". Hovering 6 on that paused step shows its path to the root, rings on 4 and 8 with the distances 1 and 2, and row 6 of the Ancestor table highlighted; the frame stays at 2 of 6.

```text
A B 4
A C 2
B D 5
B E 3
C D 1
C E 6
D F 2
E F 4
```

An earlier idea, kept as an alternative if you want to show an edit live: type the directed graph A B 4, A C 2, A D 6, C B 1, C D 7, B D 2, run Dijkstra from A, then change B D to 8 and run again. Those results were never checked on the app.

### Prepared LCA input

Choose the preset Balanced · 10 nodes (root 10), then set Root to 16 under Edit tree → Structure; the slide-17 clip shows this step. The clip then queries 8 and 20: 8 first lifts two levels to 4; at k = 3, 2 and 1 both ancestors are 16, so the cursors stay; at k = 0 the ancestors are 10 and 18, so both lift; LCA(8, 20) = 16. The earlier clips use the default tree (root 8): LCA(6, 10) = 8 and LCA(6, 2) = 4.

```text
10 4
4 2
4 6
6 8
10 16
16 12
12 14
16 18
18 20
```

### Rehearsal checks

- Use English locale, a readable viewport and a known saved layout.
- Disable Live layout for the graph drag comparison.
- Check Animate paused steps and reduced-motion preferences.
- Use Next to trigger floating text; verify the note remains legible long enough.
- The clips come from main 346e84b; if the demo build differs, check the slide-20 steps on it.
- Click through slides 14–18 of the main deck and B1–B2 of the backup file once in slideshow mode; each clip should play on →.
- Open both files before the talk and share the whole screen on Zoom, not one window, so the audience also sees the backup file and the browser when you switch to them.
- Present from copies of the two files outside OneDrive. On 16 November, after the deck in the synced folder was opened in PowerPoint, it came back with shapes from an older version doubled on slide 2.
- Kerk confirms slides 7–12 and the first integration algorithm.
- Keep March 2027 as a target, not a guaranteed release date.
- If running late, stop the demo after the DFS recap; the LCA clip was already shown on slide 17.

## Source notes

Deck media: https://github.com/BJoozz/docsforfyp/blob/main/presentation/ca-2026-11-16-deck-media/README.md
Historical screenshots: https://github.com/BJoozz/docsforfyp/blob/main/figures/README.md
Test evidence: https://github.com/BJoozz/docsforfyp/blob/main/04_figures_and_validation.md
Trial record: https://github.com/BJoozz/docsforfyp/blob/main/report/week10_user_trial_addendum.md
Architecture: https://github.com/BJoozz/docsforfyp/blob/main/03_architecture_and_decisions.md

This master supersedes earlier suggested timings and Heap-first technical sequencing. Older drafts remain useful for evidence and Q&A.
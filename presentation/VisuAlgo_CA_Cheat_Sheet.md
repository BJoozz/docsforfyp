# VisuAlgo+ CA talk: cheat sheet

One glance per slide: the message, the points to hit and the line that leads to the next slide. Clip and demo slides also list their cues. The full wording is in [the master script](VisuAlgo_CA_Master_Script.md) and in the speaker notes. Both come from `ca-2026-11-16-deck-media/deck-build/speaking_script.json`.

33 minutes of talk, then 12 minutes of questions. Order since 16 November: the title, the live demo, Bao's slides (up to 14), then Kerk's (15 to 23).

## 01 · VisuAlgo+

*Bao · Introduction · 00:00–00:30*

**Message:** We are rebuilding VisuAlgo, and we keep what it is for: learning and exploring algorithms.

- We are Bao and Kerk; the project is VisuAlgo+
- Rebuild the platform, keep its purpose
- Plan: the demo first; then why and how (Bao); then the design process, the engine and the website (Kerk)

## 02 · Live demo

*Bao · Demo · 00:30–05:20*

**Message:** A tour of the product: familiar home page, one editor for many algorithms, and a run that explains itself in three places.

- Home page: the same structure as the original VisuAlgo, one card per topic
- New: the Graph Editor and the Tree Editor; many algorithms share one input (eleven graph algorithms, with search)
- Every page: Action, e-Lecture, Pseudocode and Status around the canvas; this layout is V10
- Drawing a graph: drag a vertex, add a node, draw an edge, type its weight
- Planned for the editors: text, free drawing and vertex colours; for lecturers and tutors who teach, and students who draft competitive programming problems; these frequent users, who like to customise, are who the editors are for
- Running Dijkstra: the pseudocode line, the Status sentence and a note on the canvas change together; hover shows a shortest path
- Tree Editor: LCA with Binary Lifting is a topic I added; the root can be moved

**Cues**

- Bao's outline of 16 November; every step and value was run on app 346e84b that day. It takes a little under five minutes.
- Before the talk: open the app on the home page. In both editors choose Settings → Reset panel layout and check that 'Animate paused steps' is on. Browser zoom 100%, window maximised.
- 0:00 Home page. Scroll down a little to show the topic cards, then back up to Editors.
- 0:25 Click the Graph Editor card. It opens on Breadth-First Search with a graph of six vertices, A to F.
- 0:35 Click Algorithms ▾: 11 algorithms in 5 groups. Type dij in 'Search algorithms' (it shows 1 of 11), then click Dijkstra.
- 1:00 Point at Action. Click the E-LECTURE tab ('Dijkstra: tentative distances', slide 1 of 3), then ACTION again. Point at Pseudocode, Status and the canvas.
- 1:35 Drag vertex E a little. Click Add node, at the bottom of Action: a vertex N1 appears.
- 1:50 Drag from the dot on the edge of F to N1: a new edge. The Edges text gains the line 'F N1', and a notice says it counts as 1. Click in the Edges box, press Ctrl+End and type a space and 3: the label 3 appears. The graph now has 7 nodes and 9 edges.
- 2:10 Stop clicking while you talk about the planned tools and who the editors are for. They are plans: say "we plan to add".
- 2:40 Click Next six times, to frame 6 of 35. The note '0 + 4 = 4' is beside B, pseudocode line 6 is lit, and Status says 'Relax A → B: 0 + 4 = 4, so the distance to B becomes 4.'
- 3:05 Click Autoplay: about 15 seconds to frame 35 of 35, 'Dijkstra complete. Settled 7 nodes.'
- 3:25 Hover N1: A → C → D → F → N1 · distance 8. Hover E: A → B → E · distance 7.
- 3:45 Click HOME, then the Tree Editor card. It opens on Binary Lifting, Query, with a seven-node tree rooted at 8.
- 4:00 Under Edit tree → Structure, set Root to 12. The ROOT badge moves to 12, the tree is drawn again, and Depth goes from 2 to 3.
- If you are ahead: click Autoplay. The query ends on LCA(6, 2) = 4 after 6 frames.
- Then return to PowerPoint and press → for slide 3, Motivation.
- If drawing the edge fails, type the line 'F N1 3' in the Edges box. If anything else fails, do not debug: say what it would show and move on. Slides 9 to 13 show the same features as clips.

**Next:** Now let me step back. Why did we rebuild VisuAlgo?

## 03 · Motivation

*Bao · Introduction · 05:20–06:25*

**Message:** We keep VisuAlgo's strengths, and we follow Prof. Halim's directions: better interaction and a wider range of algorithms.

- VisuAlgo already has custom input and step-by-step runs; we keep them
- Prof. Halim's directions: easier graph editing, clearer parallel and curved edges, richer canvas interaction, side-by-side sorting
- He also encouraged a wider range of algorithms; LCA and Trie are topics I added
- My own focus, from competitive programming and teaching: explain why a step happens

**Next:** So why not just add these features to the existing site?

## 04 · Why rebuild the foundation?

*Bao · Introduction · 06:25–07:30*

**Message:** In the original code, one common change touches several topics, so we reorganised the foundation.

- The platform grew over many years; some parts are shared, such as the graph widget
- But each topic has its own input handling and state building
- So one editing change means changes and checks in several topics
- Sorting comparison: each pane needs its own state, with shared controls
- Decision: reorganise the foundation, and keep tools that fit, such as D3

**Next:** With that reason in mind, here is what we aim to deliver.

## 05 · Objectives and current scope

*Bao · Introduction · 07:30–08:40*

**Message:** We have three objectives and a working prototype; connecting the engine and a first release come next.

- Three objectives, one per card: a reusable visualization and interaction layer; a renewed website and execution foundation; a working prototype to validate
- Now: Graph, Tree and Sorting share one shell; students tried the prototype in Week 10
- Boundary: the visualizers run TypeScript in the browser; Kerk's C++ and WebAssembly engine is separate; connecting them is Semester 2 work
- Target: a first public release around March 2027; the original VisuAlgo stays online

**Next:** Let me go back to where it started: the early prototypes.

## 06 · Early visualizer prototypes

*Bao · Early Design · 08:40–10:10*

**Message:** Each early prototype tested one requirement that the final design had to meet.

- The prototypes were experiments toward the goals we discussed with Prof. Halim
- Graph: first separate edit and run views, then one canvas; input, positions and playback are separate, so moving a vertex keeps the same step
- Tree: new topics (LCA with Binary Lifting, Trie); an ancestor table under the tree; preview before Apply
- Sorting: the same array in every pane; each pane has its own state; one playback bar
- Naming: the standalone Graph rewrite is not the layout called V2

**Next:** While I was building the Graph rewrite and the Tree prototype, Kerk was designing the look of the new site.

## 07 · Two parallel foundations

*Bao · Early Design · 10:10–11:20*

**Message:** Two foundations grew side by side: my working visualizers and Kerk's design system.

- From late August, Kerk and I worked in parallel
- Mine: working algorithms, editors and playback, but separate apps with their own controls
- Kerk's: a design system from restyling visualgo.net (nine themes, twenty-six components) and a UI kit; also the first version of his engine
- Three requirements carried forward: keep the drawing available; keep playback familiar; show topic information beside the drawing

**Next:** Kerk will explain the design process later. First, here is my part of the work.

## 08 · Visualization contributions

*Bao · Algorithm Visualizers · 11:20–12:10*

**Message:** I built the visualizer foundations, the algorithms, the shell and the step explanations; I will show a few decisions you can see on screen.

- Foundations for Graph, Tree and Sorting
- Algorithms: each needs its own steps, pseudocode and inspector, for example LCA with Binary Lifting, and Trie
- The V10 shell and the integration into the site
- How each step explains itself, and how the behaviour is tested (snapshot of 1 November: 3,273 unit tests, 151 browser cases)
- Next: a few selected decisions

**Next:** The first one is the shell.

## 09 · A shared shell with clear constraints

*Bao · Algorithm Visualizers · 12:10–13:20*

**Message:** You can move panels around without losing the drawing or the run.

- The layout has state: moving a panel must keep the canvas and the panel's input
- One model keeps the groups (left, right, bottom) and enforces size limits
- One resolver computes both the real layout and the drop preview, so the preview matches the result
- Saved layouts are versioned and checked; a broken one is repaired or reset
- Trade-off: less freedom than a fully general split layout, for a stable drawing and predictable drops

**Cues**

- Press → after the first two sentences. The clip is 16 seconds and plays once.
- Name each move as it lands: the split (4 s), the left group (9 s), under the drawing (14 s).
- The footer counter stays at 12 of 21. It is small on Zoom, so say the number.

**Next:** The same care for the run applies when the user edits the graph.

## 10 · Input, layout and playback

*Bao · Algorithm Visualizers · 13:20–14:20*

**Message:** Moving a vertex changes the drawing; changing a weight changes the problem. So they are stored separately.

- Four things stored separately: the graph document, the layout, the playback session, the presentation
- Drag a vertex: only the layout changes, so the run continues
- Change a weight: the document changes, so the old run is no longer valid
- A parallel edge is a separate edge, with its own identity and weight
- Result: consistent interaction, because each piece of state has one owner

**Cues**

- Press →. The clip is 16 seconds.
- Say each action as it happens: drag B (2 s), weight 1 to 5 and NO RUN (5 s), the second edge (8 s), its weight 2 (11 s).
- End on the final frame: two B → A edges, labelled 5 and 2.

**Next:** That was one run. Sorting comparison needs several runs side by side.

## 11 · Sorting comparison

*Bao · Algorithm Visualizers · 14:20–15:20*

**Message:** The panes share one input and one clock, but each keeps its own state; the counters are operations, not runtime.

- Every pane gets the same input and keeps its own state
- One shared clock moves all panes, one logical operation at a time; they can finish at different times
- Operations come from generators; history is kept for stepping back, which costs memory on long runs
- The counters count operations in the visualization, not CPU time

**Cues**

- Press →. The clip is 10 seconds.
- Say 'both at 48' when the panes pause.
- Last is a jump to the end, not a speed result.

**Next:** The next two slides are about a different question: how one step explains itself.

## 12 · LCA: explaining a decision to stay

*Bao · Algorithm Visualizers · 15:20–17:05*

**Message:** Floating text puts the reason beside the node, so a step with no movement still explains itself.

- Binary Lifting is a topic I added; a query has several stages and reads an ancestor table
- Clip: the root moves from 10 to 16, then LCA(8, 20): 8 lifts to 4; both stay at ancestor 16; both lift at k = 0; the answer is 16
- During the query no node moves, and 5 of the 12 steps only decide to stay
- With floating text the reason sits beside the node; Status keeps the full sentence
- Why: as I remember the Week 10 trial, newer learners often had to read Status; the benefit is not measured yet

**Cues**

- Press → after the first two sentences. The clip is 28 seconds; keep pace with it.
- Clip: the root moves to 16 (3 s), the query starts (5 s), 8 lifts to 4 (10 s), both stay at 16 (14 to 20 s), both lift (20 s), the answer 16 (25 s).
- After the clip, point at the three note crops on the left.
- Say clearly that the benefit is not measured yet.
- If you are late, skip the last sentence, on advanced tree topics.

**Next:** LCA shows a note when a step arrives. The next slide adds two more tools: motion while paused, and hover on the result.

## 13 · Pause and inspect the result

*Bao · Algorithm Visualizers · 17:05–18:25*

**Message:** Emphasis and progress are separate: motion while paused, a note when a step arrives, and hover on the result never advance or rerun the algorithm.

- Dijkstra from vertex 0 on visualgo.net's nine-vertex 'Big' example
- Paused at frame 17: the light on edge 2 to 3 keeps moving, the counter does not (Kerk's suggestion, my implementation)
- Next: a note beside 3 says 12 + 14 < 33, so update; 33 becomes 26
- Final frame: hover 8 gives 0, 2, 3, 8 with distance 42; hover 4 gives distance 46; read from the stored result
- The motion can be turned off and respects the reduced-motion setting

**Cues**

- Press →. The clip is only 14 seconds: paused at 17 (0 s), Next (3 s), Last (6 s), hover 8 (8 s), hover 4 (11 s).
- During the clip, only name the steps. Explain after it stops.
- The paused motion is subtle on Zoom: say 'still 17' and point at the edge from 2 to 3.

**Next:** The editors bring these features together.

## 14 · Graph/Tree Editors

*Bao · Algorithm Visualizers · 18:25–19:10*

**Message:** The editors are for frequent users who start from their own example; that is an intended use, not a measured one.

- You saw both editors in the demo
- For frequent users: lecturers and tutors who teach, and students who practise competitive programming
- They start from their own example: a small test, an observation, a counterexample
- The original VisuAlgo already accepts custom input; ours is a more explicit entry point
- An intended use; adoption is not measured

**Next:** That is my part. Kerk will now explain how we designed the layout, and then the engine and the website.

## 15 · Wireframing

*Kerk · UI/UX Evolution · 19:10–20:20*

**Message:** From nine wireframes and a student survey, we chose two layouts to build: V2 and V7.

- Low-fidelity wireframes of the visualisation page, with an AVL tree as the example
- Nine versions: seven layouts and two drag states of V7
- Layout survey: 61 respondents, mostly past and present CS2040S and CS3230 students
- Bao and I chose V2 (split rails) and V7 (draggable docks); Bao built Graph, Tree and Sorting in both

**Next:** So what did the two builds show?

## 16 · Prototyping

*Kerk · UI/UX Evolution · 20:20–21:25*

**Message:** V10 keeps the strengths of both: visible stacked panels from V2 and draggable tabs from V7, around a canvas that is never covered.

- Trade-off: V2 has fixed places with several panels open; V7 has movable panels but one tab per dock
- Bao and I discussed it, with Prof. Halim's feedback; we arrived at V10 in Week 9
- V10: panels stacked and visible together, tabs dragged between areas, the canvas in the centre
- Bao built the panel-group model and the shell
- Kerk implemented the agreed refinements and, on 18 October, merged the site and the visualizers into one application

**Next:** Then we put V10 in front of students.

## 17 · Prototyping

*Kerk · UI/UX Evolution · 21:25–22:00*

**Message:** Eight students tried V10 in Week 10, in a formative trial.

- 8 prototype testers, mostly current CS2040S and CS3230 students
- Each used V10 on their own for 15 to 20 minutes
- Sessions recorded; then a short post-use test and feedback
- Formative: it shows what to fix, not how much students learn

**Next:** Here is what they told us.

## 18 · Prototyping

*Kerk · UI/UX Evolution · 22:00–23:10*

**Message:** The trial supported the layout, showed that onboarding is weak, and left one open question: reading versus inference.

- Plus: the layout worked for the testers
- Minus: onboarding. Overwhelming at first glance (4 of 8); e-Lecture not helpful enough (3); less common features hard to discover (3); hard to navigate between pages (3)
- Open question: should a learner read the explanation, or infer it from the animation?
- Eight testers give signals, not statistics

**Next:** Now the system behind the page.

## 19 · Architecture

*Kerk · Engine & Website · 23:10–25:10*

**Message:** The architecture has a browser side and a server side; say clearly which parts the demo already uses.

- Browser: the frontend (React, design tokens, panels and e-Lectures) starts a Run
- Algorithm engine: C++ compiled to WebAssembly; it records the History
- Render engine: d3 into SVG; it draws any History
- CDN: static files, the frontend bundle and the wasm binary
- Server: a Go API over REST, with Postgres, Redis and an email provider
- Boundary: the demo ran TypeScript algorithms in the browser; this engine is not connected to those visualizers yet

**Next:** Let me now describe that engine.

## 20 · Architecture

*Kerk · Engine & Website · same picture as slide 19*

**Message:** This slide shows the same picture as slide 19.

- In file (8), slides 19 and 20 are identical
- Kerk: delete one of them, or replace this picture with the second one you meant to show

## 21 · Engine foundation

*Kerk · Engine & Website · 25:10–27:40*

**Message:** The engine runs algorithms in a worker; the plan is that it describes their state and the visualizer explains it to the learner.

- C++ algorithms compiled to WebAssembly, running inside a worker
- The page and the engine talk through protocol messages, not direct calls
- Protobuf messages with graph and array representations; a Python path through Pyodide for tracing sorting algorithms
- Design question: expose enough state without tying the engine to the page layout
- Plan: the engine describes state and changes; the visualizer decides the note and the pseudocode line

**Next:** The harder part is connecting the engine to the visualizers.

## 22 · Reversible execution and integration

*Kerk · Engine & Website · 27:40–29:40*

**Message:** The engine and the visualizers keep history differently, so connecting them needs an explicit translation, one Graph algorithm first.

- Engine: a reversible journal, one record per step, and it can move backward
- Visualizers: Graph and Tree build all steps when a run starts; Sorting pulls from generators and keeps history
- Three things must stay consistent: node and edge identity, run identity, and the meaning of a step
- Bao's earlier integration experiment stays separate from the delivered visualizers
- Next step: one complete Graph integration, checked against the TypeScript behaviour

**Next:** Finally, the website that hosts all of this.

## 23 · Website integration

*Kerk · Engine & Website, then Future Work · 29:40–33:00*

**Message:** The site hosts the visualizers without duplicating their controls; then, with no slide of its own, the plan for Semester 2.

- The site owns the top bar and the theme; each visualizer supplies its topic-specific parts
- Bao built the working catalogue, the routes and the host adapters on the design system
- Kerk's consolidation and refinements made it a single application
- The wider website infrastructure and the engine still have to join the visualization layer
- Clear responsibilities avoid a second set of playback controls and conflicting theme state
- Future work, said over this slide: one Graph algorithm through the engine end to end; a first public release around March 2027 (a target); stabilise and evaluate; advanced tree topics are possibilities, not commitments

**Next:** That is the end of our talk.

## 24 · Questions

*Both · Q&A · after 33:00*

**Message:** Thank the audience and open the floor.

- Thank you
- Questions on the design decisions, the implementation or the evaluation plan
- The backup slides are in the second file

## B1 · Backup: recursive DFS recap (demo fallback)

*Backup*

**Message:** A spare clip: the recursive DFS recap on the final frame.

- The same S, A, B, T graph as the clips on slides 9 and 10
- The final frame replays the DFS tree in visit order: S, A, T, then S, B
- Different from Dijkstra's final frame, where you hover a vertex to see its path

**Cues**

- A spare clip of the Graph Editor: use it if a question is about traversal, or if the Graph Editor could not be shown live.
- Press → to play. The clip is 8.5 seconds.

## B2 · Backup: preview before Apply

*Backup*

**Message:** An operation that changes the tree runs as a preview first; only Apply commits it.

- A changing operation needs a different contract from a read-only query such as LCA
- BST Insert 5 runs as a preview: the search path and the new node are visible, and I can step backward
- The tree and its text do not change until Apply
- Apply commits the result: the text gains the edge 6 5 and the run ends
- Heap insertion follows the same contract

**Cues**

- Explain the preview first, on the poster. Then press →: the clip is 8.6 seconds: two steps back, forward again, then Apply.

## B3 · Backup: correctness and limitations

*Backup*

**Message:** We check results with an independent method, and we are open about the limits.

- Cut vertices and bridges: an independent check removes each candidate and counts the components again
- Exact edge identity matters: removing one of two parallel edges keeps the connection
- Limits: sorting history is not bounded; Graph and Tree build all their steps up front
- Passing tests do not prove full correctness, performance or learning benefit
- AI tools assisted under my requirements; the design choices, acceptance and validation are mine

## B4 · Backup: evidence and ownership

*Backup*

**Message:** The main evidence is in the public repository, and each slide's notes link to its sources.

- Repository: BJoozz/docsforfyp
- The CA report and the architecture records
- The contribution map and the prototype history
- The Week 10 trial addendum
- Each slide's notes link to its sources and media

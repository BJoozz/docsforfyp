# CA Presentation — Part 1: Brainstorming and Draft

Last updated: **15 November 2026**.

Working record of the **Problem, Motivation & Objectives** preparation: project-owner input, code evidence, proposed slide wording, and the latest complete English script.

**Status:** brainstormed and drafted; the script and slide wording remain proposals for team review. This document records the presentation content discussed in chat, rather than claiming that a deck or the remaining presentation sections are complete.

## 1. Core narrative

**Working message:**

VisuAlgo+ preserves VisuAlgo's interactive educational purpose while rebuilding the foundation so that improvements to the website, visualization and execution engine can be developed more consistently and extended more easily.

Connect the story in this order:

1. What VisuAlgo enables for learners.
2. Concrete improvements discussed with Prof Halim.
3. Engineering constraints that make those improvements difficult to apply consistently.
4. The rebuild objectives.
5. The current prototype and intended release direction.

Use **graph editing** and **side-by-side sorting comparison** as the opening examples. They connect user needs to engineering work without requiring a detailed architecture explanation.

## 2. Brainstorming record

The following records the project owner's answers on 15 November 2026. These are project context and intentions supplied during brainstorming, not independently verified deployment or completion claims.

### Q1. What future improvements has Prof Halim discussed?

- Prof Halim has many ideas for developing and updating VisuAlgo.
- He has substantial influence on the direction of improvements.
- Weekly supervisor discussions help guide progress and design decisions.
- Concrete examples:
  - Change the execution foundation and supporting tools to make graph editing more convenient.
  - Support smoother and richer interaction with the canvas.
  - Improve graph details, including **parallel edges and curved edges**.
  - Provide **multiple sorting panes** so students can compare the behaviour of different algorithms.
- Presentation framing: the supervisor provides direction and participates in design discussions; the project team investigates alternatives, implements solutions and evaluates the decisions.

### Q2. Why is extending the original implementation difficult?

Project owner's account:

- Many algorithms have different implementations and algorithm-specific specialisations.
- Contributions have accumulated from different students over time.
- Some common behaviours and formats are difficult to update and unify across modules.
- Parts of the existing tooling and implementation structure no longer fit the intended changes well.

The repository inspection below supports a more precise formulation:

> Shared components already exist, but substantial logic remains specific to individual modules. A common improvement can therefore require coordinated changes and checking across several topics.

Do not treat the existence of algorithm-specific behaviour as inherently bad: different algorithms legitimately need different representations. The engineering goal is to share suitable infrastructure while preserving those differences.

### Q3. What is the current state and intended release?

Project owner confirmed:

- A working experimental version has already been made available for students to try.
- It is **not yet a complete website with the engine and web infrastructure fully integrated/completed**.
- The team intends to release VisuAlgo+ **around March 2027, as early as feasible**.
- The original VisuAlgo is intended to remain available.
- Under the current transition plan, the original site would link users to topics/algorithms completed in VisuAlgo+.
- The project owner is optimistic that the team can cover **all algorithms available in the original VisuAlgo**, given the current development pace.
- The project owner identifies AI coding tools as a contributor to faster implementation.

Distinguish these three states in the presentation:

| State | How to describe it |
|---|---|
| Current achievement | A functioning prototype that students have tried |
| Release target | Initial public release around March 2027, with integration and validation still required |
| Broader ambition | Cover all algorithms available in the original platform |

This file does not claim full algorithm coverage, completed engine integration, or a production-ready release.

## 3. Repository evidence for “Why rebuild?”

Inspected sources:

- Original implementation: [BJoozz/visualgo](https://github.com/BJoozz/visualgo).
- Source revision pinned for these links: `bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58` (main inspected on 15 November 2026).
- Report background: [Introduction, objectives and related work](../report/main.tex).

These are observations from selected graph and sorting files, not a complete audit of every module.

| Observation | Code evidence | Plain-language implication |
|---|---|---|
| SSSP, MST and DFS/BFS each contain their own graph import/normalisation, drawing workflow and visualization-state construction. | [SSSP: fixJSON and import](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/resources/views/viz/sssp.blade.php#L137), [MST: fixJSON](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/resources/views/viz/mst.blade.php#L68), [DFS/BFS: fixJSON](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/resources/views/viz/dfsbfs.blade.php#L120); their respective createState functions are at lines 1240, 482 and 2056. | A common editing improvement may require changes and checks in several modules. The implication is an engineering inference from the structure, not a measured maintenance-cost result. |
| Sorting keeps its own state lists and playback position, and accesses fixed page elements such as #viz-main and #status. Playback also updates #progress-bar. | [Sorting state and rendering](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/resources/views/viz/sorting.blade.php#L475), [playback and progress bar](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/resources/views/viz/sorting.blade.php#L2016). | Multiple independent sorting panes require changes to state ownership, rendering targets and coordinated controls, beyond dividing the screen. |
| Edge rendering contains custom curve generation and geometry calculations. | [GraphEdgeWidget: curve generators](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/public/js/graph_library/GraphEdgeWidget.js#L41), [curve geometry](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/public/js/graph_library/GraphEdgeWidget.js#L450). | Improving edge interaction or representation involves underlying geometry and rendering behaviour, not only visual styling. |
| A reusable GraphWidget and graph-state format already exist. | [GraphWidget: state format and animation](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/public/js/graph_library/GraphWidget.js#L367); graph modules instantiate GraphWidget. | Say “substantial module-specific logic remains”; do not claim the old platform has no shared infrastructure. |
| Curved-edge support already exists in the inspected graph library. | [GraphEdgeWidget: curve height](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/public/js/graph_library/GraphEdgeWidget.js#L17), [GraphWidget: curve-height updates](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/public/js/graph_library/GraphWidget.js#L824). | Describe the objective as improving curved/parallel-edge handling and interaction. Do not claim curved edges are wholly absent from the original implementation. |
| The repository declares an existing Laravel/PHP and JavaScript toolchain, including Laravel ^8.40 and Vue ^2.6.12; inspected visualization code uses D3 and jQuery directly. | [composer.json](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/composer.json), [package.json](https://github.com/BJoozz/visualgo/blob/bd1756cd1d7bd4c3a2cdb6aaba62ed14238d9a58/package.json), sorting and graph source above. | Name the specific structure and requirements that motivate change. A technology's age or name alone does not prove that a rebuild is necessary. |

### Wording boundaries

- Avoid: “Every algorithm is completely separate.”
- Prefer: “Shared components exist, but substantial logic remains specific to individual modules.”
- Avoid: “The original VisuAlgo cannot be improved.”
- Prefer: “A rebuild gives us the opportunity to reorganise shared infrastructure for broader changes.”
- Avoid: “Curved edges are a completely new feature.”
- Prefer: “We aim to improve the representation and interaction of parallel and curved edges.”
- Avoid calling D3 or PHP inherently unsuitable. The CA report explicitly retains D3 for selected layout/animation tasks.
- Do not suggest that current visualizers already use the new WASM engine. The report records browser TypeScript implementations and a separate engine foundation; the latest project clarification still identifies integration/infrastructure work as incomplete.
- A working visualization and positive formative feedback do not by themselves establish measured learning improvement.

## 4. Proposed slide content

**Status: assistant-proposed wording; working draft.**

| Slide | English content |
|---|---|
| **1. VisuAlgo+: Motivation** | Preserve interactive learning of data structures and algorithms. • Support future improvements discussed with Prof Halim. • Enable easier graph editing, smoother canvas interaction, and side-by-side sorting comparison. |
| **2. Why Rebuild the Foundation?** | Substantial module-specific logic makes consistent changes harder. • Existing rendering and playback structures require reworking for new interactions. • Establish reusable components and clearer boundaries between algorithms, visualization, and website infrastructure. |
| **3. Objectives and Release Direction** | Rebuild the website and execution foundation. • Improve visualization and interaction across topics. • Validate functionality and refine the experience through user feedback. • Target an initial public release around March 2027, with a gradual transition from VisuAlgo. |

Opening time target: approximately **3–4 minutes**, to be checked in rehearsal.

Keep the release explanation brief here; reserve detailed milestones and risks for the final roadmap section.

Possible existing visuals:

- [Graph prototype screenshot](../report/figures/F2-dfsbfs-bfs-frame8.png).
- [Four-pane sorting comparison](../report/figures/F7-sorting-compare-4-panes.png).
- [Dijkstra floating-text example](../report/figures/F4-sssp-dijkstra-frame24-note.png) — optional for the later technical explanation of meaningful steps; graph editing and sorting comparison are the latest proposed opening examples.

## 5. Latest complete English script

**Status: working draft from the conversation; not yet rehearsed or confirmed by both presenters.**

VisuAlgo is an interactive platform for learning data structures and algorithms. It allows students to explore their own inputs and follow an algorithm step by step. With VisuAlgo+, we want to preserve that educational purpose while building a foundation that is easier to extend.

Prof Halim has many ideas for developing the platform further. We meet with him every week to discuss these ideas, review our progress, and consider design decisions. Examples include making graphs easier to edit, improving interaction with the canvas, handling parallel and curved edges more clearly, and allowing students to compare sorting algorithms side by side on the same input.

These improvements also raise broader engineering challenges. VisuAlgo has developed over many years through contributions from successive groups of students. Although it has shared components, substantial logic remains specific to individual modules. As a result, a common improvement may require changes in several places and careful checking across different topics.

For example, several graph modules have their own logic for importing a graph and preparing its visualization states. Similarly, supporting multiple sorting panels requires separate execution states and coordinated playback controls. These changes affect how the application is organised, as well as what users see.

Our project therefore has three main objectives.

First, we aim to rebuild the website and algorithm execution foundation using suitable, widely adopted technologies, with clearer boundaries between the main components.

Second, we aim to improve the learning experience through more convenient input editing, consistent interactions across topics, and clearer explanations of algorithm behaviour.

Third, we aim to validate the functionality and use student feedback to guide further improvements.

We already have a working prototype that students have tried. However, the engine integration and website infrastructure are still being completed.

We are targeting an initial public release around March 2027. Our current plan is to keep the original VisuAlgo available and link users to completed topics in VisuAlgo+. Our broader goal is to cover all algorithms currently available in the original platform, with the release scope guided by integration progress and validation.

We will now explain our approach and the main technical contributions behind the current prototype.

## 6. Release and AI discussion

The project owner's confidence about complete coverage should remain in the planning record. The assistant's wording recommendation is to present this as:

> We aim to cover all algorithms currently available in the original VisuAlgo.

This is a wording recommendation, not a decision to reduce project scope. The final release commitment and acceptance criteria still need to be agreed by the team.

AI tools may be discussed in the development-process section or Q&A. If included:

- Explain which tasks they actually accelerate.
- Explain how the team reviews, tests and validates the resulting work.
- Distinguish implementation speed from algorithm correctness, visualization correctness, integration readiness and release readiness.
- Do not claim a specific AI verification workflow has already been used unless it is supported by the team's actual practice.

The latest opening script does not include an AI claim.


## 7. Continue from here

Completed:

- [x] Record answers to the three brainstorming questions.
- [x] Connect concrete improvement examples to the motivation for rebuilding.
- [x] Inspect selected original graph and sorting implementations.
- [x] Correct overly broad claims about shared infrastructure and curved edges.
- [x] Draft three opening slides and a complete English script.
- [x] Distinguish current achievement, release target and broader coverage ambition.

Next:

- [ ] Review the opening wording together and choose the speaker.
- [ ] Select screenshots and rehearse the 3–4 minute opening.
- [ ] Prepare the technical contribution stories using: Problem → Alternatives → Design decision → Implementation → Result.
- [ ] Explain current architecture and planned engine integration separately.
- [ ] Prepare evaluation evidence, a stable demo, release milestones and Q&A.

## 8. References and change log

Project references:

- [CA report](../report/VisuAlgo_CA_Report.pdf).
- [Report source](../report/main.tex).
- [Week 10 user-trial addendum](../report/week10_user_trial_addendum.md).
- [Contribution evidence](../02_contribution_evidence.md).
- [Architecture and decisions](../03_architecture_and_decisions.md).

**15 November 2026:** Created this focused note to preserve the Part 1 brainstorming, repository evidence, latest slide proposal and complete English draft from the conversation.


## Technical-case continuation — 15 November 2026

[Graph editing and reproducible playback](CA_PRESENTATION_GRAPH_CASE.md) now contains the first technical case: slide wording, a 2–3 minute English script, proposed demo, Q&A, source references and a commit-based timing fix. Code and existing tests were inspected; the demo has not yet been rehearsed and tests were not rerun during this preparation.


## Broader technical review — 15 November 2026

The initial three-case shortlist was too narrow to represent the full contribution. See [Technical contribution map](CA_PRESENTATION_CONTRIBUTION_MAP.md) for nine presentation groups mapped to C1–C14, current-source checks, post-report commits and a revised breadth-first outline. V10 shell, site integration, Tree operations and algorithm validation need explicit visibility. The graph case remains a detailed draft, not the sole or necessarily first main technical story. Next prepare the contribution overview and V10 case before committing to the final case selection.


## Interactive demonstration and editor audience — 15 November 2026

The owner explicitly wants to demonstrate floating text, paused visual emphasis, final-frame interactions and the dedicated Graph/Tree Editor entry points. See [Interactive demo and editor positioning](CA_PRESENTATION_INTERACTIVE_DEMO.md) for the proposed sequence and English script. The editors aim to support experienced CP users constructing examples and thinking through problems; this is a design goal, not a measured adoption or learning result. Dijkstra final-frame hover paths and DFS final traversal recap are distinguished in the plan. Include this within the shared demo allocation, not as additional unbudgeted time.

## Selected visual evidence — 16 November 2026

A small [ready-to-use presentation pack](../presentation/ca-2026-11-16/README.md) is now available: 6 main screenshots, 2 backup screenshots and exactly 2 short MP4s (7.8s and about 10.4s), with no GIFs. Open the [visual chooser](../presentation/ca-2026-11-16/START_HERE.html) locally to browse them. The [claim-to-evidence selection note](CA_PRESENTATION_ASSET_PLAN.md) ties them to the existing outline; [captions and short speaking cues](../presentation/ca-2026-11-16/CAPTIONS_AND_CUES.md) are in simple English.

The pack uses one four-vertex Dijkstra graph, BST Insert(5), Bubble/Selection on twelve values, the editor entry points and a rearranged V10 layout. Captures were made against app `346e84b`, on 15–16 November, after pulling this documentation repo to `99990d0`. Inputs, settings, actions, source revision and fresh workflow checks are recorded in the pack. The checked subset includes paused motion with a fixed frame, a local decision note, final hover paths, preview versus Apply and a panel move preserving the run. Both exported MP4s were decoded and played locally.

This verifies the selected captures, not the entire proposed demo or a timed Zoom rehearsal. No application source was changed and the complete project test suite was not rerun. The wider contribution map, historical evidence, attribution and evaluation limits still apply. Choose where each asset belongs during rehearsal rather than repeating the same feature in both the technical section and the shared demo.

## CA deck with embedded media — 16 November 2026

The presentation deck is [`presentation/VisuAlgo_CA_Presentation.pptx`](../presentation/VisuAlgo_CA_Presentation.pptx). It has 27 slides (22 timed, 1 Q&A and 4 backup) and was built from the GPT draft, which is kept unchanged in `presentation/drafts/`.

Slides 14–18 embed five real-app clips of app `346e84b`:
- the V10 panel split, move and dock;
- a vertex drag, a weight edit and a parallel edge added;
- LCA(6, 10), keep then lift;
- Codex’s sorting clip;
- Dijkstra on a nine-vertex graph: paused motion, its note and the final hover.

Backups 24 and 27 add the BST preview/Apply clip and a recursive DFS recap for the live demo. Slide 5 shows the standalone prototypes, rebuilt at their documented commits. Each clip has its poster as a static fallback, and on 16 November PowerPoint decoded a frame from each embedded clip.

See the [media map](../presentation/CA_PRESENTATION_MEDIA_USAGE.md), the [changelog](../presentation/CA_DECK_CHANGELOG.md), the updated [master script](../presentation/VisuAlgo_CA_Master_Script.md) and the [preflight](../presentation/VisuAlgo_CA_Preflight.md).

Still open:
- Kerk’s confirmation of slides 7–12;
- one slideshow click-through on the presenting computer;
- a timed joint rehearsal.

## Algorithm coverage context — 16 November 2026

Bao added that, in early discussions, Prof. Halim also encouraged widening the range of algorithms VisuAlgo+ supports, alongside interaction, visualization and architecture. This is Bao's account; there is no written record, and no specific topic is attributed to Prof. Halim.

The deck now reflects it on slides 2, 4, 5, 13, 16 and 22: LCA with Binary Lifting and Trie as added topics (built in the standalone Tree prototype in September 2026 and present in the current app), and Heavy-Light Decomposition and Centroid Decomposition only as possible later extensions. The checks behind each statement are in the [changelog](../presentation/CA_DECK_CHANGELOG.md).

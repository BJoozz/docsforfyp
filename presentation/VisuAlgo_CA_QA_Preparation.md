# VisuAlgo+ CA — Q&A Preparation (Bao & Kerk)

**Date:** 16 November 2026  
**Purpose:** Joint FYP CA presentation, 45 minutes total (33-minute talk/demo + ~12-minute Q&A).  
**Format:** 25 core questions + 6 harder follow-ups; clear English answers with short memory cues.  
**Study method:** Do **not** memorize entire paragraphs. Recall 3–4 ideas, answer directly, explain **why/how**, then give one concrete example. Most core answers target ~20–40 seconds; expand only when asked.

> Evidence baseline: [Presentation Master Script](VisuAlgo_CA_Master_Script.md), [Contribution Map](../docs/CA_PRESENTATION_CONTRIBUTION_MAP.md), [Graph Case](../docs/CA_PRESENTATION_GRAPH_CASE.md), [Prototype Review](../docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md), [Week 10 Trial](../report/week10_user_trial_addendum.md). These are evidence-based rehearsal answers, not guaranteed official answers or newly executed tests. Verify Kerk-specific engine and website details with Kerk.

## A. Project motivation & understanding — mainly Bao

### Q1. Why do you need to rebuild VisuAlgo instead of simply extending the existing platform?

**Remember:** Original strengths → module-specific logic/state → shared changes are difficult → reusable foundation.

**Answer:**
> The original VisuAlgo already works well for many learning activities. However, much of its logic is specific to individual modules, which makes common improvements harder to implement consistently. We want to build a more reusable foundation, especially for graph editing, playback, and sorting comparison, while preserving the strengths of the original platform.

**Follow-up — Why not just refactor the old code?**
> We could refactor it gradually, but some new features require changes across several layers. Rebuilding the foundation gives us clearer state ownership and integration boundaries. That does not mean the original implementation was completely wrong.

### Q2. What are the main objectives of VisuAlgo+?

**Remember:** Better interaction → reusable architecture → renewed execution foundation → validate.

**Answer:**
> Our main objectives are to improve user interaction, make visualization components more reusable, and modernize the website and execution architecture. We also want to validate the system through software testing and user feedback, so future improvements are based on evidence.

### Q3. What makes VisuAlgo+ different from the original VisuAlgo?

**Remember:** Not only appearance → interaction workflow → explanations/comparison/flexibility.

**Answer:**
> The main difference is not just the visual design. We are improving how users interact with algorithm visualizations. For example, they can edit and run algorithms on the same canvas, rearrange supporting panels, compare sorting algorithms, and inspect explanations directly near the relevant objects.

**Boundary:** Original VisuAlgo already allows custom input. Do not claim we invented that feature.

### Q4. Who are your target users?

**Remember:** Beginners → experienced students / CP users → lecturers.

**Answer:**
> We target both students and educators. Beginners can use the visualizations to understand algorithm behavior, while more experienced students can create examples, test observations and explore edge cases. Lecturers can also use the platform to demonstrate algorithms interactively.

**Boundary:** These are intended use cases, not measured adoption or learning effects.

### Q5. Why did you build standalone prototypes before working on the final interface?

**Remember:** Explore feasibility → discover requirements → common direction.

**Answer:**
> We wanted to explore visualization requirements before committing to a shared interface. Graph helped us understand editing and playback. Tree introduced structural operations and ancestor information. Sorting explored multiple independent runs with shared controls. These prototypes helped us identify what the final interface needed to support.

## B. Design decisions & architecture — Bao / Kerk

### Q6. Why did you choose V10 over V2 and V7?

**Remember:** V2 familiar split rails → V7 flexible docks → V10 combines strengths → central canvas.

**Answer:**
> V2 provided a more familiar layout, while V7 offered greater flexibility with movable panels. After exploring these designs and discussing the trade-offs, we chose V10 to combine useful properties from both. It keeps the main visualization visible while allowing users to rearrange surrounding information.

**Follow-up — Was V10 proven better through testing?**
> Not through a controlled comparison. Our decision came from the early survey, prototype exploration and design discussions. The Week 10 trial evaluated V10 after we had selected it.

### Q7. Why is V10 more than just a resizable layout?

**Remember:** Stateful model → valid moves/sizes → canvas preserved → saved-layout recovery.

**Answer:**
> V10 is not just a set of CSS panels. It has a shared layout model that controls how groups can move, split and resize. It also enforces size constraints and preserves visualization state when panels are rearranged. For example, moving Status should not reset the algorithm or recreate the canvas.

### Q8. What are the main trade-offs of your V10 layout?

**Remember:** Flexibility versus stability; constraints protect the drawing.

**Answer:**
> We could allow completely unrestricted panel layouts, but that would make it harder to guarantee enough space for the visualization and maintain predictable behavior. We chose a more constrained layout model with a persistent central canvas. This sacrifices some flexibility, but gives users a more stable workspace.

### Q9. Why separate graph input, layout, playback and presentation?

**Remember the four owners:**

| Owner | Responsibility |
|---|---|
| Graph document | Nodes, edges, weights, identities |
| Layout | Positions and pinning |
| Playback session | Run, sequence, selected step, session ID |
| Presentation | Highlights, badges, rendered explanation |

**Answer:**
> These states represent different responsibilities. The graph document stores the algorithm input. Layout stores positions. Playback manages execution steps, and presentation determines what is highlighted. Separating them prevents visual changes from accidentally changing the algorithm input. It also makes editing and playback easier to keep consistent.

### Q10. Why does moving a vertex preserve the run, but changing an edge weight resets it?

**Remember:** Geometry does not change the problem; semantic input does.

**Answer:**
> Moving a vertex changes only its visual position, so the algorithm result remains valid. However, changing an edge weight changes the actual input. The previous execution may no longer be correct. Therefore, we invalidate the old run and require a new execution.

**Follow-up — Why not automatically rerun?**
> That is possible, but our current design makes invalidation explicit. It avoids showing an old result as if it belonged to the updated graph.

## C. Bao's algorithm visualization contributions

### Q11. What exactly did you personally contribute?

**Remember:** Foundations → algorithms/playback → V10 shell/site → explanations/testing.

**Answer:**
> My main contribution is the algorithm visualization layer. I developed the initial Graph, Tree and Sorting visualizers, implemented and extended algorithms, and worked on their state management and playback. I also implemented the core V10 layout model, integrated the visualizers into the website, and developed features such as floating text and interactive final states. Kerk focused more on the design system, engine foundation and infrastructure, although many design decisions were collaborative.

**Boundary:** Avoid reducing ownership to “Bao frontend, Kerk backend.” Both roles cross architectural boundaries.

### Q12. What was the most challenging technical problem you solved?

**Remember:** One canvas → semantic versus visual edits → separate owners → consistent behavior.

**Answer:**
> One challenging problem was keeping graph editing and algorithm playback consistent on the same canvas. The difficulty is that some user actions change only the drawing, while others change the algorithm input. I solved this by separating the graph document, layout, playback session and presentation state. This allows users to rearrange a graph without losing the current step, while preventing outdated results after semantic edits.

**Alternative example if prompted:** V10 stateful panel constraints, LCA step explanations or Sorting Compare.

### Q13. Why are floating-text explanations useful?

**Remember:** Meaningful step with little movement → users look at Status → local explanation → impact unmeasured.

**Answer:**
> Some algorithm steps involve an important decision without much visible movement. During our user trial, I observed that less experienced users still relied heavily on the Status panel, especially for multi-stage algorithms. Floating text is my design response. It places a short explanation close to the relevant object, while Status keeps the full explanation. We hope this reduces attention switching, but we have not measured that benefit yet.

### Q14. Give a concrete example of why floating text is needed.

**Remember:** LCA(6, 2) → candidate ancestors both 8 → keep both nodes → explain why.

**Answer:**
> In our LCA example, we query nodes 6 and 2. At one step, both candidate ancestors are node 8. The algorithm decides not to move either node, so the tree barely changes. Without an explanation, the user may not understand why nothing happened. The floating note explains this decision directly on the canvas.

**Boundary:** This equal-depth example does **not** demonstrate a depth-balancing move.

### Q15. Why does animation continue when playback is paused?

**Remember:** Algorithm progress ≠ visual emphasis; counter fixed.

**Answer:**
> We separate algorithm progress from visual emphasis. When playback is paused, the selected algorithm step remains unchanged. However, a subtle animation can continue to highlight the current node or edge. This helps the user inspect the current relationship without advancing the computation.

**Follow-up — Isn't that confusing?**
> It could be, so the step counter remains fixed and the motion should be subtle. We also provide animation controls and consider reduced-motion preferences.

**Attribution:** Kerk suggested paused motion; Bao implemented it.

### Q16. How does Sorting Compare work?

**Remember:** Same data → independent streams → shared logical clock → separate history.

**Answer:**
> Each sorting pane receives the same input array, but runs its own algorithm independently. A shared clock advances each active pane by one logical operation. This allows users to compare intermediate states under common playback controls, including pausing and moving backward.

**Follow-up — Is this a fair speed benchmark?**
> No. The counters represent visualization operations, not CPU execution time. A fair runtime comparison would require separate benchmarks.

**Boundary:** Future operations are buffered; retained history still costs memory for long runs.

### Q17. How do Tree operations differ from Graph visualizations?

**Remember:** Some tree operations mutate data → preview transient states → Apply commits → stale context invalidates.

**Answer:**
> Some Tree operations modify the data structure, unlike a read-only traversal or LCA query. We need to show intermediate states without immediately changing the user's input. For example, during BST insertion, the learner can inspect the steps and move backward. The actual tree changes only when they select Apply.

## D. Engine, integration & system design — mainly Kerk

### Q18. Why use C++ and WebAssembly for the execution engine?

**Remember:** Execution/visual separation → browser execution → extensible boundary.

**Answer:**
> The engine is designed to separate algorithm execution from visualization. C++ compiled to WebAssembly provides a way to run algorithm implementations in the browser, while the frontend handles interaction and presentation. This separation is intended to make the system easier to extend and maintain.

**Follow-up — Is WASM faster than TypeScript?**
> We haven't established that through a fair benchmark. Performance is not the only reason for the architecture. The separation of responsibilities is also important.

**Team check:** Kerk should confirm specific engine motivations, protobuf/worker/Pyodide implementation details and status.

### Q19. Has the WebAssembly engine been integrated with the visualizers?

**Remember:** No complete end-to-end integration → current TS visualizers → separate WASM foundation → next milestone.

**Answer:**
> Not fully. The current Graph, Tree and Sorting visualizers still execute TypeScript algorithms in the browser. Kerk has developed a separate WebAssembly engine foundation, and we have explored integration approaches. The next step is to connect one algorithm end to end before expanding coverage.

### Q20. What is the main challenge in integrating the WASM engine?

**Remember:** State translation → identities → meaningful steps → cancellation/history.

**Answer:**
> The challenge is not simply calling an algorithm from WebAssembly. The engine produces execution states, but the visualizer needs to turn them into meaningful steps, highlights and explanations. We also need stable node and edge identities, consistent playback and safe cancellation. Our plan is to integrate one Graph algorithm first and compare its behavior with the existing TypeScript version.

## E. Evaluation, limitations & future work — both

### Q21. How did you evaluate the project so far?

**Remember:** Technical validation + formative user trial.

**Answer:**
> We evaluated the project in two main ways. First, we used unit tests, browser tests and independent checks for selected algorithms and interactions. Second, we conducted a Week 10 user trial, where students used V10 independently and provided feedback. These helped us identify both technical problems and areas for improving the user experience.

**Evidence caution:** A **1 November 2026** snapshot reported **3,273 passing unit tests** and **151 Chromium browser cases**. Do not describe these as a fresh result for today's build.

### Q22. Did your user trial prove that VisuAlgo+ improves learning?

**Remember:** No → formative usability observations → design response → structured future evaluation.

**Answer:**
> Not yet. Our Week 10 trial was mainly formative. It helped us observe how students interacted with the interface and identify usability problems. For example, frequent Status reading motivated our floating-text improvements. We still need a more structured study to measure whether these changes improve understanding or reduce attention switching.

**Evidence caution:** No verified participant total, quantified success rate or causal learning improvement was established.

### Q23. How do you ensure the correctness of your algorithm visualizations?

**Remember:** Final output + intermediate state + independent oracles + UI/session behavior.

**Answer:**
> Correctness includes both the algorithm result and the visualization behavior. We use unit tests and independent checks for selected algorithms. For example, for cut vertices and bridges, we can remove a candidate vertex or edge and compare the number of connected components. We also test playback behavior, such as state invalidation and seeking. However, passing tests does not prove that every possible input is correct.

### Q24. What are the current limitations of VisuAlgo+?

**Remember:** Integration → long-run performance → learning evaluation → coverage.

**Answer:**
> The main limitation is that the engine and visualization layers are not fully integrated yet. We also need more testing for performance and memory usage, especially for longer executions. Finally, although we have useful user feedback, we have not yet measured the learning impact of our design changes.

### Q25. What is your plan for Semester 2?

**Remember:** End-to-end integration → correctness/resource validation → structured user tasks → release preparation.

**Answer:**
> Our first priority is to integrate one Graph algorithm with the WebAssembly engine end to end. Then we will expand the integration and validate correctness, interaction behavior and resource usage. We also want to evaluate the revised explanations through more structured user tasks. Our current target is an initial public release around March 2027, depending on integration and validation.

## F. Six harder follow-up questions

### F1. Why not use an existing visualization library for everything?

**Remember:** Rendering library ≠ algorithm semantics.

> Libraries such as React Flow help us render and interact with graphs, but they do not manage algorithm-specific execution, meaningful steps or session invalidation. Those are responsibilities of our visualization layer.

### F2. Why do Graph and Tree store execution sequences upfront?

**Remember:** Easy seeking/backward inspection versus startup and memory costs.

> Precomputing steps makes forward, backward and random seeking easier. The trade-off is higher startup and memory cost for long runs. That is one area we want to measure and improve.

### F3. How do you handle parallel edges correctly?

**Remember:** Edge identity, not only endpoints.

> Two edges can connect the same pair of vertices but represent different edges. We therefore need stable edge IDs, especially for algorithms such as bridge detection and for accurate highlighting.

### F4. How can you prove V10 is better than the alternatives?

**Remember:** Current design rationale, not quantitative superiority.

> We selected V10 based on prototype exploration, user feedback and design discussions. We can explain the trade-offs, but we have not established quantitative superiority. A controlled task-based comparison would provide stronger evidence.

### F5. Did you use AI tools to implement the project?

**Remember:** AI assistance → owner requirements/review → responsibility for validation.

> Yes, AI tools assisted parts of the implementation and review. I defined the requirements, evaluated design alternatives and remained responsible for accepting and validating the changes. I do not claim that every line of code was written manually.

### F6. What is the biggest risk of your Semester 2 plan?

**Remember:** Two execution models → integration uncertainty → incremental milestone.

> The main risk is integration between the engine and the visualizers, because they currently use different execution and history models. We plan to reduce this risk by integrating one algorithm first, validating it, and then expanding gradually.

## Quick recall: eight topic anchors

| Topic | Memory anchors |
|---|---|
| Motivation | Original strengths → module-specific logic → reusable foundation |
| Prototypes | Explore → discover requirements → common direction |
| V10 | Flexibility → persistent canvas → preserved state |
| Graph | Document → Layout → Session → Presentation |
| LCA and floating text | Quiet decision → local explanation → benefit still unmeasured |
| Sorting | Same input → shared clock → independent streams |
| Evaluation | Unit/browser tests → formative trial → no proven learning impact yet |
| Future work | Engine integration → validation → evaluation/release |

## Five questions to practise aloud first

1. Why rebuild VisuAlgo rather than extending it?
2. What was your most challenging technical contribution?
3. Why is floating text important, especially for LCA?
4. Why did you choose V10?
5. How do you know your visualizations are correct?

Try to answer each without reading, in 30–40 seconds; then answer again using different wording.

## Reusable answer patterns

**Design trade-off:** “We considered … The main challenge was … We chose … because … The trade-off is …”

**Unmeasured benefit:** “We have not measured that yet. Our current evidence shows … To evaluate it properly, we plan to …”

**Individual contribution:** “The design decision was made together, while my implementation work focused on …”

**When you are uncertain:** State the known limitation, describe the evidence you have, and name the next validation step. Do not guess results or claim completed integration.

## Readings / checks before the Q&A

- [Current Master Script](VisuAlgo_CA_Master_Script.md)
- [Contribution Map](../docs/CA_PRESENTATION_CONTRIBUTION_MAP.md)
- [Graph state and playback technical case](../docs/CA_PRESENTATION_GRAPH_CASE.md)
- [Prototype history and design narratives](../docs/CA_PRESENTATION_PROTOTYPE_REVIEW.md)
- [Architecture and design decisions](../03_architecture_and_decisions.md)
- [Week 10 trial evidence and limits](../report/week10_user_trial_addendum.md)
- [Preflight checklist](VisuAlgo_CA_Preflight.md)

**Final team check:** Kerk should confirm his answers about WASM, engine architecture, website ownership, and integration status against his current code before presenting.

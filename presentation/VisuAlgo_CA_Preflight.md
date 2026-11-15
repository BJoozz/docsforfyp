# VisuAlgo+ CA Presentation — preflight / rehearsal

**Meeting:** Monday, 16 November 2026, 15:00–15:45 SGT, joint presentation on Zoom. 45 minutes TOTAL for Bao and Kerk.

## What is ready

- **Editable PowerPoint, 27 slides:** [`VisuAlgo_CA_Presentation.pptx`](VisuAlgo_CA_Presentation.pptx), with 22 timed slides, 1 Questions slide and 4 backup slides. Backup 27 is new: a recursive DFS recap that serves as a fallback for the live demo.
- **Seven embedded real-app clips** with posters as static fallbacks:
  - five in the main talk, on slides 14–18 (about 67 s in total);
  - two on the backup slides 24 and 27.
  - Press → or click to play a clip. On 16 November, PowerPoint decoded a frame from inside each clip.
  - [Media map](CA_PRESENTATION_MEDIA_USAGE.md) · [what changed from the draft](CA_DECK_CHANGELOG.md).
- **Speaker notes on all 27 slides.** The notes on the clip slides give the exact frame numbers, second by second.
- **Master script:** the [master script](VisuAlgo_CA_Master_Script.md) matches the slide sequence.
- **PDF preview** in [`ca-2026-11-16-deck-media/deck-preview/`](ca-2026-11-16-deck-media/deck-preview/). The deck validates, and every slide was rendered and inspected.
- **Tree example:** LCA (Binary Lifting) is the main Tree example. Slide 16 shows LCA(6, 10); LCA(6, 2) is kept as an alternative clip.
- **Timing:** 33 minutes of presentation and demo, plus 12 minutes for discussion and buffer. These durations are **budgeted, not measured in rehearsal**.

## Run of show

| Clock (from start) | Slides | Owner | Section |
|---|---|---|---|
| 00:00–04:00 | 1–4 | Bao | Motivation, original foundation, objectives |
| 04:00–07:00 | 5–6 | Bao | Early Graph/Tree/Sorting prototypes and division of work |
| 07:00–10:00 | 7–8 | Kerk | V2/V7, user feedback, V10 |
| 10:00–18:00 | 9–12 | Kerk | Website, WASM engine, integration boundary |
| 18:00–26:00 | 13–19 | Bao | Shell, graph state, LCA, sorting, interactions (clips on 14–18) |
| 26:00–31:00 | 20–21 | Both | Live workflow demo and formative evaluation |
| 31:00–33:00 | 22 | Both | Semester 2 priorities |
| 33:00–45:00 | 23 and 24–27 as needed | Both | Q&A / buffer |

## Must complete before 3:00 PM

1. **Kerk reviews slides 7–12.**
   - Confirm the current engine implementation and the worker, protobuf and Pyodide details.
   - Confirm the exact website ownership.
   - Confirm whether the optional separate-engine demo is reliable.
   - These slides were restyled into diagrams with the draft's wording. Their content is still provisional.
2. **Click through the deck once in slideshow mode on the presenting computer.**
   - On slides 14–18, 24 and 27, press → once: the clip should play with motion. Press → again to move on.
   - Check that the poster is visible before the clip plays.
3. **Run the presentation once together.**
   - Time every section.
   - If time is tight, shorten the joint demo on slide 20 to Graph only.
   - Reserve Q&A time.
4. **Test the live demo in the exact build you will present** (slide 20 only; slides 14–18 now use clips):
   - Graph Editor input → Dijkstra → recursive DFS final recap;
   - Tree Editor LCA ancestors on hover.
   - If anything fails live, use the clips on slides 15–18 or backup slide 27. Do not debug during the talk.
5. **Zoom logistics.**
   - Send the meeting link to both Dr Terence Sim and A/P Steven Halim.
   - Verify that the host can run for more than 45 minutes, and check speaker screen-sharing permissions and audio.
   - When sharing, tick **Optimize for video clip** so the clips stay smooth.
   - Make sure both speakers can control their own section.

## Clip and demo details

| Slide | What plays | Point to |
|---|---|---|
| 14 | The Status tab splits the right group, joins the left group, then docks under the drawing | Frame stays 12/21 throughout; the drawing only re-fits when the bottom row opens |
| 15 | B dragged at 12/21; B → A changed from 1 to 5 in Draw graph → Edges; a second B → A edge drawn on the canvas, then given weight 2 | Counter unchanged after the drag; NO RUN after the edit; two separate B → A edges labelled 5 and 2 |
| 16 | LCA(6, 10) on root 8, edges 8-4, 8-12, 4-2, 4-6, 12-10, 12-14 | k = 1 note "same ancestor · keep u, v"; k = 0 "differ · lift both"; answer 8. No depth-balancing move (equal depths) |
| 17 | Bubble vs Selection, same 12 values, pause at operation 48, resume, Last | Operation counts ≠ CPU time; Last is a seek, not a speed result |
| 18 | Dijkstra on the nine-vertex Big preset: paused at 17/53, Next to 18/53 with `12 + 14 < 33 · update`, Last, hover 8 then 4 | Paused motion is subtle: point at the 2 → 3 edge while the counter reads 17 |
| 20 | **Live**: Graph Editor (Dijkstra + recursive DFS), then Tree Editor LCA | Narrate only the current action |

Live alternatives for slides 14–18 are in the notes, for use only if time allows.

## Claims to present accurately

- The current Graph, Tree and Sorting visualizers use **TypeScript** implementations. The C++/WebAssembly engine is a **separate foundation**; end-to-end integration has not been delivered.
- **3,273 unit tests / 151 Chromium cases** are a **dated report snapshot from 1 Nov 2026**, not a verified number for today's build.
- The Week 10 trial provided formative observations. Bao's specific recollection about newer learners frequently consulting Status is **not a coded analysis of recorded footage**.
- Floating text is a response to that observation. **No measured learning improvement** or reduction in attention switching has yet been established.
- March 2027 is a **target**, conditional on integration and validation, not a guaranteed release date.
- **Algorithm coverage:** Prof. Halim's direction was to widen the range of algorithms in general (Bao's account, no written record). Do not say he asked for LCA, Trie, Heavy-Light Decomposition or Centroid Decomposition specifically.
- **LCA and Trie** were built in the standalone Tree prototype (September 2026) and are in the current app. Do not say Trie provides groundwork for Heavy-Light or Centroid Decomposition; the link is from rooted trees and ancestor queries.
- **Heavy-Light Decomposition and Centroid Decomposition** are possible later extensions. They are not implemented and are not Semester 2 commitments.
- Make no claim about whether the original VisuAlgo has Trie or LCA pages; the records disagree.
- **Images and clips by date:**
  - Slides 1, 2, 8, 13–19, 24 and 27 use current captures of app `346e84b` from 15–16 November.
  - Slide 25 is historical (1 November, `662e7b3`).
  - Slide 5 shows the standalone prototypes, rebuilt at their documented commits and captured on 16 November.
  - Slide 7 is schematic.

## Suggested Q&A focus

- Why the original module-specific logic complicates common editing/playback changes.
- Why physical layout edits preserve a Graph playback session but semantic graph edits invalidate it.
- Why the V10 shell limits layout flexibility in exchange for a persistent central canvas.
- Why LCA can have a meaningful step with little visible movement; how tree, table, Status and floating note agree.
- How sorting panes share one logical clock while each keeps independent operation history.
- How node/edge identity, step meaning and cancellation need to be translated across WASM ↔ TypeScript boundaries.
- Individual contributions: Bao's visualizers/shell/integration; Kerk's design system/engine/infrastructure; V10 decisions were joint, with overlapping implementation work.

## Repository

The deck, its media, the build scripts and these notes are committed in the public repository `BJoozz/docsforfyp` under `presentation/`; the owner allowed publishing them there. The GPT draft is kept unchanged under `presentation/drafts/`. Slides 7–12 remain a draft until Kerk confirms them.

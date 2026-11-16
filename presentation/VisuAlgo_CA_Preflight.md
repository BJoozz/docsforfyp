# VisuAlgo+ CA Presentation — preflight / rehearsal

**Meeting:** Monday, 16 November 2026, 15:00–15:45 SGT, joint presentation on Zoom. 45 minutes TOTAL for Bao and Kerk.

## Order changed on 16 November, about 12:30

Kerk rearranged the deck: the live demo comes right after the title, Bao speaks to slide 14 and Kerk from 15 to 23. The run of show below is the new one. **The other sections of this file still use the earlier slide numbers**; this table converts them.

| Earlier slide | Now |
|---|---|
| 1 Title | 1 |
| 20 Live demo | 2 |
| 2–6 Motivation to Two parallel foundations | 3–7 |
| 13–19 Visualization contributions to Editors | 8–14 |
| 7, 8, 9 (wireframes, V2/V7 to V10, application boundaries) | replaced by Kerk's 15–20 |
| 10–12 Engine foundation to Website integration | 21–23 |
| 21 Evaluation, 22 Semester 2 priorities | not in the deck |
| 23 Questions | 24 |

Clips are now on slides 9–13. For Kerk before the talk: slides 19 and 20 are identical, there is no Future Work slide, and the Architecture slide needs a sentence on what runs today.

## What is ready

- **Two editable PowerPoint files:**
  - [`VisuAlgo_CA_Presentation.pptx`](VisuAlgo_CA_Presentation.pptx), 23 slides: 22 timed slides and the Questions slide.
  - [`VisuAlgo_CA_QA_Backup.pptx`](VisuAlgo_CA_QA_Backup.pptx), 4 backup slides: B1 recursive DFS recap (the fallback for the live demo), B2 preview before Apply, B3 correctness and limitations, B4 evidence and ownership.
- **Seven embedded real-app clips** with posters as static fallbacks:
  - five in the main talk, on slides 14–18 (about 85 s in total);
  - two in the backup file, on B1 and B2.
  - Press → or click to play a clip. On 16 November, PowerPoint decoded a frame from inside each clip.
  - [Media map](CA_PRESENTATION_MEDIA_USAGE.md) · [what changed from the draft](CA_DECK_CHANGELOG.md).
- **Speaker notes on every slide of both files.** The notes on the clip slides give the exact frame numbers, second by second.
- **Speaking script:** every slide has a main message, talking points, a script in plain spoken English, cues and a transition. It is in the speaker notes, in the [master script](VisuAlgo_CA_Master_Script.md) and, in short form, in the [cheat sheet](VisuAlgo_CA_Cheat_Sheet.md).
- **PDF previews** of both files in [`ca-2026-11-16-deck-media/deck-preview/`](ca-2026-11-16-deck-media/deck-preview/). Both files validate, and every slide was rendered and inspected.
- **Tree example:** LCA (Binary Lifting) is the main Tree example. Slide 17 moves the root of a ten-node tree from 10 to 16, then shows LCA(8, 20); LCA(6, 10) and LCA(6, 2) are kept as alternative clips.
- **Timing:** 33 minutes of presentation and demo, plus 12 minutes for discussion and buffer. These durations are **budgeted, not measured in rehearsal**.

## Run of show

| Clock (from start) | Slides | Owner | Section |
|---|---|---|---|
| 00:00–00:40 | 1 | Bao | Title |
| 00:40–04:30 | 2 | Bao | Live demo |
| 04:30–08:00 | 3–5 | Bao | Motivation, original foundation, objectives |
| 08:00–10:50 | 6–7 | Bao | Early prototypes and the two parallel foundations |
| 10:50–19:10 | 8–14 | Bao | Contributions, shell, graph state, sorting, LCA, interactions, editors (clips on 9–13) |
| 19:10–23:10 | 15–18 | Kerk | Wireframing, V10, the Week 10 trial and its feedback |
| 23:10–31:10 | 19–23 | Kerk | Architecture, engine, integration, website |
| 31:10–33:00 | 23 | Kerk | Future work, said over slide 23 |
| 33:00–45:00 | 24 and the backup file as needed | Both | Q&A / buffer |

## Must complete before 3:00 PM

1. **Kerk reviews slides 7–12.**
   - Confirm the current engine implementation and the worker, protobuf and Pyodide details.
   - Confirm the exact website ownership.
   - Confirm whether the optional separate-engine demo is reliable.
   - Slides 7–8 were rewritten on 16 November for the design history (nine wireframes, V2 and V7, V10). Kerk should read their new notes: they are in his voice and credit his wireframes, the feedback he organised, his refinements and the consolidation.
   - Slides 9–12 were restyled into diagrams with the draft's wording. Their content is still provisional.
2. **Click through the deck once in slideshow mode on the presenting computer.**
   - On slides 14–18, and on B1 and B2 of the backup file, press → once: the clip should play with motion. Press → again to move on.
   - Check that the poster is visible before the clip plays.
3. **Run the presentation once together.**
   - Time every section.
   - If time is tight, shorten the joint demo on slide 20 to Graph only.
   - Reserve Q&A time.
4. **Test the live demo in the exact build you will present** (slide 20 only; slides 14–18 now use clips):
   - home page → Graph Editor → Algorithms menu and search → the panels → add a node, draw an edge, type its weight → Dijkstra (six steps, Autoplay, hover);
   - Tree Editor → set Root to 12.
   - The steps and the values to expect are in the notes of the Live demo slide (now slide 2); they were run on app `346e84b` on 16 November.
   - If anything fails live, use the clips on slides 15, 17 and 18 or backup B1 (the first slide of the backup file). Do not debug during the talk.
   - Slide 20 says only "Live demo". Agree in rehearsal what the three minutes show; the notes hold a working plan.
5. **Zoom logistics.**
   - Send the meeting link to both Dr Terence Sim and A/P Steven Halim.
   - Verify that the host can run for more than 45 minutes, and check speaker screen-sharing permissions and audio.
   - Present from copies of the two files **outside OneDrive**. On 16 November, after the deck in the synced folder was opened in PowerPoint, it came back with shapes from an older version doubled on slide 2.
   - Share the **whole screen**, not one PowerPoint window: the backup slides are in a second file, and a shared window would not show it. Open both files before the meeting.
   - When sharing, tick **Optimize for video clip** so the clips stay smooth.
   - Make sure both speakers can control their own section.

## Clip and demo details

| Slide | What plays | Point to |
|---|---|---|
| 14 | The Status tab splits the right group, joins the left group, then docks under the drawing | Frame stays 12/21 throughout; the drawing only re-fits when the bottom row opens |
| 15 | B dragged at 12/21; B → A changed from 1 to 5 in Draw graph → Edges; a second B → A edge drawn on the canvas, then given weight 2 | Counter unchanged after the drag; NO RUN after the edit; two separate B → A edges labelled 5 and 2 |
| 16 | Bubble vs Selection, same 12 values, pause at operation 48, resume, Last | Operation counts ≠ CPU time; Last is a seek, not a speed result |
| 17 | On Balanced · 10 nodes the root moves from 10 to 16, then LCA(8, 20) runs (27.9 s) | The Root control under Structure in the first three seconds; then u lifts from 8 to 4; both cursors stay at k = 3, 2, 1 (ancestor 16); both lift at k = 0 (10 and 18); answer 16. Say that no node moves during the query and the notes carry the reasons, and read the frame number aloud; the benefit is not measured |
| 18 | Dijkstra on the nine-vertex Big preset: paused at 17/53, Next to 18/53 with `12 + 14 < 33 · update`, Last, hover 8 then 4 | Paused motion is subtle: point at the 2 → 3 edge while the counter reads 17 |
| 20 (now 2) | **Live**: a tour: the home page, the Graph Editor (menu, panels, drawing, Dijkstra), then the Tree Editor (re-root) | Narrate only the current action; the steps are in the notes |

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
  - Slides 1, 2, 8 and 13–19, and backups B1 and B2, use current captures of app `346e84b` from 15–16 November.
  - Backup B3 is historical (1 November, `662e7b3`).
  - On the slides these captures are labelled only "Real app capture"; the dates and commits are in the notes and the media map.
  - Slide 5 shows the standalone prototypes, rebuilt at their documented commits and captured on 16 November.
  - Slides 6–8 use design-history artifacts rendered from their own commits: Kerk's UI kit (3 September) and wireframes (4 September), and Bao's working V2 and V7 builds.

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

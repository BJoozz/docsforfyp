# VisuAlgo+ CA Presentation — preflight / rehearsal

**Meeting:** Monday, 16 November 2026, 15:00–15:45 SGT, joint presentation on Zoom. 45 minutes TOTAL for Bao and Kerk.

## What is ready
- Editable PowerPoint: **26 slides** — 22 timed, 1 Questions, 3 backup.
- Speaker notes on all 26 slides, including English scripts, timings, demo cues and source links.
- Separate master script matches the slide sequence.
- Deck rendered successfully to a 26-page PDF; no visibly missing slides or images in the contact-sheet inspection.
- LCA (Binary Lifting) is the primary Tree technical example, not Heap.
- Timing plan: **33 min presentation and demo; 12 min discussion/buffer**. These durations are budgeted, **not measured in rehearsal**.

## Run of show
| Clock (from start) | Slides | Owner | Section |
|---|---|---|---|
| 00:00–04:00 | 1–4 | Bao | Motivation, original foundation, objectives |
| 04:00–07:00 | 5–6 | Bao | Early Graph/Tree/Sorting prototypes and division of work |
| 07:00–10:00 | 7–8 | Kerk | V2/V7, user feedback, V10 |
| 10:00–18:00 | 9–12 | Kerk | Website, WASM engine, integration boundary |
| 18:00–26:00 | 13–19 | Bao | Shell, graph state, LCA, sorting, interactions |
| 26:00–31:00 | 20–21 | Both | Live workflow demo and formative evaluation |
| 31:00–33:00 | 22 | Both | Semester 2 priorities |
| 33:00–45:00 | 23 and 24–26 as needed | Both | Q&A / buffer |

## Must complete before 3:00 PM
1. **Kerk review of slides 7–12:** Confirm current engine implementation, worker/protobuf/Pyodide details, exact website ownership, and whether the optional separate-engine demo is reliable. These slides are explicitly provisional in the script.
2. **Run the presentation once together:** Time every section. If time is tight, shorten the joint demo at slide 20 to Graph only; LCA was already shown on slide 16. Reserve Q&A time.
3. **Test the live workflows in the exact deployed build** (not just historical 1 Nov screenshots): tab movement, vertex drag vs edge-weight edit, LCA's equal-ancestor note, reverse sorting step, Dijkstra pause/final path hover, DFS recursive final recap.
4. **Prepare a fallback:** Screen recording(s) or at least open the relevant static slide. No fresh motion clips were attached to this package. Do not troubleshoot unexpected browser problems during the presentation.
5. **Zoom logistics:** Send meeting link to both Dr Terence Sim and A/P Steven Halim, verify host can run >45 minutes, speaker screen-sharing permissions and audio. Keep both speakers able to control their own section.

## Demo-specific details
- **Slide 14 (20 s):** Move Status tab while paused, show canvas and frame unchanged, reset layout.
- **Slide 15 (20 s):** With Live layout disabled, drag a graph vertex (run remains), then change an edge weight (run becomes invalid).
- **Slide 16 (35 s):** Tree root 8, edges 8-4, 8-12, 4-2, 4-6, 12-10, 12-14. LCA(6,2)=4. Show candidate ancestors both 8; nodes stay. This is **not** a depth-balancing move.
- **Slide 17 (20 s):** Same sorting input in two panes, step backward once; operation counts ≠ CPU run time.
- **Slide 18 (30 s):** Pause Dijkstra, keep frame counter fixed, go to last frame and hover vertices to inspect shortest paths.
- **Slide 20 (3 min):** Graph Editor (Dijkstra + recursive DFS) then Tree Editor LCA; narrate only current action.

## Claims to present accurately
- Current Graph, Tree and Sorting visualizers use **TypeScript** implementations. The C++/WebAssembly engine is a **separate foundation**, not an end-to-end integration already delivered.
- **3,273 unit tests / 151 Chromium cases** are a **dated report snapshot from 1 Nov 2026**, not a verified number for today's build.
- Week 10 trial provided formative observations; Bao's specific recollection about newer learners frequently consulting Status is **not a coded analysis of recorded footage**.
- Floating text is a response to that observation. **No measured learning improvement** or reduction in attention switching has yet been established.
- March 2027 is a **target**, conditional on integration and validation, not a guaranteed release date.
- The deck's images are **historical captures from 1 Nov 2026**. Verify whether they match the live build; don't imply they are current screenshots.

## Suggested Q&A focus
- Why the original module-specific logic complicates common editing/playback changes.
- Why physical layout edits preserve a Graph playback session but semantic graph edits invalidate it.
- Why the V10 shell limits layout flexibility in exchange for a persistent central canvas.
- Why LCA can have a meaningful step with little visible movement; how tree, table, Status and floating note agree.
- How sorting panes share one logical clock while each keeps independent operation history.
- How node/edge identity, step meaning and cancellation need to be translated across WASM ↔ TypeScript boundaries.
- Individual contributions: Bao's visualizers/shell/integration; Kerk's design system/engine/infrastructure; V10 decisions were joint, with overlapping implementation work.

## Uploading to GitHub (after explicit approval to share)
The target repository `BJoozz/docsforfyp` is **public** and `main` currently has no `presentation/` folder. The original Work handoff did not publish the PowerPoint. This package is prepared locally, **not published**.

Place the PPTX, script, and this preflight note under `presentation/` in your local clone. From the repository root:

```bash
git pull --ff-only origin main
git add presentation/VisuAlgo_CA_Presentation.pptx presentation/VisuAlgo_CA_Master_Script.md presentation/VisuAlgo_CA_Preflight.md
git commit -m "Add CA presentation master and rehearsal notes"
git push origin main
```

Only publish after confirming you want these draft materials in a public repository. Kerk's draft slides should be reviewed before treating the package as final.
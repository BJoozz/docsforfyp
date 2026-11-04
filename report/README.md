# VisuAlgo+ CA Report — LaTeX sources

**Submission file:** [`VisuAlgo_CA_Report.pdf`](VisuAlgo_CA_Report.pdf), built from `main.tex` (15 pages including the cover and references). It replaces the earlier `VisuAlgo_CA_Report_Draft.pdf`.

Registered project details (confirmed by Bao on 4 November 2026): Project ID **H160390**; title **"Exploring New Information Visualization Techniques for VisuAlgo+"**; supervisor A/P Steven Halim; Main Evaluator SIM Mong Cheng, Terence. "Rebuilding Interactive Algorithm Visualizations" is kept as the subtitle.

## Revision of 4 November 2026 (after the CA review)

The review is in [`../docs/FYP_CA_REVIEW_VI.md`](../docs/FYP_CA_REVIEW_VI.md), with Bao's answers in its section 6. Changes applied:

- Removed every draft marker (cover, running header, PDF title, file name). The cover now gives the registered title, project ID, supervisor and Main Evaluator.
- Week 10 trial: dated as Week 10; several users, all NUS students; consent obtained in advance by Kerk; the recordings show only the screen and hands; several refinements (floating text, the legend and the Status panel); detailed results not yet compiled. It is no longer cited to the evidence snapshot `67ce56c`, which predates it.
- The floating-text motivation no longer names the supervisor. The V10 design choices are described as made by Kerk and Bao together under A/P Halim's supervision, feedback and agreement, drawing on the original visualgo.net, the early prototypes and the V2 and V7 builds (Bao's instruction, about 13:50 SGT); the internal choice numbers (1–26, 27–48) are no longer quoted. Section 1.1 gives his aim as Bao states it: the best current tools, because the old stack is dated for planned updates.
- The survey, V2/V7 and V10 order now follows Bao's account: Kerk's survey; Kerk and Bao picked V2 and V7 from Kerk's nine wireframe layouts; Bao built both (20–27 September); V10 was discussed in Week 9 and implemented by Bao, with refinements from Kerk. Choices 27–48 and the 18 October "keep only V10" decision are credited to Kerk and Bao jointly.
- Factual corrections from the review: floating-text timing, the anchoring of notes, the captions of Figures 5, 6 and 9, catalogue counts, layout floors per module, sorting history, End-node algorithms, the 700 randomized inputs, CI runs, manual checklists, Figures 1 and 2, Table 1 periods, and the wording on Halim et al. 2012.
- Testing wording: automated tests and manual checks were used to verify interface behaviour; the Week 10 trial provided formative feedback on usability (no claim that UI/UX is "confirmed").
- Section 7 and Table 5 now use the fixed SoC dates: CA presentation in Reading Week; final report by Wednesday 7 April 2027, 5 pm; final presentation 19–23 April 2027 (tentative); e-copy by 10 May 2027.
- The project records [6]–[8] are "available on request" and are cited three times instead of thirteen. The page-16 notes were replaced by one short note under the references.
- Layout: floats are now `[tbp]`, and `\page` only keeps a heading with its first lines. This and the removal of repeated caveats bring the report to 15 pages.

## Compile

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=VisuAlgo_CA_Report main.tex
```

The source uses standard TeX Live packages (including `cite` and `needspace`). It builds with MiKTeX 25.12 (Bao's machine) and with TeX Live (Debian packages `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-xetex`, `fonts-dejavu`, `latexmk`). The seven screenshots are in `figures/`; the two diagrams are drawn with TikZ; references are in `references.bib`. It can also be uploaded to Overleaf with `main.tex` as the main document (pdfLaTeX).

After building, check: `pdfinfo` reports at most 15 pages; the log has no `undefined` or `Overfull`; `pdftotext` finds no "Draft".

## Vietnamese reading versions

- [Full Vietnamese translation](vi/VisuAlgo_CA_Report_VI.pdf), source [vi/full.tex](vi/full.tex).
- [Vietnamese summary](vi/VisuAlgo_CA_Summary_VI.pdf), source [vi/summary.tex](vi/summary.tex).

They are reading aids, not the submission, and are kept in sync with the English revision. Build them with XeLaTeX (see [vi/README.md](vi/README.md)).

## Before submitting

- Send `VisuAlgo_CA_Report.pdf` as a softcopy to both A/P Steven Halim and the Main Evaluator (SIM Mong Cheng, Terence) by 17:00 SGT on 4 November 2026.
- Arrange the CA presentation with both of them for Reading Week (14–20 November 2026).
- The project records cited as [6]–[8] are in the private repository `BJoozz/docsforfyp`; share them if an examiner asks.

## Evidence boundaries

Application snapshot: `662e7b3` in `kerktaiheng/visualgo-plus-design`. Evidence snapshot: `67ce56c` in `BJoozz/docsforfyp`. Validation numbers are recorded results from 1 November 2026; on 4 November the unit tests (654 + 2,619) and lint were re-run and matched. The Week 10 trial rests on Bao's account (see [the addendum](week10_user_trial_addendum.md)). The report does not claim learning improvement, measured attention-switching reduction, comparative usability, performance improvement, complete VisuAlgo parity or current WASM integration.

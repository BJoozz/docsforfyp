"""Apply slides 6-8 (slides_6_8.py) to an already finalised deck.

Run from the docsforfyp root:
    py -3.12 presentation/ca-2026-11-16-deck-media/deck-build/apply_slides_6_8.py in.pptx out.pptx
Only slides 6, 7 and 8 change; every other part of the deck, including the
videos and the play-on-click timings PowerPoint wrote, is carried over as it is.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pptx import Presentation  # noqa: E402

import slides_6_8  # noqa: E402

src, out = sys.argv[1], sys.argv[2]
prs = Presentation(src)
S = {i + 1: s for i, s in enumerate(prs.slides)}
print('\n'.join(slides_6_8.apply({6: S[6], 7: S[7], 8: S[8]}, Path('.').resolve())))
# keep the provenance sentence in slide 26's notes in step with the new slides
OLD26 = 'Slide 7 uses schematic drawings, not screenshots.'
NEW26 = ("Slides 6 to 8 use design-history artifacts rendered from their own commits "
         "(presentation/ca-2026-11-16-deck-media/design-history/): Kerk's UI kit (634b5be, 3 September) and wireframes "
         "(69aa8e4, 4 September), and Bao's working V2 and V7 builds (ae63a62).")
tf = S[26].notes_slide.notes_text_frame
if OLD26 in tf.text:
    tf.text = tf.text.replace(OLD26, NEW26)
    print('slide 26 notes: provenance sentence updated')
prs.save(out)
print('saved', out)

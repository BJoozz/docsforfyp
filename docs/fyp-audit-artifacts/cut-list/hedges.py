import re, sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
pages = re.split(r"===== PAGE (\d+) =====", text)
# pages: ['', '1', body1, '2', body2, ...]
sents = []
for i in range(1, len(pages), 2):
    p = int(pages[i]); body = pages[i+1]
    if p > 14:  # body text only (pages 1-14; 15 = references, 16 = back matter)
        continue
    body = re.sub(r"-\n(?=[a-z])", "", body)
    body = re.sub(r"\s+", " ", body)
    for s in re.split(r"(?<=[.;])\s+(?=[A-Z(])", body):
        sents.append((p, s.strip()))
cats = {
 "learning/usability/preference not shown": r"learning (outcome|gain|benefit|effectiveness|improvement)|improved learning|attention or learning|educationally superior|users prefer|comparative usability|measured learning|do not measure usability",
 "not a benchmark / not measured perf": r"benchmark|not .*measured|has not been measured|have not yet been benchmarked|elapsed runtime|relative runtime",
 "engine not integrated": r"WASM-powered|not been connected|no runtime connection|not .*implement a general engine adapter|not part of the deployed",
 "browser drag/split coverage incomplete": r"drag-and-split|coverage of those interactions is incomplete|Systematic browser coverage|does not replace browser testing",
 "parity not complete": r"parity",
}
total = set()
for name, pat in cats.items():
    hits = [(p, s) for p, s in sents if re.search(pat, s, re.I)]
    print(f"== {name}: {len(hits)} sentences on pages {sorted(set(p for p,_ in hits))}")
    for p, s in hits:
        total.add((p, s))
        print(f"   p{p}: {s[:150]}")
neg = r"\b(not|cannot|neither|nor|no longer|does not|do not|did not|has not|have not|unavailable|incomplete|remain(s)? necessary)\b"
negs = [(p, s) for p, s in sents if re.search(neg, s, re.I)]
print(f"\nBody sentences (pp.1-14): {len(sents)}; containing a negation/limitation marker: {len(negs)}")
from collections import Counter
c = Counter(p for p, _ in negs)
print("per page:", dict(sorted(c.items())))

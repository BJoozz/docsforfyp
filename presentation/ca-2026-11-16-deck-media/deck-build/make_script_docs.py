"""Write the speaking script into the master script and the cheat sheet.

Run from the docsforfyp repository root:
    py -3.12 presentation/ca-2026-11-16-deck-media/deck-build/make_script_docs.py

speaking_script.json is the source. For every slide the master script gets its title,
speaker and clock time, a main message, talking points, the script, cues and a
transition, followed by the folded block with the slide text, clip details and sources
that is already there. The cheat sheet gets the message, the talking points and the
transition, plus the cues on the clip and demo slides. Running it again replaces what it
wrote before.
"""
import io
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MASTER = Path('presentation/VisuAlgo_CA_Master_Script.md')
CHEAT = Path('presentation/VisuAlgo_CA_Cheat_Sheet.md')
WPM = 130
SPEAK = json.loads((HERE / 'speaking_script.json').read_text(encoding='utf-8'))['slides']
SUMMARY = 'Slide text, clip details and sources'


def words(entry):
    text = ' '.join(re.sub(r'\[[^\]]*\]', '', p) for p in entry['script'] + [entry.get('transition', '')])
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’+.,-]*", text))


def script_md(entry):
    out = []
    for para in entry['script']:
        m = re.match(r'(Bao|Kerk): (.*)', para, flags=re.S)
        out.append(f'> **{m.group(1)}:** {m.group(2)}' if m else f'> {para}')
    return '\n>\n'.join(out)


def speak_block(entry):
    n = words(entry)
    fit = f'*Script: {n} words, about {round(n / WPM * 60)} s at {WPM} words per minute'
    fit += f"; the slot is {entry['seconds']} s.*" if entry['seconds'] else '.*'
    out = [fit,
           f"**Main message:** {entry['message']}",
           '**Talking points**\n\n' + '\n'.join('- ' + p for p in entry['points']),
           '**Script**\n\n' + script_md(entry)]
    if entry.get('cues'):
        out.append('**Cues**\n\n' + '\n'.join('- ' + c for c in entry['cues']))
    if entry.get('transition'):
        out.append(f"**Transition:** {entry['transition']}")
    return '\n\n'.join(out)


def header_of(entry, existing):
    return existing if entry['time'] == 'backup' else f"**{entry['speaker']} · {entry['section']} · {entry['time']}**"


raw = io.open(MASTER, encoding='utf-8', newline='').read()
crlf = '\r\n' in raw
text = raw.replace('\r\n', '\n')
parts = re.split(r'\n(?=###? )', text)
headers = {}
done = 0
for i, part in enumerate(parts):
    m = re.match(r'### (\w+)\. (.*)\n', part)
    if not m:
        continue
    key = m.group(1).lstrip('0') or '0'
    if key not in SPEAK:
        raise SystemExit(f'no speaking script for section {m.group(1)}')
    entry = SPEAK[key]
    lines = part.rstrip('\n').split('\n')
    hi = next(j for j, ln in enumerate(lines) if j > 0 and ln.startswith('**'))
    header = header_of(entry, lines[hi])
    headers[key] = header.strip('*')
    body = '\n'.join(lines[hi + 1:]).strip('\n')
    if '<details>' not in body:
        raise SystemExit(f'section {m.group(1)} has no folded reference block')
    ref = body[body.index('<details>'):]
    ref = re.sub(r'^<details>\n<summary>[^\n]*</summary>\n\n', '', ref)
    ref = re.sub(r'\n\n</details>\s*$', '', ref)
    num = key if key.startswith('B') else f'{int(key):02d}'
    new = '\n\n'.join([f"### {num}. {entry['title']}", header, speak_block(entry),
                       f'<details>\n<summary>{SUMMARY}</summary>\n\n{ref}\n\n</details>'])
    parts[i] = new + '\n'
    done += 1
if done != len(SPEAK):
    raise SystemExit(f'{done} sections found for {len(SPEAK)} script entries')
text = '\n'.join(parts)

FORMAT = ('Script format, 16 November, at Bao\'s request: every slide has a main message, three to five talking points, '
          'a script in plain spoken English, cues and a transition to the next slide. The talking points are there so the '
          'speaker can say it in their own words; the script is not meant to be learned by heart. The slide text, clip '
          'timings and sources are folded under each script. The same text is in the speaker notes of both PowerPoint '
          'files, and [the cheat sheet](VisuAlgo_CA_Cheat_Sheet.md) has the short version. The word counts assume about '
          f'{WPM} words per minute and are a guide, not a measurement. Kerk\'s slides are 15 to 23. For the ones he remade '
          '(15 to 20) the script is a draft built from the slide text and his earlier script; all of them are his to confirm.')
if 'Script format, 16 November' not in text:
    raise SystemExit('master script: the script-format paragraph is missing')
text = re.sub(r'Script format, 16 November[^\n]*', lambda m: FORMAT, text)
io.open(MASTER, 'w', encoding='utf-8', newline='').write(text.replace('\n', '\r\n') if crlf else text)
print(f'{MASTER}: {done} sections written')

# ---------------------------------------------------------------- cheat sheet
sheet = ['# VisuAlgo+ CA talk: cheat sheet', '',
         'One glance per slide: the message, the points to hit and the line that leads to the next slide. '
         'Clip and demo slides also list their cues. The full wording is in [the master script](VisuAlgo_CA_Master_Script.md) '
         'and in the speaker notes. Both come from `ca-2026-11-16-deck-media/deck-build/speaking_script.json`.', '',
         '33 minutes of talk, then 12 minutes of questions. Order since 16 November: the title, the live demo, '
         "Bao's slides (up to 14), then Kerk's (15 to 23).", '']
for key, entry in SPEAK.items():
    num = key if key.startswith('B') else f'{int(key):02d}'
    who = re.sub(r'^Backup / [^,]*, outside timed talk$', 'Backup', headers[key])
    sheet += [f"## {num} · {entry['title']}", '', f'*{who}*', '', f"**Message:** {entry['message']}", '']
    sheet += ['- ' + p for p in entry['points']]
    has_clip = any('[Press →' in p for p in entry['script']) or entry['title'] == 'Live demo'
    if has_clip and entry.get('cues'):
        sheet += ['', '**Cues**', ''] + ['- ' + c for c in entry['cues']]
    if entry.get('transition'):
        sheet += ['', f"**Next:** {entry['transition']}"]
    sheet.append('')
io.open(CHEAT, 'w', encoding='utf-8', newline='\n').write('\n'.join(sheet))
print(f'{CHEAT}: {len(SPEAK)} slides')

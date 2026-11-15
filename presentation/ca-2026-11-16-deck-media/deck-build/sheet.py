import sys, glob, os
from PIL import Image, ImageDraw
src, prefix = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 3
per = int(sys.argv[4]) if len(sys.argv) > 4 else 9
files = sorted(glob.glob(os.path.join(src, 'slide-*.png')))
tw, th = 600, 338
for k in range(0, len(files), per):
    chunk = files[k:k + per]
    rows = (len(chunk) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * (tw + 12) + 12, rows * (th + 30) + 12), (200, 200, 200))
    d = ImageDraw.Draw(sheet)
    for i, f in enumerate(chunk):
        im = Image.open(f).convert('RGB').resize((tw, th), Image.LANCZOS)
        x = 12 + (i % cols) * (tw + 12); y = 12 + (i // cols) * (th + 30)
        d.text((x, y), os.path.basename(f), fill=(0, 0, 0))
        sheet.paste(im, (x, y + 16))
    out = f'{prefix}-{k // per + 1}.png'
    sheet.save(out); print(out)

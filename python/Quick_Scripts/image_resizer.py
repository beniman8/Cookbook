from PIL import Image
from pathlib import Path
import zipfile

src = Path('path')
img = Image.open(src).convert("RGBA")

sizes = [28, 56, 112]
out_paths = []

for s in sizes:
    resized = img.resize((s, s), Image.LANCZOS)
    out = Path(f"/mnt/data/penny_twitch_{s}x{s}.png")
    resized.save(out)
    out_paths.append(out)

zip_path = Path("/mnt/data/penny_twitch_sizes.zip")
with zipfile.ZipFile(zip_path, 'w') as z:
    for p in out_paths:
        z.write(p, arcname=p.name)

print("Created files:")
for p in out_paths:
    print(p)

print(f"\nZIP archive: {zip_path}")

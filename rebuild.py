import os, subprocess, urllib.parse

photos_dir = "/Users/olivertusiime/Documents/Optimum Web/FeelEric/images/photos"
html_file = "/Users/olivertusiime/Documents/Optimum Web/FeelEric/gallery.html"

try:
    files = [f for f in os.listdir(photos_dir) if f.lower().endswith((".jpg", ".jpeg", ".png", ".heic"))]
    files.sort()
except:
    files = []

items_html = ""

for f in files:
    path = os.path.join(photos_dir, f)
    is_landscape = True # fallback
    try:
        out = subprocess.check_output(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path], text=True)
        w, h = 0, 0
        for line in out.splitlines():
            if "pixelWidth" in line:
                w = int(line.split(":")[-1].strip())
            elif "pixelHeight" in line:
                h = int(line.split(":")[-1].strip())
        if h > w:
            is_landscape = False
    except:
        pass

    p = "images/photos/" + urllib.parse.quote(f)
    classes = "masonry-item hover-target reveal-item"
    if is_landscape:
        classes += " small-landscape"
        
    items_html += f'            <div class="{classes}">\n                <img src="{p}" alt="">\n            </div>\n'

layout_html = f'<div class="masonry-grid">\n{items_html}        </div>'

with open(html_file, "r") as f_in:
    content = f_in.read()

import re
new_content = re.sub(
    r"(<section class=\"gallery-section\">).*?(</section>)",
    f"\\1\n        {layout_html}\n    \\2",
    content,
    flags=re.DOTALL
)

with open(html_file, "w") as f_out:
    f_out.write(new_content)

print("Gallery reverted to mixed grid!")

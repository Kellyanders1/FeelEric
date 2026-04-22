import os, re
folder = "/Users/olivertusiime/Documents/Optimum Web/FeelEric"
files = ["index.html", "gallery.html", "about.html", "video.html"]

# Delete work.html if it exists
work_path = os.path.join(folder, "work.html")
if os.path.exists(work_path):
    os.remove(work_path)

menu_html = """            <ul class="nav-links">
                <li><a href="gallery.html" class="hover-target"><span class="num">01</span> Profile</a></li>
                <li><a href="video.html" class="hover-target">Video <span class="num">02</span></a></li>
                <li><a href="about.html" class="hover-target"><span class="num">03</span> About</a></li>
                <li><a href="mailto:info@feeleric.com" class="hover-target">Contact <span class="num">04</span></a></li>
            </ul>"""

for f in files:
    filepath = os.path.join(folder, f)
    with open(filepath, "r") as file:
        content = file.read()
    
    new_content = re.sub(
        r"<ul class=\"nav-links\">.*?</ul>",
        menu_html,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    with open(filepath, "w") as file:
        file.write(new_content)
        
print("Menu updated and commissions removed.")

import os, re
folder = "/Users/olivertusiime/Documents/Optimum Web/FeelEric"
files = ["index.html", "gallery.html", "work.html", "about.html", "video.html"]

logos_html = """        <div class="partner-logos">
            <img src="images/logos/Amujae-Initiative-LogoVERT3.png" alt="Amujae">
            <img src="images/logos/download%20(1).png" alt="Partner">
            <img src="images/logos/download%20(2).png" alt="Partner">
            <img src="images/logos/download%20(3).png" alt="Partner">
            <img src="images/logos/download.jpeg" alt="Partner">
            <img src="images/logos/download.png" alt="Partner">
        </div>
"""

for f in files:
    filepath = os.path.join(folder, f)
    with open(filepath, "r") as file:
        content = file.read()
    
    # Use re.sub to inject the logos inside the start-section just before it closes
    new_content = re.sub(
        r"(<section class=\"start-section\" id=\"contact\">.*?)(\s*</section>)",
        lambda m: m.group(1) + "\n" + logos_html + m.group(2) if "partner-logos" not in m.group(1) else m.group(0),
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    with open(filepath, "w") as file:
        file.write(new_content)
        
print("Appended logos successfully.")

import os, re

folder = "/Users/olivertusiime/Documents/Optimum Web/FeelEric"
files = ["index.html", "gallery.html", "about.html", "video.html"]

logos_html = """        <div class="partner-logos">
            <img src="images/logos/Amujae-Initiative-LogoVERT3.png" alt="Amujae">
            <img src="images/logos/anlm%20logo%20green%20new.png" alt="ANLM">
            <img src="images/logos/download%20(1).png" alt="Partner">
            <img src="images/logos/download%20(2).png" alt="Partner">
            <img src="images/logos/download%20(3).png" alt="Partner">
            <img src="images/logos/download.jpeg" alt="Partner">
            <img src="images/logos/download.png" alt="Partner">
        </div>"""

for f in files:
    filepath = os.path.join(folder, f)
    with open(filepath, "r") as file:
        content = file.read()
    
    new_content = re.sub(
        r"        <div class=\"partner-logos\">.*?</div>",
        logos_html,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    with open(filepath, "w") as file:
        file.write(new_content)
        
print("Updated partner logos across all HTML files.")

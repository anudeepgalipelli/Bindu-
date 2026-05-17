import os
import sys
import shutil

source_final = r"c:\Users\Atom\Desktop\dr_bindu_v1_final (6).html"
backup_final = r"c:\Users\Atom\Desktop\dr_bindu_v1_final (6)_backup.html"
template_html = r"c:\Users\Atom\Desktop\workspace\bindu-site\index.html"

print("Creating backup of original final file...")
shutil.copy2(source_final, backup_final)

print("Reading original final file to extract base64 images...")
with open(source_final, "r", encoding="utf-8") as f:
    orig_lines = f.readlines()

b64_images = [line.strip() for line in orig_lines if "data:image" in line]

if len(b64_images) != 3:
    print(f"ERROR: Expected exactly 3 base64 images, found {len(b64_images)}")
    sys.exit(1)

print(f"Successfully extracted {len(b64_images)} base64 image strings.")
b64_desktop = b64_images[0]
b64_mobile = b64_images[1]
b64_about = b64_images[2]

print("Reading new 3D template HTML...")
with open(template_html, "r", encoding="utf-8") as f:
    new_html = f.read()

target_hero_img = '<img src="images/photo_1.jpg" alt="Dr. K Bindu Pavani">'
target_about_img = '<img src="images/photo_3.jpg" class="about-img" alt="Dr. Bindu Pavani">'

if target_hero_img not in new_html or target_about_img not in new_html:
    print("ERROR: Target placeholder images not found in template HTML.")
    sys.exit(1)

print("Replacing placeholder images with original embedded base64 strings...")
hero_replacement = f"          {b64_desktop}\n          {b64_mobile}"
about_replacement = f"            {b64_about}"

new_html = new_html.replace(target_hero_img, hero_replacement)
new_html = new_html.replace(target_about_img, about_replacement)

print("Writing assembled premium 3D design to active desktop file...")
with open(source_final, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Assembly complete! Premium 3D Theme successfully replicated.")

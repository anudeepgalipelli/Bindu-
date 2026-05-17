import re, base64, os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

os.makedirs('images', exist_ok=True)

pattern = r'src="data:image/(\w+);base64,([A-Za-z0-9+/=\s]+)"'
matches = list(re.finditer(pattern, content))
print(f"Found {len(matches)} base64 images")

new_content = content
for i, m in enumerate(reversed(matches)):
    img_type = m.group(1)
    b64_data = m.group(2).replace('\n','').replace('\r','').replace(' ','')
    ext = 'jpg' if img_type == 'jpeg' else img_type
    filename = f"images/photo_{len(matches)-i}.{ext}"
    
    img_bytes = base64.b64decode(b64_data)
    with open(filename, 'wb') as f:
        f.write(img_bytes)
    
    old_src = m.group(0)
    new_src = f'src="{filename}"'
    new_content = new_content[:m.start()] + new_src + new_content[m.end():]
    print(f"  Extracted {filename} ({len(img_bytes)} bytes)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! Images extracted and HTML updated.")

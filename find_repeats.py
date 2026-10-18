import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

curr_section = 'none'
img_occurrences = {}
for i, line in enumerate(lines):
    m_sec = re.search(r'<section\s+([^>]+)>', line)
    if m_sec:
        curr_section = m_sec.group(1).replace('\n', ' ')
    for m_img in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', line):
        src = m_img.group(1)
        img_occurrences.setdefault(src, []).append((i+1, curr_section[:60]))

for src, locs in img_occurrences.items():
    if len(locs) > 1:
        print(f"\n{src} ({len(locs)} times):")
        for line_num, sec in locs:
            print(f"  Line {line_num} in <section {sec}...>")

with open('build_master_pages.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="case-photo-frame[^>]*>.*?<img src="([^"]+)"', text, re.DOTALL)
print('Case photo frames in build_master_pages.py:', len(matches))
for i, m in enumerate(matches):
    print(f"  {i+1}: {m}")

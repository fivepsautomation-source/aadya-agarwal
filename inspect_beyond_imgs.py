with open('beyond-stem.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="case-photo-frame[^"]*"[^>]*data-src="([^"]+)"[^>]*>.*?<img src="([^"]+)"[^>]*alt="([^"]*)"', text, re.DOTALL)
print("Beyond-stem case photo frames:")
for i, m in enumerate(matches):
    print(f"{i+1}: data-src={m[0]} | img src={m[1]} | alt={m[2]}")

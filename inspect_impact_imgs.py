with open('impact.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="case-photo-frame[^"]*"[^>]*data-src="([^"]+)"[^>]*>.*?<img src="([^"]+)"[^>]*alt="([^"]*)"', text, re.DOTALL)
print("Impact case photo frames:")
for i, m in enumerate(matches):
    print(f"{i+1}: data-src={m[0]} | img src={m[1]} | alt={m[2]}")

stills = re.findall(r'<div class="still-item[^"]*"[^>]*data-src="([^"]+)"[^>]*>.*?<img src="([^"]+)"[^>]*alt="([^"]*)"', text, re.DOTALL)
print("Impact stills:")
for i, s in enumerate(stills):
    print(f"{i+1}: data-src={s[0]} | img src={s[1]} | alt={s[2]}")

with open('research.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
cases = re.findall(r'<section class="editorial-case-study".*?</section>', text, re.DOTALL)
print(f"Total cases in research.html: {len(cases)}")
for i, c in enumerate(cases):
    title = re.search(r'<h2 class="case-title">(.*?)</h2>', c)
    kicker = re.search(r'<p class="case-kicker">(.*?)</p>', c)
    img = re.search(r'<img src="([^"]+)"', c)
    print(f"Case {i+1}:")
    print(f"  kicker: {kicker.group(1) if kicker else ''}")
    print(f"  title: {title.group(1) if title else ''}")
    print(f"  img: {img.group(1) if img else ''}")

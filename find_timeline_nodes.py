with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pattern = r'<div class="timeline-milestone-node">.*?</div>\s*(?=<div class="timeline-milestone-node"|</div>\s*</div>\s*</section>)'
matches = re.findall(pattern, text, re.DOTALL)
print(f"Total nodes: {len(matches)}")
for i, m in enumerate(matches):
    year = re.search(r'<span class="timeline-year-pill">(.*?)</span>', m)
    title = re.search(r'<h3 class="timeline-node-title">(.*?)</h3>', m)
    print(f"Node {i+1}: {year.group(1) if year else ''} - {title.group(1) if title else ''}")

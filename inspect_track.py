with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<div class="gallery-carousel-track">.*?</div>\s*<button class="carousel-btn carousel-next")', text, re.DOTALL)
if m:
    print(m.group(1))

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('class="evidence-card"')
print(text[idx:idx+1500])

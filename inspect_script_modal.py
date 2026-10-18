with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'modal', text, re.I)]
for m in matches:
    print(text[m-20:m+200])
    print('---'*10)

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<section[^>]*id="evidenceVault".*?</section>)', text, re.DOTALL)
if m:
    print(m.group(1)[:2500])

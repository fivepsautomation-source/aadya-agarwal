with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<section[^>]*id="evidenceVault".*?</section>', text, re.DOTALL)
vault = m.group(0)

parts = vault.split('<div class="evidence-card" data-category="')[1:]

for idx in [11, 16, 18, 22]: # 0-indexed for 12, 17, 19, 23
    print(f"=== CARD #{idx+1} ===")
    print('<div class="evidence-card" data-category="' + parts[idx][:800])

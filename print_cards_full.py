with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<section[^>]*id="evidenceVault".*?</section>', text, re.DOTALL)
vault = m.group(0)
parts = vault.split('<div class="evidence-card" data-category="')[1:]

for idx in [11, 16, 18, 22]:
    print(f"=== FULL CARD #{idx+1} ===")
    p = parts[idx]
    # find where this card ends (before next card or section close)
    end_idx = p.find('<div class="evidence-card"')
    if end_idx == -1:
        end_idx = p.find('</div>\n        </div>\n      </div>')
    print('<div class="evidence-card" data-category="' + p[:end_idx].strip())

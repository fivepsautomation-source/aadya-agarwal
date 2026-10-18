with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<section[^>]*id="evidenceVault".*?</section>', text, re.DOTALL)
if not m:
    print("evidenceVault not found")
    exit()

vault_html = m.group(0)

# Find all cards
cards = re.findall(r'<div class="evidence-card".*?</div>\s*</div>\s*</div>', vault_html, re.DOTALL)
print(f"Total evidence cards found: {len(cards)}")

card_images = []
# Match each card's src and title
pattern = r'data-category="([^"]+)".*?data-title="([^"]+)".*?src="([^"]+)".*?<h4 class="evidence-card-title">([^<]+)</h4>'
matches = re.findall(r'<div class="evidence-card"[^>]*data-category="([^"]+)"[^>]*>.*?<img src="([^"]+)"[^>]*>.*?<h4 class="evidence-card-title">([^<]+)</h4>', vault_html, re.DOTALL)

print(f"Matched cards: {len(matches)}")
seen = {}
duplicates = []
for i, (cat, src, title) in enumerate(matches):
    print(f"{i+1}. [{cat}] {title} -> {src}")
    if src in seen:
        duplicates.append((src, seen[src], title))
    else:
        seen[src] = title

print("\n--- DUPLICATES FOUND ---")
for src, first, second in duplicates:
    print(f"DUPLICATE: '{src}' used in:")
    print(f"   1. {first}")
    print(f"   2. {second}")

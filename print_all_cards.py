with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<section[^>]*id="evidenceVault".*?</section>', text, re.DOTALL)
vault = m.group(0)

parts = vault.split('<div class="evidence-card" data-category="')[1:]
print(f"Total parts split: {len(parts)}")

seen_src = {}
duplicates = []

for i, p in enumerate(parts):
    cat = p.split('"')[0]
    img_match = re.search(r'<img[^>]*src="([^"]+)"', p)
    title_match = re.search(r'<h4[^>]*class="evidence-item-title"[^>]*>([^<]+)</h4>', p)
    src = img_match.group(1) if img_match else "NO_IMG"
    title = title_match.group(1).strip() if title_match else "NO_TITLE"
    print(f"{i+1:2d}. [{cat:12s}] {title:45s} -> {src}")
    if src in seen_src:
        duplicates.append((src, seen_src[src], title, i+1))
    else:
        seen_src[src] = (title, i+1)

print("\n--- DUPLICATES FOUND ---")
for src, (first_title, first_idx), sec_title, sec_idx in duplicates:
    print(f"DUPLICATE SRC: {src}")
    print(f"   Card #{first_idx}: {first_title}")
    print(f"   Card #{sec_idx}: {sec_title}")

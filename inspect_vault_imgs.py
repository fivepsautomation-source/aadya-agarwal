with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<section[^>]*id="evidenceVault".*?</section>', text, re.DOTALL)
if m:
    vault = m.group(0)
    # find all img tags inside evidenceVault
    imgs = re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', vault)
    print(f"Total img tags in evidenceVault: {len(imgs)}")
    seen = {}
    dups = []
    for i, (src, alt) in enumerate(imgs):
        print(f"{i+1}: {src} (alt: {alt})")
        if src in seen:
            dups.append((src, seen[src], alt))
        else:
            seen[src] = alt
    print("\n--- DUPLICATES ---")
    for src, a1, a2 in dups:
        print(f"Duplicate image: {src}")
        print(f"  First used for: {a1}")
        print(f"  Second used for: {a2}")

import os
import glob
import re

html_files = [
    'index.html', 'about.html', 'projects.html', 'research.html', 
    'impact.html', 'beyond-stem.html', 'contact.html', 'robotics.html',
    'academics.html', 'community.html', 'speaking-writing.html', 'arts-athletics.html'
]

print("=== CHECKING ALL HTML FILES FOR CONSECUTIVE DUPLICATES AND MISSING FILES ===")

total_missing = 0
total_consecutive = 0

for fn in html_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all <img> tags and their src in order of appearance
    img_matches = re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', content)
    evidence_matches = re.findall(r'data-src="([^"]+)"', content)
    
    print(f"\n--- {fn} (Total img tags: {len(img_matches)}, data-src: {len(evidence_matches)}) ---")
    
    # Check consecutive images
    consecutive_found = False
    for i in range(len(img_matches) - 1):
        src1, alt1 = img_matches[i]
        src2, alt2 = img_matches[i+1]
        if src1 == src2:
            print(f"  [CONSECUTIVE DUPLICATE] #{i+1} & #{i+2}: '{src1}' (Alt1: '{alt1}', Alt2: '{alt2}')")
            total_consecutive += 1
            consecutive_found = True
    if not consecutive_found:
        print("  [OK] Zero consecutive duplicate images.")
        
    # Check physical existence of all referenced files
    all_refs = set([src for src, _ in img_matches] + evidence_matches)
    missing_refs = []
    for ref in all_refs:
        if ref.startswith('http') or ref.startswith('#'):
            continue
        clean_ref = ref.split('?')[0].split('#')[0]
        if not os.path.exists(clean_ref):
            missing_refs.append(clean_ref)
            total_missing += 1
            
    if missing_refs:
        print(f"  [MISSING 404 ASSETS]: {missing_refs}")
    else:
        print(f"  [OK] All {len(all_refs)} asset files physically exist on disk (200 OK).")

print(f"\n=======================================================")
print(f"AUDIT SUMMARY: Total consecutive duplicates = {total_consecutive}, Total missing files = {total_missing}")
print(f"=======================================================")

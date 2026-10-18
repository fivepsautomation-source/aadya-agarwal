import os
import glob
import re

html_files = glob.glob('*.html')

pattern = re.compile(
    r'(?:\s*<!--\s*Admissions Top Bar\s*-->)*\s*<div class="admissions-top-bar">.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

# Also fallback pattern in case of slight variance
pattern2 = re.compile(
    r'(?:\s*<!--\s*Admissions Top Bar\s*-->)*\s*<div class="admissions-top-bar">.*?</div>\s*</div>',
    re.DOTALL
)

for fn in html_files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = pattern.subn('', content)
    if count == 0:
        new_content, count = pattern2.subn('', content)
    
    if count > 0:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"SUCCESS: Removed top bar from {fn} (removed {count} occurrence(s))")
    else:
        if 'admissions-top-bar' in content:
            print(f"WARNING: admissions-top-bar still found in {fn} but regex did not match!")
        else:
            print(f"No top bar found in {fn}")

# Also update build_master_pages.py
with open('build_master_pages.py', 'r', encoding='utf-8') as f:
    bmp_content = f.read()

new_bmp, count_bmp = pattern.subn('', bmp_content)
if count_bmp == 0:
    new_bmp, count_bmp = pattern2.subn('', bmp_content)

if count_bmp > 0:
    with open('build_master_pages.py', 'w', encoding='utf-8') as f:
        f.write(new_bmp)
    print(f"SUCCESS: Removed top bar from build_master_pages.py (removed {count_bmp} occurrence(s))")
else:
    print("No top bar in build_master_pages.py or regex did not match")

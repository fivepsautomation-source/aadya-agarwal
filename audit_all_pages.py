import os
import glob
import re

html_files = glob.glob('*.html')

print("=== AUDITING ALL HTML PAGES FOR BROKEN IMAGES & SYNTAX ===")

for fn in sorted(html_files):
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Check all image paths
    imgs = re.findall(r'<img[^>]*src="([^"]+)"', html)
    missing_imgs = [src for src in imgs if not os.path.exists(src)]
    
    # 2. Check all data-src paths
    data_srcs = re.findall(r'data-src="([^"]+)"', html)
    missing_data = [src for src in data_srcs if not os.path.exists(src)]
    
    # 3. Check tags
    div_opens = len(re.findall(r'<div\b', html))
    div_closes = len(re.findall(r'</div>', html))
    
    section_opens = len(re.findall(r'<section\b', html))
    section_closes = len(re.findall(r'</section>', html))
    
    print(f"\n{fn}:")
    print(f"  Images total: {len(imgs)} | Missing images: {len(missing_imgs)}")
    if missing_imgs:
        print(f"    MISSING: {missing_imgs}")
    print(f"  Data-src total: {len(data_srcs)} | Missing data-src: {len(missing_data)}")
    if missing_data:
        print(f"    MISSING DATA: {missing_data}")
    print(f"  Divs: {div_opens} open, {div_closes} close | Sections: {section_opens} open, {section_closes} close")
    if div_opens != div_closes:
        print(f"  [MISMATCH] Div tag mismatch by {div_opens - div_closes}!")
    if section_opens != section_closes:
        print(f"  [MISMATCH] Section tag mismatch by {section_opens - section_closes}!")

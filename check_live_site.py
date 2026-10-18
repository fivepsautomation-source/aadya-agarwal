import urllib.request
import re

req = urllib.request.Request('https://aadyaagarwal.com/', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    
    print("Found text matches:")
    for m in re.finditer(r'(Hello|Durga|primaeval|Fun Facts|energy)', html, re.I):
        s = max(0, m.start() - 150)
        e = min(len(html), m.end() + 250)
        print(html[s:e])
        print("="*40)
        
    imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
    print("\nAll images on page:")
    for img in imgs:
        print(img)
except Exception as e:
    print("Error:", e)

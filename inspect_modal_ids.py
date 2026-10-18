with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("IDs with modal/media/evidence:")
print(re.findall(r'id=["\']([^"\']*(?:modal|media|evidence)[^"\']*)["\']', text, re.I))

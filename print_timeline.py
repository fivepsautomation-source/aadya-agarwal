with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<section[^>]*id="timeline".*?</section>)', text, re.DOTALL)
if m:
    print(m.group(1))

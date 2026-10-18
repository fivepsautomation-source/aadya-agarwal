with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="timeline"')
if idx != -1:
    print(text[idx-50:idx+2000])
else:
    print("timeline id not found")

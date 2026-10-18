with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('openMediaModal')
print(text[idx:idx+1500])

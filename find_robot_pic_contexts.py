with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'pic 1 - with robot.jpg' in l:
        print(f"Line {i+1}: {l.strip()[:120]}")
        # print surrounding 3 lines
        for j in range(max(0, i-2), min(len(lines), i+3)):
            print(f"   {j+1}: {lines[j].strip()[:100]}")
        print('-'*30)

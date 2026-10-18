with open('build_master_pages.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'Receiving THE JOHN H IMBRIE' in l:
        print(f"Line {i+1}:")
        for j in range(max(0, i-4), min(len(lines), i+5)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        print('='*40)

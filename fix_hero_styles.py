with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Ensure .inner-page-hero has high z-index
css = css.replace(
    '.inner-page-hero {\n  background: linear-gradient(180deg, #F8F8F8 0%, #EFE8DE 100%);\n  border-bottom: 1px solid rgba(62, 69, 44, 0.12);\n  padding: 130px 0 60px;\n  position: relative;\n}',
    '.inner-page-hero {\n  background: linear-gradient(180deg, #F8F8F8 0%, #EFE8DE 100%);\n  border-bottom: 1px solid rgba(62, 69, 44, 0.12);\n  padding: 130px 0 60px;\n  position: relative;\n  z-index: 50;\n}'
)

# 2. Add invisible hover bridge ::before and improve panel positioning
bridge_fix = '''
/* Invisible hover bridge to prevent any gap flicker */
.hero-dropdown-panel::before {
  content: "";
  position: absolute;
  top: -18px;
  left: 0;
  right: 0;
  height: 18px;
  background: transparent;
}
'''

if 'Invisible hover bridge' not in css:
    css = css.replace('.hero-dropdown-panel {', bridge_fix + '\n.hero-dropdown-panel {')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: styles.css updated with z-index and hover bridge!")

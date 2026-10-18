with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .curated-visual-frame img
css = css.replace(
    '''.curated-visual-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: opacity 0.35s ease, transform 0.6s ease;
}''',
    '''.curated-visual-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  display: block;
  transition: opacity 0.35s ease, transform 0.6s ease;
}'''
)

# 2. Update .gallery-carousel-track .gallery-card img
css = css.replace(
    '''.gallery-carousel-track .gallery-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease;
}''',
    '''.gallery-carousel-track .gallery-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  display: block;
  transition: transform 0.6s ease;
}'''
)

# 3. Add universal rule for the robotics holding photo across all sections and pages
global_fix = '''
/* ==========================================================================
   ROBOTICS PHOTO FRAMING FIX (Never crop Aadya's face or robot)
   ========================================================================== */
img[src*="pic 1 - with robot"],
img[src*="pic%201%20-%20with%20robot"],
.gallery-card img[src*="pic 1"],
.curated-visual-frame img[src*="pic 1"],
.hero-slide img[src*="pic 1"],
.expanding-strip-panel img[src*="pic 1"],
.evidence-thumb-img[src*="pic 1"] {
  object-position: top center !important;
}
'''

if 'ROBOTICS PHOTO FRAMING FIX' not in css:
    css += '\n' + global_fix
    print("SUCCESS: Appended global robotics photo framing fix!")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: styles.css updated!")

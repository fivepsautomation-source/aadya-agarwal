sticky_css = '''
/* ==========================================================================
   STICKY EDITORIAL SHOWCASE (Inspired by rituguptagarg.in)
   Image sticks on the side while rich text and points scroll past
   ========================================================================== */
.editorial-sticky-showcase {
  padding: 110px 0;
  background: #fbf9f5;
  border-top: 1px solid rgba(62, 69, 44, 0.12);
  border-bottom: 1px solid rgba(62, 69, 44, 0.12);
  position: relative;
}

.editorial-sticky-showcase .case-study-grid {
  display: grid;
  grid-template-columns: 5fr 7fr;
  gap: 68px;
  align-items: start !important; /* Required for sticky */
}

/* Left Sticky Column */
.sticky-photo-column {
  position: -webkit-sticky;
  position: sticky;
  top: 105px; /* Clear sticky header */
  align-self: start;
  z-index: 20;
}

.sticky-photo-frame {
  background: #ffffff;
  padding: 16px;
  border-radius: 20px;
  border: 1px solid rgba(62, 69, 44, 0.14);
  box-shadow: 0 20px 48px rgba(10, 34, 24, 0.10), 0 4px 14px rgba(0, 0, 0, 0.04);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
  cursor: pointer;
}

.sticky-photo-frame:hover {
  transform: translateY(-4px);
  box-shadow: 0 28px 64px rgba(10, 34, 24, 0.15);
}

.sticky-photo-frame img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  display: block;
  object-fit: cover;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
}

.sticky-photo-meta {
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid rgba(62, 69, 44, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.sticky-photo-tag {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--c-forest);
}

.sticky-photo-zoom {
  font-family: var(--font-heading);
  font-size: 0.78rem;
  font-weight: 600;
  color: #71717a;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  transition: color 0.2s ease;
}

.sticky-photo-frame:hover .sticky-photo-zoom {
  color: var(--c-dark-slate);
}

/* Right Scrolling Content Column */
.scrolling-content-copy {
  display: flex;
  flex-direction: column;
}

.scrolling-top-line {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.scrolling-line-rule {
  height: 2px;
  width: 48px;
  background: var(--c-forest);
}

.scrolling-line-text {
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--c-dark-olive);
}

.scrolling-title {
  font-family: var(--font-serif);
  font-size: clamp(2.3rem, 4vw, 3.3rem);
  font-weight: 700;
  color: var(--c-dark-slate);
  line-height: 1.15;
  letter-spacing: -0.02em;
  margin-bottom: 12px;
}

.scrolling-subtitle {
  font-family: var(--font-serif);
  font-size: 1.15rem;
  font-style: italic;
  color: var(--c-forest);
  margin-bottom: 24px;
  line-height: 1.5;
}

.scrolling-lead {
  font-size: 1.04rem;
  line-height: 1.75;
  color: #3f3f46;
  margin-bottom: 24px;
}

.scrolling-lead strong {
  color: var(--c-dark-slate);
}

/* Styled Points List */
.scrolling-points-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin: 10px 0 32px;
}

.scrolling-point-item {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  padding: 16px 20px;
  background: #ffffff;
  border: 1px solid rgba(62, 69, 44, 0.10);
  border-radius: 14px;
  box-shadow: 0 2px 8px rgba(10, 34, 24, 0.03);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.scrolling-point-item:hover {
  border-color: rgba(48, 96, 40, 0.3);
  box-shadow: 0 8px 24px rgba(10, 34, 24, 0.07);
  transform: translateX(4px);
}

.point-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--c-forest);
  margin-top: 7px;
  flex-shrink: 0;
  box-shadow: 0 0 0 3px rgba(48, 96, 40, 0.15);
}

.point-text {
  font-size: 0.94rem;
  line-height: 1.65;
  color: #3f3f46;
}

.point-text strong {
  color: var(--c-dark-slate);
  font-weight: 700;
}

.point-text em {
  font-style: italic;
  color: var(--c-forest);
}

/* Actions at bottom */
.scrolling-actions {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-top: 10px;
  flex-wrap: wrap;
}

@media (max-width: 960px) {
  .editorial-sticky-showcase .case-study-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .sticky-photo-column {
    position: static;
    max-width: 480px;
  }
}
'''

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'STICKY EDITORIAL SHOWCASE' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write('\n' + sticky_css)
    print("SUCCESS: Sticky showcase CSS added to styles.css!")
else:
    print("CSS already exists in styles.css")

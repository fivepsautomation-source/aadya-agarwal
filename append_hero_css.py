hero_dropdown_css = '''
/* ==========================================================================
   ABOUT PAGE HERO INTERACTIVE BUTTONS & MEGA-DROPDOWNS
   ========================================================================== */
.hero-interactive-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-top: 36px;
  margin-bottom: 8px;
  position: relative;
  z-index: 100;
  flex-wrap: wrap;
}

.hero-dropdown-container {
  position: relative;
}

/* Interactive Pill Trigger Buttons */
.hero-interactive-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #ffffff;
  border: 1px solid rgba(62, 69, 44, 0.22);
  border-radius: 9999px;
  padding: 13px 24px;
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--c-dark-slate);
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(10, 34, 24, 0.06);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  user-select: none;
  text-decoration: none;
}

.hero-btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(62, 69, 44, 0.08);
  color: var(--c-forest);
  transition: all 0.25s ease;
}

.hero-btn-label {
  letter-spacing: -0.01em;
}

.hero-btn-count {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  padding: 3px 9px;
  border-radius: 999px;
  background: rgba(62, 69, 44, 0.08);
  color: var(--c-forest);
  transition: all 0.25s ease;
}

.hero-btn-chevron {
  color: #71717a;
  transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1), color 0.25s ease;
}

/* Hover & Active States */
.hero-interactive-btn:hover,
.hero-dropdown-container.is-open .hero-interactive-btn,
.hero-dropdown-container.intro-active .hero-interactive-btn {
  background: var(--c-dark-slate);
  color: #ffffff;
  border-color: var(--c-dark-slate);
  box-shadow: 0 10px 28px rgba(62, 69, 44, 0.25);
  transform: translateY(-2px);
}

.hero-interactive-btn:hover .hero-btn-icon,
.hero-dropdown-container.is-open .hero-interactive-btn .hero-btn-icon,
.hero-dropdown-container.intro-active .hero-interactive-btn .hero-btn-icon {
  background: rgba(192, 200, 82, 0.3);
  color: var(--c-writing);
}

.hero-interactive-btn:hover .hero-btn-count,
.hero-dropdown-container.is-open .hero-interactive-btn .hero-btn-count,
.hero-dropdown-container.intro-active .hero-interactive-btn .hero-btn-count {
  background: rgba(255, 255, 255, 0.18);
  color: #ffffff;
}

.hero-interactive-btn:hover .hero-btn-chevron,
.hero-dropdown-container.is-open .hero-interactive-btn .hero-btn-chevron,
.hero-dropdown-container.intro-active .hero-interactive-btn .hero-btn-chevron {
  color: #ffffff;
  transform: rotate(180deg);
}

/* Projects specific styling accents */
.hero-btn-projects:hover,
#heroProjectsContainer.is-open .hero-btn-projects {
  border-color: #306028;
}

/* Mega-Dropdown Panels */
.hero-dropdown-panel {
  position: absolute;
  top: calc(100% + 14px);
  left: 0;
  width: min(900px, 92vw);
  max-height: 72vh;
  overflow-y: auto;
  overflow-x: hidden;
  background: #ffffff;
  border: 1px solid rgba(62, 69, 44, 0.16);
  border-radius: 20px;
  padding: 28px;
  box-shadow: 0 24px 64px rgba(10, 34, 24, 0.18), 0 4px 16px rgba(0, 0, 0, 0.04);
  z-index: 120;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(14px) scale(0.98);
  transform-origin: top left;
  transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.3s cubic-bezier(0.16, 1, 0.3, 1),
              visibility 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  scrollbar-width: thin;
  scrollbar-color: rgba(62, 69, 44, 0.3) transparent;
}

.hero-dropdown-panel::-webkit-scrollbar {
  width: 6px;
}
.hero-dropdown-panel::-webkit-scrollbar-thumb {
  background: rgba(62, 69, 44, 0.25);
  border-radius: 999px;
}

/* Align right-side dropdown cleanly */
#heroAchievementsContainer .hero-dropdown-panel {
  left: auto;
  right: -80px;
  transform-origin: top right;
}
@media (max-width: 960px) {
  #heroAchievementsContainer .hero-dropdown-panel {
    left: 0;
    right: auto;
    transform-origin: top left;
  }
}

/* Panel Header */
.hero-panel-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  border-bottom: 1px solid rgba(62, 69, 44, 0.12);
  padding-bottom: 18px;
  margin-bottom: 22px;
}

.hero-panel-eyebrow {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--c-forest);
  margin-bottom: 4px;
}

.hero-panel-title {
  font-family: var(--font-serif);
  font-size: 1.45rem;
  font-weight: 700;
  color: var(--c-dark-slate);
  letter-spacing: -0.01em;
}

.hero-panel-all-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--c-forest);
  text-decoration: none;
  padding: 6px 14px;
  background: rgba(48, 96, 40, 0.08);
  border-radius: 999px;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.hero-panel-all-link:hover {
  background: var(--c-forest);
  color: #ffffff;
  transform: translateX(3px);
}

/* ==========================================================================
   PROJECTS MEGA-DROPDOWN GRID
   ========================================================================== */
.hero-projects-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
@media (max-width: 680px) {
  .hero-projects-grid {
    grid-template-columns: 1fr;
  }
}

.hero-proj-card {
  background: #fbfbf9;
  border: 1px solid rgba(62, 69, 44, 0.12);
  border-radius: 14px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-proj-card:hover {
  background: #ffffff;
  border-color: rgba(48, 96, 40, 0.35);
  box-shadow: 0 8px 24px rgba(10, 34, 24, 0.08);
  transform: translateY(-2px);
}

.hero-proj-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 10px;
}

.hero-proj-badge {
  font-family: var(--font-mono);
  font-size: 0.70rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 3px 8px;
  border-radius: 6px;
  background: rgba(48, 96, 40, 0.1);
  color: #24491e;
}
.hero-proj-badge.badge-robotics { background: rgba(56, 189, 248, 0.15); color: #0284c7; }
.hero-proj-badge.badge-water { background: rgba(48, 96, 40, 0.15); color: #1e4a1a; }
.hero-proj-badge.badge-health { background: rgba(225, 29, 72, 0.12); color: #be123c; }
.hero-proj-badge.badge-eco { background: rgba(192, 200, 82, 0.3); color: #4d540d; }
.hero-proj-badge.badge-ai { background: rgba(147, 51, 234, 0.12); color: #7e22ce; }
.hero-proj-badge.badge-genomics { background: rgba(13, 148, 136, 0.15); color: #0f766e; }
.hero-proj-badge.badge-hardware { background: rgba(234, 88, 12, 0.12); color: #c2410c; }
.hero-proj-badge.badge-civic { background: rgba(79, 70, 229, 0.12); color: #4338ca; }

.hero-proj-role {
  font-size: 0.74rem;
  font-weight: 600;
  color: #71717a;
}

.hero-proj-title {
  font-family: var(--font-heading);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--c-dark-slate);
  margin-bottom: 6px;
  letter-spacing: -0.01em;
}

.hero-proj-desc {
  font-size: 0.86rem;
  color: #52525b;
  line-height: 1.5;
  margin-bottom: 14px;
}

.hero-proj-links {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: auto;
  flex-wrap: wrap;
}

.hero-proj-nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: var(--font-heading);
  font-size: 0.80rem;
  font-weight: 700;
  text-decoration: none;
  padding: 6px 12px;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.hero-proj-nav-btn.primary {
  background: var(--c-forest);
  color: #ffffff;
}
.hero-proj-nav-btn.primary:hover {
  background: var(--c-dark-slate);
  transform: translateY(-1px);
}

.hero-proj-nav-btn.official {
  background: rgba(37, 99, 235, 0.12);
  color: #1d4ed8;
  border: 1px solid rgba(37, 99, 235, 0.25);
}
.hero-proj-nav-btn.official:hover {
  background: #1d4ed8;
  color: #ffffff;
  transform: translateY(-1px);
}

.hero-proj-nav-btn.secondary {
  color: #52525b;
  padding: 6px 8px;
}
.hero-proj-nav-btn.secondary:hover {
  color: var(--c-dark-slate);
  text-decoration: underline;
}

/* ==========================================================================
   ACHIEVEMENTS MEGA-DROPDOWN CATEGORIES
   ========================================================================== */
.hero-achieve-categories {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
@media (max-width: 820px) {
  .hero-achieve-categories {
    grid-template-columns: 1fr;
  }
}

.hero-achieve-col {
  background: #fbfbf9;
  border: 1px solid rgba(62, 69, 44, 0.10);
  border-radius: 14px;
  padding: 18px 16px;
}

.hero-col-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--c-dark-slate);
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(62, 69, 44, 0.12);
  margin-bottom: 12px;
}

.hero-col-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
.hero-col-dot.dot-robotics { background: #0284c7; }
.hero-col-dot.dot-water { background: #306028; }
.hero-col-dot.dot-arts { background: #c0c852; }

.hero-achieve-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.hero-achieve-item {
  border-bottom: 1px solid rgba(0, 0, 0, 0.04);
  padding-bottom: 10px;
}
.hero-achieve-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.achieve-item-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 6px;
  margin-bottom: 4px;
}

.achieve-title {
  font-family: var(--font-heading);
  font-size: 0.90rem;
  font-weight: 700;
  color: var(--c-dark-slate);
  line-height: 1.35;
}

.achieve-pill {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(62, 69, 44, 0.08);
  color: #3f3f46;
  white-space: nowrap;
}
.achieve-pill.pill-gold {
  background: rgba(192, 200, 82, 0.35);
  color: #4a510c;
  font-weight: 800;
}

.achieve-desc {
  font-size: 0.78rem;
  color: #71717a;
  line-height: 1.45;
}

/* ==========================================================================
   ENTRANCE CLOSING TEASER ANIMATION
   "drop down bnd hoti dikhni chiye upr phele project ki then achievements ki"
   ========================================================================== */
@keyframes peekAndCloseUp {
  0% {
    opacity: 0;
    visibility: visible;
    transform: translateY(14px) scale(0.98);
  }
  15% {
    opacity: 1;
    visibility: visible;
    transform: translateY(0) scale(1);
    box-shadow: 0 28px 72px rgba(10, 34, 24, 0.22);
  }
  75% {
    opacity: 1;
    visibility: visible;
    transform: translateY(0) scale(1);
  }
  100% {
    opacity: 0;
    visibility: hidden;
    transform: translateY(-16px) scale(0.97);
  }
}

.hero-dropdown-panel.intro-animating {
  animation: peekAndCloseUp 1.15s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  pointer-events: none;
}

/* Standard hover interaction once intro finishes or user hovers */
.hero-dropdown-container:hover .hero-dropdown-panel,
.hero-dropdown-container.is-open .hero-dropdown-panel {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateY(0) scale(1) !important;
  animation: none !important;
}
'''

with open('styles.css', 'r', encoding='utf-8') as f:
    existing_css = f.read()

# Check if already appended
if 'ABOUT PAGE HERO INTERACTIVE BUTTONS & MEGA-DROPDOWNS' not in existing_css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write('\n' + hero_dropdown_css)
    print("SUCCESS: Hero dropdown CSS appended to styles.css!")
else:
    print("CSS already present, skipping append.")

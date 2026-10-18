with open('script.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace initHeroInteractiveDropdowns with pure hover/click behavior, NO entrance animation
old_func_start = "/* ==========================================================================\n   ABOUT PAGE HERO INTERACTIVE BUTTONS & TEASER ENTRANCE ANIMATION\n   ========================================================================== */"
new_func = '''/* ==========================================================================
   ABOUT PAGE HERO INTERACTIVE BUTTONS (HOVER-ACTIVATED DROPDOWNS)
   ========================================================================== */
function initHeroInteractiveDropdowns() {
  const row = document.getElementById('heroInteractiveRow');
  const projContainer = document.getElementById('heroProjectsContainer');
  const achContainer = document.getElementById('heroAchievementsContainer');
  const projPanel = document.getElementById('heroProjectsPanel');
  const achPanel = document.getElementById('heroAchievementsPanel');
  const projTrigger = document.getElementById('heroProjectsTrigger');
  const achTrigger = document.getElementById('heroAchievementsTrigger');

  if (!row || !projContainer || !achContainer || !projPanel || !achPanel) return;

  // 1. Hover & Click Interactivity for Projects
  projContainer.addEventListener('mouseenter', () => {
    achContainer.classList.remove('is-open');
    if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
    projContainer.classList.add('is-open');
    if (projTrigger) projTrigger.setAttribute('aria-expanded', 'true');
  });

  projContainer.addEventListener('mouseleave', () => {
    projContainer.classList.remove('is-open');
    if (projTrigger) projTrigger.setAttribute('aria-expanded', 'false');
  });

  if (projTrigger) {
    projTrigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = projContainer.classList.contains('is-open');
      achContainer.classList.remove('is-open');
      if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
      projContainer.classList.toggle('is-open', !isOpen);
      projTrigger.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
    });
  }

  // 2. Hover & Click Interactivity for Achievements
  achContainer.addEventListener('mouseenter', () => {
    projContainer.classList.remove('is-open');
    if (projTrigger) projTrigger.setAttribute('aria-expanded', 'false');
    achContainer.classList.add('is-open');
    if (achTrigger) achTrigger.setAttribute('aria-expanded', 'true');
  });

  achContainer.addEventListener('mouseleave', () => {
    achContainer.classList.remove('is-open');
    if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
  });

  if (achTrigger) {
    achTrigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = achContainer.classList.contains('is-open');
      projContainer.classList.remove('is-open');
      if (projTrigger) projTrigger.setAttribute('aria-expanded', 'false');
      achContainer.classList.toggle('is-open', !isOpen);
      achTrigger.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
    });
  }

  // 3. Close when clicking outside or pressing Escape
  document.addEventListener('click', (e) => {
    if (!projContainer.contains(e.target) && !achContainer.contains(e.target)) {
      projContainer.classList.remove('is-open');
      achContainer.classList.remove('is-open');
      if (projTrigger) projTrigger.setAttribute('aria-expanded', 'false');
      if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      projContainer.classList.remove('is-open');
      achContainer.classList.remove('is-open');
      if (projTrigger) projTrigger.setAttribute('aria-expanded', 'false');
      if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
    }
  });
}
'''

idx = code.find(old_func_start)
if idx != -1:
    code = code[:idx] + new_func
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print("SUCCESS: script.js updated to remove entrance animation and keep pure hover/click!")
else:
    print("Could not find old_func_start in script.js")

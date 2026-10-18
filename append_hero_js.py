hero_js = '''
/* ==========================================================================
   ABOUT PAGE HERO INTERACTIVE BUTTONS & TEASER ENTRANCE ANIMATION
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

  let introTimeouts = [];

  function cancelIntroAnimation() {
    introTimeouts.forEach(t => clearTimeout(t));
    introTimeouts = [];
    projPanel.classList.remove('intro-animating');
    projContainer.classList.remove('intro-active');
    achPanel.classList.remove('intro-animating');
    achContainer.classList.remove('intro-active');
    row.dataset.introDone = 'true';
  }

  // 1. Entrance Sequenced Animation
  // First Projects dropdown opens and tucks closed upward, then Achievements does the same!
  introTimeouts.push(setTimeout(() => {
    if (row.dataset.introDone === 'true') return;
    projContainer.classList.add('intro-active');
    projPanel.classList.add('intro-animating');
  }, 450));

  introTimeouts.push(setTimeout(() => {
    if (row.dataset.introDone === 'true') return;
    projContainer.classList.remove('intro-active');
    projPanel.classList.remove('intro-animating');
  }, 1600));

  introTimeouts.push(setTimeout(() => {
    if (row.dataset.introDone === 'true') return;
    achContainer.classList.add('intro-active');
    achPanel.classList.add('intro-animating');
  }, 1900));

  introTimeouts.push(setTimeout(() => {
    if (row.dataset.introDone === 'true') return;
    achContainer.classList.remove('intro-active');
    achPanel.classList.remove('intro-animating');
    row.dataset.introDone = 'true';
  }, 3050));

  // 2. Hover & Click Interactivity for Projects
  projContainer.addEventListener('mouseenter', () => {
    cancelIntroAnimation();
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
      cancelIntroAnimation();
      const isOpen = projContainer.classList.contains('is-open');
      achContainer.classList.remove('is-open');
      if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
      projContainer.classList.toggle('is-open', !isOpen);
      projTrigger.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
    });
  }

  // 3. Hover & Click Interactivity for Achievements
  achContainer.addEventListener('mouseenter', () => {
    cancelIntroAnimation();
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
      cancelIntroAnimation();
      const isOpen = achContainer.classList.contains('is-open');
      projContainer.classList.remove('is-open');
      if (projTrigger) projTrigger.setAttribute('aria-expanded', 'false');
      achContainer.classList.toggle('is-open', !isOpen);
      achTrigger.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
    });
  }

  // Close when clicking outside or pressing Escape
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

with open('script.js', 'r', encoding='utf-8') as f:
    existing_js = f.read()

if 'initHeroInteractiveDropdowns' not in existing_js:
    # also call initHeroInteractiveDropdowns() in DOMContentLoaded
    updated_js = existing_js.replace(
        'initEvidenceModal();',
        'initEvidenceModal();\n  initHeroInteractiveDropdowns();'
    )
    updated_js += '\n' + hero_js
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(updated_js)
    print("SUCCESS: initHeroInteractiveDropdowns added to script.js!")
else:
    print("Function already in script.js, skipping.")

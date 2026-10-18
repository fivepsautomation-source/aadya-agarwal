/* ==========================================================================
   AADYA AGARWAL — AWARD-WINNING CINEMA STAGE & SLIDER INTERACTION
   Story-style progress tabs, modal lightbox & live sensor telemetry
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initHeroShowcase();
  initHeaderScroll();
  initModal();
  initTelemetrySimulator();
});

/* ==========================================================================
   AWARDS & RESEARCH HERO SHOWCASE STAGE CONTROLLER
   Smooth 6-discipline auto-cycle, live progress fills, tabs & touch navigation
   ========================================================================== */
function initHeroShowcase() {
  const section = document.getElementById('heroShowcase') || document.getElementById('heroSlider');
  if (!section) return;

  const slides = section.querySelectorAll('.showcase-slide, .hero-slide');
  const tabs = section.querySelectorAll('.showcase-tab-btn, .story-tab-btn');
  const dots = section.querySelectorAll('.hero-dot');
  const prevBtn = document.getElementById('showcasePrevBtn') || document.getElementById('heroPrevBtn');
  const nextBtn = document.getElementById('showcaseNextBtn') || document.getElementById('heroNextBtn');

  if (!slides.length) return;

  let currentIndex = 0;
  let progress = 0;
  let timerInterval = null;
  const slideDuration = 3000; // 3.0s per slide
  const stepTime = 40;       // 25 fps smooth progress
  const stepIncrement = (stepTime / slideDuration) * 100;
  let isPaused = false;

  function showSlide(index) {
    if (index >= slides.length) index = 0;
    if (index < 0) index = slides.length - 1;
    currentIndex = index;
    progress = 0;

    // Toggle active slide
    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === currentIndex);
    });

    // Toggle indicator dots
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentIndex);
    });

    // Update story tabs & reset their progress fills
    tabs.forEach((tab, i) => {
      tab.classList.toggle('active', i === currentIndex);
      const fill = tab.querySelector('.showcase-tab-fill, .story-tab-progress');
      if (fill) {
        if (i < currentIndex) {
          fill.style.width = '100%';
        } else {
          fill.style.width = '0%';
        }
      }
    });
  }

  function startTimer() {
    stopTimer();
    timerInterval = setInterval(() => {
      if (!isPaused) {
        progress += stepIncrement;
        const activeTab = tabs[currentIndex];
        if (activeTab) {
          const fill = activeTab.querySelector('.showcase-tab-fill, .story-tab-progress');
          if (fill) {
            fill.style.width = Math.min(progress, 100) + '%';
          }
        }
        if (progress >= 100) {
          showSlide(currentIndex + 1);
        }
      }
    }, stepTime);
  }

  function stopTimer() {
    if (timerInterval) {
      clearInterval(timerInterval);
      timerInterval = null;
    }
  }

  // Next / Prev button events
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      showSlide(currentIndex + 1);
      startTimer();
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      showSlide(currentIndex - 1);
      startTimer();
    });
  }

  // Tab click events
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => {
      showSlide(i);
      startTimer();
    });
  });

  // Indicator dot click events
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      showSlide(i);
      startTimer();
    });
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (window.scrollY < 650) {
      if (e.key === 'ArrowRight') {
        showSlide(currentIndex + 1);
        startTimer();
      } else if (e.key === 'ArrowLeft') {
        showSlide(currentIndex - 1);
        startTimer();
      }
    }
  });

  // Touch Swipe support for mobile
  let touchStartX = 0;
  let touchEndX = 0;
  const theater = section.querySelector('.showcase-theater-box, .hero-slider-track');
  if (theater) {
    theater.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    theater.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) {
        showSlide(currentIndex + 1);
        startTimer();
      } else if (touchEndX - touchStartX > 50) {
        showSlide(currentIndex - 1);
        startTimer();
      }
    }, { passive: true });
  }

  // Pause on hover
  section.addEventListener('mouseenter', () => { isPaused = true; });
  section.addEventListener('mouseleave', () => { isPaused = false; });

  showSlide(0);
  startTimer();
}

/* ==========================================================================
   HEADER SCROLL SHADOW
   ========================================================================== */
function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

/* ==========================================================================
   AUTHENTIC MEDIA LIGHTBOX MODAL
   ========================================================================== */
function initModal() {
  const modal = document.getElementById('evidenceModal') || document.getElementById('mediaModal');
  if (modal) {
    const closeBtn = document.getElementById('modalClose') || modal.querySelector('.evidence-modal-close, .modal-close-btn');
    if (closeBtn) closeBtn.onclick = closeModal;
    const backdrop = document.getElementById('modalBackdrop');
    if (backdrop) backdrop.onclick = closeModal;
    modal.onclick = (e) => {
      if (e.target === modal) closeModal();
    };
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
  });

  // Delegated click handler for any zoomable item across the entire website
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('[data-zoom-src], .photo-gallery-card, .evidence-thumb-wrapper, .evidence-card');
    if (trigger) {
      // If trigger already had an inline onclick that called openMediaModal, don't duplicate
      const hasInline = trigger.getAttribute('onclick') && trigger.getAttribute('onclick').includes('openMediaModal');
      if (!hasInline) {
        const src = trigger.getAttribute('data-zoom-src') || trigger.querySelector('img')?.getAttribute('src');
        const title = trigger.getAttribute('data-zoom-title') || trigger.querySelector('h3, h4, .photo-gallery-caption h4, figcaption')?.textContent || 'Verified Portfolio Evidence';
        const desc = trigger.getAttribute('data-zoom-desc') || trigger.querySelector('p, .photo-gallery-caption p')?.textContent || '';
        const badge = trigger.getAttribute('data-zoom-badge') || trigger.querySelector('.photo-gallery-badge, .gallery-badge')?.textContent || 'Official Admissions Verification';
        const type = trigger.getAttribute('data-zoom-type') || (src && src.match(/\.(mp4|mov|webm)$/i) ? 'video' : 'image');
        if (src) {
          e.preventDefault();
          openMediaModal({ src, title, desc, badge, type });
        }
      }
    }
  });
}

function openMediaModal(data) {
  let modal = document.getElementById('evidenceModal') || document.getElementById('mediaModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'evidenceModal';
    modal.className = 'evidence-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.innerHTML = `
      <div class="evidence-modal-backdrop" id="modalBackdrop"></div>
      <div class="evidence-modal-container">
        <div class="evidence-modal-header">
          <div class="evidence-modal-title-group">
            <span class="evidence-modal-badge" id="modalBadge">Verification</span>
            <h3 class="evidence-modal-title" id="modalTitle">Evidence Preview</h3>
          </div>
          <button class="evidence-modal-close" id="modalClose" aria-label="Close modal">&times;</button>
        </div>
        <div class="evidence-modal-body" id="modalBody"></div>
        <div class="evidence-modal-footer">
          <span class="evidence-modal-caption" id="modalCaption"></span>
          <a href="#" id="modalDirectLink" target="_blank" rel="noopener noreferrer" class="evidence-modal-download-btn">Open Full Resolution &rarr;</a>
        </div>
      </div>
    `;
    document.body.appendChild(modal);
    const closeBtn = document.getElementById('modalClose');
    if (closeBtn) closeBtn.onclick = closeModal;
    const backdrop = document.getElementById('modalBackdrop');
    if (backdrop) backdrop.onclick = closeModal;
  }

  const title = document.getElementById('modalTitle');
  const caption = document.getElementById('modalCaption') || document.getElementById('modalDesc');
  const badge = document.getElementById('modalBadge');
  const holder = document.getElementById('modalBody') || document.getElementById('modalMediaHolder');
  const directLink = document.getElementById('modalDirectLink');

  if (title) title.textContent = data.title || 'Verified Milestone Evidence';
  if (caption) caption.textContent = data.desc || data.caption || '';
  if (badge) badge.textContent = data.badge || 'Official Admissions Verification';
  if (directLink && data.src) {
    directLink.href = data.src;
    directLink.style.display = 'inline-flex';
  }

  if (holder) {
    holder.innerHTML = '';
    if (data.type === 'video') {
      const video = document.createElement('video');
      video.src = data.src;
      video.controls = true;
      video.autoplay = true;
      video.playsInline = true;
      video.style.maxWidth = '100%';
      video.style.maxHeight = '65vh';
      video.style.borderRadius = '8px';
      holder.appendChild(video);
    } else {
      const img = document.createElement('img');
      img.src = data.src;
      img.alt = data.title || 'Portfolio Evidence';
      img.style.maxWidth = '100%';
      img.style.maxHeight = '65vh';
      img.style.objectFit = 'contain';
      img.style.borderRadius = '8px';
      img.style.boxShadow = '0 8px 30px rgba(0, 0, 0, 0.15)';
      holder.appendChild(img);
    }
  }

  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const modal = document.getElementById('evidenceModal') || document.getElementById('mediaModal');
  const holder = document.getElementById('modalBody') || document.getElementById('modalMediaHolder');
  if (modal) {
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (holder) {
      const video = holder.querySelector('video');
      if (video) video.pause();
      holder.innerHTML = '';
    }
  }
}
window.openMediaModal = openMediaModal;
window.closeModal = closeModal;

/* ==========================================================================
   LIVE IOT SENSOR SIMULATOR (MIT SOLVE BUOY)
   ========================================================================== */
function initTelemetrySimulator() {
  const tdsElem = document.getElementById('valTds');
  const phElem = document.getElementById('valPh');
  const tempElem = document.getElementById('valTemp');
  const doElem = document.getElementById('valDo');

  if (!tdsElem || !phElem) return;

  setInterval(() => {
    // Subtle realistic variations in water parameters
    const tds = (310 + Math.sin(Date.now() / 3000) * 8).toFixed(1);
    const ph = (7.42 + Math.cos(Date.now() / 4000) * 0.12).toFixed(2);
    const temp = (19.8 + Math.sin(Date.now() / 5000) * 0.4).toFixed(1);
    const dissolvedOxy = (8.4 + Math.cos(Date.now() / 3500) * 0.25).toFixed(2);

    tdsElem.textContent = `${tds} ppm`;
    phElem.textContent = `${ph} pH`;
    if (tempElem) tempElem.textContent = `${temp} °C`;
    if (doElem) doElem.textContent = `${dissolvedOxy} mg/L`;
  }, 1800);
}

/* ==========================================================================
   EVIDENCE VAULT FILTER LOGIC
   ========================================================================== */
function initEvidenceVault() {
  const filterBtns = document.querySelectorAll('.evidence-filter-btn');
  const cards = document.querySelectorAll('.evidence-card');

  if (!filterBtns.length || !cards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      cards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
          card.style.animation = 'fadeInUp 0.4s ease forwards';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   EVIDENCE MODAL LIGHTBOX FOR ALL EDITORIAL PAGES
   ========================================================================== */
function initEvidenceModal() {
  const modal = document.getElementById('evidenceModal');
  if (!modal) return;

  const closeBtn = document.getElementById('modalClose');
  const backdrop = document.getElementById('modalBackdrop');
  const title = document.getElementById('modalTitle');
  const badge = document.getElementById('modalBadge');
  const caption = document.getElementById('modalCaption');
  const body = document.getElementById('modalBody');
  const directLink = document.getElementById('modalDirectLink');

  function openEvidence(src, t, type, b, cap) {
    if (!body) return;
    title.textContent = t || 'Milestone Evidence Preview';
    badge.textContent = b || 'Verified Milestone';
    caption.textContent = cap || '';
    directLink.href = src;

    body.innerHTML = '';
    if (type === 'video') {
      const v = document.createElement('video');
      v.src = src;
      v.controls = true;
      v.autoplay = true;
      v.style.maxWidth = '100%';
      v.style.maxHeight = '65vh';
      v.style.borderRadius = '8px';
      body.appendChild(v);
    } else if (type === 'pdf') {
      const iframe = document.createElement('iframe');
      iframe.src = src;
      iframe.style.width = '100%';
      iframe.style.height = '65vh';
      iframe.style.border = 'none';
      iframe.style.borderRadius = '8px';
      body.appendChild(iframe);
    } else {
      const img = document.createElement('img');
      img.src = src;
      img.alt = t || 'Evidence Preview';
      img.style.maxWidth = '100%';
      img.style.maxHeight = '65vh';
      img.style.objectFit = 'contain';
      img.style.borderRadius = '8px';
      body.appendChild(img);
    }

    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  window.openEvidenceGlobal = openEvidence;
  window.openMediaModal = function(opts) {
    if (!opts) return;
    openEvidence(opts.src, opts.title, opts.type || 'image', opts.badge, opts.desc || opts.caption);
  };

  function closeEvidence() {
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (body) {
      const v = body.querySelector('video');
      if (v) v.pause();
      body.innerHTML = '';
    }
  }

  if (closeBtn) closeBtn.addEventListener('click', closeEvidence);
  if (backdrop) backdrop.addEventListener('click', closeEvidence);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeEvidence();
    }
  });

  document.addEventListener('click', (e) => {
    const link = e.target.closest('.evidence-link');
    if (link) {
      const src = link.getAttribute('data-src') || link.getAttribute('href');
      const t = link.getAttribute('data-title') || link.textContent;
      const type = link.getAttribute('data-type') || 'image';
      const b = link.getAttribute('data-badge') || 'Evidence';
      const cap = link.getAttribute('data-caption') || '';

      if (src && (src.endsWith('.jpg') || src.endsWith('.jpeg') || src.endsWith('.png') || src.endsWith('.pdf') || src.endsWith('.mp4') || src.endsWith('.webm'))) {
        e.preventDefault();
        openEvidence(src, t, type, b, cap);
      }
    }
  });
}

/* ==========================================================================
   DROPDOWN MENU ENHANCEMENT
   ========================================================================== */
function initDropdownMenus() {
  const items = document.querySelectorAll('.nav-dropdown-item');
  items.forEach(item => {
    const trigger = item.querySelector('.dropdown-trigger');
    if (!trigger) return;

    trigger.addEventListener('click', (e) => {
      if (window.innerWidth <= 1024 || e.target.closest('.dropdown-arrow')) {
        e.preventDefault();
        const isOpen = item.classList.contains('is-open');
        items.forEach(other => other.classList.remove('is-open'));
        if (!isOpen) item.classList.add('is-open');
      }
    });

    item.addEventListener('mouseenter', () => {
      item.classList.add('is-open');
    });

    item.addEventListener('mouseleave', () => {
      item.classList.remove('is-open');
    });
  });

  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-dropdown-item')) {
      items.forEach(item => item.classList.remove('is-open'));
    }
  });
}
/* Interactive Curated Tabs (eternallesagaproductions.com style) */
function initCuratedShowcase() {
  const tabs = document.querySelectorAll('.curated-tab-item');
  const frameImg = document.querySelector('.curated-visual-frame img');
  const floatTitle = document.querySelector('.curated-floating-title');
  const floatText = document.querySelector('.curated-floating-text');

  if (!tabs.length || !frameImg) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const img = tab.getAttribute('data-image');
      const title = tab.getAttribute('data-title');
      const desc = tab.getAttribute('data-desc');

      frameImg.style.opacity = '0';
      setTimeout(() => {
        if (img) frameImg.src = img;
        if (floatTitle && title) floatTitle.textContent = title;
        if (floatText && desc) floatText.textContent = desc;
        frameImg.style.opacity = '1';
      }, 200);
    });
  });
}

/* Gallery Carousel Navigation */
function initGalleryCarousel() {
  const carousels = document.querySelectorAll('.project-gallery-carousel-section, .editorial-stills-section');
  carousels.forEach(carousel => {
    const track = carousel.querySelector('.gallery-carousel-track, .carousel-track');
    const prevBtn = carousel.querySelector('.carousel-prev');
    const nextBtn = carousel.querySelector('.carousel-next');

    if (!track) return;

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        track.scrollBy({ left: -340, behavior: 'smooth' });
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        track.scrollBy({ left: 340, behavior: 'smooth' });
      });
    }
  });
}

/* Expanding Strips Accordion */
function initExpandingStrips() {
  const panels = document.querySelectorAll('.expanding-strip-panel');
  if (!panels.length) return;

  panels.forEach(panel => {
    panel.addEventListener('mouseenter', () => {
      panels.forEach(p => p.classList.remove('active'));
      panel.classList.add('active');
    });

    panel.addEventListener('click', () => {
      panels.forEach(p => p.classList.remove('active'));
      panel.classList.add('active');
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initEvidenceVault();
  initEvidenceModal();
  initHeroInteractiveDropdowns();
  initDropdownMenus();
  initCuratedShowcase();
  initGalleryCarousel();
  initExpandingStrips();
});


/* ==========================================================================
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

  let projTimer = null;
  let achTimer = null;

  // 1. Hover & Click Interactivity for Projects
  projContainer.addEventListener('mouseenter', () => {
    if (projTimer) {
      clearTimeout(projTimer);
      projTimer = null;
    }
    if (achTimer) {
      clearTimeout(achTimer);
      achTimer = null;
    }
    achContainer.classList.remove('is-open');
    if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
    projContainer.classList.add('is-open');
    if (projTrigger) projTrigger.setAttribute('aria-expanded', 'true');
  });

  projContainer.addEventListener('mouseleave', () => {
    projTimer = setTimeout(() => {
      projContainer.classList.remove('is-open');
      if (projTrigger) projTrigger.setAttribute('aria-expanded', 'false');
    }, 150);
  });

  if (projTrigger) {
    projTrigger.addEventListener('click', (e) => {
      e.stopPropagation();
      if (projTimer) clearTimeout(projTimer);
      if (achTimer) clearTimeout(achTimer);
      const isOpen = projContainer.classList.contains('is-open');
      achContainer.classList.remove('is-open');
      if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
      projContainer.classList.toggle('is-open', !isOpen);
      projTrigger.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
    });
  }

  // 2. Hover & Click Interactivity for Achievements
  achContainer.addEventListener('mouseenter', () => {
    if (achTimer) {
      clearTimeout(achTimer);
      achTimer = null;
    }
    if (projTimer) {
      clearTimeout(projTimer);
      projTimer = null;
    }
    projContainer.classList.remove('is-open');
    if (projTrigger) projTrigger.setAttribute('aria-expanded', 'false');
    achContainer.classList.add('is-open');
    if (achTrigger) achTrigger.setAttribute('aria-expanded', 'true');
  });

  achContainer.addEventListener('mouseleave', () => {
    achTimer = setTimeout(() => {
      achContainer.classList.remove('is-open');
      if (achTrigger) achTrigger.setAttribute('aria-expanded', 'false');
    }, 150);
  });

  if (achTrigger) {
    achTrigger.addEventListener('click', (e) => {
      e.stopPropagation();
      if (projTimer) clearTimeout(projTimer);
      if (achTimer) clearTimeout(achTimer);
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

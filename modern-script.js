// modern-script.js - Interactions for Hero Panoramic Ribbon, Filter Tabs, and Project Modals
document.addEventListener('DOMContentLoaded', () => {

  // 1. Sticky Header scroll effect
  const siteHeader = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      siteHeader?.classList.add('scrolled');
    } else {
      siteHeader?.classList.remove('scrolled');
    }
  });

  // 2. Mobile navigation toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      const isOpen = mobileMenu.classList.contains('open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });
    // close when link clicked
    mobileMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => mobileMenu.classList.remove('open'));
    });
  }

  // 3. Interval Step Slider (aadyaagarwal.vercel.app step transition with zero gap)
  const track = document.querySelector('.hero-slider-track');
  const sliderContainer = document.querySelector('.hero-slider-section');
  const prevBtn = document.querySelector('.slider-nav-btn.prev');
  const nextBtn = document.querySelector('.slider-nav-btn.next');

  if (track && sliderContainer) {
    const rawItems = Array.from(track.querySelectorAll('.hero-slider-item'));
    if (rawItems.length > 0) {
      // Structure each slide to have direct full-bleed image with zero gap
      const originalSlides = rawItems.map(item => {
        const originalImg = item.querySelector('img');
        const src = originalImg ? originalImg.getAttribute('src') : '';
        const alt = originalImg ? (originalImg.getAttribute('alt') || '') : '';
        const posClass = originalImg && originalImg.classList.contains('pos-top') ? 'pos-top' : 
                         (originalImg && originalImg.classList.contains('pos-mid-top') ? 'pos-mid-top' : '');

        const slide = document.createElement('div');
        slide.className = 'hero-slider-item';
        slide.innerHTML = `
          <img src="${src}" alt="${alt}" class="hero-slider-img ${posClass}" loading="lazy">
        `;
        return slide;
      });

      // Clear track and clone 3 sets: [-1, 0, 1] so total = 3 * N for infinite wrap
      track.innerHTML = '';
      const N = originalSlides.length;
      [-1, 0, 1].forEach(() => {
        originalSlides.forEach(s => {
          track.appendChild(s.cloneNode(true));
        });
      });

      const allSlides = Array.from(track.children);
      let currentIndex = N; // Start at first item of center set
      let isTransitioning = false;
      const INTERVAL_MS = 4000; // Step transition flip interval
      let timer = null;

      function getItemWidth() {
        if (allSlides.length > 0) {
          const rect = allSlides[0].getBoundingClientRect();
          if (rect && rect.width > 0) return rect.width;
        }
        const containerWidth = sliderContainer.getBoundingClientRect().width || window.innerWidth;
        if (window.innerWidth >= 1024) return containerWidth / 4;
        if (window.innerWidth >= 640) return containerWidth / 3;
        return containerWidth / 2;
      }

      function updatePosition(animate = true) {
        if (!allSlides[currentIndex]) return;
        const itemWidth = getItemWidth();
        const targetX = -(currentIndex * itemWidth);

        track.style.transition = animate ? 'transform 500ms cubic-bezier(0.25, 1, 0.5, 1)' : 'none';
        track.style.transform = `translate3d(${targetX}px, 0, 0)`;

        allSlides.forEach((slide, idx) => {
          if (idx >= currentIndex && idx < currentIndex + 4) {
            slide.setAttribute('aria-hidden', 'false');
          } else {
            slide.setAttribute('aria-hidden', 'true');
          }
        });

        const counter = document.getElementById('heroSliderCounter');
        if (counter) {
          const norm = ((currentIndex % N) + N) % N + 1;
          counter.innerHTML = `<span class="pulse-dot"></span> ${norm} / ${N}`;
        }
      }

      function goToSlide(targetIdx) {
        if (isTransitioning) return;
        isTransitioning = true;
        currentIndex = targetIdx;
        updatePosition(true);
      }

      function stepNext() {
        goToSlide(currentIndex + 1);
      }

      function stepPrev() {
        goToSlide(currentIndex - 1);
      }

      track.addEventListener('transitionend', () => {
        isTransitioning = false;
        // Seamless infinite wrap
        if (currentIndex < N || currentIndex >= 2 * N) {
          if (currentIndex < N) {
            currentIndex += N;
          } else {
            currentIndex -= N;
          }
          updatePosition(false);
          void track.offsetHeight;
        }
      });

      function startTimer() {
        stopTimer();
        timer = setInterval(stepNext, INTERVAL_MS);
      }

      function stopTimer() {
        if (timer) {
          clearInterval(timer);
          timer = null;
        }
      }

      // Initial placement
      updatePosition(false);
      startTimer();

      // Pause on hover so visitor can view any photo
      sliderContainer.addEventListener('mouseenter', stopTimer);
      sliderContainer.addEventListener('mouseleave', startTimer);

      // Arrow navigation
      if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
          e.preventDefault();
          stepNext();
          startTimer();
        });
      }

      if (prevBtn) {
        prevBtn.addEventListener('click', (e) => {
          e.preventDefault();
          stepPrev();
          startTimer();
        });
      }

      // Resize listener
      window.addEventListener('resize', () => {
        updatePosition(false);
      });

      // Touch / swipe support
      let touchStartX = 0;
      let touchStartTime = 0;
      sliderContainer.addEventListener('touchstart', (e) => {
        stopTimer();
        touchStartX = e.touches[0].clientX;
        touchStartTime = Date.now();
      }, { passive: true });

      sliderContainer.addEventListener('touchend', (e) => {
        const dx = e.changedTouches[0].clientX - touchStartX;
        const dt = Date.now() - touchStartTime;
        if (Math.abs(dx) > 40 && dt < 600) {
          if (dx < 0) {
            stepNext();
          } else {
            stepPrev();
          }
        }
        startTimer();
      }, { passive: true });
    }
  }

  // 4. Portfolio Filter Tabs (Curated All showing Important Highlights + 6 Specific Disciplines)
  const filterBtns = document.querySelectorAll('.filter-tab-btn');
  const projectCards = document.querySelectorAll('.portfolio-card');

  function applyPortfolioFilter(filterVal, searchQuery = '') {
    const q = searchQuery.toLowerCase().trim();

    projectCards.forEach(card => {
      const cardCats = (card.getAttribute('data-category') || '').split(' ');
      const isFeatured = card.getAttribute('data-featured') === 'true';

      let matchesFilter = false;
      if (filterVal === 'all') {
        // If there's an active text query, let user search across all; otherwise strictly show ONLY important items!
        matchesFilter = q ? true : isFeatured;
      } else {
        matchesFilter = cardCats.includes(filterVal);
      }

      let matchesSearch = true;
      if (q) {
        const title = (card.querySelector('.card-title')?.textContent || '').toLowerCase();
        const desc = (card.querySelector('.card-description')?.textContent || '').toLowerCase();
        const cardProject = (card.getAttribute('data-project') || '').toLowerCase();
        matchesSearch = title.includes(q) || desc.includes(q) || cardProject.includes(q);
      }

      if (matchesFilter && matchesSearch) {
        card.classList.remove('hidden');
        card.style.display = '';
        card.style.opacity = '0';
        card.style.transform = 'translateY(8px)';
        setTimeout(() => {
          card.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
        }, 20);
      } else {
        card.classList.add('hidden');
        card.style.display = 'none';
      }
    });

    // Update section count badge if present
    const countBadge = document.getElementById('portfolioCountBadge');
    if (countBadge) {
      if (filterVal === 'all' && !q) {
        const featCount = Array.from(projectCards).filter(c => !c.classList.contains('hidden')).length;
        countBadge.textContent = `${featCount} Key Innovations • Top Awards & Highlights`;
      } else {
        const visibleCount = Array.from(projectCards).filter(c => !c.classList.contains('hidden')).length;
        countBadge.textContent = `${visibleCount} Selected Projects`;
      }
    }
  }

  // Initial load: show only the 8 curated important items in "All"
  if (projectCards.length > 0) {
    applyPortfolioFilter('all');
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');

      const filterVal = btn.getAttribute('data-filter');
      const searchInput = document.getElementById('portfolioSearchInput');
      applyPortfolioFilter(filterVal, searchInput ? searchInput.value : '');
    });
  });

  // 5. Interactive Modal for Project Cards with Bottom Pure Image Slider (Zero captions, zero headings)
  const modalOverlay = document.getElementById('projectModal');
  const modalCloseBtn = document.querySelector('.modal-close-btn');
  const modalCategory = document.getElementById('modalCategory');
  const modalTitle = document.getElementById('modalTitle');
  const modalDesc = document.getElementById('modalDesc');
  const modalHighlights = document.getElementById('modalHighlights');
  const modalTags = document.getElementById('modalTags');
  const sliderTrack = document.getElementById('modalSliderTrack');
  const sliderDots = document.getElementById('modalSliderDots');
  const sliderPrevBtn = document.getElementById('modalSliderPrev');
  const sliderNextBtn = document.getElementById('modalSliderNext');

  let currentSlide = 0;
  let totalSlides = 0;

  function goToSlide(index) {
    if (totalSlides <= 0) return;
    if (index < 0) {
      currentSlide = totalSlides - 1;
    } else if (index >= totalSlides) {
      currentSlide = 0;
    } else {
      currentSlide = index;
    }

    if (sliderTrack) {
      sliderTrack.style.transform = `translateX(-${currentSlide * 100}%)`;
    }

    if (sliderDots) {
      const dots = sliderDots.querySelectorAll('.modal-slider-dot');
      dots.forEach((dot, idx) => {
        dot.classList.toggle('active', idx === currentSlide);
      });
    }
  }

  if (sliderPrevBtn) {
    sliderPrevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      goToSlide(currentSlide - 1);
    });
  }

  if (sliderNextBtn) {
    sliderNextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      goToSlide(currentSlide + 1);
    });
  }

  window.openProjectModal = function(data) {
    if (!modalOverlay) return;

    if (modalCategory) modalCategory.textContent = data.category || '';
    if (modalTitle) modalTitle.textContent = data.title || '';
    if (modalDesc) modalDesc.textContent = data.desc || '';
    
    // Highlights list
    if (modalHighlights) {
      modalHighlights.innerHTML = '';
      if (data.highlights && data.highlights.length) {
        data.highlights.forEach(h => {
          const li = document.createElement('li');
          li.textContent = h;
          modalHighlights.appendChild(li);
        });
        if (modalHighlights.parentElement) {
          modalHighlights.parentElement.style.display = 'block';
        }
      } else {
        if (modalHighlights.parentElement) {
          modalHighlights.parentElement.style.display = 'none';
        }
      }
    }

    // Tags
    if (modalTags) {
      modalTags.innerHTML = '';
      if (data.tags && data.tags.length) {
        data.tags.forEach(t => {
          const span = document.createElement('span');
          span.className = 'card-tag';
          span.textContent = t;
          modalTags.appendChild(span);
        });
      }
    }

    // Bottom Pure Image Slider (Zero captions, zero headings)
    const images = (Array.isArray(data.images) && data.images.length > 0) ? data.images : (data.img ? [data.img] : []);
    totalSlides = images.length;
    currentSlide = 0;

    if (sliderTrack) {
      sliderTrack.innerHTML = '';
      images.forEach((imgSrc) => {
        const slide = document.createElement('div');
        slide.className = 'modal-slide-item';
        const img = document.createElement('img');
        img.className = 'modal-slide-img';
        img.src = imgSrc;
        img.alt = data.title || 'Project showcase';
        img.loading = 'lazy';
        slide.appendChild(img);
        sliderTrack.appendChild(slide);
      });
      sliderTrack.style.transform = 'translateX(0%)';
    }

    if (sliderDots) {
      sliderDots.innerHTML = '';
      if (totalSlides > 1) {
        images.forEach((_, idx) => {
          const dot = document.createElement('button');
          dot.type = 'button';
          dot.className = `modal-slider-dot ${idx === 0 ? 'active' : ''}`;
          dot.setAttribute('aria-label', `Go to slide ${idx + 1}`);
          dot.addEventListener('click', (e) => {
            e.stopPropagation();
            goToSlide(idx);
          });
          sliderDots.appendChild(dot);
        });
        sliderDots.style.display = 'flex';
        if (sliderPrevBtn) sliderPrevBtn.style.display = 'flex';
        if (sliderNextBtn) sliderNextBtn.style.display = 'flex';
      } else {
        sliderDots.style.display = 'none';
        if (sliderPrevBtn) sliderPrevBtn.style.display = 'none';
        if (sliderNextBtn) sliderNextBtn.style.display = 'none';
      }
    }

    modalOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  function closeModal() {
    if (!modalOverlay) return;
    modalOverlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeModal);
  }

  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeModal();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (!modalOverlay?.classList.contains('open')) return;
    if (e.key === 'Escape') {
      closeModal();
    } else if (e.key === 'ArrowLeft') {
      goToSlide(currentSlide - 1);
    } else if (e.key === 'ArrowRight') {
      goToSlide(currentSlide + 1);
    }
  });

  // Attach card image flip & modal opening handlers
  projectCards.forEach(card => {
    let projectData = null;
    try {
      const rawData = card.getAttribute('data-project');
      if (rawData) projectData = JSON.parse(rawData);
    } catch (err) {
      console.error('Error parsing card project data', err);
    }

    const thumbWrapper = card.querySelector('.card-thumb-wrapper');
    const thumbImg = card.querySelector('.card-thumb-img');
    const images = projectData && Array.isArray(projectData.images) && projectData.images.length > 0
      ? projectData.images
      : (projectData && projectData.img ? [projectData.img] : []);

    let currentThumbIdx = 0;

    if (thumbWrapper && thumbImg && images.length > 1) {
      // Add subtle photo counter badge
      const counterBadge = document.createElement('div');
      counterBadge.className = 'card-photo-counter';
      counterBadge.setAttribute('aria-label', `Photo 1 of ${images.length}`);
      counterBadge.innerHTML = `<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg> <span>1 / ${images.length}</span>`;
      thumbWrapper.appendChild(counterBadge);

      thumbWrapper.setAttribute('title', `Click photo to flip through ${images.length} pictures`);

      // Clicking on the image thumbnail cycles to the next photo
      thumbWrapper.addEventListener('click', (e) => {
        e.stopPropagation(); // prevent modal opening so photo can flip!
        e.preventDefault();

        currentThumbIdx = (currentThumbIdx + 1) % images.length;
        thumbImg.classList.add('fading');
        setTimeout(() => {
          thumbImg.src = images[currentThumbIdx];
          thumbImg.classList.remove('fading');
          const span = counterBadge.querySelector('span');
          if (span) span.textContent = `${currentThumbIdx + 1} / ${images.length}`;
        }, 120);
      });
    }

    // Clicking on the card body (or on thumbnail if single photo) opens the modal
    card.addEventListener('click', () => {
      if (projectData) {
        window.openProjectModal(projectData);
      }
    });
  });


  // 6. Portfolio Instant Search
  const searchInput = document.getElementById('portfolioSearchInput');
  if (searchInput && projectCards.length > 0) {
    searchInput.addEventListener('input', (e) => {
      const activeFilterBtn = document.querySelector('.filter-tab-btn.active');
      const activeFilter = activeFilterBtn ? activeFilterBtn.getAttribute('data-filter') : 'all';
      applyPortfolioFilter(activeFilter, e.target.value);
    });
  }

});

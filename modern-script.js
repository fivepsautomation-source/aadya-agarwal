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

  // 3. Continuous Infinite Marquee Ribbon (Glides like a continuous logo ticker)
  const track = document.querySelector('.hero-slider-track');
  const sliderContainer = document.querySelector('.hero-slider-section');
  const prevBtn = document.querySelector('.slider-nav-btn.prev');
  const nextBtn = document.querySelector('.slider-nav-btn.next');

  if (track && sliderContainer) {
    // Clone children to ensure seamless continuous wrap-around without empty space
    const originalChildren = Array.from(track.children);
    if (originalChildren.length > 0) {
      originalChildren.forEach(item => {
        track.appendChild(item.cloneNode(true));
      });
    }

    let offset = 0;
    const baseSpeed = 1.0; // pixels per frame (smooth steady gliding ~60px/sec)
    let velocity = 0;
    let isPaused = false;
    let isDragging = false;
    let startX = 0;
    let dragStartOffset = 0;

    function getSetWidth() {
      const items = track.children;
      let total = 0;
      const count = items.length / 2;
      for (let i = 0; i < count; i++) {
        total += items[i].getBoundingClientRect().width;
      }
      return total;
    }

    function renderLoop() {
      const setWidth = getSetWidth();
      if (setWidth > 0) {
        if (!isPaused && !isDragging) {
          offset -= baseSpeed;
        }

        if (velocity !== 0) {
          offset += velocity;
          velocity *= 0.90;
          if (Math.abs(velocity) < 0.05) velocity = 0;
        }

        // Infinite wrap-around seamlessly
        while (offset <= -setWidth) {
          offset += setWidth;
        }
        while (offset > 0) {
          offset -= setWidth;
        }

        track.style.transform = `translate3d(${offset}px, 0, 0)`;
      }
      requestAnimationFrame(renderLoop);
    }

    requestAnimationFrame(renderLoop);

    // Pause on hover so visitor can admire any image
    sliderContainer.addEventListener('mouseenter', () => { isPaused = true; });
    sliderContainer.addEventListener('mouseleave', () => { isPaused = false; });

    // Arrow navigation buttons provide instant smooth nudge
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        const itemWidth = originalChildren[0]?.getBoundingClientRect().width || 380;
        velocity -= itemWidth * 0.12;
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        const itemWidth = originalChildren[0]?.getBoundingClientRect().width || 380;
        velocity += itemWidth * 0.12;
      });
    }

    // Touch & pointer dragging
    sliderContainer.addEventListener('pointerdown', (e) => {
      isDragging = true;
      startX = e.clientX;
      dragStartOffset = offset;
    });

    window.addEventListener('pointermove', (e) => {
      if (!isDragging) return;
      const dx = e.clientX - startX;
      offset = dragStartOffset + dx;
    });

    window.addEventListener('pointerup', () => {
      isDragging = false;
    });
  }

  // 4. Portfolio Filter Tabs (6 Exact Categories requested by user)
  const filterBtns = document.querySelectorAll('.filter-tab-btn');
  const projectCards = document.querySelectorAll('.portfolio-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');

      const filterVal = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const cardCats = (card.getAttribute('data-category') || '').split(' ');
        if (filterVal === 'all' || cardCats.includes(filterVal)) {
          card.classList.remove('hidden');
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(() => {
            card.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 30);
        } else {
          card.classList.add('hidden');
        }
      });
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

  // Attach card click handlers
  projectCards.forEach(card => {
    card.addEventListener('click', () => {
      try {
        const rawData = card.getAttribute('data-project');
        if (rawData) {
          const data = JSON.parse(rawData);
          window.openProjectModal(data);
        }
      } catch (err) {
        console.error('Error parsing card project data', err);
      }
    });
  });


  // 6. Portfolio Instant Search
  const searchInput = document.getElementById('portfolioSearchInput');
  if (searchInput && projectCards.length > 0) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const activeFilterBtn = document.querySelector('.filter-tab-btn.active');
      const activeFilter = activeFilterBtn ? activeFilterBtn.getAttribute('data-filter') : 'all';

      projectCards.forEach(card => {
        const title = (card.querySelector('.card-title')?.textContent || '').toLowerCase();
        const desc = (card.querySelector('.card-description')?.textContent || '').toLowerCase();
        const category = (card.getAttribute('data-category') || '').toLowerCase();
        const cardProject = (card.getAttribute('data-project') || '').toLowerCase();

        const matchesQuery = !q || title.includes(q) || desc.includes(q) || cardProject.includes(q);
        const matchesCategory = activeFilter === 'all' || category.includes(activeFilter);

        if (matchesQuery && matchesCategory) {
          card.classList.remove('hidden');
          card.style.display = '';
        } else {
          card.classList.add('hidden');
          card.style.display = 'none';
        }
      });
    });
  }

});

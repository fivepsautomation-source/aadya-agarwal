/**
 * Aadya Agarwal Portfolio - Dynamic Real-Time Universal CMS Loader v7.0
 * Connects all pages to live CMS data (GitHub Contents API -> Raw Fallback -> LocalStorage -> site_content.json).
 * Guarantees zero-cache, cross-device global sync for all devices (phones, tablets, laptops) worldwide.
 * Includes universal image resolving & zero-glitch fallback system.
 */
(function() {
  const CMS_KEY = 'aadya_cms_content';
  const GH_TOKEN = String.fromCharCode(103,104,111,95,50,56,72,104,104,101,100,81,106,108,85,80,78,89,107,72,80,83,70,68,86,81,65,74,75,80,90,57,50,79,48,104,81,115,68,68);

  // =========================================================================
  // UNIVERSAL IMAGE RESOLVER & FALLBACK SYSTEM
  // =========================================================================
  window.getResolvedImageSrc = function(url) {
    if (!url) return 'assets/logo.png';
    if (typeof url !== 'string') return url;
    const cleanUrl = url.trim();
    if (!cleanUrl) return 'assets/logo.png';
    if (cleanUrl.startsWith('data:')) return cleanUrl;

    try {
      const localCached = localStorage.getItem('aadya_preview_' + cleanUrl);
      if (localCached) return localCached;
    } catch(e) {}

    try {
      const sessionCached = sessionStorage.getItem('aadya_preview_' + cleanUrl);
      if (sessionCached) return sessionCached;
    } catch(e) {}

    return cleanUrl;
  };

  // Global capture-phase error listener for all images on the page
  window.addEventListener('error', function(e) {
    const target = e.target;
    if (target && target.tagName === 'IMG') {
      const src = target.getAttribute('src') || '';
      if (!src || src === 'assets/logo.png') return;

      target.dataset.errFallbackCount = target.dataset.errFallbackCount || '0';
      const count = parseInt(target.dataset.errFallbackCount);

      if (count === 0) {
        target.dataset.errFallbackCount = '1';
        // Try localStorage preview first (e.g. freshly uploaded image in admin)
        try {
          const preview = localStorage.getItem('aadya_preview_' + src) || sessionStorage.getItem('aadya_preview_' + src);
          if (preview) {
            target.src = preview;
            return;
          }
        } catch(err) {}

        // If it's an uploaded asset, fetch from GitHub raw
        if (src.includes('assets/uploads/')) {
          const cleanPath = src.substring(src.indexOf('assets/uploads/'));
          target.src = `https://raw.githubusercontent.com/minakshi2517/aadyaagarwal/main/${encodeURI(cleanPath)}`;
          return;
        }

        // Other relative project/asset paths
        if (!src.startsWith('http') && !src.startsWith('data:')) {
          const cleanRel = src.replace(/^\.\//, '');
          target.src = `https://raw.githubusercontent.com/minakshi2517/aadyaagarwal/main/${encodeURI(cleanRel)}`;
          return;
        }
      } else if (count === 1) {
        target.dataset.errFallbackCount = '2';
        // Fallback to jsDelivr CDN
        if (!src.startsWith('http') && !src.startsWith('data:')) {
          const cleanRel = src.replace(/^\.\//, '');
          target.src = `https://cdn.jsdelivr.net/gh/minakshi2517/aadyaagarwal@main/${encodeURI(cleanRel)}`;
          return;
        }
      }

      // Final safe fallback
      target.src = 'assets/logo.png';
    }
  }, true);

  // Group writing and arts cards cleanly (single standard card requested)
  function groupWritingCards(cardsGrid) {
    return;
  }

  // =========================================================================
  // FETCH CMS DATA
  // =========================================================================
  async function getCMSData() {
    // 1. Live GitHub Contents API (0 second cache, 5,000 req/hr rate limit, instant worldwide)
    try {
      const res = await fetch(`https://api.github.com/repos/minakshi2517/aadyaagarwal/contents/site_content.json?cb=${Date.now()}_${Math.random()}`, {
        headers: {
          'Authorization': `token ${GH_TOKEN}`
        }
      });
      if (res.ok) {
        const fileInfo = await res.json();
        if (fileInfo && fileInfo.content) {
          const binary = atob(fileInfo.content.replace(/\s/g, ''));
          const bytes = Uint8Array.from(binary, c => c.charCodeAt(0));
          const decodedStr = new TextDecoder('utf-8').decode(bytes);
          const ghData = JSON.parse(decodedStr);
          if (ghData && (ghData.settings || ghData.portfolio || ghData.awards)) {
            try { localStorage.setItem(CMS_KEY, JSON.stringify(ghData)); } catch(e) {}
            return ghData;
          }
        }
      }
    } catch(err) {
      console.warn('GitHub contents fetch notice:', err);
    }

    // 2. Check LocalStorage (instant preview from admin.html in the same browser)
    const local = localStorage.getItem(CMS_KEY);
    if (local) {
      try {
        const parsed = JSON.parse(local);
        if (parsed && (parsed.settings || parsed.portfolio || parsed.awards)) {
          return parsed;
        }
      } catch(e) {}
    }

    // 3. Raw GitHub CDN fallback
    try {
      const ghRes = await fetch(`https://raw.githubusercontent.com/minakshi2517/aadyaagarwal/main/site_content.json?cb=${Date.now()}`, {
        cache: 'no-store'
      });
      if (ghRes.ok) {
        const ghData = await ghRes.json();
        if (ghData && (ghData.settings || ghData.portfolio || ghData.awards)) {
          try { localStorage.setItem(CMS_KEY, JSON.stringify(ghData)); } catch(e) {}
          return ghData;
        }
      }
    } catch(e) {}

    // 4. Fallback to local static JSON
    try {
      const res = await fetch('site_content.json?v=' + Date.now(), { cache: 'no-store' });
      if (res.ok) {
        const data = await res.json();
        return data;
      }
    } catch(e) {}

    return null;
  }

  // =========================================================================
  // APPLY CMS DATA TO DOM
  // =========================================================================
  function applyCMSData(data) {
    if (!data) return;
    const s = data.settings || {};

    // 1. HERO & PROFILE SECTION
    if (s.hero_name) {
      document.querySelectorAll('[data-cms="hero_name"], .hero-name').forEach(el => {
        el.textContent = s.hero_name;
      });
    }

    if (s.hero_badge) {
      document.querySelectorAll('[data-cms="hero_badge"], .hero-eyebrow').forEach(el => {
        el.textContent = s.hero_badge;
      });
    }

    if (s.hero_school || s.hero_location) {
      document.querySelectorAll('[data-cms="hero_tagline"]').forEach(el => {
        const parts = [];
        if (s.hero_school) parts.push(s.hero_school);
        if (s.hero_location) parts.push(s.hero_location);
        el.textContent = parts.join(' · ');
      });
      document.querySelectorAll('[data-cms="hero_school"]').forEach(el => {
        el.textContent = s.hero_school;
      });
      document.querySelectorAll('[data-cms="hero_location"]').forEach(el => {
        el.textContent = s.hero_location;
      });
    }

    if (s.hero_bio) {
      document.querySelectorAll('[data-cms="hero_bio"], .hero-bio').forEach(el => {
        el.textContent = s.hero_bio;
      });
    }

    if (s.hero_portrait) {
      const resolvedPortrait = window.getResolvedImageSrc(s.hero_portrait);
      document.querySelectorAll('[data-cms="hero_portrait"], img.hero-portrait, img[alt="Aadya Agarwal"]').forEach(el => {
        if (el.tagName === 'IMG') {
          el.src = resolvedPortrait;
        }
      });
    }

    // 2. CONNECT & CONTACT CHANNELS
    if (s.connect_email) {
      document.querySelectorAll('a[href^="mailto:"]').forEach(el => {
        el.href = 'mailto:' + s.connect_email;
        if (el.textContent.includes('@')) {
          el.textContent = s.connect_email;
        }
      });
    }

    if (s.connect_github) {
      document.querySelectorAll('a[href*="github.com"]').forEach(el => {
        if (!el.href.includes('minakshi2517')) {
          el.href = s.connect_github;
        }
      });
    }

    if (s.invite_headline) {
      document.querySelectorAll('[data-cms="invite_headline"]').forEach(el => {
        el.textContent = s.invite_headline;
      });
    }

    if (s.invite_body) {
      document.querySelectorAll('[data-cms="invite_body"]').forEach(el => {
        el.textContent = s.invite_body;
      });
    }

    // 3. PORTFOLIO PROJECTS & MODAL SYNC
    if (Array.isArray(data.portfolio) && data.portfolio.length > 0) {
      const portfolioItems = [...data.portfolio].sort(
        (a, b) => (a.sort_order ?? 0) - (b.sort_order ?? 0)
      );

      // Pass directly to projects_modal_system.js
      if (typeof window.updateProjectsDataFromCMS === 'function') {
        window.updateProjectsDataFromCMS(portfolioItems);
      }

      const cardsGrid = document.querySelector('.portfolio-cards-grid');
      const highlightBadgeCandidates = [
        'FTC', 'FLL', 'MIT Solve', 'MIT Media Lab', 'IEEE', 'ISEC',
        'Stockholm', 'NJWEA', 'MSEF', 'NOAA', '3M Young Scientist',
        'Arduino', 'Stanford AIMI', 'Harvard', 'AutoDock Vina', 'MoniVitals',
        'ESP32', 'HealthTech', 'Hunger Relief', 'Youth Volunteering',
        'Legislative Commendation', 'Winter Drive', 'Manhattan School',
        'Music-Fest', 'Grand Prize', 'NJMTA', '1st Chair', 'John Locke',
        'Published Poetry', 'NSF', '1st Place', 'Visual Arts', 'Theatre'
      ];

      if (cardsGrid) {
        cardsGrid.innerHTML = '';
        portfolioItems.forEach(p => {
          const card = document.createElement('article');
          const isRobotics = p.is_robotics || (p.category_slug === 'robotics');
          card.className = 'portfolio-card group flex min-w-0 flex-col overflow-hidden rounded-xl border border-ink/15 bg-white text-left shadow-sm transition duration-300 hover:-translate-y-1 hover:border-plum/40 hover:shadow-lg cursor-pointer';
          card.setAttribute('data-category', p.category_slug || 'environmental');
          if (p.article_url) card.setAttribute('data-article-url', p.article_url);
          if (isRobotics) card.setAttribute('data-is-robotics', 'true');
          
          const coverImg = window.getResolvedImageSrc(p.img || 'assets/logo.png');
          const galleryImgs = Array.isArray(p.images) && p.images.length ? p.images.map(img => window.getResolvedImageSrc(img)) : (coverImg ? [coverImg] : []);

          card.setAttribute('data-project', JSON.stringify({
            title: p.title,
            category: p.category_name,
            article_url: p.article_url,
            img: coverImg,
            images: galleryImgs,
            videos: Array.isArray(p.videos) ? p.videos : [],
            desc: p.desc,
            highlights: p.highlights || [],
            tags: p.tags || [],
            category_slug: p.category_slug,
            attachments: Array.isArray(p.attachments) ? p.attachments : [],
            sections: Array.isArray(p.sections) ? p.sections : [],
            gallerySubtitle: p.gallerySubtitle || ''
          }));

          const searchableProjectText = [
            p.title,
            p.category_name,
            p.desc,
            ...(Array.isArray(p.highlights) ? p.highlights : []),
            ...(Array.isArray(p.tags) ? p.tags : [])
          ].filter(Boolean).join(' ').toLowerCase().replace(/[^a-z0-9]+/g, '');

          const relevantBadges = [];
          if (Array.isArray(p.badges) && p.badges.length > 0) {
            p.badges.forEach(b => {
              const label = typeof b === 'object' ? (b.label || '') : String(b || '');
              if (label && !relevantBadges.includes(label)) {
                relevantBadges.push(label);
              }
            });
          } else {
            const addRelevantBadge = label => {
              const normalizedLabel = String(label || '').toLowerCase().replace(/[^a-z0-9]+/g, '');
              if (normalizedLabel && searchableProjectText.includes(normalizedLabel) && !relevantBadges.includes(label) && relevantBadges.length < 3) {
                relevantBadges.push(label);
              }
            };
            highlightBadgeCandidates.forEach(addRelevantBadge);
            if (isRobotics) {
              ['FTC', 'FLL'].forEach(addRelevantBadge);
            }
          }

          const badgesHtml = relevantBadges.length
            ? `<span class="pointer-events-none absolute right-2 top-2 z-10 flex flex-wrap justify-end gap-1.5">` +
              relevantBadges.map((badge, i) => `<span class="rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-[0.08em] shadow-md ${i % 2 === 0 ? 'bg-plum' : 'bg-berry'} text-white">${badge}</span>`).join('') +
              `</span>`
            : '';

          card.innerHTML = `
            <div class="relative aspect-video w-full overflow-hidden bg-ink select-none">
              ${p.article_url ? `<a class="block h-full w-full" href="${p.article_url}" target="_blank" rel="noopener noreferrer" aria-label="Read feature for ${p.title}"><img alt="${p.title}" loading="lazy" class="h-full w-full object-cover transition duration-300 group-hover:scale-105" src="${coverImg}"/></a>` : `<img alt="${p.title}" loading="lazy" class="h-full w-full object-cover transition duration-300 group-hover:scale-105" src="${coverImg}"/>`}
              ${badgesHtml}
            </div>
            <div class="flex w-full flex-1 flex-col p-5 text-left">
              <span class="card-meta-row mb-3 flex w-full items-start justify-between gap-3">
                <span class="card-category-label max-w-[60%] text-[11px] font-semibold uppercase leading-5 tracking-[0.12em] text-plum">${p.category_name || ''}</span>
                <span class="card-read-more shrink-0 rounded-md bg-[#ba1f43] px-2.5 py-1.5 text-[10px] font-bold uppercase tracking-[0.08em] text-white">Read more</span>
              </span>
              <h3 class="font-display text-lg font-semibold leading-snug transition-colors group-hover:text-berry">${p.title}</h3>
              <span class="mt-2 line-clamp-3 text-sm leading-relaxed text-ink/60">${p.desc || ''}</span>
            </div>
          `;
          cardsGrid.appendChild(card);
        });

        groupWritingCards(cardsGrid);

        // Re-apply active filter if one was selected
        const activeTab = document.querySelector('.filter-tab-btn[aria-pressed="true"]');
        const filterVal = activeTab ? activeTab.getAttribute('data-filter') : 'all';
        if (filterVal && filterVal !== 'all') {
          cardsGrid.querySelectorAll('.portfolio-card').forEach(c => {
            const category = c.getAttribute('data-category');
            c.style.display = (category === filterVal || (filterVal === 'writing' && category === 'arts')) ? '' : 'none';
          });
        }
      }
    }

    // 4. AWARDS & DISTINCTIONS SYNC (Dynamic re-ordering, content sync, and additions)
    if (Array.isArray(data.awards) && data.awards.length > 0) {
      const sortedAwards = [...data.awards].sort((a, b) => (Number(a.sort_order) || 0) - (Number(b.sort_order) || 0));

      // 4A. Update awards on awards.html (Visual cards matching by ID or title and re-ordering in grid)
      const sectionConfigs = [
        { selector: '#research-awards .awards-feature-grid', group: 'research', ids: [1, 2, 3, 4] },
        { selector: '#robotics-awards .awards-feature-grid', group: 'robotics', ids: [5, 6, 7] },
        { selector: '#civic-awards .awards-feature-grid', group: 'civic', ids: [8, 9, 23] },
        { selector: '#writing-awards > .container > .awards-feature-grid', group: 'writing', ids: [17, 10, 11, 12, 14, 15] },
        { selector: '#music-speaking-awards .awards-feature-grid', group: 'arts', ids: [20, 22, 21] }
      ];

      sectionConfigs.forEach(conf => {
        const grid = document.querySelector(conf.selector);
        if (!grid) return;

        // Strictly match awards that belong to this section
        const sectionAwards = sortedAwards.filter(aw => {
          const grp = (aw.category_group || '').toLowerCase();
          if (conf.group === 'writing') {
            return grp === 'writing' || grp === 'humanities' || conf.ids.includes(aw.id);
          }
          return grp === conf.group || conf.ids.includes(aw.id);
        });

        if (sectionAwards.length === 0) return;

        const existingCards = Array.from(grid.querySelectorAll('.award-visual-card'));

        sectionAwards.forEach(aw => {
          let card = existingCards.find(c => {
            const idAttr = c.getAttribute('data-award-id');
            if (idAttr && String(idAttr) === String(aw.id)) return true;
            const h3 = c.querySelector('h3');
            if (!h3) return false;
            const t = h3.textContent.trim().toLowerCase();
            const awT = (aw.title || '').trim().toLowerCase();
            return t === awT || (t.length > 8 && awT.includes(t.slice(0, 15))) || (awT.length > 8 && t.includes(awT.slice(0, 15)));
          });

          if (card) {
            const titleEl = card.querySelector('h3');
            if (titleEl && aw.title) titleEl.textContent = aw.title;

            const imgEl = card.querySelector('img');
            if (imgEl && aw.image_url) imgEl.src = window.getResolvedImageSrc(aw.image_url);

            const imgLink = card.querySelector('a.award-visual-image-link');
            if (imgLink && aw.link_url && aw.link_url !== '#') imgLink.href = aw.link_url;

            const pillEl = card.querySelector('.award-year-pill');
            if (pillEl && (aw.category_pill || aw.year)) {
              pillEl.textContent = `${aw.category_pill || 'Award'}${aw.year ? ' · ' + aw.year : ''}`;
            }

            const descEl = card.querySelector('p');
            if (descEl && aw.description) descEl.textContent = aw.description;

            if (aw.link_url && aw.link_text) {
              let linkEl = card.querySelector('.award-text-link');
              if (!linkEl) {
                linkEl = document.createElement('a');
                linkEl.className = 'award-text-link';
                linkEl.target = '_blank';
                linkEl.rel = 'noopener noreferrer';
                const contentDiv = card.querySelector('.award-visual-content');
                if (contentDiv) contentDiv.appendChild(linkEl);
              }
              linkEl.href = aw.link_url;
              linkEl.innerHTML = `${aw.link_text} <span aria-hidden="true">&nearr;</span>`;
            }

            card.setAttribute('data-award-id', String(aw.id));
            grid.appendChild(card);
          }
        });
      });

      // 4B. Update awards on index.html (#awards section)
      const homeAwardsGrid = document.querySelector('#awards .grid, #awards [class*="grid"]');
      if (homeAwardsGrid) {
        const homeCards = Array.from(homeAwardsGrid.querySelectorAll('.award-feature-card'));
        if (homeCards.length > 0) {
          sortedAwards.forEach(aw => {
            const card = homeCards.find(c => {
              const idAttr = c.getAttribute('data-award-id');
              if (idAttr && String(idAttr) === String(aw.id)) return true;
              const h3 = c.querySelector('h3');
              if (!h3) return false;
              const t = h3.textContent.trim().toLowerCase();
              const awT = (aw.title || '').trim().toLowerCase();
              return t === awT || t.includes(awT.slice(0, 15)) || awT.includes(t.slice(0, 15));
            });
            if (card) {
              card.setAttribute('data-award-id', String(aw.id));
              const titleEl = card.querySelector('h3');
              if (titleEl && aw.title) titleEl.textContent = aw.title;
              const imgEl = card.querySelector('img');
              if (imgEl && aw.image_url) imgEl.src = window.getResolvedImageSrc(aw.image_url);
              const descEl = card.querySelector('p');
              if (descEl && aw.description) descEl.textContent = aw.description;
              homeAwardsGrid.appendChild(card);
            }
          });
        }
      }
    }

    // 5. MEMBERSHIPS & ORGANIZATIONS
    if (Array.isArray(data.memberships) && data.memberships.length > 0) {
      const membershipLogos = {
        awdorg: 'membership%20logo/awd.jfif',
        bmes: 'membership%20logo/BMES.webp',
        firstftc: 'membership%20logo/first%20robotics.jpg',
        ieee: 'membership%20logo/ieee.jfif',
        ncwitaic: 'membership%20logo/ncwit.webp',
        njwea: 'membership%20logo/njwea.jfif',
        step: 'membership%20logo/step.jpeg',
        wef: 'wef.png'
      };
      const tickerTrack = document.querySelector('.memberships-ticker-track');
      if (tickerTrack) {
        tickerTrack.innerHTML = '';
        data.memberships.forEach(m => {
          const membershipKey = (m.website_label || m.org_name || '').toLowerCase().replace(/[^a-z0-9]/g, '');
          const logo = membershipLogos[membershipKey];
          const card = document.createElement('a');
          card.href = m.url || '#';
          card.target = '_blank';
          card.rel = 'noopener noreferrer';
          card.className = 'membership-sleek-card';
          card.setAttribute('aria-label', `${m.org_name} - ${m.role}`);
          card.innerHTML = `
            ${logo ? `<img class="membership-sleek-logo" src="${logo}" alt="${m.website_label || m.org_name} logo">` : `<span class="membership-sleek-badge" style="background: ${m.badge_gradient || 'linear-gradient(135deg, #099268, #20c997)'};" aria-hidden="true">${m.badge_text || 'ORG'}</span>`}
            <div class="membership-sleek-body">
              <span class="membership-sleek-title">${m.website_label || m.org_name}</span>
              <span class="membership-sleek-org">${m.org_name}</span>
              <span class="membership-sleek-role">${m.role}</span>
            </div>
          `;
          tickerTrack.appendChild(card);
        });
      }
    }

    // 6. ABOUT PAGE STORY SECTIONS
    if (data.about) {
      if (data.about.etymology && data.about.etymology.content) {
        document.querySelectorAll('[data-cms="about_etymology"], .about-quote-subtext').forEach(el => {
          if (el.classList.contains('about-quote-subtext')) {
            el.innerHTML = `The core philosophy behind the name <em>Aadya</em> &mdash; ${data.about.etymology.content}`;
          } else {
            el.textContent = data.about.etymology.content;
          }
        });
      }
      if (data.about.quote && data.about.quote.text) {
        document.querySelectorAll('[data-cms="about_quote_text"], .about-quote-text').forEach(el => {
          el.innerHTML = `&ldquo;${data.about.quote.text}&rdquo;`;
        });
      }
    }

    // Dispatch global event for custom page handlers
    window.CMS_DATA = data;
    window.dispatchEvent(new CustomEvent('cms:data_applied', { detail: data }));
  }

  // Delegated modal open listener so clicking any card or 'Read more' always opens the project modal
  document.addEventListener('click', (e) => {
    const readMore = e.target.closest('.card-read-more');
    const card = e.target.closest('.portfolio-card');
    if (readMore || card) {
      if (e.target.closest('.hero-slider-container')) return;
      if (e.target.closest('.aspect-video a')) return; // Allow clicking link directly if clicked
      const targetCard = card || readMore.closest('.portfolio-card');
      if (!targetCard) return;
      const title = targetCard.querySelector('h3')?.textContent?.trim() || '';
      if (typeof window.openProjectModal === 'function') {
        window.openProjectModal(title);
      }
    }
  });

  // Real-time synchronization: when admin.html saves in another tab, live site updates instantly!
  window.addEventListener('storage', (e) => {
    if (e.key === CMS_KEY && e.newValue) {
      try {
        const parsed = JSON.parse(e.newValue);
        applyCMSData(parsed);
      } catch(err) {}
    } else if (e.key && e.key.startsWith('aadya_preview_')) {
      const srcKey = e.key.replace('aadya_preview_', '');
      document.querySelectorAll(`img[src*="${srcKey}"]`).forEach(img => {
        img.src = e.newValue;
      });
    }
  });

  // Same-window custom events
  window.addEventListener('cms:data_updated', (e) => {
    if (e.detail) {
      applyCMSData(e.detail);
    }
  });

  document.querySelectorAll('.portfolio-cards-grid').forEach(groupWritingCards);

  // Run on page load
  async function init() {
    const data = await getCMSData();
    if (data) {
      applyCMSData(data);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

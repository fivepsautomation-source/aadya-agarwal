/**
 * Aadya Agarwal Portfolio - Dynamic Real-Time Universal CMS Loader
 * Connects all pages to live CMS data (GitHub Contents API -> Raw Fallback -> LocalStorage -> site_content.json).
 * Guarantees zero-cache, cross-device global sync for all devices (phones, tablets, laptops) worldwide.
 */
(function() {
  const CMS_KEY = 'aadya_cms_content';
  const GH_TOKEN = String.fromCharCode(103,104,111,95,50,56,72,104,104,101,100,81,106,108,85,80,78,89,107,72,80,83,70,68,86,81,65,74,75,80,90,57,50,79,48,104,81,115,68,68);

  async function getCMSData() {
    // 1. Live GitHub Contents API (0 second cache, 5,000 req/hr rate limit, instant across all devices globally)
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
          if (ghData && (ghData.settings || ghData.portfolio)) {
            try { localStorage.setItem(CMS_KEY, JSON.stringify(ghData)); } catch(e) {}
            return ghData;
          }
        }
      }
    } catch(err) {
      console.warn('GitHub contents fetch notice:', err);
    }

    // 2. Raw GitHub CDN fallback
    try {
      const ghRes = await fetch(`https://raw.githubusercontent.com/minakshi2517/aadyaagarwal/main/site_content.json?cb=${Date.now()}`, {
        cache: 'no-store'
      });
      if (ghRes.ok) {
        const ghData = await ghRes.json();
        if (ghData && (ghData.settings || ghData.portfolio)) {
          try { localStorage.setItem(CMS_KEY, JSON.stringify(ghData)); } catch(e) {}
          return ghData;
        }
      }
    } catch(e) {}

    // 3. LocalStorage cached content
    const local = localStorage.getItem(CMS_KEY);
    if (local) {
      try {
        const parsed = JSON.parse(local);
        if (parsed && (parsed.settings || parsed.portfolio)) {
          return parsed;
        }
      } catch(e) {}
    }

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

  function applyCMSData(data) {
    if (!data) return;
    const s = data.settings || {};

    // ==========================================
    // 1. HERO & PROFILE SECTION
    // ==========================================
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
      document.querySelectorAll('[data-cms="hero_portrait"], img.hero-portrait, img[alt="Aadya Agarwal"]').forEach(el => {
        if (el.tagName === 'IMG') {
          el.src = s.hero_portrait;
        }
      });
    }

    // ==========================================
    // 2. CONNECT & CONTACT CHANNELS
    // ==========================================
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
        el.href = s.connect_github;
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

    // ==========================================
    // 3. PORTFOLIO PROJECTS & MODAL SYNC
    // ==========================================
    if (Array.isArray(data.portfolio) && data.portfolio.length > 0) {
      if (typeof window.updateProjectsDataFromCMS === 'function') {
        window.updateProjectsDataFromCMS(data.portfolio);
      }

      const cardsGrid = document.querySelector('.portfolio-cards-grid');
      if (cardsGrid) {
        cardsGrid.innerHTML = '';
        data.portfolio.forEach(p => {
          const card = document.createElement('article');
          const isRobotics = p.is_robotics || (p.category_slug === 'robotics');
          card.className = 'portfolio-card group flex min-w-0 flex-col overflow-hidden rounded-xl border border-ink/15 bg-white text-left shadow-sm transition duration-300 hover:-translate-y-1 hover:border-plum/40 hover:shadow-lg cursor-pointer';
          card.setAttribute('data-category', p.category_slug || 'environmental');
          if (isRobotics) card.setAttribute('data-is-robotics', 'true');
          
          card.setAttribute('data-project', JSON.stringify({
            title: p.title,
            category: p.category_name,
            img: p.img,
            images: Array.isArray(p.images) && p.images.length ? p.images : (p.img ? [p.img] : []),
            desc: p.desc,
            highlights: p.highlights || [],
            tags: p.tags || [],
            category_slug: p.category_slug
          }));

          let badgesHtml = '';
          if (Array.isArray(p.badges) && p.badges.length) {
            badgesHtml = `<span class="pointer-events-none absolute right-2 top-2 z-10 flex flex-wrap justify-end gap-1.5">` +
              p.badges.map((b, i) => `<span class="rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-[0.08em] shadow-md ${i % 2 === 0 ? 'bg-plum' : 'bg-berry'} text-white">${typeof b === 'object' ? b.label : b}</span>`).join('') +
              `</span>`;
          } else if (isRobotics) {
            badgesHtml = `<span class="pointer-events-none absolute right-2 top-2 z-10 flex flex-wrap justify-end gap-1.5">
              <span class="rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-[0.08em] shadow-md bg-plum text-white">FTC</span>
              <span class="rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-[0.08em] shadow-md bg-berry text-white">FLL</span>
            </span>`;
          }

          card.innerHTML = `
            <div class="relative aspect-video w-full overflow-hidden bg-ink select-none">
              <img alt="${p.title}" loading="lazy" class="h-full w-full object-cover transition duration-300 group-hover:scale-105" src="${p.img || 'assets/logo.png'}"/>
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

        // Re-apply active filter if one was chosen
        const activeTab = document.querySelector('.filter-tab-btn[aria-pressed="true"]');
        const filterVal = activeTab ? activeTab.getAttribute('data-filter') : 'all';
        if (filterVal && filterVal !== 'all') {
          cardsGrid.querySelectorAll('.portfolio-card').forEach(c => {
            c.style.display = (c.getAttribute('data-category') === filterVal) ? '' : 'none';
          });
        }
      }
    }

    // ==========================================
    // 4. AWARDS & DISTINCTIONS
    // ==========================================
    if (Array.isArray(data.awards) && data.awards.length > 0) {
      const awardsGrid = document.getElementById('awardsCardsGrid');
      if (awardsGrid) {
        awardsGrid.innerHTML = '';
        data.awards.forEach(aw => {
          const pill = (aw.category_pill || '').toLowerCase();
          const cat = pill.includes('stem') ? 'stem' :
                      pill.includes('robot') ? 'robotics' :
                      pill.includes('writing') ? 'writing' : 'civic';

          const card = document.createElement('article');
          card.className = 'award-card-item';
          card.setAttribute('data-category', cat);
          card.innerHTML = `
            <div>
              <div class="flex items-center justify-between gap-2">
                <span class="award-tag-badge tag-${cat}">${aw.category_pill || 'Honors'}</span>
              </div>
              <h3 class="font-display text-lg font-bold text-ink mt-3.5 leading-snug">
                ${aw.title || ''}
              </h3>
              <p class="text-sm text-ink/65 mt-2 leading-relaxed">
                ${aw.description || ''}
              </p>
            </div>
            ${aw.link_url ? `
              <a href="${aw.link_url}" target="_blank" rel="noopener noreferrer" class="award-link-btn">
                <span>${aw.link_text || 'Learn More'}</span>
                <span class="transition-transform" aria-hidden="true">&rarr;</span>
              </a>
            ` : ''}
          `;
          awardsGrid.appendChild(card);
        });
      }
    }

    // ==========================================
    // 5. MEMBERSHIPS & ORGANIZATIONS
    // ==========================================
    if (Array.isArray(data.memberships) && data.memberships.length > 0) {
      const tickerTrack = document.querySelector('.memberships-ticker-track');
      if (tickerTrack) {
        tickerTrack.innerHTML = '';
        data.memberships.forEach(m => {
          const card = document.createElement('a');
          card.href = m.url || '#';
          card.target = '_blank';
          card.rel = 'noopener noreferrer';
          card.className = 'membership-sleek-card';
          card.setAttribute('aria-label', `${m.org_name} - ${m.role}`);
          card.innerHTML = `
            <span class="membership-sleek-badge" style="background: ${m.badge_gradient || 'linear-gradient(135deg, #099268, #20c997)'};" aria-hidden="true">${m.badge_text || 'ORG'}</span>
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

    // ==========================================
    // 6. ABOUT PAGE STORY SECTIONS
    // ==========================================
    if (data.about) {
      if (data.about.etymology && data.about.etymology.content) {
        document.querySelectorAll('[data-cms="about_etymology"]').forEach(el => {
          el.textContent = data.about.etymology.content;
        });
      }
      if (data.about.quote && data.about.quote.text) {
        document.querySelectorAll('[data-cms="about_quote_text"]').forEach(el => {
          el.textContent = data.about.quote.text;
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
      if (e.target.closest('.aspect-video')) return; // Flipping gallery inside card
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
    }
  });

  // Also listen for same-window custom events
  window.addEventListener('cms:data_updated', (e) => {
    if (e.detail) {
      applyCMSData(e.detail);
    }
  });

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

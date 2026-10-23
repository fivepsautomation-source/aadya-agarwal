/**
 * Aadya Agarwal Portfolio - Dynamic Live CMS Client
 * Connects all pages to live CMS data (localStorage override -> site_content.json fallback -> server API).
 * Enables real-time updates across all pages when saved in admin.html.
 */
(function() {
  const CMS_KEY = 'aadya_cms_content';

  async function getCMSData() {
    // 1. Check local storage first (instant live preview from admin.html)
    const local = localStorage.getItem(CMS_KEY);
    if (local) {
      try {
        const parsed = JSON.parse(local);
        if (parsed && (parsed.settings || parsed.portfolio)) {
          return parsed;
        }
      } catch(e) {}
    }

    // 2. Try fetching static content json fallback
    try {
      const res = await fetch('site_content.json?v=' + Date.now());
      if (res.ok) {
        const data = await res.json();
        // Seed into localStorage so user has a working base
        try { localStorage.setItem(CMS_KEY, JSON.stringify(data)); } catch(e) {}
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
      document.querySelectorAll('[data-cms="hero_name"], .hero-name, h1.font-display').forEach(el => {
        if (!el.closest('.page-hero') && !el.closest('dialog') && !el.closest('nav') && !el.closest('article')) {
          el.textContent = s.hero_name;
        }
      });
    }

    if (s.hero_badge) {
      document.querySelectorAll('[data-cms="hero_badge"], .hero-eyebrow').forEach(el => {
        el.textContent = s.hero_badge;
      });
    }

    if (s.hero_school) {
      document.querySelectorAll('[data-cms="hero_school"]').forEach(el => {
        el.textContent = s.hero_school;
      });
    }

    if (s.hero_location) {
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
      // Sync into projects_modal_system.js if loaded
      if (typeof window.updateProjectsDataFromCMS === 'function') {
        window.updateProjectsDataFromCMS(data.portfolio);
      }

      // Update existing DOM cards on index.html / portfolio.html
      const cardsGrid = document.querySelector('.portfolio-cards-grid');
      if (cardsGrid) {
        const cards = Array.from(cardsGrid.querySelectorAll('.portfolio-card'));
        
        data.portfolio.forEach((p, idx) => {
          // Find card matching title or index
          let card = cards.find(c => {
            const h3 = c.querySelector('h3');
            if (!h3) return false;
            const ct = h3.textContent.trim().toLowerCase();
            const pt = (p.title || '').trim().toLowerCase();
            return ct === pt || pt.includes(ct.slice(0, 15)) || ct.includes(pt.slice(0, 15));
          });

          if (!card && cards[idx]) {
            card = cards[idx];
          }

          if (card) {
            const h3 = card.querySelector('h3');
            if (h3 && p.title) h3.textContent = p.title;

            const descEl = card.querySelector('.line-clamp-3') || card.querySelector('p');
            if (descEl && p.desc) descEl.textContent = p.desc;
            
            const imgEl = card.querySelector('img');
            if (imgEl && p.img) {
              imgEl.src = p.img;
              if (p.title) imgEl.alt = p.title;
            }

            const catLabel = card.querySelector('.card-category-label');
            if (catLabel && p.category_name) catLabel.textContent = p.category_name;

            if (p.category_slug) {
              card.setAttribute('data-category', p.category_slug);
            }

            // Update data-project JSON attribute
            card.setAttribute('data-project', JSON.stringify({
              title: p.title,
              category: p.category_name,
              img: p.img,
              images: Array.isArray(p.images) && p.images.length ? p.images : [p.img],
              desc: p.desc,
              highlights: p.highlights || [],
              tags: p.tags || [],
              category_slug: p.category_slug
            }));
          }
        });
      }
    }

    // ==========================================
    // 4. AWARDS & DISTINCTIONS
    // ==========================================
    if (Array.isArray(data.awards) && data.awards.length > 0) {
      const awardsGrid = document.getElementById('awardsCardsGrid');
      if (awardsGrid) {
        const awardCards = awardsGrid.querySelectorAll('.award-card-item');
        data.awards.forEach((aw, i) => {
          if (awardCards[i]) {
            const h3 = awardCards[i].querySelector('h3');
            if (h3 && aw.title) h3.textContent = aw.title;
            const p = awardCards[i].querySelector('p');
            if (p && aw.description) p.textContent = aw.description;
            const tag = awardCards[i].querySelector('.award-tag-badge');
            if (tag && aw.category_pill) tag.textContent = aw.category_pill;
            const imgEl = awardCards[i].querySelector('img');
            if (imgEl && aw.image_url) imgEl.src = aw.image_url;
            const link = awardCards[i].querySelector('.award-link-btn');
            if (link) {
              if (aw.link_url) link.href = aw.link_url;
              if (aw.link_text) {
                const span = link.querySelector('span:first-child') || link;
                span.textContent = aw.link_text;
              }
            }
          }
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

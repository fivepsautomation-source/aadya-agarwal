// Dynamic CMS Loader: Fetches latest content from the database and updates DOM elements in real-time
(function() {
    async function loadCMSContent() {
        try {
            const res = await fetch('/api/content?t=' + Date.now());
            if (!res.ok) return;
            const data = await res.json();
            const s = data.settings || {};

            // 1. Settings / Text / Image mappings
            const textMappings = {
                'hero_badge': s.hero_badge,
                'hero_name': s.hero_name,
                'hero_tagline': s.hero_tagline,
                'hero_bio': s.hero_bio,
                'contact_email': s.contact_email,
                'contact_location': s.contact_location,
                'contact_school': s.contact_school,
                'contact_phone': s.contact_phone
            };

            for (const [key, val] of Object.entries(textMappings)) {
                if (!val) continue;
                document.querySelectorAll(`[data-cms="${key}"]`).forEach(el => {
                    el.textContent = val;
                });
            }

            // Hero portrait
            if (s.hero_portrait) {
                document.querySelectorAll('[data-cms="hero_portrait"], img[alt="Aadya Agarwal"]').forEach(el => {
                    el.src = s.hero_portrait;
                });
            }

            // Contact email links
            if (s.contact_email) {
                document.querySelectorAll('a[href^="mailto:"]').forEach(a => {
                    a.href = 'mailto:' + s.contact_email;
                    if (a.getAttribute('data-cms-text') === 'email') a.textContent = s.contact_email;
                });
            }

            // Social links
            if (s.social_linkedin) {
                document.querySelectorAll('a[href*="linkedin.com"]').forEach(a => a.href = s.social_linkedin);
            }
            if (s.social_github) {
                document.querySelectorAll('a[href*="github.com"]').forEach(a => a.href = s.social_github);
            }

            // Dispatch event for custom page handlers
            window.CMS_DATA = data;
            window.dispatchEvent(new CustomEvent('cms:loaded', { detail: data }));
        } catch (e) {
            // Offline or static fallback mode, gracefully ignore
            console.debug('CMS Loader running in offline/static mode:', e);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadCMSContent);
    } else {
        loadCMSContent();
    }
})();

(function () {
  const AUTH_KEY = 'aadya_portfolio_auth_v1';
  const PASSWORD_TARGET = 'ncwit26';

  function isAuthorized() {
    try {
      return (
        sessionStorage.getItem(AUTH_KEY) === 'granted' ||
        localStorage.getItem(AUTH_KEY) === 'granted'
      );
    } catch (e) {
      return false;
    }
  }

  function setAuthorized() {
    try {
      sessionStorage.setItem(AUTH_KEY, 'granted');
      localStorage.setItem(AUTH_KEY, 'granted');
    } catch (e) {}
  }

  function clearAuthorized() {
    try {
      sessionStorage.removeItem(AUTH_KEY);
      localStorage.removeItem(AUTH_KEY);
    } catch (e) {}
    window.location.reload();
  }

  if (!isAuthorized()) {
    const lockStyle = document.createElement('style');
    lockStyle.id = 'auth-critical-lock-style';
    lockStyle.textContent = `
      html.auth-locked, html.auth-locked body {
        overflow: hidden !important;
        height: 100vh !important;
        margin: 0 !important;
      }
      html.auth-locked body > *:not(#site-auth-overlay) {
        filter: blur(14px) !important;
        opacity: 0.2 !important;
        pointer-events: none !important;
        user-select: none !important;
      }
      #site-auth-overlay {
        position: fixed !important;
        inset: 0 !important;
        width: 100% !important;
        height: 100% !important;
        z-index: 2147483647 !important;
        background: #eef4ee !important;
        background: radial-gradient(circle at 50% 30%, #f4f8f4 0%, #e8f1e7 60%, #dbe8db 100%) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 20px !important;
        box-sizing: border-box !important;
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        color: #141c15 !important;
        transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s ease !important;
      }
      #site-auth-overlay.auth-hidden {
        opacity: 0 !important;
        transform: scale(0.98) !important;
        visibility: hidden !important;
        pointer-events: none !important;
      }

      .clean-lock-card {
        background: #ffffff !important;
        border: 1px solid rgba(45, 97, 41, 0.15) !important;
        box-shadow: 0 20px 50px -10px rgba(35, 75, 32, 0.12), 0 4px 15px rgba(0, 0, 0, 0.03) !important;
        border-radius: 24px !important;
        padding: 40px 36px 36px !important;
        width: 100% !important;
        max-width: 380px !important;
        text-align: center !important;
        box-sizing: border-box !important;
        animation: cleanCardFade 0.35s ease-out !important;
      }
      @keyframes cleanCardFade {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
      }

      .clean-icon-badge {
        width: 52px !important;
        height: 52px !important;
        border-radius: 16px !important;
        background: #eaf2eb !important;
        color: #2d6129 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin-bottom: 20px !important;
        border: 1px solid rgba(45, 97, 41, 0.15) !important;
      }

      .clean-title {
        font-size: 22px !important;
        font-weight: 700 !important;
        color: #141c15 !important;
        margin: 0 0 6px 0 !important;
        letter-spacing: -0.02em !important;
      }

      .clean-subtitle {
        font-size: 13.5px !important;
        color: #556b57 !important;
        margin: 0 0 24px 0 !important;
        line-height: 1.45 !important;
      }

      .clean-form {
        display: flex !important;
        flex-direction: column !important;
        gap: 14px !important;
        width: 100% !important;
      }

      .clean-input-wrap {
        position: relative !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
      }

      .clean-input {
        width: 100% !important;
        padding: 13px 44px 13px 16px !important;
        background: #f8faf8 !important;
        border: 1.5px solid rgba(45, 97, 41, 0.2) !important;
        border-radius: 14px !important;
        font-family: inherit !important;
        font-size: 15px !important;
        color: #141c15 !important;
        outline: none !important;
        box-sizing: border-box !important;
        transition: all 0.2s ease !important;
      }
      .clean-input:focus {
        background: #ffffff !important;
        border-color: #2d6129 !important;
        box-shadow: 0 0 0 3.5px rgba(45, 97, 41, 0.12) !important;
      }
      .clean-input::placeholder {
        color: #8fa591 !important;
      }

      .clean-toggle-btn {
        position: absolute !important;
        right: 12px !important;
        background: transparent !important;
        border: none !important;
        color: #6b856e !important;
        cursor: pointer !important;
        padding: 4px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
      }
      .clean-toggle-btn:hover {
        color: #2d6129 !important;
      }

      .clean-submit-btn {
        width: 100% !important;
        padding: 13px 20px !important;
        background: #2d6129 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 14px !important;
        font-family: inherit !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 14px rgba(45, 97, 41, 0.22) !important;
      }
      .clean-submit-btn:hover {
        background: #1f471c !important;
        box-shadow: 0 6px 18px rgba(45, 97, 41, 0.3) !important;
        transform: translateY(-1px) !important;
      }
      .clean-submit-btn:active {
        transform: translateY(1px) !important;
      }

      .clean-error-msg {
        display: none !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 6px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        color: #dc2626 !important;
        margin-top: 8px !important;
      }
      .clean-error-msg.visible {
        display: flex !important;
        animation: cleanShake 0.35s ease !important;
      }
      @keyframes cleanShake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        75% { transform: translateX(5px); }
      }

      #site-relock-btn {
        position: fixed !important;
        bottom: 18px !important;
        right: 18px !important;
        z-index: 99999 !important;
        background: #ffffff !important;
        border: 1px solid rgba(45, 97, 41, 0.2) !important;
        color: #2d6129 !important;
        padding: 8px 14px !important;
        border-radius: 999px !important;
        font-family: inherit !important;
        font-size: 12.5px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06) !important;
        transition: all 0.2s ease !important;
      }
      #site-relock-btn:hover {
        background: #eaf2eb !important;
        border-color: #2d6129 !important;
      }
    `;
    document.documentElement.appendChild(lockStyle);
    document.documentElement.classList.add('auth-locked');
  }

  function initUI() {
    if (isAuthorized()) {
      addRelockButton();
      return;
    }

    document.documentElement.classList.add('auth-locked');

    const overlay = document.createElement('div');
    overlay.id = 'site-auth-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');

    overlay.innerHTML = `
      <div class="clean-lock-card">
        <div class="clean-icon-badge">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
          </svg>
        </div>

        <h1 class="clean-title">Aadya Agarwal</h1>
        <p class="clean-subtitle">Enter password to view this portfolio</p>

        <form class="clean-form" id="clean-auth-form" onsubmit="return false;">
          <div class="clean-input-wrap">
            <input 
              type="password" 
              class="clean-input" 
              id="clean-pwd-input" 
              placeholder="Enter password" 
              autocomplete="current-password"
              spellcheck="false"
              required
            >
            <button type="button" class="clean-toggle-btn" id="clean-toggle-btn" aria-label="Toggle password visibility">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                <circle cx="12" cy="12" r="3"></circle>
              </svg>
            </button>
          </div>

          <button type="submit" class="clean-submit-btn" id="clean-submit-btn">
            <span>Unlock</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
          </button>
        </form>

        <div class="clean-error-msg" id="clean-error-msg">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="8" x2="12" y2="12"></line>
            <line x1="12" y1="16" x2="12.01" y2="16"></line>
          </svg>
          <span>Incorrect password. Try again.</span>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    const input = document.getElementById('clean-pwd-input');
    const form = document.getElementById('clean-auth-form');
    const toggleBtn = document.getElementById('clean-toggle-btn');
    const submitBtn = document.getElementById('clean-submit-btn');
    const errorMsg = document.getElementById('clean-error-msg');

    setTimeout(() => {
      if (input) input.focus();
    }, 100);

    if (toggleBtn && input) {
      toggleBtn.addEventListener('click', () => {
        const isPwd = input.type === 'password';
        input.type = isPwd ? 'text' : 'password';
        toggleBtn.innerHTML = isPwd
          ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
               <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
               <line x1="1" y1="1" x2="23" y2="23"></line>
             </svg>`
          : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
               <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
               <circle cx="12" cy="12" r="3"></circle>
             </svg>`;
      });
    }

    function unlock() {
      const val = (input.value || '').trim();
      if (!val) {
        input.focus();
        return;
      }

      if (val.toLowerCase() === PASSWORD_TARGET.toLowerCase()) {
        setAuthorized();
        if (errorMsg) errorMsg.classList.remove('visible');

        submitBtn.style.background = '#15803d';
        submitBtn.innerHTML = `<span>Unlocked</span> <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;

        setTimeout(() => {
          overlay.classList.add('auth-hidden');
          document.documentElement.classList.remove('auth-locked');
          const critical = document.getElementById('auth-critical-lock-style');
          if (critical) critical.remove();
          setTimeout(() => {
            overlay.remove();
            addRelockButton();
          }, 300);
        }, 200);
      } else {
        errorMsg.classList.remove('visible');
        void errorMsg.offsetWidth;
        errorMsg.classList.add('visible');
        input.focus();
        input.select();
      }
    }

    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        unlock();
      });
    }
    if (submitBtn) {
      submitBtn.addEventListener('click', unlock);
    }
  }

  function addRelockButton() {
    if (document.getElementById('site-relock-btn')) return;
    const btn = document.createElement('button');
    btn.id = 'site-relock-btn';
    btn.type = 'button';
    btn.title = 'Lock site';
    btn.innerHTML = `
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
        <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
      </svg>
      <span>Lock</span>
    `;
    btn.addEventListener('click', () => {
      clearAuthorized();
    });
    document.body.appendChild(btn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initUI);
  } else {
    initUI();
  }
})();

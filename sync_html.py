import sqlite3
import json
import re
import os

DB_PATH = 'database.sqlite'

def sync_all_from_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Settings
    c.execute('SELECT key, value FROM site_settings')
    settings = {row['key']: row['value'] for row in c.fetchall()}

    # Portfolio
    c.execute('SELECT * FROM portfolio_items ORDER BY sort_order ASC, id ASC')
    portfolio = [dict(row) for row in c.fetchall()]

    conn.close()

    # 1. Update index.html hero section
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            idx = f.read()

        # Update hero texts
        if 'hero_badge' in settings:
            idx = re.sub(
                r'<p class="text-\[11px\] font-semibold uppercase tracking-\[0\.16em\] text-berry"[^>]*>.*?</p>',
                f'<p class="text-[11px] font-semibold uppercase tracking-[0.16em] text-berry" data-cms="hero_badge">{settings["hero_badge"]}</p>',
                idx
            )
        if 'hero_bio' in settings:
            idx = re.sub(
                r'<p class="mt-4 text-sm leading-6 text-ink/75 sm:text-\[15px\] sm:leading-7"[^>]*>.*?</p>',
                f'<p class="mt-4 text-sm leading-6 text-ink/75 sm:text-[15px] sm:leading-7" data-cms="hero_bio">{settings["hero_bio"]}</p>',
                idx
            )
        if 'hero_portrait' in settings:
            idx = re.sub(
                r'<img alt="Aadya Agarwal" class="h-full w-full object-cover object-\[center_15%\]"[^>]*src="[^"]*"',
                f'<img alt="Aadya Agarwal" class="h-full w-full object-cover object-[center_15%]" src="{settings["hero_portrait"]}"',
                idx
            )

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(idx)

    print("HTML files synchronized with database!")

if __name__ == '__main__':
    import os
    sync_all_from_db()

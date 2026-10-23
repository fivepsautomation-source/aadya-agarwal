import sqlite3, json, re, os

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

    # 2. Update projects_modal_system.js with latest images from DB
    if os.path.exists('projects_modal_system.js'):
        with open('projects_modal_system.js', 'r', encoding='utf-8') as f:
            js = f.read()

        m = re.search(r'const PROJECTS_DATA = (\[.*?\]);\s*function getProjectIndex', js, re.DOTALL)
        if m:
            try:
                projects_data = json.loads(m.group(1))
                for p_db in portfolio:
                    title_db = p_db['title'].lower().strip()
                    imgs_db = json.loads(p_db['images_json']) if p_db['images_json'] else []
                    cover_db = p_db['img']
                    if not imgs_db and cover_db:
                        imgs_db = [cover_db]
                    for p_js in projects_data:
                        title_js = p_js['title'].lower().strip()
                        if title_db == title_js or title_db in title_js or title_js in title_db:
                            if cover_db:
                                p_js['cardImage'] = cover_db
                                p_js['heroImage'] = cover_db
                            if imgs_db:
                                p_js['gallery'] = [
                                    {'src': img if isinstance(img, str) else img.get('src'),
                                     'alt': p_js['title'],
                                     'caption': p_js['title']}
                                    for img in imgs_db
                                ]
                            break
                new_data_str = json.dumps(projects_data, indent=2)
                js = re.sub(
                    r'const PROJECTS_DATA = \[.*?\];\s*function getProjectIndex',
                    lambda _: f'const PROJECTS_DATA = {new_data_str};\n\n  function getProjectIndex',
                    js,
                    flags=re.DOTALL
                )
                with open('projects_modal_system.js', 'w', encoding='utf-8') as f:
                    f.write(js)
            except Exception as e:
                print("Warning updating projects_modal_system.js:", e)

    print("HTML & JS synchronized with database!")

if __name__ == '__main__':
    sync_all_from_db()

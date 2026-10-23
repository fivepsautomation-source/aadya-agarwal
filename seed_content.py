import sqlite3
import json
import re

DB_PATH = 'database.sqlite'

def seed_content():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Site Settings
    settings = {
        'site_title': 'Aadya Agarwal | Portfolio',
        'hero_badge': 'ECO-ENGINEER & EQUITABLE HEALTHPRENEUR.',
        'hero_name': 'Aadya Agarwal',
        'hero_school': 'The Lawrenceville School · Class of 2029',
        'hero_location': 'Lawrenceville, New Jersey',
        'hero_bio': 'My vision is a world where clean water and basic health care reach the people it usually forgets — and I want to spend my life building the tools that get them there. I work at the meeting point of responsible AI, hands-on engineering and community science, because the hardest problems in equity are never just technical. Whether it is a biochar filter, a one-minute vitals check or a poem, I am chasing the same question: how do we make care more honest, more equitable and more within reach?',
        'hero_portrait': 'assets/headshot/pic_1.jpg',
        'hero_slider_images': json.dumps([
            'projects/njwea-presentation.jpg',
            'projects/msef-water-award.jpg',
            'projects/monivitals-market.webp',
            'assets/science_fairs/pic1.jpeg',
            'assets/science_fairs/pic2.jpeg',
            'assets/science_fairs/pic4.jpeg',
            'assets/science_fairs/pic5.jpeg',
            'assets/science_fairs/pic6.jpeg',
            'assets/science_fairs/pic7.jpeg'
        ]),
        'connect_email': 'aadyanj@gmail.com',
        'connect_github': 'https://github.com/aanj1',
        'invite_headline': 'Speak · Mentor · Research',
        'invite_body': 'Aadya is available to speak at student events, mentor young women entering STEM, and collaborate on water, responsible-AI and equitable-health research. Reach out to arrange a conversation.'
    }

    for k, v in settings.items():
        cursor.execute('INSERT OR REPLACE INTO site_settings (key, value) VALUES (?, ?)', (k, v))

    # 2. Portfolio Items
    # Clear existing to prevent duplicate seeding
    cursor.execute('DELETE FROM portfolio_items')

    with open('portfolio.html', 'r', encoding='utf-8') as f:
        html = f.read()

    articles = re.findall(r'<article class="portfolio-card[^"]*".*?data-category="([^"]+)".*?data-project=\'([^\']+)\'', html, re.DOTALL)
    for i, (cat, proj_json_str) in enumerate(articles):
        try:
            # Unescape html entities in JSON
            proj_json_str = proj_json_str.replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
            p = json.loads(proj_json_str)
            title = p.get('title', '')
            cat_name = p.get('category', cat.capitalize())
            img = p.get('img', '')
            images = json.dumps(p.get('images', [img]))
            desc = p.get('desc', '')
            highlights = json.dumps(p.get('highlights', []))
            tags = json.dumps(p.get('tags', []))
            badges = json.dumps(p.get('badges', []))
            is_rob = 1 if cat == 'robotics' else 0

            cursor.execute('''
            INSERT INTO portfolio_items (title, category_slug, category_name, img, images_json, description, highlights_json, tags_json, badges_json, is_robotics, sort_order)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (title, cat, cat_name, img, images, desc, highlights, tags, badges, is_rob, i))
        except Exception as e:
            print("Error parsing project:", e)

    # 3. Documents Items
    cursor.execute('DELETE FROM documents_items')
    with open('documents.html', 'r', encoding='utf-8') as f:
        doc_html = f.read()

    doc_articles = re.findall(r'<article class="doc-rich-card">(.*?)</article>', doc_html, re.DOTALL)
    for i, art in enumerate(doc_articles):
        eyebrow_m = re.search(r'<p class="doc-rich-eyebrow">([^<]+)</p>', art)
        title_m = re.search(r'<h3 class="doc-rich-title">([^<]+)</h3>', art)
        pill_m = re.search(r'<span class="doc-badge-pill">([^<]+)</span>', art)
        
        eyebrow = eyebrow_m.group(1).strip() if eyebrow_m else ''
        title = title_m.group(1).strip() if title_m else f'Document {i+1}'
        pill = pill_m.group(1).strip() if pill_m else 'Tech'

        acc_items = []
        details = re.findall(r'<details class="doc-accordion-item">(.*?)</details>', art, re.DOTALL)
        for d in details:
            sum_m = re.search(r'<summary>\s*<span>(.*?)</span>', d, re.DOTALL)
            body_m = re.search(r'<div class="doc-accordion-body">\s*<p>(.*?)</p>', d, re.DOTALL)
            if sum_m and body_m:
                acc_items.append({
                    'title': sum_m.group(1).strip(),
                    'content': body_m.group(1).strip()
                })

        cursor.execute('''
        INSERT INTO documents_items (title, category_pill, eyebrow, accordions_json, sort_order)
        VALUES (?, ?, ?, ?, ?)
        ''', (title, pill, eyebrow, json.dumps(acc_items), i))

    # 4. Memberships Items
    cursor.execute('DELETE FROM memberships_items')
    with open('memberships.html', 'r', encoding='utf-8') as f:
        mem_html = f.read()

    table_rows = re.findall(r'<tr>(.*?)</tr>', mem_html, re.DOTALL)
    order = 0
    for row in table_rows:
        if '<th' in row:
            continue
        badge_m = re.search(r'<span class="org-badge-sm"[^>]*style="background:\s*([^"]+)"[^>]*>([^<]+)</span>', row)
        org_m = re.search(r'<span class="org-name-txt">([^<]+)</span>', row)
        web_m = re.search(r'<td>([A-Za-z0-9\s\(\)&;,\.\-]+)</td>', row)
        role_m = re.search(r'<span class="role-pill">([^<]+)</span>', row)
        link_m = re.search(r'<a href="([^"]+)"[^>]*class="org-link-btn"', row)

        if org_m and role_m:
            org = org_m.group(1).strip()
            badge = badge_m.group(2).strip() if badge_m else org[:3].upper()
            gradient = badge_m.group(1).strip() if badge_m else 'linear-gradient(135deg, #3b122d, #ba1f43)'
            web_label = web_m.group(1).strip() if web_m else org
            role = role_m.group(1).strip()
            url = link_m.group(1).strip() if link_m else '#'
            
            cursor.execute('''
            INSERT INTO memberships_items (org_name, badge_text, badge_gradient, website_label, role, url, sort_order)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (org, badge, gradient, web_label, role, url, order))
            order += 1

    # 5. Awards Items
    cursor.execute('DELETE FROM awards_items')
    with open('awards.html', 'r', encoding='utf-8') as f:
        awards_html = f.read()

    award_cards = re.findall(r'<article class="award-rich-card">(.*?)</article>', awards_html, re.DOTALL)
    for i, ac in enumerate(award_cards):
        img_m = re.search(r'<img[^>]*src="([^"]+)"', ac)
        pill_m = re.search(r'<span class="award-badge-pill">([^<]+)</span>', ac)
        year_m = re.search(r'<span class="award-year-tag">([^<]+)</span>', ac)
        title_m = re.search(r'<h3 class="award-rich-title">([^<]+)</h3>', ac)
        desc_m = re.search(r'<p class="award-rich-desc">([^<]+)</p>', ac)
        link_m = re.search(r'<a href="([^"]+)"[^>]*class="award-rich-link">(.*?)</a>', ac, re.DOTALL)

        img = img_m.group(1).strip() if img_m else ''
        pill = pill_m.group(1).strip() if pill_m else 'Honors'
        year = year_m.group(1).strip() if year_m else '2026'
        title = title_m.group(1).strip() if title_m else f'Award {i+1}'
        desc = desc_m.group(1).strip() if desc_m else ''
        url = link_m.group(1).strip() if link_m else '#'
        link_text = re.sub(r'<[^>]+>', '', link_m.group(2)).strip() if link_m else 'Learn More'

        cursor.execute('''
        INSERT INTO awards_items (title, category_pill, year, image_url, description, link_text, link_url, sort_order)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, pill, year, img, desc, link_text, url, i))

    # 6. About Sections
    cursor.execute('DELETE FROM about_sections')
    about_data = {
        'etymology': {
            'tag': 'IDENTITY · ETYMOLOGY',
            'title': 'What "Aadya" Means to Me',
            'content': 'My name is rooted in ancient Sanskrit (आद्या), meaning "The First" and "The Primordial". In Indian tradition, it represents intentional agency, calm resilience, and the quiet responsibility to act before others do. To me, it has never meant finishing first in an easy race. It means being willing to take the very first step into uncomfortable, unpaved problems—whether that\'s diagnosing heavy-metal contamination in agricultural runoff or stepping up to code complex odometry splines under competition pressure.'
        },
        'quote': {
            'text': 'Nothing beats kindness. It sits quietly beyond all things.',
            'author': 'CHARLIE MACKESY, THE BOY, THE MOLE, THE FOX AND THE HORSE',
            'reflection': 'In high-velocity engineering, it\'s dangerously easy to obsess solely over performance—PID loops, velocity constraints, or sensor parts-per-million. This quote is my compass: technical rigor is hollow if it doesn\'t leave people feeling treated with gentleness and dignity.'
        },
        'books': [
            {'author': 'RICHARD FEYNMAN', 'title': 'The Pleasure of Finding Things Out', 'note': 'Taught me that genuine breakthroughs start with ruthless intellectual honesty and the unfiltered joy of asking why.'},
            {'author': 'JOHN LOCKE', 'title': 'Second Treatise of Government', 'note': 'Instilled the conviction that technological authority is only legitimate when it protects human dignity and fundamental equity.'},
            {'author': 'RACHEL CARSON', 'title': 'Silent Spring', 'note': 'Proved that meticulous empirical chemistry paired with urgent moral clarity has the power to shift a civilization\'s conscience.'}
        ],
        'five_things': [
            {'tag': '01 / ADRENALINE', 'title': '20-Foot Cliff Jump at Age 10', 'desc': 'Leaped off a 20-foot limestone cliff into the deep waters of Cenote Cristalino in Riviera Maya, Mexico. Love whitewater rafting and parasailing.'},
            {'tag': '02 / CULINARY CHEMISTRY', 'title': 'Avocado Buttercream', 'desc': 'Competed in a youth culinary contest and invented an "avocado buttercream" recipe that has become a permanent signature family dessert.'},
            {'tag': '03 / CONCERT HALLS', 'title': 'Solo at Manhattan School of Music', 'desc': 'Solo classical piano performance at Greenfield Hall, alongside first-chair flute in competitive regional orchestras.'},
            {'tag': '04 / COMMUNITY WORK', 'title': '3,500+ lbs of Food Packaged', 'desc': 'President of STEP For A Better World LEO Club, mobilizing youth cohorts to package emergency food supplies recognized by a NJ Legislative Citation.'},
            {'tag': '05 / PHILOSOPHY COMMENDATION', 'title': 'John Locke Essay Commendation', 'desc': 'Wrote commended critical essays exploring where algorithmic automation ends and human moral accountability begins.'}
        ]
    }

    for k, v in about_data.items():
        cursor.execute('INSERT OR REPLACE INTO about_sections (key, data_json) VALUES (?, ?)', (k, json.dumps(v)))

    conn.commit()
    conn.close()
    print("Content successfully seeded into database!")

if __name__ == '__main__':
    seed_content()

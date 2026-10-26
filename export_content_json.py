import sqlite3
import json

DB_PATH = 'database.sqlite'

def dump_content():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # settings
    c.execute('SELECT key, value FROM site_settings')
    settings = {row['key']: row['value'] for row in c.fetchall()}

    # portfolio
    c.execute('SELECT * FROM portfolio_items ORDER BY sort_order ASC, id ASC')
    portfolio = []
    for row in c.fetchall():
        portfolio.append({
            'id': row['id'],
            'title': row['title'],
            'category_slug': row['category_slug'],
            'category_name': row['category_name'],
            'img': row['img'],
            'images': json.loads(row['images_json']) if row['images_json'] else [],
            'desc': row['description'],
            'highlights': json.loads(row['highlights_json']) if row['highlights_json'] else [],
            'tags': json.loads(row['tags_json']) if row['tags_json'] else [],
            'badges': json.loads(row['badges_json']) if row['badges_json'] else [],
            'sections': json.loads(row['sections_json']) if ('sections_json' in row.keys() and row['sections_json']) else [],
            'hide_badges': bool(row['hide_badges']) if ('hide_badges' in row.keys() and row['hide_badges']) else False,
            'is_robotics': bool(row['is_robotics']),
            'sort_order': row['sort_order']
        })

    # documents
    c.execute('SELECT * FROM documents_items ORDER BY sort_order ASC, id ASC')
    documents = []
    for row in c.fetchall():
        documents.append({
            'id': row['id'],
            'title': row['title'],
            'category_pill': row['category_pill'],
            'eyebrow': row['eyebrow'],
            'accordions': json.loads(row['accordions_json']) if row['accordions_json'] else [],
            'sort_order': row['sort_order']
        })

    # memberships
    c.execute('SELECT * FROM memberships_items ORDER BY sort_order ASC, id ASC')
    memberships = []
    for row in c.fetchall():
        memberships.append({
            'id': row['id'],
            'org_name': row['org_name'],
            'badge_text': row['badge_text'],
            'badge_gradient': row['badge_gradient'],
            'website_label': row['website_label'],
            'role': row['role'],
            'url': row['url'],
            'sort_order': row['sort_order']
        })

    # awards
    c.execute('SELECT * FROM awards_items ORDER BY sort_order ASC, id ASC')
    awards = []
    for row in c.fetchall():
        awards.append({
            'id': row['id'],
            'title': row['title'],
            'category_pill': row['category_pill'],
            'year': row['year'],
            'image_url': row['image_url'],
            'description': row['description'],
            'link_text': row['link_text'],
            'link_url': row['link_url'],
            'sort_order': row['sort_order']
        })

    # about
    c.execute('SELECT key, data_json FROM about_sections')
    about = {row['key']: json.loads(row['data_json']) for row in c.fetchall()}

    # media
    c.execute('SELECT * FROM media_library ORDER BY id DESC')
    media = [dict(row) for row in c.fetchall()]

    conn.close()

    payload = {
        'settings': settings,
        'portfolio': portfolio,
        'documents': documents,
        'memberships': memberships,
        'awards': awards,
        'about': about,
        'media': media
    }

    with open('site_content.json', 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print("Exported site_content.json successfully!")

if __name__ == '__main__':
    dump_content()

import sqlite3
import json
import hashlib
import os

DB_PATH = 'database.sqlite'

def hash_password(password, salt="aadya_salt_2026"):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Admin users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 2. Sessions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        token TEXT PRIMARY KEY,
        user_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')

    # 3. Key-Value Settings (Hero, Site metadata, etc.)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS site_settings (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
    ''')

    # 4. Portfolio Projects table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS portfolio_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category_slug TEXT NOT NULL,
        category_name TEXT NOT NULL,
        img TEXT NOT NULL,
        images_json TEXT NOT NULL,
        description TEXT NOT NULL,
        highlights_json TEXT NOT NULL,
        tags_json TEXT NOT NULL,
        badges_json TEXT NOT NULL,
        is_robotics INTEGER DEFAULT 0,
        sort_order INTEGER DEFAULT 0
    )
    ''')

    # 5. Project Documents table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category_pill TEXT NOT NULL,
        eyebrow TEXT NOT NULL,
        accordions_json TEXT NOT NULL,
        sort_order INTEGER DEFAULT 0
    )
    ''')

    # 6. Memberships table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS memberships_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        org_name TEXT NOT NULL,
        badge_text TEXT NOT NULL,
        badge_gradient TEXT NOT NULL,
        website_label TEXT NOT NULL,
        role TEXT NOT NULL,
        url TEXT NOT NULL,
        sort_order INTEGER DEFAULT 0
    )
    ''')

    # 7. Awards table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS awards_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category_pill TEXT NOT NULL,
        year TEXT NOT NULL,
        image_url TEXT NOT NULL,
        description TEXT NOT NULL,
        link_text TEXT NOT NULL,
        link_url TEXT NOT NULL,
        sort_order INTEGER DEFAULT 0
    )
    ''')

    # 8. About sections table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS about_sections (
        key TEXT PRIMARY KEY,
        data_json TEXT NOT NULL
    )
    ''')

    # 9. Media library table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS media_library (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        url TEXT NOT NULL,
        size_bytes INTEGER DEFAULT 0,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Seed Admin User
    admin_email = 'aadyaagarwal.com'
    admin_pass = 'AADYA@FIVEPS'
    pass_hash = hash_password(admin_pass)

    cursor.execute('SELECT id FROM users WHERE email = ?', (admin_email,))
    user_row = cursor.fetchone()
    if not user_row:
        cursor.execute('INSERT INTO users (email, password_hash) VALUES (?, ?)', (admin_email, pass_hash))
        # Also add alias admin@aadyaagarwal.com for convenience
        cursor.execute('INSERT OR IGNORE INTO users (email, password_hash) VALUES (?, ?)', ('admin@aadyaagarwal.com', pass_hash))
    else:
        cursor.execute('UPDATE users SET password_hash = ? WHERE email = ?', (pass_hash, admin_email))
        cursor.execute('UPDATE users SET password_hash = ? WHERE email = ?', (pass_hash, 'admin@aadyaagarwal.com'))

    conn.commit()
    conn.close()
    print("Database schema created and admin credentials initialized.")

if __name__ == '__main__':
    init_database()

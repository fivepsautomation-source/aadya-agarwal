import http.server
import socketserver
import urllib.parse
import json
import sqlite3
import hashlib
import secrets
import os
import mimetypes
import re
import datetime

PORT = 8000
DB_PATH = 'database.sqlite'
UPLOAD_DIR = os.path.join('assets', 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password, salt="aadya_salt_2026"):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def verify_token(token):
    if not token:
        return False
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT user_id FROM sessions WHERE token = ?', (token,))
    row = c.fetchone()
    conn.close()
    return bool(row)

def parse_multipart(data, boundary):
    parts = {}
    files = []
    delimiter = ('--' + boundary).encode('utf-8')
    chunks = data.split(delimiter)
    for chunk in chunks:
        if not chunk or chunk == b'--\r\n' or chunk == b'--' or chunk == b'--\r\n\r\n':
            continue
        if b'\r\n\r\n' in chunk:
            header_bytes, body = chunk.split(b'\r\n\r\n', 1)
            if body.endswith(b'\r\n'):
                body = body[:-2]
            header_str = header_bytes.decode('utf-8', errors='ignore')
            if 'filename=' in header_str:
                fn_m = re.search(r'filename=["\']?([^"\'\r\n]+)', header_str)
                name_m = re.search(r'name=["\']?([^"\'\r\n;]+)', header_str)
                ct_m = re.search(r'Content-Type:\s*([^\r\n]+)', header_str, re.IGNORECASE)
                fn = fn_m.group(1) if fn_m else 'upload.bin'
                field_name = name_m.group(1) if name_m else 'file'
                ct = ct_m.group(1) if ct_m else 'application/octet-stream'
                files.append({'name': field_name, 'filename': fn, 'data': body, 'content_type': ct})
            else:
                name_m = re.search(r'name=["\']?([^"\'\r\n;]+)', header_str)
                if name_m:
                    parts[name_m.group(1)] = body.decode('utf-8', errors='ignore')
    return parts, files

class AdminCMSHandler(http.server.SimpleHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def get_auth_token(self):
        auth_header = self.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            return auth_header[7:].strip()
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)
        if 'token' in qs:
            return qs['token'][0]
        return None

    def require_auth(self):
        token = self.get_auth_token()
        if not verify_token(token):
            self.send_json({'error': 'Unauthorized', 'message': 'Invalid or expired session token.'}, 401)
            return False
        return True

    def read_json_body(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            raw = self.rfile.read(content_length)
            return json.loads(raw.decode('utf-8'))
        return {}

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # 1. API routes
        if path == '/api/auth/me':
            token = self.get_auth_token()
            if verify_token(token):
                self.send_json({'authenticated': True, 'email': 'aadyaagarwal.com'})
            else:
                self.send_json({'authenticated': False}, 401)
            return

        if path == '/api/content':
            conn = get_db()
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
                    'videos': json.loads(row['videos_json']) if ('videos_json' in row.keys() and row['videos_json']) else [],
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

            self.send_json({
                'settings': settings,
                'portfolio': portfolio,
                'documents': documents,
                'memberships': memberships,
                'awards': awards,
                'about': about,
                'media': media
            })
            return

        if path == '/api/media':
            conn = get_db()
            c = conn.cursor()
            c.execute('SELECT * FROM media_library ORDER BY id DESC')
            media = [dict(row) for row in c.fetchall()]
            conn.close()
            self.send_json({'media': media})
            return

        # Default static file serving
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # 1. Login
        if path == '/api/auth/login':
            data = self.read_json_body()
            email = (data.get('email') or '').strip().lower()
            password = data.get('password') or ''
            
            # Check target credentials
            target_emails = ['aadyaagarwal.com', 'admin@aadyaagarwal.com']
            target_pass = 'AADYA@FIVEPS'

            if email in target_emails and password == target_pass:
                token = secrets.token_hex(24)
                conn = get_db()
                c = conn.cursor()
                c.execute('SELECT id FROM users WHERE email IN (?, ?)', (target_emails[0], target_emails[1]))
                user_row = c.fetchone()
                user_id = user_row['id'] if user_row else 1
                c.execute('INSERT INTO sessions (token, user_id) VALUES (?, ?)', (token, user_id))
                conn.commit()
                conn.close()
                self.send_json({
                    'success': True,
                    'token': token,
                    'email': email,
                    'message': 'Login successful!'
                })
            else:
                self.send_json({
                    'success': False,
                    'error': 'Invalid email or password. Please verify your credentials.'
                }, 401)
            return

        # 2. Logout
        if path == '/api/auth/logout':
            token = self.get_auth_token()
            if token:
                conn = get_db()
                c = conn.cursor()
                c.execute('DELETE FROM sessions WHERE token = ?', (token,))
                conn.commit()
                conn.close()
            self.send_json({'success': True, 'message': 'Logged out successfully.'})
            return

        # All subsequent endpoints require valid authentication
        if not self.require_auth():
            return

        # 3. Update Settings
        if path == '/api/settings/update':
            data = self.read_json_body()
            conn = get_db()
            c = conn.cursor()
            for k, v in data.items():
                if isinstance(v, (list, dict)):
                    v = json.dumps(v)
                c.execute('INSERT OR REPLACE INTO site_settings (key, value) VALUES (?, ?)', (k, str(v)))
            conn.commit()
            conn.close()
            self.send_json({'success': True, 'message': 'Site settings updated.'})
            return

        # 4. Save Portfolio Item
        if path == '/api/portfolio/save':
            data = self.read_json_body()
            item_id = data.get('id')
            title = data.get('title', 'Untitled Project')
            cat_slug = data.get('category_slug', 'robotics')
            cat_name = data.get('category_name', 'Robotics & Coding')
            img = data.get('img', '')
            images = json.dumps(data.get('images', [img]))
            desc = data.get('desc', '')
            highlights = json.dumps(data.get('highlights', []))
            tags = json.dumps(data.get('tags', []))
            badges = json.dumps(data.get('badges', []))
            sections = json.dumps(data.get('sections', []))
            videos = json.dumps(data.get('videos', []))
            hide_badges = 1 if data.get('hide_badges') else 0
            is_rob = 1 if cat_slug == 'robotics' else 0
            sort_order = int(data.get('sort_order', 0))

            conn = get_db()
            c = conn.cursor()
            if item_id:
                c.execute('''
                UPDATE portfolio_items 
                SET title=?, category_slug=?, category_name=?, img=?, images_json=?, description=?, highlights_json=?, tags_json=?, badges_json=?, sections_json=?, videos_json=?, hide_badges=?, is_robotics=?, sort_order=?
                WHERE id=?
                ''', (title, cat_slug, cat_name, img, images, desc, highlights, tags, badges, sections, videos, hide_badges, is_rob, sort_order, item_id))
            else:
                c.execute('''
                INSERT INTO portfolio_items (title, category_slug, category_name, img, images_json, description, highlights_json, tags_json, badges_json, sections_json, videos_json, hide_badges, is_robotics, sort_order)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (title, cat_slug, cat_name, img, images, desc, highlights, tags, badges, sections, videos, hide_badges, is_rob, sort_order))
                item_id = c.lastrowid
            conn.commit()
            conn.close()
            self.send_json({'success': True, 'id': item_id, 'message': 'Portfolio project saved.'})
            return

        # 5. Delete Portfolio Item
        if path == '/api/portfolio/delete':
            data = self.read_json_body()
            item_id = data.get('id')
            if item_id:
                conn = get_db()
                c = conn.cursor()
                c.execute('DELETE FROM portfolio_items WHERE id = ?', (item_id,))
                conn.commit()
                conn.close()
            self.send_json({'success': True, 'message': 'Portfolio project deleted.'})
            return

        # 6. Save Document Item
        if path == '/api/documents/save':
            data = self.read_json_body()
            doc_id = data.get('id')
            title = data.get('title', '')
            category_pill = data.get('category_pill', 'Tech')
            eyebrow = data.get('eyebrow', '')
            accordions = json.dumps(data.get('accordions', []))
            sort_order = int(data.get('sort_order', 0))

            conn = get_db()
            c = conn.cursor()
            if doc_id:
                c.execute('UPDATE documents_items SET title=?, category_pill=?, eyebrow=?, accordions_json=?, sort_order=? WHERE id=?',
                          (title, category_pill, eyebrow, accordions, sort_order, doc_id))
            else:
                c.execute('INSERT INTO documents_items (title, category_pill, eyebrow, accordions_json, sort_order) VALUES (?, ?, ?, ?, ?)',
                          (title, category_pill, eyebrow, accordions, sort_order))
                doc_id = c.lastrowid
            conn.commit()
            conn.close()
            self.send_json({'success': True, 'id': doc_id, 'message': 'Document saved.'})
            return

        # 7. Delete Document Item
        if path == '/api/documents/delete':
            data = self.read_json_body()
            doc_id = data.get('id')
            if doc_id:
                conn = get_db()
                c = conn.cursor()
                c.execute('DELETE FROM documents_items WHERE id = ?', (doc_id,))
                conn.commit()
                conn.close()
            self.send_json({'success': True, 'message': 'Document deleted.'})
            return

        # 8. Save Membership Item
        if path == '/api/memberships/save':
            data = self.read_json_body()
            mem_id = data.get('id')
            org_name = data.get('org_name', '')
            badge_text = data.get('badge_text', org_name[:3].upper())
            badge_gradient = data.get('badge_gradient', 'linear-gradient(135deg, #3b122d, #ba1f43)')
            website_label = data.get('website_label', org_name)
            role = data.get('role', 'Member')
            url = data.get('url', '#')
            sort_order = int(data.get('sort_order', 0))

            conn = get_db()
            c = conn.cursor()
            if mem_id:
                c.execute('''
                UPDATE memberships_items SET org_name=?, badge_text=?, badge_gradient=?, website_label=?, role=?, url=?, sort_order=? WHERE id=?
                ''', (org_name, badge_text, badge_gradient, website_label, role, url, sort_order, mem_id))
            else:
                c.execute('''
                INSERT INTO memberships_items (org_name, badge_text, badge_gradient, website_label, role, url, sort_order)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (org_name, badge_text, badge_gradient, website_label, role, url, sort_order))
                mem_id = c.lastrowid
            conn.commit()
            conn.close()
            self.send_json({'success': True, 'id': mem_id, 'message': 'Membership saved.'})
            return

        # 9. Delete Membership Item
        if path == '/api/memberships/delete':
            data = self.read_json_body()
            mem_id = data.get('id')
            if mem_id:
                conn = get_db()
                c = conn.cursor()
                c.execute('DELETE FROM memberships_items WHERE id = ?', (mem_id,))
                conn.commit()
                conn.close()
            self.send_json({'success': True, 'message': 'Membership deleted.'})
            return

        # 10. Save Award Item
        if path == '/api/awards/save':
            data = self.read_json_body()
            aw_id = data.get('id')
            title = data.get('title', '')
            category_pill = data.get('category_pill', 'Honors')
            year = data.get('year', '2026')
            image_url = data.get('image_url', '')
            description = data.get('description', '')
            link_text = data.get('link_text', 'Learn More')
            link_url = data.get('link_url', '#')
            sort_order = int(data.get('sort_order', 0))

            conn = get_db()
            c = conn.cursor()
            if aw_id:
                c.execute('''
                UPDATE awards_items SET title=?, category_pill=?, year=?, image_url=?, description=?, link_text=?, link_url=?, sort_order=? WHERE id=?
                ''', (title, category_pill, year, image_url, description, link_text, link_url, sort_order, aw_id))
            else:
                c.execute('''
                INSERT INTO awards_items (title, category_pill, year, image_url, description, link_text, link_url, sort_order)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (title, category_pill, year, image_url, description, link_text, link_url, sort_order))
                aw_id = c.lastrowid
            conn.commit()
            conn.close()
            self.send_json({'success': True, 'id': aw_id, 'message': 'Award saved.'})
            return

        # 11. Delete Award Item
        if path == '/api/awards/delete':
            data = self.read_json_body()
            aw_id = data.get('id')
            if aw_id:
                conn = get_db()
                c = conn.cursor()
                c.execute('DELETE FROM awards_items WHERE id = ?', (aw_id,))
                conn.commit()
                conn.close()
            self.send_json({'success': True, 'message': 'Award deleted.'})
            return

        # 12. Save About Section
        if path == '/api/about/save':
            data = self.read_json_body()
            key = data.get('key')
            val = data.get('data')
            if key and val is not None:
                conn = get_db()
                c = conn.cursor()
                c.execute('INSERT OR REPLACE INTO about_sections (key, data_json) VALUES (?, ?)', (key, json.dumps(val)))
                conn.commit()
                conn.close()
            self.send_json({'success': True, 'message': 'About section updated.'})
            return

        # 13. Image / File Upload
        if path == '/api/upload':
            content_type = self.headers.get('Content-Type', '')
            content_length = int(self.headers.get('Content-Length', 0))

            # Handle base64 JSON payload
            if 'application/json' in content_type:
                data = self.read_json_body()
                b64_data = data.get('base64', '')
                orig_name = data.get('filename', 'uploaded_image.jpg')
                if ',' in b64_data:
                    b64_data = b64_data.split(',', 1)[1]
                import base64
                file_bytes = base64.b64decode(b64_data)
                
                safe_name = re.sub(r'[^a-zA-Z0-9_\.-]', '_', orig_name)
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                final_filename = f"{timestamp}_{safe_name}"
                dest_path = os.path.join(UPLOAD_DIR, final_filename)
                
                with open(dest_path, 'wb') as f:
                    f.write(file_bytes)
                
                public_url = f"assets/uploads/{final_filename}"
                conn = get_db()
                c = conn.cursor()
                c.execute('INSERT INTO media_library (filename, url, size_bytes) VALUES (?, ?, ?)',
                          (final_filename, public_url, len(file_bytes)))
                conn.commit()
                conn.close()

                self.send_json({
                    'success': True,
                    'url': public_url,
                    'filename': final_filename,
                    'size': len(file_bytes),
                    'message': 'Image uploaded and saved to database!'
                })
                return

            # Handle standard multipart/form-data
            if 'multipart/form-data' in content_type:
                boundary = content_type.split('boundary=')[-1].strip()
                raw_data = self.rfile.read(content_length)
                parts, files = parse_multipart(raw_data, boundary)
                if not files:
                    self.send_json({'error': 'No file uploaded'}, 400)
                    return
                
                f_item = files[0]
                orig_name = f_item['filename']
                file_bytes = f_item['data']

                safe_name = re.sub(r'[^a-zA-Z0-9_\.-]', '_', orig_name)
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                final_filename = f"{timestamp}_{safe_name}"
                dest_path = os.path.join(UPLOAD_DIR, final_filename)

                with open(dest_path, 'wb') as f:
                    f.write(file_bytes)

                public_url = f"assets/uploads/{final_filename}"
                conn = get_db()
                c = conn.cursor()
                c.execute('INSERT INTO media_library (filename, url, size_bytes) VALUES (?, ?, ?)',
                          (final_filename, public_url, len(file_bytes)))
                conn.commit()
                conn.close()

                self.send_json({
                    'success': True,
                    'url': public_url,
                    'filename': final_filename,
                    'size': len(file_bytes),
                    'message': 'Image uploaded and saved to database!'
                })
                return

            self.send_json({'error': 'Unsupported upload content type'}, 400)
            return

        # 14. Delete Media
        if path == '/api/media/delete':
            data = self.read_json_body()
            media_id = data.get('id')
            url = data.get('url')
            if media_id or url:
                conn = get_db()
                c = conn.cursor()
                if media_id:
                    c.execute('SELECT url FROM media_library WHERE id = ?', (media_id,))
                    row = c.fetchone()
                    if row:
                        url = row['url']
                    c.execute('DELETE FROM media_library WHERE id = ?', (media_id,))
                elif url:
                    c.execute('DELETE FROM media_library WHERE url = ?', (url,))
                conn.commit()
                conn.close()

                if url and url.startswith('assets/uploads/'):
                    disk_path = os.path.join('.', url)
                    if os.path.exists(disk_path):
                        try:
                            os.remove(disk_path)
                        except Exception:
                            pass
            self.send_json({'success': True, 'message': 'Media deleted.'})
            return

        # 15. Publish / Sync to Static HTML Files
        if path == '/api/publish':
            try:
                import sync_html
                sync_html.sync_all_from_db()
                self.send_json({'success': True, 'message': 'All site pages successfully synchronized and published!'})
            except Exception as e:
                self.send_json({'success': False, 'error': str(e)}, 500)
            return

        self.send_json({'error': 'Endpoint not found'}, 404)

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

def run_server():
    server = ThreadingHTTPServer(("", PORT), AdminCMSHandler)
    print(f"Server started on http://localhost:{PORT}/")
    print(f"Admin portal available at http://localhost:{PORT}/admin.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == '__main__':
    run_server()

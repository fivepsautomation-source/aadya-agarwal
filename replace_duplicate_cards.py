with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Card 12
old_card_12 = '''<div class="evidence-card" data-category="awards">
            <div class="evidence-thumb-wrapper" onclick="openMediaModal({ title: 'Lions Club District Governor Award', desc: 'Recognition by District Governor for exceptional youth community leadership.', badge: 'District Governor Honors', type: 'image', src: 'assets/certificates/Service Award - NJ State Assembly.jpeg' })">
              <img src="assets/certificates/Service Award - NJ State Assembly.jpeg" alt="District Governor Award" class="evidence-thumb-img">
              <div class="evidence-thumb-overlay"><span class="evidence-zoom-icon">Inspect High-Res &rarr;</span></div>
              <span class="evidence-source-tag">Folder: Community Social Service</span>
            </div>
            <div class="evidence-card-content">
              <span class="evidence-cat-tag" style="color: #D97706;">Civic Honors &bull; Lions Club</span>
              <h4 class="evidence-item-title">District Governor Leadership Award</h4>
              <p class="evidence-item-meta">Lions Club International &bull; District 16-N Honors</p>
            </div>
          </div>'''

new_card_12 = '''<div class="evidence-card" data-category="community">
            <div class="evidence-thumb-wrapper" onclick="openMediaModal({ title: 'State Senate & Assembly Civic Leadership', desc: 'Aadya presenting youth community drives at the New Jersey State Senate House.', badge: 'Legislative Civic Honors', type: 'image', src: 'assets/community/Sock Drive - NJ AssemblyWoman-NJ State Senate House - photo2.jpg' })">
              <img src="assets/community/Sock Drive - NJ AssemblyWoman-NJ State Senate House - photo2.jpg" alt="State Senate Civic Leadership" class="evidence-thumb-img">
              <div class="evidence-thumb-overlay"><span class="evidence-zoom-icon">Inspect High-Res &rarr;</span></div>
              <span class="evidence-source-tag">Folder: Community Social Service</span>
            </div>
            <div class="evidence-card-content">
              <span class="evidence-cat-tag" style="color: #4F46E5;">Civic Action &bull; State Senate</span>
              <h4 class="evidence-item-title">State Senate &amp; Assembly Advocacy</h4>
              <p class="evidence-item-meta">15th Legislative District &bull; Community Drives</p>
            </div>
          </div>'''

# Replace Card 17
old_card_17 = '''<div class="evidence-card" data-category="arts">
            <div class="evidence-thumb-wrapper" onclick="openMediaModal({ title: 'Classical Piano Repertoire Mastery', desc: 'Mastering sonatinas and Chopin preludes during intensive coaching.', badge: 'Piano Studio', type: 'image', src: 'assets/writing_arts/piano_recital.jpg' })">
              <img src="assets/writing_arts/piano_recital.jpg" alt="Piano Studio Practice" class="evidence-thumb-img">
              <div class="evidence-thumb-overlay"><span class="evidence-zoom-icon">Inspect High-Res &rarr;</span></div>
              <span class="evidence-source-tag">Folder: Arts</span>
            </div>
            <div class="evidence-card-content">
              <span class="evidence-cat-tag" style="color: #7E22CE;">Fine Arts &bull; Classical Piano</span>
              <h4 class="evidence-item-title">Chopin &amp; Classical Repertoire Studies</h4>
              <p class="evidence-item-meta">Studio Coaching &bull; Advanced Keyboard Technique</p>
            </div>
          </div>'''

new_card_17 = '''<div class="evidence-card" data-category="arts">
            <div class="evidence-thumb-wrapper" onclick="openMediaModal({ title: 'Music-Fest International Grand Prize', desc: 'Grand Prize Winner for Piano Solo with performance at Greenfield Hall, Manhattan School of Music.', badge: 'International Grand Prize', type: 'image', src: 'assets/writing_arts/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg' })">
              <img src="assets/writing_arts/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg" alt="Music-Fest Grand Prize Recital" class="evidence-thumb-img">
              <div class="evidence-thumb-overlay"><span class="evidence-zoom-icon">Inspect High-Res &rarr;</span></div>
              <span class="evidence-source-tag">Folder: Writing &amp; Arts</span>
            </div>
            <div class="evidence-card-content">
              <span class="evidence-cat-tag" style="color: #7E22CE;">Fine Arts &bull; International Prize</span>
              <h4 class="evidence-item-title">Music-Fest Grand Prize Winner</h4>
              <p class="evidence-item-meta">Piano Solo &bull; Manhattan School Performance</p>
            </div>
          </div>'''

# Replace Card 19
old_card_19 = '''<div class="evidence-card" data-category="athletics">
            <div class="evidence-thumb-wrapper" onclick="openMediaModal({ title: 'Tennis Sportsmanship & Tournament Honors', desc: 'High-Performance Nike Tennis Camp sportsmanship and tournament honors.', badge: 'Tournament Honors', type: 'image', src: 'assets/athletics/tennis_action.jpg' })">
              <img src="assets/athletics/tennis_action.jpg" alt="Tennis Tournament Trophy" class="evidence-thumb-img">
              <div class="evidence-thumb-overlay"><span class="evidence-zoom-icon">Inspect High-Res &rarr;</span></div>
              <span class="evidence-source-tag">Folder: Athletics - Tennis</span>
            </div>
            <div class="evidence-card-content">
              <span class="evidence-cat-tag" style="color: #E11D48;">Athletics &bull; Awards</span>
              <h4 class="evidence-item-title">Nike High-Performance Award</h4>
              <p class="evidence-item-meta">Rafa Nadal &amp; Evert Tennis Academies Alum</p>
            </div>
          </div>'''

new_card_19 = '''<div class="evidence-card" data-category="athletics">
            <div class="evidence-thumb-wrapper" onclick="openMediaModal({ title: 'Alpine Downhill Ski Racing', desc: 'Competitive alpine downhill skiing developing agility, endurance, and physical focus.', badge: 'Varsity Athletics', type: 'image', src: 'assets/athletics/skiing.jpg' })">
              <img src="assets/athletics/skiing.jpg" alt="Alpine Downhill Skiing" class="evidence-thumb-img">
              <div class="evidence-thumb-overlay"><span class="evidence-zoom-icon">Inspect High-Res &rarr;</span></div>
              <span class="evidence-source-tag">Folder: Athletics</span>
            </div>
            <div class="evidence-card-content">
              <span class="evidence-cat-tag" style="color: #059669;">Athletics &bull; Alpine Skiing</span>
              <h4 class="evidence-item-title">Alpine Downhill Skiing &amp; Racing</h4>
              <p class="evidence-item-meta">Competitive Alpine Terrain &bull; Winter Athletics</p>
            </div>
          </div>'''

# Replace Card 23
old_card_23 = '''<div class="evidence-card" data-category="awards">
            <div class="evidence-thumb-wrapper" onclick="openMediaModal({ title: 'Melvin Jones Humanitarian Recognition', desc: 'Recognized for raising over $1,000 in direct emergency humanitarian relief.', badge: 'Melvin Jones Honors', type: 'image', src: 'assets/certificates/STEP Meals Packaging.jpeg' })">
              <img src="assets/certificates/STEP Meals Packaging.jpeg" alt="Melvin Jones Award" class="evidence-thumb-img">
              <div class="evidence-thumb-overlay"><span class="evidence-zoom-icon">Inspect High-Res &rarr;</span></div>
              <span class="evidence-source-tag">Folder: Awards &amp; Certs</span>
            </div>
            <div class="evidence-card-content">
              <span class="evidence-cat-tag" style="color: #D97706;">Humanitarian &bull; Lions International</span>
              <h4 class="evidence-item-title">Melvin Jones Humanitarian Honors</h4>
              <p class="evidence-item-meta">Lions Clubs International Foundation Recognition</p>
            </div>
          </div>'''

new_card_23 = '''<div class="evidence-card" data-category="awards">
            <div class="evidence-thumb-wrapper" onclick="openMediaModal({ title: 'United Nations Future of Service Award', desc: 'Honored at United Nations Headquarters NYC for youth mobilization and humanitarian leadership.', badge: 'UN Global Honors', type: 'image', src: 'assets/certificates/STEP UN Future of Service.jpeg' })">
              <img src="assets/certificates/STEP UN Future of Service.jpeg" alt="United Nations Future of Service Award" class="evidence-thumb-img">
              <div class="evidence-thumb-overlay"><span class="evidence-zoom-icon">Inspect High-Res &rarr;</span></div>
              <span class="evidence-source-tag">Folder: Awards &amp; Certs</span>
            </div>
            <div class="evidence-card-content">
              <span class="evidence-cat-tag" style="color: #D97706;">UN Global Honors &bull; Humanitarian</span>
              <h4 class="evidence-item-title">UN Future of Service Award</h4>
              <p class="evidence-item-meta">United Nations Headquarters NYC &bull; Youth Delegation</p>
            </div>
          </div>'''

replacements = [
    (old_card_12, new_card_12, "Card 12"),
    (old_card_17, new_card_17, "Card 17"),
    (old_card_19, new_card_19, "Card 19"),
    (old_card_23, new_card_23, "Card 23"),
]

for old, new, name in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        print(f"SUCCESS: Replaced {name}!")
    else:
        print(f"FAILED to find {name}!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

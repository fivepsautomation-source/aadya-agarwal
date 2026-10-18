with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Line 496 in stills section
old_still_item = """          <div class="still-item" onclick="openMediaModal({ title: 'BioResearch Lab Protocols', desc: 'Laboratory trials evaluating biochar adsorption efficiency for heavy metals and PFAS.', badge: 'Lab Certification', type: 'image', src: 'assets/certificates/BioResearch Academy Certificate.jpeg' })" style="cursor: pointer;">
            <img src="assets/certificates/BioResearch Academy Certificate.jpeg" alt="Biochar and Environmental Laboratory Research">
            <p class="still-caption">Empirical PFAS &amp; toxic lead adsorption trials with American Biochar Co.</p>
          </div>"""

new_still_item = """          <div class="still-item" onclick="openMediaModal({ title: 'Aqua Science & Biochar Remediation', desc: 'Laboratory trials evaluating biochar adsorption efficiency for heavy metals and PFAS.', badge: 'Water Science Certificate', type: 'image', src: 'assets/certificates/Aqua Science Certificate.jpg' })" style="cursor: pointer;">
            <img src="assets/certificates/Aqua Science Certificate.jpg" alt="Biochar and Environmental Laboratory Research">
            <p class="still-caption">Empirical PFAS &amp; toxic lead adsorption trials with American Biochar Co.</p>
          </div>"""

# 2. Line 540 in Curated tab item 02
old_tab_02 = """              <div class="curated-tab-item" 
                   data-image="assets/certificates/BioResearch Academy Certificate.jpeg" 
                   data-title="WATER ECO-ENGINEERING" 
                   data-desc="American Biochar Co. research featured on Ambiochar.com. 89.4% lead ion reduction and continuous PFAS filtration.">"""

new_tab_02 = """              <div class="curated-tab-item" 
                   data-image="assets/certificates/Aqua Science Certificate.jpg" 
                   data-title="WATER ECO-ENGINEERING" 
                   data-desc="American Biochar Co. research featured on Ambiochar.com. 89.4% lead ion reduction and continuous PFAS filtration.">"""

# 3. Line 568 in Curated tab item 04
old_tab_04 = """              <div class="curated-tab-item" 
                   data-image="assets/speaking/speech_stage.jpg" 
                   data-title="HUMANITIES &amp; ARTS" 
                   data-desc="Oxford John Locke Global Commendation (Top 3%), 3x published poet, and Chopin recital at Manhattan School of Music.">"""

new_tab_04 = """              <div class="curated-tab-item" 
                   data-image="assets/certificates/John Locke 2026 - High Commendation.jpg" 
                   data-title="HUMANITIES &amp; ARTS" 
                   data-desc="Oxford John Locke Global Commendation (Top 3%), 3x published poet, and Chopin recital at Manhattan School of Music.">"""

# 4. Line 926 in Feature 4
old_feat_04 = """            <div class="case-photo-frame" onclick="openMediaModal({ title: 'Humanities & Academic Writing Award', desc: 'Receiving academic recognition in humanities and scientific writing.', badge: 'Humanities Award', type: 'image', src: 'assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg' })" style="cursor: pointer;">
              <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Aadya Agarwal Receiving Humanities Award">
            </div>"""

new_feat_04 = """            <div class="case-photo-frame" onclick="openMediaModal({ title: 'Oxford John Locke Institute High Commendation', desc: 'High Commendation certificate in the global essay competition evaluated by Oxford and Princeton faculty.', badge: 'Oxford Global Award', type: 'image', src: 'assets/certificates/John Locke 2026 - High Commendation.jpg' })" style="cursor: pointer;">
              <img src="assets/certificates/John Locke 2026 - High Commendation.jpg" alt="Oxford John Locke Institute High Commendation">
            </div>"""

# 5. Elsewhere Card 3 (MIT Solve Buoy) and Card 5 (Oxford John Locke / Scholastic)
old_card_03 = """          <!-- 3. MIT Solve Buoy -->
          <a href="robotics.html" class="clip-card" style="border-top-color: #C0C852;">
            <div class="clip-card-photo-wrap">
              <img src="assets/robotics/Copy of Engg Device.jpg" alt="MIT Solve Buoy Hardware">
            </div>"""

new_card_03 = """          <!-- 3. MIT Solve Buoy -->
          <a href="robotics.html" class="clip-card" style="border-top-color: #C0C852;">
            <div class="clip-card-photo-wrap">
              <img src="assets/certificates/Day of AI Certificate - MIT RAISE.jpeg" alt="MIT Solve Buoy National Award">
            </div>"""

old_card_05 = """          <!-- 5. John Locke Oxford -->
          <a href="speaking-writing.html" class="clip-card" style="border-top-color: #92886F;">
            <div class="clip-card-photo-wrap">
              <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="John Locke Oxford Honors">
            </div>
            <h3 class="clip-card-title">Oxford John Locke</h3>
            <p class="clip-card-note">High Commendation global essay competition &amp; 3x published anthology poet.</p>
            <span class="clip-card-action">Read Essay <span class="arrow">&rarr;</span></span>
          </a>"""

new_card_05 = """          <!-- 5. John Locke Oxford -->
          <a href="speaking-writing.html" class="clip-card" style="border-top-color: #92886F;">
            <div class="clip-card-photo-wrap">
              <img src="assets/certificates/Scholastic_Poetry_Silver_Key_Certificate.jpg" alt="Scholastic Art and Writing Awards Silver Key">
            </div>
            <h3 class="clip-card-title">Scholastic Silver Key</h3>
            <p class="clip-card-note">National Silver Key in Poetry &amp; Oxford John Locke Global Commendation.</p>
            <span class="clip-card-action">Read Poetry <span class="arrow">&rarr;</span></span>
          </a>"""

checks = [
    ("Check 1 (stills)", old_still_item in content),
    ("Check 2 (tab 02)", old_tab_02 in content),
    ("Check 3 (tab 04)", old_tab_04 in content),
    ("Check 4 (feat 04)", old_feat_04 in content),
    ("Check 5 (card 03)", old_card_03 in content),
    ("Check 6 (card 05)", old_card_05 in content),
]

for name, res in checks:
    print(f"{name}: {res}")

if all(c[1] for c in checks):
    content = content.replace(old_still_item, new_still_item)
    content = content.replace(old_tab_02, new_tab_02)
    content = content.replace(old_tab_04, new_tab_04)
    content = content.replace(old_feat_04, new_feat_04)
    content = content.replace(old_card_03, new_card_03)
    content = content.replace(old_card_05, new_card_05)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated index.html!")
else:
    print("ERROR: One or more checks failed.")

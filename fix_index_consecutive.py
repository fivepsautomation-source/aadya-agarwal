with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_expanding = '''          <div class="expanding-strip-panel active">
            <img src="assets/robotics/pic 1 - with robot.jpg" alt="Robotics Autonomy">
            <div class="strip-panel-overlay">
              <span class="strip-panel-badge">FIRST Robotics</span>
              <h3 class="strip-panel-title">AUTONOMOUS ROBOT</h3>
              <p class="strip-panel-desc">WPI International #14. Precision Bezier curve trajectory tracking &amp; dual AprilTag cameras.</p>
            </div>
          </div>

          <div class="expanding-strip-panel">
            <img src="assets/certificates/BioResearch Academy Certificate.jpeg" alt="Water &amp; BioResearch">
            <div class="strip-panel-overlay">
              <span class="strip-panel-badge">Eco-Engineering</span>
              <h3 class="strip-panel-title">BIOCHAR FILTRATION</h3>
              <p class="strip-panel-desc">Empirical stormwater PFAS and heavy metal sequestration research featured on Ambiochar.com.</p>
            </div>
          </div>'''

new_expanding = '''          <div class="expanding-strip-panel active">
            <img src="assets/robotics/pic12 -WPI Team.png" alt="WPI Championship Team">
            <div class="strip-panel-overlay">
              <span class="strip-panel-badge">FIRST Robotics</span>
              <h3 class="strip-panel-title">WPI WORLD CHAMPIONSHIP</h3>
              <p class="strip-panel-desc">World Rank #14 of 108 international teams. Precision Bezier trajectory tracking &amp; dual AprilTag cameras.</p>
            </div>
          </div>

          <div class="expanding-strip-panel">
            <img src="assets/certificates/Aqua Science Certificate.jpg" alt="Water &amp; Biochar Research">
            <div class="strip-panel-overlay">
              <span class="strip-panel-badge">Eco-Engineering</span>
              <h3 class="strip-panel-title">BIOCHAR FILTRATION</h3>
              <p class="strip-panel-desc">Empirical stormwater PFAS and heavy metal sequestration research featured on Ambiochar.com.</p>
            </div>
          </div>'''

if old_expanding in text:
    text = text.replace(old_expanding, new_expanding, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: index.html expanding strips updated with unique images!")
else:
    print("FAILED: old_expanding not found in index.html")

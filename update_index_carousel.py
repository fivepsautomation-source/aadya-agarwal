with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

new_cards = '''<div class="gallery-carousel-track">
            <div class="gallery-card evidence-link" data-src="assets/robotics/pic 10 - wpi award.jpg" data-title="WPI US Open World #14 Trophy" data-badge="Robotics" data-caption="Robot Design Award Finalist among 108 international teams">
              <img src="assets/robotics/pic 10 - wpi award.jpg" alt="WPI US Open World #14 Trophy" loading="lazy">
              <div class="gallery-card-overlay">
                <span class="gallery-card-tag">Robotics</span>
                <h4 class="gallery-card-title">WPI US Open Trophy</h4>
                <p class="gallery-card-sub">World Rank #14 &bull; 108 international teams</p>
              </div>
            </div>
            <div class="gallery-card evidence-link" data-src="assets/certificates/Day of AI Certificate - MIT RAISE.jpeg" data-title="MIT Solve Top 5 National Winner" data-badge="AI &amp; Water IoT" data-caption="National recognition at MIT Media Lab for real-time water quality monitoring">
              <img src="assets/certificates/Day of AI Certificate - MIT RAISE.jpeg" alt="MIT Solve Top 5 National Winner" loading="lazy">
              <div class="gallery-card-overlay">
                <span class="gallery-card-tag">AI &amp; Water IoT</span>
                <h4 class="gallery-card-title">MIT Solve National Winner</h4>
                <p class="gallery-card-sub">Top 5 across USA &bull; MIT Media Lab</p>
              </div>
            </div>
            <div class="gallery-card evidence-link" data-src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" data-title="John H. Imbrie Humanities Award" data-badge="Lawrenceville School" data-caption="Highest English &amp; humanities distinction awarded to top 9th grade scholar">
              <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="John H. Imbrie Humanities Award" loading="lazy">
              <div class="gallery-card-overlay">
                <span class="gallery-card-tag">Lawrenceville School</span>
                <h4 class="gallery-card-title">Imbrie Humanities Award</h4>
                <p class="gallery-card-sub">Top 9th grade English &amp; humanities honor</p>
              </div>
            </div>
            <div class="gallery-card evidence-link" data-src="assets/certificates/Service Award - NJ State Assembly.jpeg" data-title="NJ Legislative Resolution" data-badge="Civic Leadership" data-caption="Official commendation by 15th Legislative District for 150k+ meals &amp; youth advocacy">
              <img src="assets/certificates/Service Award - NJ State Assembly.jpeg" alt="NJ Legislative Resolution" loading="lazy">
              <div class="gallery-card-overlay">
                <span class="gallery-card-tag">Civic Leadership</span>
                <h4 class="gallery-card-title">NJ Legislative Resolution</h4>
                <p class="gallery-card-sub">Honored by NJ General Assembly</p>
              </div>
            </div>
            <div class="gallery-card evidence-link" data-src="assets/certificates/STEP Meals Packaging.jpeg" data-title="150,624 Meals Packaged" data-badge="STEP LEO Club" data-caption="Mobilized 350+ volunteers and hunger relief partner agencies">
              <img src="assets/certificates/STEP Meals Packaging.jpeg" alt="150,624 Meals Packaged" loading="lazy">
              <div class="gallery-card-overlay">
                <span class="gallery-card-tag">STEP LEO Club</span>
                <h4 class="gallery-card-title">150,624 Meals Packaged</h4>
                <p class="gallery-card-sub">Project Hunger &bull; Melvin Jones Fellow</p>
              </div>
            </div>
            <div class="gallery-card evidence-link" data-src="assets/certificates/Award Certificate - NSF PS1 contest .jpg" data-title="1st Place National Speech Champion" data-badge="Public Speaking" data-caption="National Champion at North South Foundation Public Speaking Championship">
              <img src="assets/certificates/Award Certificate - NSF PS1 contest .jpg" alt="1st Place National Speech Champion" loading="lazy">
              <div class="gallery-card-overlay">
                <span class="gallery-card-tag">Public Speaking</span>
                <h4 class="gallery-card-title">National Speech 1st Place</h4>
                <p class="gallery-card-sub">North South Foundation Champion</p>
              </div>
            </div>
            <div class="gallery-card evidence-link" data-src="assets/certificates/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg" data-title="Music-Fest Grand Prize Winner" data-badge="Fine Arts" data-caption="Piano Solo Grand Prize and Manhattan School of Music recital">
              <img src="assets/certificates/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg" alt="Music-Fest Grand Prize Winner" loading="lazy">
              <div class="gallery-card-overlay">
                <span class="gallery-card-tag">Fine Arts</span>
                <h4 class="gallery-card-title">Music-Fest Grand Prize</h4>
                <p class="gallery-card-sub">Piano Solo &bull; Manhattan School Performance</p>
              </div>
            </div>
            <div class="gallery-card evidence-link" data-src="assets/robotics/pic 1 - with robot.jpg" data-title="FTC BioBuzz Autonomous Robot" data-badge="Robotics" data-caption="Custom odometry, Pedro Pathing, and Limelight 3G visual pipeline">
              <img src="assets/robotics/pic 1 - with robot.jpg" alt="FTC BioBuzz Autonomous Robot" loading="lazy">
              <div class="gallery-card-overlay">
                <span class="gallery-card-tag">Robotics</span>
                <h4 class="gallery-card-title">FTC BioBuzz Robot</h4>
                <p class="gallery-card-sub">Custom odometry &amp; Pedro Pathing</p>
              </div>
            </div>
          </div>'''

# Replace gallery-carousel-track
pattern = r'<div class="gallery-carousel-track">.*?</div>\s*(?=<button class="carousel-btn carousel-next")'
updated_html, count = re.subn(pattern, new_cards + '\n          ', html, flags=re.DOTALL)

if count == 1:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print("SUCCESS: index.html carousel updated successfully!")
else:
    print(f"FAILED: Match count was {count}")

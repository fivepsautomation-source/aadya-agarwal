with open('build_master_pages.py', 'r', encoding='utf-8') as f:
    bmp = f.read()

# 1. In impact_body: fix missing STEP Meals Packaging path
bmp = bmp.replace(
    'assets/community/STEP Meals Packaging.jpeg',
    'assets/certificates/STEP Meals Packaging.jpeg'
)

# 2. In research_body:
# Case 1: Biochar -> Aqua Science Certificate
bmp = bmp.replace(
    '''            <div class="case-photo-frame evidence-link" data-src="assets/certificates/BioResearch Academy Certificate.jpeg" data-title="BioResearch Academy Molecular Laboratory" data-badge="Harvard Academy" data-caption="BioResearch Academy certified laboratory techniques in molecular biology.">
              <img src="assets/certificates/BioResearch Academy Certificate.jpeg" alt="BioResearch Certificate">
            </div>''',
    '''            <div class="case-photo-frame evidence-link" data-src="assets/certificates/Aqua Science Certificate.jpg" data-title="Aqua Science &amp; Water Remediation Honors" data-badge="Water Science Award" data-caption="Aqua Science environmental research honors for heavy metal adsorption trials.">
              <img src="assets/certificates/Aqua Science Certificate.jpg" alt="Aqua Science Research Certificate">
            </div>'''
)

# Case 3: Harvard BioResearch -> BioResearch Academy Certificate (previously was Imbrie Humanities Award!)
bmp = bmp.replace(
    '''            <div class="case-photo-frame evidence-link" data-src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" data-title="Academic Distinction &amp; Laboratory Research" data-badge="Harvard BioResearch" data-caption="Academic distinction and laboratory research excellence.">
              <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Academic Distinction Ceremony">
            </div>''',
    '''            <div class="case-photo-frame evidence-link" data-src="assets/certificates/BioResearch Academy Certificate.jpeg" data-title="BioResearch Academy Molecular Laboratory" data-badge="Harvard Academy" data-caption="BioResearch Academy certified laboratory techniques in molecular biology with Prof. Sam Kunes.">
              <img src="assets/certificates/BioResearch Academy Certificate.jpeg" alt="Harvard BioResearch Certificate">
            </div>'''
)

# Case 4: scRNA-seq -> InspiritAI_AI_Scholars_Certificate.jpg
bmp = bmp.replace(
    '''            <div class="case-photo-frame evidence-link" data-src="assets/certificates/Copy of InspiritAI_AI_Scholars_Certificate_AadyaAgarwal.pdf" data-title="Inspirit AI Scholars Certification" data-badge="Machine Learning" data-caption="Stanford and MIT alumni-mentored deep learning research in oncology.">
              <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Inspirit AI Scholars Certification">
            </div>''',
    '''            <div class="case-photo-frame evidence-link" data-src="assets/certificates/InspiritAI_AI_Scholars_Certificate.jpg" data-title="Inspirit AI Scholars Certification" data-badge="Machine Learning" data-caption="Stanford and MIT alumni-mentored deep learning research in oncology.">
              <img src="assets/certificates/InspiritAI_AI_Scholars_Certificate.jpg" alt="Inspirit AI Scholars Certification">
            </div>'''
)

# 3. In beyond_body:
# Case 1: Oxford John Locke -> John Locke 2026 - High Commendation.jpg (previously was Imbrie Humanities Award!)
bmp = bmp.replace(
    '''            <div class="case-photo-frame evidence-link" data-src="assets/writing_arts/John Locke 2026 - High Commendation.pdf" data-title="Oxford John Locke Institute High Commendation" data-badge="Oxford Global Award" data-caption="Official High Commendation certificate from the Oxford John Locke Institute.">
              <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Oxford John Locke High Commendation">
            </div>''',
    '''            <div class="case-photo-frame evidence-link" data-src="assets/certificates/John Locke 2026 - High Commendation.jpg" data-title="Oxford John Locke Institute High Commendation" data-badge="Oxford Global Award" data-caption="Official High Commendation certificate from the Oxford John Locke Institute.">
              <img src="assets/certificates/John Locke 2026 - High Commendation.jpg" alt="Oxford John Locke High Commendation">
            </div>'''
)

# 4. In projects_body:
# Still 1: WPI Team photo instead of repeating pic 10
bmp = bmp.replace(
    '''          <div class="still-item evidence-link" data-src="assets/robotics/pic 10 - wpi award.jpg" data-title="WPI World Championship Award" data-badge="WPI World #14" data-caption="Holding the World Rank #14 Robot Design Award trophy.">
            <img src="assets/robotics/pic 10 - wpi award.jpg" alt="WPI FLL Robot Design Award">
            <p class="still-caption">WPI US Open World Rank #14 Robot Design Award</p>
          </div>''',
    '''          <div class="still-item evidence-link" data-src="assets/robotics/pic12 -WPI Team.png" data-title="WPI World Championship Team" data-badge="WPI World #14" data-caption="Team LeapcoderZ celebrating World Rank #14 at Worcester Polytechnic Institute.">
            <img src="assets/robotics/pic12 -WPI Team.png" alt="WPI FLL World Championship Team">
            <p class="still-caption">Team LeapcoderZ celebrating WPI World Rank #14</p>
          </div>'''
)

with open('build_master_pages.py', 'w', encoding='utf-8') as f:
    f.write(bmp)

print("SUCCESS: build_master_pages.py updated with unique authentic images!")

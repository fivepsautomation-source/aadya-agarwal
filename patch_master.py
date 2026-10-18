with open('build_master_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Projects body: replace duplicated pic 10 - wpi award in stills gallery
old_wpi_still = """<div class="still-item evidence-link" data-src="assets/robotics/pic 10 - wpi award.jpg" data-title="WPI US Open World Design Award Finalist" data-badge="World Tournament" data-caption="WPI FLL US Open Robot Design Award Finalist trophy ceremony.">
            <img src="assets/robotics/pic 10 - wpi award.jpg" alt="WPI FLL Robot Design Award">
            <p class="still-caption">WPI FLL US Open World Event: Robot Design Award Finalist Trophy</p>
          </div>"""

new_wpi_still = """<div class="still-item evidence-link" data-src="assets/robotics/pic12 -WPI Team.png" data-title="WPI US Open World Tournament Team" data-badge="World Tournament" data-caption="Aadya and the team at the WPI FLL US Open World Event celebrating their design recognition.">
            <img src="assets/robotics/pic12 -WPI Team.png" alt="WPI FLL Team Celebration">
            <p class="still-caption">WPI FLL US Open World Event: Team Celebration &amp; Pit Exhibition</p>
          </div>"""

# 2. Research Case 1: Biochar Water Filtration -> Aqua Science Certificate
old_res_c1 = """<div class="case-photo-frame evidence-link" data-src="assets/certificates/BioResearch Academy Certificate.jpeg" data-title="BioResearch Academy Certification" data-badge="Laboratory Certification" data-caption="BioResearch Academy molecular and environmental testing certification.">
            <img src="assets/certificates/BioResearch Academy Certificate.jpeg" alt="BioResearch Certificate">
          </div>"""

new_res_c1 = """<div class="case-photo-frame evidence-link" data-src="assets/certificates/Aqua Science Certificate.jpg" data-title="Aqua Science Project Certification" data-badge="Water Science &amp; Remediation" data-caption="Official Aqua Science Research Certification for Biochar Water Filtration and Adsorption Kinetics.">
            <img src="assets/certificates/Aqua Science Certificate.jpg" alt="Aqua Science Research Certificate">
          </div>"""

# 3. Research Case 3: Harvard BioResearch -> BioResearch Academy Certificate
old_res_c3 = """<div class="case-photo-frame evidence-link" data-src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" data-title="Academic Honors Ceremony" data-badge="Scholarly Distinction" data-caption="Aadya receiving academic honors at The Lawrenceville School.">
            <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Academic Distinction Ceremony">
          </div>"""

new_res_c3 = """<div class="case-photo-frame evidence-link" data-src="assets/certificates/BioResearch Academy Certificate.jpeg" data-title="Harvard BioResearch Academy Certification" data-badge="Laboratory Certification" data-caption="BioResearch Academy molecular diagnostics and CRISPR-Cas biotechnology laboratory certification.">
            <img src="assets/certificates/BioResearch Academy Certificate.jpeg" alt="BioResearch Academy Certificate">
          </div>"""

# 4. Research Case 4: Inspirit AI Scholars -> InspiritAI_AI_Scholars_Certificate.jpg
old_res_c4 = """<div class="case-photo-frame evidence-link" data-src="assets/certificates/Copy of InspiritAI_AI_Scholars_Certificate_AadyaAgarwal.pdf" data-title="AI Research Scholar Certification" data-badge="AI Scholars" data-caption="Inspirit AI Scholars Machine Learning Certification.">
            <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Inspirit AI Scholars Certification">
          </div>"""

new_res_c4 = """<div class="case-photo-frame evidence-link" data-src="assets/certificates/InspiritAI_AI_Scholars_Certificate.jpg" data-title="Inspirit AI Scholars Certification" data-badge="AI Scholars" data-caption="Inspirit AI Scholars Machine Learning &amp; Single-Cell RNA Sequencing Certification.">
            <img src="assets/certificates/InspiritAI_AI_Scholars_Certificate.jpg" alt="Inspirit AI Scholars Certification">
          </div>"""

# 5. Beyond Case 1: Oxford John Locke -> John Locke 2026 - High Commendation.jpg
old_bey_c1 = """<div class="case-photo-frame evidence-link" data-src="assets/writing_arts/John Locke 2026 - High Commendation.pdf" data-title="Oxford John Locke Institute High Commendation" data-badge="Oxford Global Award" data-caption="Official High Commendation certificate from the Oxford John Locke Institute.">
            <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Oxford John Locke High Commendation">
          </div>"""

new_bey_c1 = """<div class="case-photo-frame evidence-link" data-src="assets/certificates/John Locke 2026 - High Commendation.jpg" data-title="Oxford John Locke Institute High Commendation" data-badge="Oxford Global Award" data-caption="Official High Commendation certificate from the Oxford John Locke Institute.">
            <img src="assets/certificates/John Locke 2026 - High Commendation.jpg" alt="Oxford John Locke High Commendation">
          </div>"""

checks = [
    ("Check 1 (wpi still)", old_wpi_still in content),
    ("Check 2 (res c1)", old_res_c1 in content),
    ("Check 3 (res c3)", old_res_c3 in content),
    ("Check 4 (res c4)", old_res_c4 in content),
    ("Check 5 (bey c1)", old_bey_c1 in content),
]

for name, res in checks:
    print(f"{name}: {res}")

if all(c[1] for c in checks):
    content = content.replace(old_wpi_still, new_wpi_still)
    content = content.replace(old_res_c1, new_res_c1)
    content = content.replace(old_res_c3, new_res_c3)
    content = content.replace(old_res_c4, new_res_c4)
    content = content.replace(old_bey_c1, new_bey_c1)
    with open('build_master_pages.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated build_master_pages.py!")
else:
    print("ERROR: One or more checks failed.")

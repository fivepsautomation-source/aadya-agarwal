import re

sticky_section = '''    <!-- Editorial Memoir Feature (Sticky Layout inspired by rituguptagarg.in) -->
    <section class="editorial-case-study editorial-sticky-showcase" id="lawrencevilleExperience">
      <div class="container">
        <div class="case-study-grid">
          
          <!-- Sticky Left Photo Column -->
          <div class="sticky-photo-column">
            <div class="sticky-photo-frame evidence-link" data-src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" data-title="John H. Imbrie Award Ceremony" data-badge="Lawrenceville Award" data-caption="Aadya receiving the John H. Imbrie Humanities Award from the Head of School.">
              <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Receiving John H. Imbrie Award" loading="lazy">
              <div class="sticky-photo-meta">
                <span class="sticky-photo-tag">Lawrenceville Distinction</span>
                <span class="sticky-photo-zoom">Inspect Certificate &rarr;</span>
              </div>
            </div>
          </div>

          <!-- Scrolling Right Content Column -->
          <div class="scrolling-content-copy">
            <div class="scrolling-top-line">
              <span class="scrolling-line-rule"></span>
              <span class="scrolling-line-text">The Lawrenceville Experience &bull; Leadership &amp; Rigor</span>
            </div>

            <h2 class="scrolling-title">Curiosity, Rigor &amp; Discourse at the Harkness Table</h2>
            <p class="scrolling-subtitle">Elected House Academic Representative &bull; Leopold Scholar &bull; Big Data &amp; AI Club Co-Lead</p>

            <p class="scrolling-lead">
              At <strong>The Lawrenceville School</strong>, Aadya balances highest-level coursework (Pre-Calculus BC Honors, Calculus BC Honors, Accelerated Chemistry, Advanced Technical Design &amp; Fabrication, French, Biological &amp; Environmental Sciences) with extensive campus leadership and deep ethical inquiry:
            </p>

            <div class="scrolling-points-list">
              <div class="scrolling-point-item">
                <span class="point-dot"></span>
                <div class="point-text">
                  <strong>Leopold Scholar in Ecology and Ethics:</strong> Selected for a highly selective ecology, sustainability, and environmental-ethics research program studying stream ecology at the Stroud Water Research Center.
                </div>
              </div>

              <div class="scrolling-point-item">
                <span class="point-dot"></span>
                <div class="point-text">
                  <strong>Lawrenceville Rising Scholars Program:</strong> Chosen for leadership development and discussion-based seminar scholarship.
                </div>
              </div>

              <div class="scrolling-point-item">
                <span class="point-dot"></span>
                <div class="point-text">
                  <strong>John H. Imbrie Humanities / English Award:</strong> Recognized for excellence in English within the Humanities program, selected from 150 ninth-grade students.
                </div>
              </div>

              <div class="scrolling-point-item">
                <span class="point-dot"></span>
                <div class="point-text">
                  <strong>Elected Grade 9 House Academic Representative:</strong> Fostering supportive learning environments, organizing alumni panels, and collaborating with the Dean of Academics.
                </div>
              </div>

              <div class="scrolling-point-item">
                <span class="point-dot"></span>
                <div class="point-text">
                  <strong>Lawrenceville Environment &amp; Sustainability Council:</strong> Community Service &amp; Events Subcommittee Lead.
                </div>
              </div>

              <div class="scrolling-point-item">
                <span class="point-dot"></span>
                <div class="point-text">
                  <strong>Big Data and AI Club:</strong> Co-Lead; app developer creating the <em>Greeniculum</em> educational platform.
                </div>
              </div>

              <div class="scrolling-point-item">
                <span class="point-dot"></span>
                <div class="point-text">
                  <strong>Statistical Modeling for Social Impact:</strong> Partnered with a local farm to model solar energy generation parameters with machine learning.
                </div>
              </div>

              <div class="scrolling-point-item">
                <span class="point-dot"></span>
                <div class="point-text">
                  <strong>Lawrenceville TechTrek &amp; Science Reports:</strong> Contributing science writer and biology/chemistry editor.
                </div>
              </div>
            </div>

            <div class="scrolling-actions">
              <a href="#timeline" class="arrow-link">
                <span>View verified milestone chronology</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
              <a href="contact.html" class="arrow-link">
                <span>Academic counselor inquiry</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>'''

# 1. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_text = f.read()

pattern = r'<!-- Editorial Memoir Feature -->\s*<section class="editorial-case-study">.*?</section>'
new_about, count1 = re.subn(pattern, sticky_section, about_text, flags=re.DOTALL)
if count1 == 1:
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(new_about)
    print("SUCCESS: about.html updated with sticky showcase section!")
else:
    print(f"FAILED about.html: count is {count1}")

# 2. Update build_master_pages.py
with open('build_master_pages.py', 'r', encoding='utf-8') as f:
    bmp_text = f.read()

new_bmp, count2 = re.subn(pattern, sticky_section, bmp_text, flags=re.DOTALL)
if count2 == 1:
    with open('build_master_pages.py', 'w', encoding='utf-8') as f:
        f.write(new_bmp)
    print("SUCCESS: build_master_pages.py updated with sticky showcase section!")
else:
    print(f"FAILED build_master_pages.py: count is {count2}")

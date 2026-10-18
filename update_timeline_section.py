import re

new_timeline_css = '''/* ==========================================================================
   ENHANCED TIMELINE CHRONOLOGY CARDS (Boxed Editorial Style)
   ========================================================================== */
.clean-timeline-flow {
  position: relative;
  max-width: 860px;
  margin: 0 auto;
  padding-left: 48px;
  border-left: 3px solid rgba(62, 69, 44, 0.16);
}

.timeline-milestone-node {
  position: relative;
  background: #ffffff;
  border: 1px solid rgba(62, 69, 44, 0.14);
  border-radius: 20px;
  padding: 28px 32px;
  margin-bottom: 34px;
  box-shadow: 0 10px 30px rgba(10, 34, 24, 0.05), 0 2px 6px rgba(0, 0, 0, 0.02);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.timeline-milestone-node:last-child {
  margin-bottom: 0;
}

.timeline-milestone-node:hover {
  transform: translateY(-3px) translateX(4px);
  border-color: rgba(48, 96, 40, 0.35);
  box-shadow: 0 20px 48px rgba(10, 34, 24, 0.10);
}

.timeline-milestone-node::before {
  content: '';
  position: absolute;
  left: -58px;
  top: 30px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--c-forest);
  border: 4px solid #ffffff;
  box-shadow: 0 0 0 3px rgba(48, 96, 40, 0.25);
  transition: all 0.25s ease;
}

.timeline-milestone-node:hover::before {
  background: var(--c-writing);
  box-shadow: 0 0 0 5px rgba(192, 200, 82, 0.35);
  transform: scale(1.15);
}

.timeline-node-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.timeline-year-pill {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 800;
  color: #3b420a;
  background: rgba(192, 200, 82, 0.25);
  border: 1px solid rgba(192, 200, 82, 0.5);
  padding: 4px 14px;
  border-radius: 999px;
  display: inline-block;
  letter-spacing: 0.04em;
}

.timeline-era-tag {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--c-forest);
}

.timeline-node-title {
  font-family: var(--font-serif);
  font-size: 1.38rem;
  font-weight: 700;
  color: var(--c-dark-slate);
  line-height: 1.3;
  margin-bottom: 18px;
  letter-spacing: -0.01em;
}

/* Internal Items List */
.timeline-achievements-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.timeline-achievement-row {
  display: flex;
  align-items: baseline;
  gap: 14px;
  padding: 10px 14px;
  background: #fbfbf9;
  border: 1px solid rgba(62, 69, 44, 0.08);
  border-radius: 10px;
  transition: all 0.2s ease;
}

.timeline-achievement-row:hover {
  background: #ffffff;
  border-color: rgba(48, 96, 40, 0.22);
  box-shadow: 0 4px 12px rgba(10, 34, 24, 0.04);
  transform: translateX(3px);
}

.timeline-row-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--c-forest);
  background: rgba(48, 96, 40, 0.08);
  padding: 3px 8px;
  border-radius: 6px;
  white-space: nowrap;
  flex-shrink: 0;
}

.timeline-row-desc {
  font-size: 0.90rem;
  color: #3f3f46;
  line-height: 1.55;
}

.timeline-row-desc strong {
  color: var(--c-dark-slate);
}

.timeline-row-desc em {
  color: var(--c-forest);
  font-style: italic;
}

@media (max-width: 680px) {
  .clean-timeline-flow {
    padding-left: 28px;
  }
  .timeline-milestone-node {
    padding: 20px 18px;
  }
  .timeline-milestone-node::before {
    left: -37px;
    top: 24px;
  }
  .timeline-achievement-row {
    flex-direction: column;
    gap: 6px;
  }
}
'''

# 1. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace old timeline styles in styles.css
old_tl_pattern = r'/\* -+ \*/\s*\.clean-timeline-flow\s*\{.*?(?=\n/\*|\Z)'
if re.search(old_tl_pattern, css, re.DOTALL):
    css = re.sub(old_tl_pattern, new_timeline_css, css, flags=re.DOTALL)
    print("SUCCESS: Replaced old timeline CSS with new boxed timeline CSS!")
else:
    css += '\n' + new_timeline_css
    print("SUCCESS: Appended new boxed timeline CSS!")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Prepare new HTML for timeline
new_timeline_html = '''        <div class="clean-timeline-flow">
          
          <!-- 2026 Milestone Card -->
          <div class="timeline-milestone-node">
            <div class="timeline-node-header">
              <span class="timeline-year-pill">2026</span>
              <span class="timeline-era-tag">National Honors &bull; Global Scholarship</span>
            </div>
            <h3 class="timeline-node-title">MIT Solve National Winner, Stockholm Junior Water Prize &amp; Oxford Commendation</h3>
            <div class="timeline-achievements-list">
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">MIT Solve</span>
                <span class="timeline-row-desc">Top 5 National Winner in <em>AI for A Better World</em>; presented at MIT Media Lab.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">MSEF / ISEF</span>
                <span class="timeline-row-desc">U.S. Stockholm Junior Water Prize Regional Award (State Nominee), NOAA Pulse of the Planet Award, NJWEA Winner.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">IEEE ISEC</span>
                <span class="timeline-row-desc">Extended Abstract accepted for archival in IEEE Xplore; poster presentation at Princeton University.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Oxford John Locke</span>
                <span class="timeline-row-desc">Global High Commendation (Top 3% worldwide) in Science &amp; Technology.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Harvard HIR</span>
                <span class="timeline-row-desc">Bronze Medal in Harvard International Review (Technology &amp; Innovation).</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Stanford AIMI</span>
                <span class="timeline-row-desc">30-week Academic Year Research Internship in Medical AI &amp; Assistive Vision.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Harvard BioResearch</span>
                <span class="timeline-row-desc">24-week program and residential wet lab academy with Prof. Sam Kunes.</span>
              </div>
            </div>
          </div>

          <!-- 2025 Milestone Card -->
          <div class="timeline-milestone-node">
            <div class="timeline-node-header">
              <span class="timeline-year-pill">2025</span>
              <span class="timeline-era-tag">The Lawrenceville School &bull; Genomics</span>
            </div>
            <h3 class="timeline-node-title">The Lawrenceville School Leopold Scholar, Imbrie Award &amp; Cancer scRNA-seq</h3>
            <div class="timeline-achievements-list">
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Lawrenceville</span>
                <span class="timeline-row-desc">Selected as Leopold Scholar in Ecology &amp; Ethics; elected Grade 9 House Academic Representative.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Imbrie Award</span>
                <span class="timeline-row-desc">Winner of 9th-grade English Humanities distinction (selected from 150 students).</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Cambridge Cancer Lab</span>
                <span class="timeline-row-desc">12-week fellowship with Cambridge mentor Dr. Kristina Kordova (32 scRNA-seq biomarker clusters).</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">FTC Robotics</span>
                <span class="timeline-row-desc">Joined Lawrenceville FTC programming team for BioBuzz autonomous control &amp; Pedro Pathing.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">3M Young Scientist</span>
                <span class="timeline-row-desc">Autonomous ocean acidification pH-monitoring buoy state innovation commendation.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Scholastic Writing</span>
                <span class="timeline-row-desc">2 Silver Keys in Poetry; 4 Honorable Mentions in Personal Memoir.</span>
              </div>
            </div>
          </div>

          <!-- 2024 Milestone Card -->
          <div class="timeline-milestone-node">
            <div class="timeline-node-header">
              <span class="timeline-year-pill">2024</span>
              <span class="timeline-era-tag">World Tournament &bull; Civic Recognition</span>
            </div>
            <h3 class="timeline-node-title">WPI FLL US Open #14 in World, UN Award &amp; NJ General Assembly Citation</h3>
            <div class="timeline-achievements-list">
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">WPI US Open</span>
                <span class="timeline-row-desc">Ranked #14 of 108 international teams; Robot Design Award Finalist.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">United Nations</span>
                <span class="timeline-row-desc">Recipient of the UN Future of Service Award; attended UN HQ Conference in NYC.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">State of NJ</span>
                <span class="timeline-row-desc">Enacted General Assembly Legislative Resolution and Citation of Service (15th District).</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Project Hunger</span>
                <span class="timeline-row-desc">Coordinated volunteer effort packing 150,624 meals for regional food banks.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Music-Fest Grand Prize</span>
                <span class="timeline-row-desc">Grand Prize Winner for solo piano recital; Carnegie Hall invitation.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">MoniVitals.com</span>
                <span class="timeline-row-desc">Co-founded remote patient telehealth portal for telemetry monitoring.</span>
              </div>
            </div>
          </div>

          <!-- 2023 Milestone Card -->
          <div class="timeline-milestone-node">
            <div class="timeline-node-header">
              <span class="timeline-year-pill">2023</span>
              <span class="timeline-era-tag">State Championship &bull; Humanitarian</span>
            </div>
            <h3 class="timeline-node-title">FLL State Breakthrough Award, Melvin Jones Fellow &amp; Published Poetry</h3>
            <div class="timeline-achievements-list">
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">FLL NJ State</span>
                <span class="timeline-row-desc">Breakthrough Award Winner (Mt. Olive); 3rd Place Regional Qualifiers.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Lions International</span>
                <span class="timeline-row-desc">Melvin Jones Fellowship Award ($1,000 humanitarian commitment raised).</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Poetic Power</span>
                <span class="timeline-row-desc">Poems <em>In a Shift of Heart</em> and <em>Balance</em> published in national anthologies.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">American Biochar</span>
                <span class="timeline-row-desc">Research collaboration initiated on biochar water filtration and heavy metal binding.</span>
              </div>
            </div>
          </div>

          <!-- 2020 - 2022 Milestone Card -->
          <div class="timeline-milestone-node">
            <div class="timeline-node-header">
              <span class="timeline-year-pill">2020 &ndash; 2022</span>
              <span class="timeline-era-tag">National Oratory &bull; Early Robotics</span>
            </div>
            <h3 class="timeline-node-title">NSF National Public Speaking Champion &amp; FLL Robot Design Award</h3>
            <div class="timeline-achievements-list">
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">North South Foundation</span>
                <span class="timeline-row-desc">1st Place National Champion in Junior Public Speaking Championship.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">Toastmasters YLP</span>
                <span class="timeline-row-desc">Outstanding Communicator Award; model speech selected for district showcase.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">FLL Robotics</span>
                <span class="timeline-row-desc">Co-founded Team The LeapcoderZ; Robot Design Award at NJ Regionals.</span>
              </div>
              <div class="timeline-achievement-row">
                <span class="timeline-row-badge">The Telling Room</span>
                <span class="timeline-row-desc">Published story <em>When Kindness Was Planted</em> in youth literary journal.</span>
              </div>
            </div>
          </div>

        </div>'''

flow_pattern = r'<div class="clean-timeline-flow">.*?</div>\s*</div>\s*</section>'

# 3. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_h = f.read()

new_about_h, count_a = re.subn(flow_pattern, new_timeline_html + '\n      </div>\n    </section>', about_h, flags=re.DOTALL)
if count_a == 1:
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(new_about_h)
    print("SUCCESS: about.html updated with boxed timeline cards!")
else:
    print(f"FAILED about.html: count is {count_a}")

# 4. Update build_master_pages.py
with open('build_master_pages.py', 'r', encoding='utf-8') as f:
    bmp_h = f.read()

new_bmp_h, count_b = re.subn(flow_pattern, new_timeline_html + '\n      </div>\n    </section>', bmp_h, flags=re.DOTALL)
if count_b == 1:
    with open('build_master_pages.py', 'w', encoding='utf-8') as f:
        f.write(new_bmp_h)
    print("SUCCESS: build_master_pages.py updated with boxed timeline cards!")
else:
    print(f"FAILED build_master_pages.py: count is {count_b}")

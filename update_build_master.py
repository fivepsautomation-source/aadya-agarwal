with open('build_master_pages.py', 'r', encoding='utf-8') as f:
    content = f.read()

interactive_buttons_html = '''          <!-- Interactive Hero Action Buttons with Expanding Mega-Dropdowns -->
          <div class="hero-interactive-row" id="heroInteractiveRow">
            
            <!-- Projects Button & Mega Dropdown -->
            <div class="hero-dropdown-container" id="heroProjectsContainer">
              <button class="hero-interactive-btn hero-btn-projects" id="heroProjectsTrigger" aria-expanded="false" aria-haspopup="true">
                <span class="hero-btn-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                </span>
                <span class="hero-btn-label">Key Projects &amp; Systems</span>
                <span class="hero-btn-count">8 Innovations</span>
                <svg class="hero-btn-chevron" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </button>

              <!-- Mega Dropdown Panel -->
              <div class="hero-dropdown-panel hero-panel-projects" id="heroProjectsPanel" role="region" aria-label="Key Projects and Inventions">
                <div class="hero-panel-header">
                  <div class="hero-panel-header-text">
                    <span class="hero-panel-eyebrow">Engineering &bull; Telemetry &bull; Systems</span>
                    <h3 class="hero-panel-title">Autonomous &amp; Applied Innovations</h3>
                  </div>
                  <a href="projects.html" class="hero-panel-all-link">
                    <span>Full Catalog</span>
                    <span class="arrow">&rarr;</span>
                  </a>
                </div>

                <div class="hero-projects-grid">
                  <!-- Project 1: FTC BioBuzz -->
                  <div class="hero-proj-card">
                    <div class="hero-proj-top">
                      <span class="hero-proj-badge badge-robotics">FIRST Tech Challenge</span>
                      <span class="hero-proj-role">Lead Controls &amp; Odometry</span>
                    </div>
                    <h4 class="hero-proj-title">FTC BioBuzz Autonomous Controls</h4>
                    <p class="hero-proj-desc">Custom 3-dead-wheel localization, Pedro Pathing B&eacute;zier spline motion, and Limelight 3G neural machine vision on The Lawrenceville School team.</p>
                    <div class="hero-proj-links">
                      <a href="projects.html#ftc-biobuzz" class="hero-proj-nav-btn primary">
                        <span>Navigate to System</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                      </a>
                    </div>
                  </div>

                  <!-- Project 2: MIT Solve Buoy -->
                  <div class="hero-proj-card">
                    <div class="hero-proj-top">
                      <span class="hero-proj-badge badge-water">Top 5 USA &bull; MIT RAISE</span>
                      <span class="hero-proj-role">Hardware &amp; LoRaWAN</span>
                    </div>
                    <h4 class="hero-proj-title">MIT Solve AI IoT Ocean Buoy</h4>
                    <p class="hero-proj-desc">Solar marine telemetry package tracking multiparameter water contaminants in real time with mesh radio &amp; predictive anomaly detection.</p>
                    <div class="hero-proj-links">
                      <a href="research.html#mitBuoy" class="hero-proj-nav-btn primary">
                        <span>Navigate to Research</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                      </a>
                    </div>
                  </div>

                  <!-- Project 3: MoniVitals.com -->
                  <div class="hero-proj-card">
                    <div class="hero-proj-top">
                      <span class="hero-proj-badge badge-health">Production Telehealth</span>
                      <span class="hero-proj-role">Full-Stack &amp; Biometrics</span>
                    </div>
                    <h4 class="hero-proj-title">MoniVitals.com Telehealth Platform</h4>
                    <p class="hero-proj-desc">Remote patient monitoring dashboard processing dual-pipeline PPG cardiac telemetry, respiratory rate, and real-time clinical triage.</p>
                    <div class="hero-proj-links">
                      <a href="https://monivitals.com" target="_blank" rel="noopener noreferrer" class="hero-proj-nav-btn official">
                        <span>Official Platform</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                      </a>
                      <a href="projects.html#monivitals" class="hero-proj-nav-btn secondary">System Specs &rarr;</a>
                    </div>
                  </div>

                  <!-- Project 4: Ambiochar.com -->
                  <div class="hero-proj-card">
                    <div class="hero-proj-top">
                      <span class="hero-proj-badge badge-eco">Eco-Materials &bull; Water</span>
                      <span class="hero-proj-role">Filtration Research Lead</span>
                    </div>
                    <h4 class="hero-proj-title">American Biochar Co. (Ambiochar)</h4>
                    <p class="hero-proj-desc">Empirical microporous filtration media binding PFAS, microplastics, and agricultural nitrates to revitalize regional waterways.</p>
                    <div class="hero-proj-links">
                      <a href="https://ambiochar.com" target="_blank" rel="noopener noreferrer" class="hero-proj-nav-btn official">
                        <span>Official Partnership</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                      </a>
                      <a href="research.html#biochar" class="hero-proj-nav-btn secondary">Research Trials &rarr;</a>
                    </div>
                  </div>

                  <!-- Project 5: Stanford AIMI Vision AI -->
                  <div class="hero-proj-card">
                    <div class="hero-proj-top">
                      <span class="hero-proj-badge badge-ai">Stanford AIMI &bull; 30 Wks</span>
                      <span class="hero-proj-role">Computer Vision Fellow</span>
                    </div>
                    <h4 class="hero-proj-title">Assistive AI for Visually Impaired</h4>
                    <p class="hero-proj-desc">Real-time object detection, obstacle elevation mapping, and audio-spatial guidance engine designed for accessibility.</p>
                    <div class="hero-proj-links">
                      <a href="research.html#stanford" class="hero-proj-nav-btn primary">
                        <span>Navigate to Research</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                      </a>
                    </div>
                  </div>

                  <!-- Project 6: Cambridge scRNA-seq Explorer -->
                  <div class="hero-proj-card">
                    <div class="hero-proj-top">
                      <span class="hero-proj-badge badge-genomics">Transcriptomics</span>
                      <span class="hero-proj-role">Computational Biology</span>
                    </div>
                    <h4 class="hero-proj-title">Cambridge scRNA-seq Cancer Atlas</h4>
                    <p class="hero-proj-desc">Bioinformatic pipeline clustering 32 distinct cellular subpopulations to identify differential oncological lineage markers with Dr. Kristina Kordova.</p>
                    <div class="hero-proj-links">
                      <a href="research.html#scrna" class="hero-proj-nav-btn primary">
                        <span>Navigate to Atlas</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                      </a>
                    </div>
                  </div>

                  <!-- Project 7: 3M Young Scientist System -->
                  <div class="hero-proj-card">
                    <div class="hero-proj-top">
                      <span class="hero-proj-badge badge-hardware">3M State Finalist</span>
                      <span class="hero-proj-role">Acoustic &amp; Hardware</span>
                    </div>
                    <h4 class="hero-proj-title">3M Emergency Alert Telemetry</h4>
                    <p class="hero-proj-desc">Directional acoustic sensor array detecting emergency vehicle sirens and thermal spikes to notify drivers ahead of line-of-sight.</p>
                    <div class="hero-proj-links">
                      <a href="projects.html#3m" class="hero-proj-nav-btn primary">
                        <span>Navigate to Project</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                      </a>
                    </div>
                  </div>

                  <!-- Project 8: Project Hunger Supply Engine -->
                  <div class="hero-proj-card">
                    <div class="hero-proj-top">
                      <span class="hero-proj-badge badge-civic">150,624 Meals</span>
                      <span class="hero-proj-role">Operations &amp; Logistics Lead</span>
                    </div>
                    <h4 class="hero-proj-title">Project Hunger Supply Logistics</h4>
                    <p class="hero-proj-desc">End-to-end community distribution network mobilizing 350+ student volunteers to pack and deliver non-perishable food to urban shelters.</p>
                    <div class="hero-proj-links">
                      <a href="impact.html#stepLeo" class="hero-proj-nav-btn primary">
                        <span>Navigate to Impact</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Achievements Button & Mega Dropdown -->
            <div class="hero-dropdown-container" id="heroAchievementsContainer">
              <button class="hero-interactive-btn hero-btn-achievements" id="heroAchievementsTrigger" aria-expanded="false" aria-haspopup="true">
                <span class="hero-btn-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                </span>
                <span class="hero-btn-label">Honors &amp; Achievements</span>
                <span class="hero-btn-count">Top Awards</span>
                <svg class="hero-btn-chevron" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </button>

              <!-- Mega Dropdown Panel -->
              <div class="hero-dropdown-panel hero-panel-achievements" id="heroAchievementsPanel" role="region" aria-label="Verified Honors and Recognitions">
                <div class="hero-panel-header">
                  <div class="hero-panel-header-text">
                    <span class="hero-panel-eyebrow">Awards &bull; Accolades &bull; Distinctions</span>
                    <h3 class="hero-panel-title">Honors, Features &amp; Competitive Milestones</h3>
                  </div>
                  <a href="#timeline" class="hero-panel-all-link">
                    <span>Full Chronology</span>
                    <span class="arrow">&rarr;</span>
                  </a>
                </div>

                <div class="hero-achieve-categories">
                  
                  <!-- Category 1: Robotics & Engineering -->
                  <div class="hero-achieve-col">
                    <div class="hero-col-title">
                      <span class="hero-col-dot dot-robotics"></span>
                      <span>Robotics &amp; Autonomous Tech</span>
                    </div>
                    <ul class="hero-achieve-list">
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">WPI US Open World #14 Trophy</span>
                          <span class="achieve-pill pill-gold">World Rank #14</span>
                        </div>
                        <p class="achieve-desc">Robot Design Finalist out of 108 international teams from USA, Canada, &amp; Japan.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">FIRST Tech Challenge (BioBuzz)</span>
                          <span class="achieve-pill">State Qualifier</span>
                        </div>
                        <p class="achieve-desc">Lead autonomous programmer with Pedro Pathing B&eacute;zier motion &amp; custom odometry.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">3M Young Scientist Challenge</span>
                          <span class="achieve-pill">State Finalist</span>
                        </div>
                        <p class="achieve-desc">Recognition for real-time acoustic emergency response sensing innovation.</p>
                      </li>
                    </ul>
                  </div>

                  <!-- Category 2: Science & Water Research -->
                  <div class="hero-achieve-col">
                    <div class="hero-col-title">
                      <span class="hero-col-dot dot-water"></span>
                      <span>Water, Climate &amp; Medical AI</span>
                    </div>
                    <ul class="hero-achieve-list">
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">MIT Solve Day of AI National Winner</span>
                          <span class="achieve-pill pill-gold">Top 5 USA</span>
                        </div>
                        <p class="achieve-desc">National presentation at MIT Media Lab for real-time IoT ocean buoy.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">U.S. Stockholm Junior Water Prize</span>
                          <span class="achieve-pill">Regional Winner</span>
                        </div>
                        <p class="achieve-desc">Distinction in water science &amp; agricultural runoff adsorption.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">NOAA Pulse of the Planet Award</span>
                          <span class="achieve-pill">National Honor</span>
                        </div>
                        <p class="achieve-desc">Honored for coastal and environmental telemetry innovation.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">IEEE ISEC Princeton Publication</span>
                          <span class="achieve-pill">IEEE Xplore</span>
                        </div>
                        <p class="achieve-desc">Paper presented at Princeton University and indexed in IEEE Xplore.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">Stanford AIMI 30-Wk Fellowship</span>
                          <span class="achieve-pill">Academic Fellow</span>
                        </div>
                        <p class="achieve-desc">Deep learning and computer vision for visually impaired navigation.</p>
                      </li>
                    </ul>
                  </div>

                  <!-- Category 3: Civic, Writing & Arts -->
                  <div class="hero-achieve-col">
                    <div class="hero-col-title">
                      <span class="hero-col-dot dot-arts"></span>
                      <span>Civic, Humanities &amp; Fine Arts</span>
                    </div>
                    <ul class="hero-achieve-list">
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">UN Future of Service Award</span>
                          <span class="achieve-pill pill-gold">UN HQ NYC</span>
                        </div>
                        <p class="achieve-desc">Honored at United Nations Headquarters for youth mobilization &amp; service.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">NJ General Assembly Resolution</span>
                          <span class="achieve-pill">Legislative</span>
                        </div>
                        <p class="achieve-desc">Official commendation by 15th Legislative District for 150k+ meals packed.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">Oxford John Locke Commendation</span>
                          <span class="achieve-pill pill-gold">Top 3% Global</span>
                        </div>
                        <p class="achieve-desc">Global High Commendation evaluated by senior Oxford faculty.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">Music-Fest Grand Prize (Piano)</span>
                          <span class="achieve-pill">Carnegie Hall</span>
                        </div>
                        <p class="achieve-desc">Grand Prize Solo Recitalist with Carnegie Hall Weill Hall invitation.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">NSF 1st Place National Speech</span>
                          <span class="achieve-pill">1st in USA</span>
                        </div>
                        <p class="achieve-desc">National Champion at North South Foundation Public Speaking Championship.</p>
                      </li>
                      <li class="hero-achieve-item">
                        <div class="achieve-item-head">
                          <span class="achieve-title">John H. Imbrie Humanities Award</span>
                          <span class="achieve-pill">Lawrenceville</span>
                        </div>
                        <p class="achieve-desc">Top 9th grade English and humanities scholar of 150 students.</p>
                      </li>
                    </ul>
                  </div>

                </div>
              </div>
            </div>

          </div>'''

target = '''          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Class of '29</div>
              <div class="inner-metric-label">The Lawrenceville School</div>
              <div class="inner-metric-sub">Harkness table scholar</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Leopold Scholar</div>
              <div class="inner-metric-label">Ecology &amp; Ethics</div>
              <div class="inner-metric-sub">Research Institute fellow</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Imbrie Award</div>
              <div class="inner-metric-label">English Distinction</div>
              <div class="inner-metric-sub">Top 9th grade scholar of 150</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">House Rep</div>
              <div class="inner-metric-label">Academic Council</div>
              <div class="inner-metric-sub">Elected representative</div>
            </div>
          </div>'''

replacement = target + '\n\n' + interactive_buttons_html

if target in content:
    new_content = content.replace(target, replacement, 1)
    with open('build_master_pages.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: build_master_pages.py updated with interactive buttons!")
else:
    print("TARGET NOT FOUND in build_master_pages.py")

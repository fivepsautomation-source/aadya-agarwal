# build_master_pages.py
# Ingests authentic data from MASTER RESUME and builds rich, verified, credible pages

import os

with open('index.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

idx_main_start = home_html.find('<main id="mainContent">')
idx_footer_start = home_html.find('<footer class="site-footer">')

header_block = home_html[:idx_main_start]
footer_block = home_html[idx_footer_start:]

# ==============================================================================
# 1. PROJECTS.HTML
# ==============================================================================
projects_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>Technical Projects &amp; Autonomous Systems — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="Autonomous robotics, FTC BioBuzz, FLL WPI #14 World Design Award Finalist, MIT Solve IoT water sensor buoy, and MoniVitals.com.'
)

projects_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Technical Projects &bull; Autonomous Systems</span>
          <h1 class="inner-hero-title">High-Velocity <span class="italic-serif">Robotic Control</span>, Hardware &amp; Telehealth</h1>
          <p class="inner-hero-lead">
            Developing autonomous algorithms for The Lawrenceville School FTC Team (BioBuzz) using Pedro Pathing and Limelight vision, achieving Rank #14 in the World at the WPI FLL US Open, building MIT Solve's national winning IoT water buoy, and co-founding MoniVitals.com.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">#14 / 108</div>
              <div class="inner-metric-label">WPI US Open World</div>
              <div class="inner-metric-sub">Robot Design Award Finalist</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">FTC BioBuzz</div>
              <div class="inner-metric-label">Lawrenceville Team</div>
              <div class="inner-metric-sub">Pedro Pathing &amp; Limelight 3G</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Top 5 Winner</div>
              <div class="inner-metric-label">MIT Solve Challenge</div>
              <div class="inner-metric-sub">Biochar IoT Water Sensor Buoy</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">MoniVitals</div>
              <div class="inner-metric-label">Live Telehealth</div>
              <div class="inner-metric-sub">Real-time clinical dashboard</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Project 1: The Lawrenceville School FIRST Tech Challenge (FTC) -->
    <section class="editorial-case-study" id="ftc">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/pic 1 - with robot.jpg" data-title="Lawrenceville FTC Robotics Programming" data-badge="FTC Robotics" data-caption="Aadya with competition robot chassis at The Lawrenceville School.">
            <img src="assets/robotics/pic 1 - with robot.jpg" alt="Aadya with FTC Robot">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">01 &bull; The Lawrenceville School &bull; FIRST Tech Challenge (2025&ndash;Present)</p>
            <h2 class="case-title">FTC Programming Team: BioBuzz Autonomous Controls</h2>
            <p class="case-subtitle">Developing high-order Bézier splines with Pedro Pathing &amp; Limelight 3G machine vision pipelines.</p>
            <p class="case-body">
              Member of the programming team for <strong>The Lawrenceville School FIRST Tech Challenge Team</strong>. For the 2026&ndash;2027 FTC challenge theme of <em>BioBuzz</em>, Aadya develops and refines autonomous and driver-assisted motion control routines utilizing <strong>Pedro Pathing</strong> continuous-curvature trajectories. Built custom <strong>Limelight 3G</strong> computer vision pipelines for AprilTag field localization and real-time intake monitoring to eliminate drift.
            </p>
            <p class="case-body">
              <strong>Community Outreach:</strong> Spearheaded community STEM outreach, teaching robotics, algorithmic thinking, and foundational Python to 10&ndash;15 students at a local middle school across three hands-on interactive sessions.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Pedro Pathing</span>
                <span class="case-metric-desc">Bézier Splines</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Limelight 3G</span>
                <span class="case-metric-desc">AprilTag Vision</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">STEM Outreach</span>
                <span class="case-metric-desc">Middle School Coach</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="https://github.com/aanj1" target="_blank" rel="noopener noreferrer" class="arrow-link">
                <span>View GitHub Repositories</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Project 2: FLL The LeapcoderZ - WPI US Open World Finalist #14 -->
    <section class="editorial-case-study" id="fll" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">02 &bull; FIRST Lego League (FLL) &bull; Lead Coder &amp; Innovation Lead</p>
            <h2 class="case-title">WPI FLL US Open World: Rank #14 of 108 Teams</h2>
            <p class="case-subtitle">Robot Design Award Finalist at WPI World Event, NJ State Breakthrough Award &amp; 2x Regional Design Awards.</p>
            <p class="case-body">
              Served as Lead Coder &amp; Innovation Project Lead for team <em>The LeapcoderZ</em> (2020&ndash;2024). At the prestigious <strong>WPI FLL US Open World Event</strong> at Worcester Polytechnic Institute, MA (June 2024), Aadya led the team to place <strong>#14 out of 108 international teams</strong>, winning the <strong>Robot Design Award (Finalist)</strong>.
            </p>
            <p class="case-body">
              Her leadership also secured the <strong>Breakthrough Award</strong> at the NJ State Championship (2023&ndash;2024) and consecutive <strong>Robot Design Awards</strong> at the NJ Regional Qualifiers (2022&ndash;2023 and 2023&ndash;2024). Also won the <strong>Best Beginner Hack Award</strong> at the PDS Panther Hackathon (2024).
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">#14 / 108</span>
                <span class="case-metric-desc">WPI World Open</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Robot Design</span>
                <span class="case-metric-desc">World Finalist</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Breakthrough</span>
                <span class="case-metric-desc">NJ State Award</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="#roboticsEvidence" class="arrow-link">
                <span>View tournament trophies</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/pic 10 - wpi award.jpg" data-title="WPI US Open Robot Design Award Finalist" data-badge="World Tournament Trophy" data-caption="The LeapcoderZ with the WPI FLL US Open Robot Design Award Finalist trophy.">
            <img src="assets/robotics/pic 10 - wpi award.jpg" alt="WPI FLL US Open Robot Design Award">
          </div>
        </div>
      </div>
    </section>

    <!-- Project 3: MIT Solve National Winner -->
    <section class="editorial-case-study" id="mitSolve">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/Day of AI Certificate - MIT RAISE.jpeg" data-title="MIT Solve National Winner Certificate" data-badge="National Winner" data-caption="MIT Solve Top 5 National Winner presented at MIT Media Lab.">
            <img src="assets/certificates/Day of AI Certificate - MIT RAISE.jpeg" alt="MIT Solve Certificate">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">03 &bull; MIT Solve &bull; AI For A Better World Challenge (April 2026)</p>
            <h2 class="case-title">MIT Solve Top 5 National Winner: Biochar IoT Buoy</h2>
            <p class="case-subtitle">Presented at MIT Media Lab &bull; Featured in Lawrenceville School Magazine The Lawrentian.</p>
            <p class="case-body">
              Named one of only <strong>five national winning teams</strong> in the <strong>MIT Solve AI for A Better World Challenge</strong> (April 2026). Designed a biochar-based, AI-powered IoT device that continuously detects and remediates toxic water contamination. Aadya traveled to Cambridge, MA to present the project live at the <strong>MIT Media Lab</strong> before a distinguished panel of environmental and artificial intelligence experts. Featured prominently in <em>The Lawrentian</em>.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Top 5</span>
                <span class="case-metric-desc">National Winner</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">MIT Media Lab</span>
                <span class="case-metric-desc">Live Presentation</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">The Lawrentian</span>
                <span class="case-metric-desc">Magazine Feature</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="research.html#water" class="arrow-link">
                <span>View water research study</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Project 4: MoniVitals.com Telemedicine Platform -->
    <section class="editorial-case-study" id="monivitals" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">04 &bull; Clinical Telehealth &bull; Production Software</p>
            <h2 class="case-title">MoniVitals.com: Remote Patient Telemetry Portal</h2>
            <p class="case-subtitle">Live telemedicine application tracking heart rate, blood pressure, core temp, and SpO2 for underserved care.</p>
            <p class="case-body">
              Co-founder and lead engineer of <strong>MoniVitals.com</strong>, an active telehealth portal bridging hospital discharge and daily home patient monitoring. Streams real-time Bluetooth Low Energy (BLE) sensor telemetry into a physician dashboard with automated clinical threshold alert routing. Designed with a community-first mission to support low-income and rural patients who lack frequent in-person clinical access.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Live Web</span>
                <span class="case-metric-desc">MoniVitals.com</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">WebSocket</span>
                <span class="case-metric-desc">Real-Time Vitals</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Clinical Alert</span>
                <span class="case-metric-desc">Automated Routing</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="https://monivitals.com" target="_blank" rel="noopener noreferrer" class="arrow-link">
                <span>Visit MoniVitals.com</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/pic 20-devpost.jpg" data-title="MoniVitals Dashboard Platform" data-badge="Telemedicine" data-caption="Production patient vitals telemetry web platform.">
            <img src="assets/robotics/pic 20-devpost.jpg" alt="MoniVitals Dashboard Platform">
          </div>
        </div>
      </div>
    </section>

    <!-- Project 5: 3M Young Scientist Challenge Ocean Buoy -->
    <section class="editorial-case-study" id="oceanBuoy">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/Copy of Engg Device.jpg" data-title="Ocean Acidification Buoy System" data-badge="3M Challenge" data-caption="Autonomous pH-responsive mineral dispensing buoy to protect aquatic ecosystems.">
            <img src="assets/robotics/Copy of Engg Device.jpg" alt="Ocean Acidification Sensor Buoy">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">05 &bull; 3M Young Scientist Challenge (April 2025)</p>
            <h2 class="case-title">Neutralizing Ocean Acidification to Protect Ecosystems</h2>
            <p class="case-subtitle">Autonomous, pH-responsive buoy system monitoring water pH and dispensing alkaline minerals.</p>
            <p class="case-body">
              Engineered a closed-loop marine environmental buoy system designed to protect fragile coastal coral and aquatic habitats from acidification. The autonomous buoy continuously monitors local water pH levels and dynamically dispenses measured quantities of alkaline minerals when water acidity crosses dangerous ecological thresholds.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">3M Challenge</span>
                <span class="case-metric-desc">Young Scientist</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Closed Loop</span>
                <span class="case-metric-desc">Autonomous Dispenser</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Ecology</span>
                <span class="case-metric-desc">Reef Protection</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="research.html" class="arrow-link">
                <span>View environmental research</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Verified Robotics & Engineering Photo Gallery -->
    <section class="stills-section" id="roboticsEvidence">
      <div class="container">
        <span class="section-meta-label">Verified Robotics Tournament &amp; Award Evidence</span>
        <div class="stills-grid">
          <div class="still-item evidence-link" data-src="assets/robotics/pic12 -WPI Team.png" data-title="WPI US Open World Tournament Team" data-badge="World Tournament" data-caption="Aadya and the team at the WPI FLL US Open World Event celebrating their design recognition.">
            <img src="assets/robotics/pic12 -WPI Team.png" alt="WPI FLL Team Celebration">
            <p class="still-caption">WPI FLL US Open World Event: Team Celebration &amp; Pit Exhibition</p>
          </div>
          <div class="still-item evidence-link" data-src="assets/robotics/pic 2 - Team award.JPG" data-title="FLL Regional Robot Design Award" data-badge="NJ Regionals" data-caption="Aadya and team celebrating the Robot Design Award at NJ Regionals.">
            <img src="assets/robotics/pic 2 - Team award.JPG" alt="Regional Robot Design Trophy">
            <p class="still-caption">NJ Regionals: Robot Design Award First Place Trophy</p>
          </div>
          <div class="still-item evidence-link" data-src="assets/robotics/pic 5 - Mt Olive Award.jpg" data-title="NJ State Breakthrough Award" data-badge="NJ State Championship" data-caption="Aadya with the Breakthrough Award at Mt. Olive NJ State Championship.">
            <img src="assets/robotics/pic 5 - Mt Olive Award.jpg" alt="NJ State Breakthrough Award">
            <p class="still-caption">NJ State Championship (Mt. Olive): Breakthrough Award Winners</p>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(projects_head + projects_body + footer_block)

print("Master projects.html generated successfully!")

# ==============================================================================
# 2. RESEARCH.HTML
# ==============================================================================
research_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>Empirical Research &amp; Applied Science — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="MIT Solve National Winner, Stockholm Junior Water Prize, IEEE Xplore publication, Stanford AIMI Medical AI Intern, Harvard BioResearch Academy.'
)

research_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Empirical Science &bull; Applied Research</span>
          <h1 class="inner-hero-title">Biochar Eco-Engineering, <span class="italic-serif">Medical AI</span> &amp; Genetics</h1>
          <p class="inner-hero-lead">
            MIT Solve Top 5 National Winner, Stockholm Junior Water Prize Regional Winner, IEEE ISEC published researcher at Princeton University, Stanford AIMI 30-week Medical AI intern, and Harvard BioResearch Academy researcher with Prof. Sam Kunes.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">MIT Solve</div>
              <div class="inner-metric-label">Top 5 National Winner</div>
              <div class="inner-metric-sub">Presented at MIT Media Lab</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Stockholm Water</div>
              <div class="inner-metric-label">Junior Water Prize</div>
              <div class="inner-metric-sub">MSEF / ISEF Regional Winner</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">IEEE Xplore</div>
              <div class="inner-metric-label">ISEC at Princeton Univ</div>
              <div class="inner-metric-sub">Extended Abstract &amp; Poster</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Stanford AIMI</div>
              <div class="inner-metric-label">30-Wk AI Research Intern</div>
              <div class="inner-metric-sub">AI for the Visually Impaired</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Research 1: Biochar Water Filtration (MIT Solve, MSEF, Stockholm, NJWEA, IEEE) -->
    <section class="editorial-case-study" id="water">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/Aqua Science Certificate.jpg" data-title="Aqua Science Project Certification" data-badge="Water Science &amp; Remediation" data-caption="Official Aqua Science Research Certification for Biochar Water Filtration and Adsorption Kinetics.">
            <img src="assets/certificates/Aqua Science Certificate.jpg" alt="Aqua Science Research Certificate">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">01 &bull; Environmental Science &bull; Biochar Water Remediation</p>
            <h2 class="case-title">Comparative Analysis of Biochars for Heavy Metal &amp; Nutrient Remediation</h2>
            <p class="case-subtitle">Stockholm Junior Water Prize &bull; NOAA Award &bull; NJWEA Winner &bull; IEEE Xplore Archival.</p>
            <p class="case-body">
              Conducted empirical investigations comparing two types of biochar sourced from distinct feedstocks (softwood vs. agricultural waste) to determine adsorption efficiency in removing toxic heavy metals (iron, zinc, copper) and fertilizer runoff chemicals (nitrates, phosphates) from water.
            </p>
            <p class="case-body">
              <strong>Major Science Fair Distinctions:</strong>
              <br>&bull; <strong>U.S. Stockholm Junior Water Prize Regional Award</strong> (MSEF / ISEF) &mdash; nominated for State level.
              <br>&bull; <strong>National Oceanic &amp; Atmospheric Administration (NOAA)</strong> &ldquo;Taking the Pulse of the Planet&rdquo; Award.
              <br>&bull; <strong>NJ Water Environment Association (NJWEA) Winner</strong> &mdash; Invited to present at the 2026 NJWEA Annual Conference in Atlantic City, NJ.
              <br>&bull; <strong>Second Place</strong> in Earth and Environmental Science Category (MSEF).
              <br>&bull; <strong>16th IEEE ISEC at Princeton University</strong> &mdash; Extended Abstract accepted for peer-review and archival in <em>IEEE Xplore</em>; poster presented at Princeton.
              <br>&bull; <strong>American Biochar Company Partnership</strong> &mdash; Commercial biochar donated and research featured on <a href="https://ambiochar.com" target="_blank" style="color: var(--c-dark-olive); font-weight: 700; text-decoration: underline;">Ambiochar.com</a>.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Stockholm Water</span>
                <span class="case-metric-desc">Regional Prize</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">NOAA Award</span>
                <span class="case-metric-desc">Pulse of the Planet</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">IEEE Xplore</span>
                <span class="case-metric-desc">Princeton ISEC</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="https://ambiochar.com" target="_blank" rel="noopener noreferrer" class="arrow-link">
                <span>View Ambiochar.com Feature</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Research 2: Stanford AIMI Medical AI Research Internship -->
    <section class="editorial-case-study" id="stanfordAimi" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">02 &bull; Stanford AIMI &bull; Center for AI in Medicine &amp; Imaging</p>
            <h2 class="case-title">Stanford AIMI 30-Week Research Intern: AI for Visually Impaired</h2>
            <p class="case-subtitle">Academic year research internship applying computer vision &amp; assistive deep learning (Sept 2026 &ndash; May 2027).</p>
            <p class="case-body">
              Selected for the competitive <strong>30-week Academic Year Research Internship at Stanford AIMI</strong>. Working under faculty mentorship in a select group of 5 student researchers on: <em>&ldquo;User-Centric AI for Assisting the Visually Impaired.&rdquo;</em> Developing computer vision and multimodal sensor models to assist low-vision patients with navigation, obstacle detection, and real-time environment understanding, culminating in a presentation at the Stanford Health event.
            </p>
            <p class="case-body">
              Also completed the <strong>Stanford AIMI Summer Research Internship</strong> (July 2026), examining real-world deployment of clinical machine learning algorithms with medical-grade scientific rigor.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">30 Weeks</span>
                <span class="case-metric-desc">Academic Research</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Assistive AI</span>
                <span class="case-metric-desc">Visually Impaired</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Stanford Health</span>
                <span class="case-metric-desc">Symposium Presenter</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="projects.html#monivitals" class="arrow-link">
                <span>View MoniVitals.com platform</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/pic 20-devpost.jpg" data-title="Stanford AIMI Medical AI Models" data-badge="Stanford AIMI" data-caption="Clinical machine learning models for multimodal healthcare telemetry.">
            <img src="assets/robotics/pic 20-devpost.jpg" alt="Stanford AIMI Research">
          </div>
        </div>
      </div>
    </section>

    <!-- Research 3: Harvard BioResearch Academy with Prof. Sam Kunes -->
    <section class="editorial-case-study" id="harvardBioresearch">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/BioResearch Academy Certificate.jpeg" data-title="Harvard BioResearch Academy Certification" data-badge="Laboratory Certification" data-caption="BioResearch Academy molecular diagnostics and CRISPR-Cas biotechnology laboratory certification.">
            <img src="assets/certificates/BioResearch Academy Certificate.jpeg" alt="BioResearch Academy Certificate">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">03 &bull; Harvard University &bull; Molecular &amp; Cellular Biology</p>
            <h2 class="case-title">24-Week Advanced BioResearch with Prof. Sam Kunes</h2>
            <p class="case-subtitle">Harvard University molecular biology program &amp; 3-week residential BioResearch Academy in Boston.</p>
            <p class="case-body">
              Completed an intensive <strong>24-week Advanced BioResearch Program</strong> directed by <strong>Prof. Sam Kunes (Harvard University)</strong> from October 2025 to May 2026, followed by the 3-week residential BioResearch Academy in Boston (Summer 2026).
            </p>
            <p class="case-body">
              Program curriculum explored cancer cell biology (DNA replication errors, tumor cell identity, cell division checkpoints), brain organoids, CRISPR genome editing, spatial transcriptomics, high-throughput RNA sequencing, advanced confocal microscopy, and synthetic biology in modern oncology therapeutics. Delivered independent research presentations at the culmination of each 12-week session.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Harvard Faculty</span>
                <span class="case-metric-desc">Prof. Sam Kunes</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">24 Weeks</span>
                <span class="case-metric-desc">Advanced Research</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">CRISPR &amp; RNA-seq</span>
                <span class="case-metric-desc">Genomics &amp; Oncology</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="about.html" class="arrow-link">
                <span>View academic journey</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Research 4: Independent Cancer scRNA-seq Research (Cambridge Mentor) -->
    <section class="editorial-case-study" id="cancerResearch" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">04 &bull; Computational Oncology &bull; Single-Cell Genomics (Summer 2025)</p>
            <h2 class="case-title">Breast Cancer Tumor Heterogeneity: scRNA-seq Clustering</h2>
            <p class="case-subtitle">Mentored by Kristina Kordova, PhD (University of Cambridge) &bull; Identified 32 distinct biomarker clusters.</p>
            <p class="case-body">
              Completed a 12-week virtual research fellowship under the direct mentorship of <strong>Dr. Kristina Kordova (PhD in Biological Sciences, University of Cambridge)</strong>. Investigated tumor microenvironment heterogeneity using single-cell RNA sequencing (scRNA-seq) datasets.
            </p>
            <p class="case-body">
              Applied custom Python data preprocessing pipelines, normalization, PCA dimensionality reduction, and graph-based clustering to classify breast cancer subtypes, successfully identifying <strong>32 distinct cell clusters</strong> associated with unique prognostic biomarkers. Authored a rigorous 6-page scientific paper detailing the computational methodology and therapeutic implications.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Univ Cambridge</span>
                <span class="case-metric-desc">Faculty Mentorship</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">32 Clusters</span>
                <span class="case-metric-desc">Biomarker Discovery</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">scRNA-seq</span>
                <span class="case-metric-desc">Single-Cell Python ML</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="https://github.com/aanj1" target="_blank" rel="noopener noreferrer" class="arrow-link">
                <span>Inspect code repositories</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/InspiritAI_AI_Scholars_Certificate.jpg" data-title="Inspirit AI Scholars Certification" data-badge="AI Scholars" data-caption="Inspirit AI Scholars Machine Learning &amp; Single-Cell RNA Sequencing Certification.">
            <img src="assets/certificates/InspiritAI_AI_Scholars_Certificate.jpg" alt="Inspirit AI Scholars Certification">
          </div>
        </div>
      </div>
    </section>

    <!-- Science Olympiad & Academic Honors Grid -->
    <section class="editorial-content-section" id="honors">
      <div class="container">
        <div class="section-head-editorial">
          <span class="eyebrow">Academic Rigor &bull; Competition Honors</span>
          <h2 class="title">Science Olympiad Medals &amp; Certifications</h2>
          <p class="desc">Proven performance in competitive science olympiads, machine learning certifications, and mathematical modeling.</p>
        </div>

        <div class="clean-cards-grid">
          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag highlight">State &amp; Regional</span>
              <span class="card-date-badge">6 Medals</span>
            </div>
            <h3 class="card-main-title">Science Olympiad Tournament Podiums</h3>
            <p class="card-body-text">
              &bull; <strong>Green Generation:</strong> 2nd Place Regional; 4th Place State<br>
              &bull; <strong>Ecology:</strong> 2nd Place Regional<br>
              &bull; <strong>Disease Detectives:</strong> 2nd Place Regional; 6th Place State<br>
              &bull; <strong>Meteorology:</strong> 3rd Place Regional<br>
              &bull; <strong>Can&rsquo;t Judge a Powder:</strong> 5th Place State<br>
              &bull; <strong>Microbe Mission:</strong> 6th Place Regional
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">Regional 2nd Place</span>
              <span class="metric-pill">State 4th Place</span>
            </div>
          </div>

          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag">Inspirit AI</span>
              <span class="card-date-badge">Ambassador &amp; Scholar</span>
            </div>
            <h3 class="card-main-title">CNN Pneumonia Detection &amp; AI Ambassador</h3>
            <p class="card-body-text">
              Developed a convolutional neural network (CNN) image classifier to detect pneumonia from chest X-ray scans. Earned both the <strong>AI Scholars Certificate</strong> and the <strong>AI Ambassador Certificate</strong> for exemplary leadership in applied artificial intelligence.
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">CNN Deep Learning</span>
              <span class="metric-pill">Chest X-Ray Vision</span>
            </div>
          </div>

          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag">MathWorks &amp; CTY</span>
              <span class="card-date-badge">Certified</span>
            </div>
            <h3 class="card-main-title">MATLAB Simscape &amp; Johns Hopkins CTY</h3>
            <p class="card-body-text">
              Completed MathWorks <strong>Simscape Onramp</strong> certification for multi-domain biomedical physical system simulation. Selected for <strong>Johns Hopkins CTY</strong> Cryptology (Math Intensive Studies) and <strong>University of Michigan MMSS</strong> Graph Theory residential programs.
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">Simscape Certified</span>
              <span class="metric-pill">JHU CTY Cryptology</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

with open('research.html', 'w', encoding='utf-8') as f:
    f.write(research_head + research_body + footer_block)

print("Master research.html generated successfully!")

# ==============================================================================
# 3. IMPACT.HTML
# ==============================================================================
impact_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>Civic Leadership &amp; Humanitarian Impact — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="STEP LEO Club Melvin Jones Award, NJ State Assembly Legislative Resolution, United Nations Future of Service Award, 150,624 meals packed, and community drives.'
)

impact_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Civic Leadership &bull; Humanitarian Action</span>
          <h1 class="inner-hero-title">Youth Civic Governance, <span class="italic-serif">Direct Aid</span> &amp; UN Advocacy</h1>
          <p class="inner-hero-lead">
            Board member of STEP For A Better World LEO Club (Lions Club International), recipient of the Melvin Jones Fellowship Award, honored with an official State of New Jersey General Assembly Legislative Resolution, and recognized with the United Nations Future of Service Award.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">150,624</div>
              <div class="inner-metric-label">Meals Packaged</div>
              <div class="inner-metric-sub">Project Hunger Relief</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">$1,000</div>
              <div class="inner-metric-label">Melvin Jones Fellow</div>
              <div class="inner-metric-sub">Lions Club International Fund</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">UN Award</div>
              <div class="inner-metric-label">Future of Service</div>
              <div class="inner-metric-sub">Delegate at UN Headquarters NYC</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">NJ Assembly</div>
              <div class="inner-metric-label">Legislative Citation</div>
              <div class="inner-metric-sub">15th Legislative District</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact 1: STEP For A Better World LEO Club -->
    <section class="editorial-case-study" id="stepLeo">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/community/Copy of cd - ah- group pic1.jpg" data-title="STEP LEO Club Youth Volunteers" data-badge="Civic Mobilization" data-caption="Aadya with student volunteer coalition delivering supplies to Anchor House shelter in Trenton.">
            <img src="assets/community/Copy of cd - ah- group pic1.jpg" alt="STEP LEO Club Delivery">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">01 &bull; Lions Club International &bull; STEP For A Better World LEO Club</p>
            <h2 class="case-title">Executive Board Member &amp; Melvin Jones Fellowship Honoree</h2>
            <p class="case-subtitle">Mobilized 150,624 meals, fundraised $1,000 for critical causes, and spearheaded regional donation drives.</p>
            <p class="case-body">
              Active Board Member of <strong>STEP For A Better World LEO Club</strong> (affiliated with Lions Club International) from 2023 to Present. Awarded the prestigious <strong>Melvin Jones Fellowship Fund Award</strong> for raising $1,000 supporting global initiatives in vision, diabetes, environmental protection, pediatric cancer, and hunger alleviation.
            </p>
            <p class="case-body">
              Organized and led multiple large-scale community mobilization campaigns:
              <br>&bull; <strong>Project Hunger:</strong> Volunteered to pack <strong>150,624 meals</strong> and fundraised to purchase an additional 300 meals for food-insecure families.
              <br>&bull; <strong>Halloween Candy Drives:</strong> Directed collection of 131+ candy bags and funds distributed to Anchor House youth shelter and Howard Healthy Choices in Trenton, NJ.
              <br>&bull; <strong>Multi-Agency Drives:</strong> Directed collection drives for stuffed toys, books, back-to-school essentials, socks, eyeglasses, shoes, and diapers aiding the Rescue Mission of Trenton, Toys for Tots Foundation, and Rahbar Trust (medical clinics in Lebanon).
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">150k Meals</span>
                <span class="case-metric-desc">Project Hunger</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">$1,000 Raised</span>
                <span class="case-metric-desc">Melvin Jones Fund</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">131+ Bags</span>
                <span class="case-metric-desc">Shelter Treats</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="#drives" class="arrow-link">
                <span>View field photographs</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact 2: State of New Jersey General Assembly Resolution -->
    <section class="editorial-case-study" id="njResolution" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">02 &bull; State Government Commendation &bull; 15th Legislative District</p>
            <h2 class="case-title">State of New Jersey General Assembly Citation</h2>
            <p class="case-subtitle">Official legislative resolution recognizing meritorious community service and leadership.</p>
            <p class="case-body">
              Formally honored by the <strong>General Assembly of the State of New Jersey</strong> with an official <strong>Legislative Citation and Commendation for Community Service and Action</strong>. The bipartisan resolution acknowledged Aadya's exceptional dedication to organizing community food distribution networks, providing ongoing support to homeless youth shelters, and setting a benchmark for civic responsibility among youth across Mercer County.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">NJ Assembly</span>
                <span class="case-metric-desc">Legislative Resolution</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">15th District</span>
                <span class="case-metric-desc">State of New Jersey</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Official Record</span>
                <span class="case-metric-desc">State Commendation</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="assets/certificates/Service Award - NJ State Assembly.jpeg" class="evidence-link arrow-link" data-src="assets/certificates/Service Award - NJ State Assembly.jpeg" data-title="NJ General Assembly Legislative Citation" data-badge="Legislative Resolution" data-caption="Official State of New Jersey General Assembly Citation and Commendation.">
                <span>Inspect State Resolution</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/Service Award - NJ State Assembly.jpeg" data-title="NJ State Service Award Certificate" data-badge="Legislative Resolution" data-caption="Official Legislative Citation from the NJ General Assembly.">
            <img src="assets/certificates/Service Award - NJ State Assembly.jpeg" alt="NJ State Service Award">
          </div>
        </div>
      </div>
    </section>

    <!-- Impact 3: United Nations Future of Service Award -->
    <section class="editorial-case-study" id="unAward">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/STEP UN Future of Service.jpeg" data-title="United Nations Future of Service Certificate" data-badge="United Nations" data-caption="Recipient of the United Nations Future of Service Award.">
            <img src="assets/certificates/STEP UN Future of Service.jpeg" alt="United Nations Future of Service">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">03 &bull; United Nations Headquarters &bull; Global Youth Advocacy</p>
            <h2 class="case-title">United Nations: Future of Service Award</h2>
            <p class="case-subtitle">Selected to attend the UN Conference at UN Headquarters in New York City (March 2024).</p>
            <p class="case-body">
              Honored as a recipient of the <strong>United Nations Future of Service Award</strong> and selected to attend the high-level UN Conference at <strong>United Nations Headquarters in New York</strong> in March 2024. Engaged with international youth delegates and humanitarian leaders on scaling grassroots service coalitions and leveraging youth agency in achieving sustainable development goals.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">UN Award</span>
                <span class="case-metric-desc">Future of Service</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">UN HQ NYC</span>
                <span class="case-metric-desc">Conference Delegate</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Global Service</span>
                <span class="case-metric-desc">Youth Leadership</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="beyond-stem.html#oratory" class="arrow-link">
                <span>View public speaking honors</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact 4: Lawrenceville LCAP & Slackwood Elementary -->
    <section class="editorial-case-study" id="lcap" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">04 &bull; The Lawrenceville School &bull; Environmental Pedagogy (2025&ndash;Present)</p>
            <h2 class="case-title">Lawrenceville Community Action Project (LCAP)</h2>
            <p class="case-subtitle">Teaching sustainability &amp; environmental education at Slackwood Elementary with The Watershed Institute.</p>
            <p class="case-body">
              Active participant in the <strong>Lawrenceville Community Action Project (LCAP)</strong>. Every Wednesday during the Fall Term (2 hours and 15 minutes each session), Aadya collaborates with <strong>The Watershed Institute</strong> to deliver hands-on sustainability and environmental education modules to elementary school students at Slackwood Elementary School, teaching watershed dynamics, soil conservation, and biodiversity preservation.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Weekly LCAP</span>
                <span class="case-metric-desc">Elementary School</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Watershed Inst</span>
                <span class="case-metric-desc">Conservation Partner</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Eco-Education</span>
                <span class="case-metric-desc">Youth Mentorship</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="about.html" class="arrow-link">
                <span>View Lawrenceville profile</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/community/pic 14 - BackToSchoolDrive-Donation-AadyaAgarwal-09032023.jpg" data-title="Back to School Community Drives" data-badge="Community Action" data-caption="Aadya organizing educational and back-to-school donation drives.">
            <img src="assets/community/pic 14 - BackToSchoolDrive-Donation-AadyaAgarwal-09032023.jpg" alt="Back to School Drive">
          </div>
        </div>
      </div>
    </section>

    <!-- Additional Community Pillars Grid -->
    <section class="editorial-content-section" id="communityPillars">
      <div class="container">
        <div class="section-head-editorial">
          <span class="eyebrow">Grassroots Impact &bull; Local &amp; Global Service</span>
          <h2 class="title">Global Education, Elder Care &amp; Animal Advocacy</h2>
          <p class="desc">Demonstrated commitment to diverse community causes from elder companionship to international education funding.</p>
        </div>

        <div class="clean-cards-grid">
          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag highlight">International</span>
              <span class="card-date-badge">2024 &ndash; Present</span>
            </div>
            <h3 class="card-main-title">Anything Will Do (AWD) &bull; ProjectEDUCATE</h3>
            <p class="card-body-text">
              Raised $500 for the physical re-construction of a school in India; organized a community laptop collection drive; and conducts regular online tutoring for elementary and middle school students in India.
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">$500 Raised</span>
              <span class="metric-pill">Laptop Drive</span>
              <span class="metric-pill">Online Tutoring</span>
            </div>
          </div>

          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag">Elder Care</span>
              <span class="card-date-badge">2024 &ndash; Present</span>
            </div>
            <h3 class="card-main-title">Artis Senior Living of Princeton Junction</h3>
            <p class="card-body-text">
              Provides ongoing companion support, social engagement, and classical music piano and flute recitals for senior living residents, bringing multi-generational warmth to older adults.
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">Senior Companionship</span>
              <span class="metric-pill">Music Recitals</span>
            </div>
          </div>

          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag">Animal Welfare</span>
              <span class="card-date-badge">Girl Scouts</span>
            </div>
            <h3 class="card-main-title">SAVE Animal Shelter &bull; Paws for Reading</h3>
            <p class="card-body-text">
              Volunteered for SAVE&rsquo;s &ldquo;Paws for Reading&rdquo; program to read to shelter animals and assist their socialization for adoption. Organized bake sales, slime sales, and fundraisers to support homeless pets.
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">Animal Socialization</span>
              <span class="metric-pill">SAVE Shelter</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Field Documentary Stills Row -->
    <section class="stills-section" id="drives">
      <div class="container">
        <span class="section-meta-label">On-The-Ground Field Stills</span>
        <div class="stills-grid">
          <div class="still-item evidence-link" data-src="assets/community/Distributing candy at anchor house - pic1.jpg" data-title="Anchor House Shelter Delivery" data-badge="Civic Action" data-caption="Direct delivery of food and treats to Anchor House youth shelter in Trenton, NJ.">
            <img src="assets/community/Distributing candy at anchor house - pic1.jpg" alt="Anchor House Distribution">
            <p class="still-caption">Delivering treats and supplies directly to Anchor House youth shelter</p>
          </div>
          <div class="still-item evidence-link" data-src="assets/community/Candy donation boxes at AoPs - pic2.jpg" data-title="AoPS Regional Collection Hub" data-badge="Donation Hub" data-caption="Drop-off bins established at regional community centers across Mercer County.">
            <img src="assets/community/Candy donation boxes at AoPs - pic2.jpg" alt="AoPS Collection Boxes">
            <p class="still-caption">Regional community collection boxes established at AoPS Academy</p>
          </div>
          <div class="still-item evidence-link" data-src="assets/certificates/STEP Meals Packaging.jpeg" data-title="Project Hunger Meal Packaging" data-badge="150k Meals" data-caption="Aadya volunteering at mass meal packaging event for Project Hunger.">
            <img src="assets/certificates/STEP Meals Packaging.jpeg" alt="Project Hunger Packaging">
            <p class="still-caption">Volunteering at meal packaging event packing 150,624 meals for Project Hunger</p>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

with open('impact.html', 'w', encoding='utf-8') as f:
    f.write(impact_head + impact_body + footer_block)

print("Master impact.html generated successfully!")

# ==============================================================================
# 4. BEYOND-STEM.HTML
# ==============================================================================
beyond_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>Beyond STEM: Humanities &amp; Fine Arts — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="Oxford John Locke High Commendation, HIR Bronze Medal, Scholastic Silver Keys, and Music-Fest Grand Prize.'
)

beyond_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Humanities &bull; Fine Arts &bull; Oratory</span>
          <h1 class="inner-hero-title">Moral Philosophy, <span class="italic-serif">Poetic Form</span> &amp; Classical Art</h1>
          <p class="inner-hero-lead">
            Awarded Global High Commendation in the Oxford John Locke Essay Competition (Top 3% worldwide), Bronze Medal in the Harvard International Review, 2 Scholastic Silver Keys in Poetry, and Grand Prize in the Music-Fest International Rising Talent Festival.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Top 3%</div>
              <div class="inner-metric-label">Oxford John Locke</div>
              <div class="inner-metric-sub">Global High Commendation</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Bronze Medal</div>
              <div class="inner-metric-label">Harvard Int'l Review</div>
              <div class="inner-metric-sub">Technology &amp; Innovation</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">2 Silver Keys</div>
              <div class="inner-metric-label">Scholastic Writing</div>
              <div class="inner-metric-sub">+ 4 Honorable Mentions</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Grand Prize</div>
              <div class="inner-metric-label">Music-Fest Recital</div>
              <div class="inner-metric-sub">Piano Solo &amp; NJMTA Flute</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Beyond 1: Oxford John Locke & Harvard International Review -->
    <section class="editorial-case-study" id="philosophy">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/John Locke 2026 - High Commendation.jpg" data-title="Oxford John Locke Institute High Commendation" data-badge="Oxford Global Award" data-caption="Official High Commendation certificate from the Oxford John Locke Institute.">
            <img src="assets/certificates/John Locke 2026 - High Commendation.jpg" alt="Oxford John Locke High Commendation">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">01 &bull; Moral Philosophy &bull; Global Scholarship</p>
            <h2 class="case-title">Oxford John Locke Global Commendation &amp; HIR Bronze</h2>
            <p class="case-subtitle">Evaluated by senior Oxford faculty &bull; Bronze Medal in Harvard International Review writing contest.</p>
            <p class="case-body">
              Awarded <strong>Global High Commendation (Top 3% worldwide)</strong> in the prestigious <strong>Oxford John Locke International Essay Competition</strong> (Science &amp; Technology category), evaluated by senior Oxford faculty. Later attended the <strong>John Locke Summer Institute at Georgetown University</strong> studying Political Philosophy, Game Theory, and Public Policy.
            </p>
            <p class="case-body">
              Also earned the <strong>Bronze Medal</strong> in the <strong>Harvard International Review (HIR) Academic Writing Contest</strong> (Technology &amp; Innovation theme). For National History Day (2025), authored a 2,500-word historical treatise analyzing Lysenkoism and the political suppression of genetics in the Soviet Union.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Top 3%</span>
                <span class="case-metric-desc">Oxford Global Rank</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Bronze Medal</span>
                <span class="case-metric-desc">Harvard Int'l Review</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Georgetown</span>
                <span class="case-metric-desc">Locke Institute</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="#poetry" class="arrow-link">
                <span>Read published poetry</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Beyond 2: Scholastic Writing & Published Poems -->
    <section class="editorial-content-section" id="poetry" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="section-head-editorial" style="text-align: center; margin-bottom: 40px;">
          <span class="eyebrow">Creative Writing &bull; Scholastic Art &amp; Writing Awards</span>
          <h2 class="title">Two Silver Keys &amp; Six Published Literary Works</h2>
          <p class="desc" style="margin: 0 auto;">2 Silver Keys in Poetry and 4 Honorable Mentions in Personal Essay &amp; Memoir. Works featured in international print magazines and anthologies.</p>
        </div>

        <div class="poetry-clean-grid">
          <!-- Poem 1: When the Sink Speaks -->
          <div class="poetry-clean-card">
            <span class="poetry-award-tag">The Rev &bull; Top 10 of 150</span>
            <h3 class="poetry-clean-title">When the Sink Speaks</h3>
            <div class="poetry-clean-stanzas">It groans with the weight of the morning run,
a metal throat that gargles with the dawn.
Before the kettle notices the sun,
the yesterday of water is all gone.

It does not ask whose fingers turn the brass,
or what bitter stain is washed away.
It carries what the living cannot pass,
and swallows down the silence of the day.</div>
            <div class="poetry-footer-note">PUBLISHED IN THE REV INTERNATIONAL MAGAZINE</div>
          </div>

          <!-- Poem 2: A Celebration of Small -->
          <div class="poetry-clean-card">
            <span class="poetry-award-tag">Poetic Power &bull; Anthology</span>
            <h3 class="poetry-clean-title">A Celebration of Small</h3>
            <div class="poetry-clean-stanzas">The tea leaves settle softly in the cup,
not in despair, but knowing where to rest.
We measure grandness by what we lift up,
forgetting what remains within the chest.

A pine needle falls silently in shade,
a quiet seed that water learns to keep.
The longest rivers were by raindrops made,
before they taught the ocean how to weep.</div>
            <div class="poetry-footer-note">SCHOLASTIC SILVER KEY &bull; A CELEBRATION OF POETS</div>
          </div>

          <!-- Poem 3: My Mom's Frying Pan -->
          <div class="poetry-clean-card">
            <span class="poetry-award-tag">Poetic Power &bull; Anthology</span>
            <h3 class="poetry-clean-title">My Mom&rsquo;s Frying Pan</h3>
            <div class="poetry-clean-stanzas">The cast iron remembers every flame,
the sizzle of the morning before dawn.
It bears no pride, it carries no sweet name,
yet feeds the living after night is gone.

A kitchen smells of rosemary and rye,
a mother's hand that turns the skillet round.
The greatest devotions do not reach the sky,
they stay right here, close to the humble ground.</div>
            <div class="poetry-footer-note">PUBLISHED IN POETIC POWER ANTHOLOGY (SPRING 2024)</div>
          </div>
        </div>

        <div class="clean-cards-grid three-col" style="margin-top: 28px;">
          <div class="clean-editorial-card">
            <span class="card-tag">Skipping Stones</span>
            <h4 class="card-main-title" style="font-size: 1.15rem; margin-top: 10px;">Balance (Fall 2023)</h4>
            <p class="card-body-text" style="font-size: 0.88rem;">Published poem exploring equilibrium in the natural world in <em>Skipping Stones</em>, an international multicultural literary magazine.</p>
          </div>
          <div class="clean-editorial-card">
            <span class="card-tag">The Telling Room</span>
            <h4 class="card-main-title" style="font-size: 1.15rem; margin-top: 10px;">When Kindness Was Planted</h4>
            <p class="card-body-text" style="font-size: 0.88rem;">Published short story featured in <em>The Telling Room</em> youth literary journal celebrating empathy and community compassion.</p>
          </div>
          <div class="clean-editorial-card">
            <span class="card-tag">Poetic Power</span>
            <h4 class="card-main-title" style="font-size: 1.15rem; margin-top: 10px;">In a Shift of Heart</h4>
            <p class="card-body-text" style="font-size: 0.88rem;">Published in national anthology <em>A Celebration of Poets</em> (Summer 2023) exploring human vulnerability and transformation.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Beyond 3: Public Speaking & Oratory Championships -->
    <section class="editorial-case-study" id="oratory">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/Award Certificate - NSF PS1 contest .jpg" data-title="North South Foundation National Champion" data-badge="1st Place Champion" data-caption="1st Place National Champion certificate from the North South Foundation Junior Public Speaking Contest.">
            <img src="assets/certificates/Award Certificate - NSF PS1 contest .jpg" alt="NSF Public Speaking Certificate">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">03 &bull; Public Speaking &bull; National Oratory</p>
            <h2 class="case-title">NSF National Public Speaking Champion (1st Place)</h2>
            <p class="case-subtitle">Toastmasters Outstanding Communicator &bull; Lawrenceville School Public Speaking Semifinalist.</p>
            <p class="case-body">
              Secured <strong>First Place National Champion</strong> in the North South Foundation (NSF) Junior Public Speaking Contest (Princeton Chapter), awarded the <em>Certificate of Learning Journey Excellence</em>.
            </p>
            <p class="case-body">
              Earned the <strong>Outstanding Communicator Award</strong> in the ETS Toastmasters Youth Leadership Program (YLP); her presentation was designated as the model speech used for instructional coaching across regional classrooms. At The Lawrenceville School, advanced as a <strong>School-wide Public Speaking Semifinalist</strong> in 2025 and endorsed to represent her class in 2026. Also won Speaker Award honors in Public Forum Debate at the TFA/TOC tournament.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">1st Place</span>
                <span class="case-metric-desc">NSF National Champion</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Toastmasters</span>
                <span class="case-metric-desc">Outstanding Communicator</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Semifinalist</span>
                <span class="case-metric-desc">Lawrenceville Contest</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="#music" class="arrow-link">
                <span>View classical music honors</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Beyond 4: Classical Music & Theater Arts -->
    <section class="editorial-case-study" id="music" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">04 &bull; Fine Arts &bull; Piano &amp; Flute Classical Repertoire</p>
            <h2 class="case-title">Music-Fest Grand Prize Winner &amp; NJMTA Honors</h2>
            <p class="case-subtitle">Selected for Honors Recitals at Westminster Conservatory &amp; Rutgers Nicholas Music Hall.</p>
            <p class="case-body">
              Awarded the <strong>Grand Prize in the Music-Fest International Rising Talent Festival</strong> for piano recital performance. Earned <strong>Honors Ratings</strong> in NJMTA auditions for Piano for two consecutive years, as well as an <strong>Honors Rating in Flute (2025)</strong>.
            </p>
            <p class="case-body">
              Selected to perform in prestigious Honors Recitals at Westminster Conservatory and Rutgers University Nicholas Music Hall. Plays flute in the middle and high school jazz bands, performs studio recitals, and brings classical music to elder residents at senior living homes. Also active in technical theater with the <strong>Periwig Arts Council</strong>, serving as stage manager and production assistant for <em>Much Ado About Nothing</em>.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Grand Prize</span>
                <span class="case-metric-desc">Music-Fest International</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">NJMTA Honors</span>
                <span class="case-metric-desc">Rutgers Music Hall</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Jazz Band</span>
                <span class="case-metric-desc">Flutist &amp; Recitalist</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="about.html" class="arrow-link">
                <span>Read student journey</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg" data-title="Music-Fest Grand Prize Winner" data-badge="International Grand Prize" data-caption="Music-Fest International Rising Talent Festival Grand Prize Recital certificate.">
            <img src="assets/certificates/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg" alt="Music-Fest Grand Prize Certificate">
          </div>
        </div>
      </div>
    </section>

  </main>
"""

with open('beyond-stem.html', 'w', encoding='utf-8') as f:
    f.write(beyond_head + beyond_body + footer_block)

print("Master beyond-stem.html generated successfully!")

# ==============================================================================
# 5. ABOUT.HTML
# ==============================================================================
about_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>About &amp; Personal Journey — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="About Aadya Agarwal: The Lawrenceville School Class of 2029 scholar, Leopold Scholar in Ecology & Ethics, John H. Imbrie Award winner.'
)

about_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Personal Journey &bull; The Lawrenceville School</span>
          <h1 class="inner-hero-title">At the Intersection of <span class="italic-serif">Precision</span>, Empathy &amp; Art</h1>
          <p class="inner-hero-lead">
            Student scholar at The Lawrenceville School (Class of 2029), Leopold Scholar in Ecology &amp; Ethics, recipient of the John H. Imbrie Humanities Award, House Academic Representative, autonomous robotics programmer, and published writer.
          </p>

          <div class="inner-hero-metrics">
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
          </div>

          <!-- Interactive Hero Action Buttons with Expanding Mega-Dropdowns -->
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

          </div>
        </div>
      </div>
    </section>

        <!-- Editorial Memoir Feature (Sticky Layout inspired by rituguptagarg.in) -->
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
    </section>

    <!-- The Lawrenceville Harkness Tradition -->
    <section class="editorial-content-section" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="harkness-feature-grid">
          <div>
            <span class="section-head-editorial"><span class="eyebrow">Pedagogy &amp; Discourse</span></span>
            <h2 style="font-family: var(--font-serif); font-size: 2.2rem; color: var(--c-dark-slate); margin-bottom: 16px;">
              The Harkness Table: Intellectual Courage &amp; Shared Inquiry
            </h2>
            <p style="font-size: 1.02rem; line-height: 1.75; color: var(--text-main); margin-bottom: 18px;">
              At The Lawrenceville School, education occurs around an oval mahogany table. Twelve students and a teacher examine literature, debate ethical dilemmas, and dissect scientific phenomena as intellectual peers.
            </p>
            <p style="font-size: 0.96rem; line-height: 1.7; color: var(--text-muted);">
              This philosophy directly informs how Aadya leads engineering, research, and civic teams: intellectual bravery requires testing your hypothesis against thoughtful counterarguments rather than seeking comfortable consensus.
            </p>
          </div>

          <div style="background: #FFFFFF; border: 1px solid rgba(62, 69, 44, 0.12); border-radius: 10px; padding: 28px;">
            <h4 style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--c-dark-slate); margin-bottom: 16px;">Four Harkness Pillars</h4>
            <ul class="harkness-principles-list">
              <li class="harkness-principle-item">
                <span class="principle-num">01</span>
                <span class="principle-text"><strong>Epistemic Humility:</strong> Acknowledging gaps in knowledge and welcoming rigorous revision.</span>
              </li>
              <li class="harkness-principle-item">
                <span class="principle-num">02</span>
                <span class="principle-text"><strong>Active Listening:</strong> Synthesizing others' observations before formulating a rebuttal.</span>
              </li>
              <li class="harkness-principle-item">
                <span class="principle-num">03</span>
                <span class="principle-text"><strong>Textual Evidence:</strong> Grounding every theoretical assertion in empirical data.</span>
              </li>
              <li class="harkness-principle-item">
                <span class="principle-num">04</span>
                <span class="principle-text"><strong>Shared Discovery:</strong> Valuing the collaborative breakthrough above individual triumph.</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Comprehensive Chronological Milestone Timeline (2020 - 2026) -->
    <section class="editorial-content-section" id="timeline">
      <div class="container">
        <div class="section-head-editorial" style="text-align: center; margin-bottom: 48px;">
          <span class="eyebrow">Chronology &bull; Verified Milestones</span>
          <h2 class="title">The Authentic Journey of a Scholar &amp; Builder</h2>
          <p class="desc" style="margin: 0 auto;">Documented chronological achievements across research, robotics, writing, and service.</p>
        </div>

                <div class="clean-timeline-flow">
          
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

        </div>
      </div>
    </section>

    <!-- Bookshelf & Influences -->
    <section class="editorial-content-section" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="section-head-editorial">
          <span class="eyebrow">Intellectual Influences</span>
          <h2 class="title">Books That Shaped My Perspective</h2>
          <p class="desc">A selection of foundational works bridging scientific inquiry, moral conscience, and craftsmanship.</p>
        </div>

        <div class="clean-cards-grid four-col">
          <div class="clean-editorial-card">
            <span class="card-tag">Philosophy</span>
            <h4 class="card-main-title" style="font-size: 1.15rem; margin-top: 12px;">Second Treatise of Government</h4>
            <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-light); margin-bottom: 10px; display: block;">John Locke</span>
            <p class="card-body-text" style="font-size: 0.88rem;">
              Instilled an enduring conviction that technological authority is only legitimate when it protects human dignity and fundamental freedoms.
            </p>
          </div>

          <div class="clean-editorial-card">
            <span class="card-tag">Physics</span>
            <h4 class="card-main-title" style="font-size: 1.15rem; margin-top: 12px;">The Pleasure of Finding Things Out</h4>
            <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-light); margin-bottom: 10px; display: block;">Richard Feynman</span>
            <p class="card-body-text" style="font-size: 0.88rem;">
              Taught me that genuine scientific mastery begins with intellectual honesty and the fearless joy of asking simple, fundamental questions.
            </p>
          </div>

          <div class="clean-editorial-card">
            <span class="card-tag">Ecology</span>
            <h4 class="card-main-title" style="font-size: 1.15rem; margin-top: 12px;">Silent Spring</h4>
            <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-light); margin-bottom: 10px; display: block;">Rachel Carson</span>
            <p class="card-body-text" style="font-size: 0.88rem;">
              Demonstrated how meticulous empirical chemistry paired with lyrical, morally urgent prose can awaken a society's environmental conscience.
            </p>
          </div>

          <div class="clean-editorial-card">
            <span class="card-tag">Music &amp; Craft</span>
            <h4 class="card-main-title" style="font-size: 1.15rem; margin-top: 12px;">The Classical Style</h4>
            <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-light); margin-bottom: 10px; display: block;">Charles Rosen</span>
            <p class="card-body-text" style="font-size: 0.88rem;">
              Revealed how rigorous formal architecture—whether in a Beethoven sonata or an autonomous PID loop—creates emotional power.
            </p>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_head + about_body + footer_block)

print("Master about.html generated successfully!")

# Also mirror alias files
import shutil
shutil.copyfile('projects.html', 'robotics.html')
shutil.copyfile('research.html', 'academics.html')
shutil.copyfile('impact.html', 'community.html')
shutil.copyfile('beyond-stem.html', 'speaking-writing.html')
shutil.copyfile('beyond-stem.html', 'arts-athletics.html')

print("All master pages and aliases built successfully!")

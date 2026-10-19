# Rebuilder script for all 5 inner pages with 100% Home Page Color Theme & Clean Structure
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
    'content="Technical projects portfolio: FIRST Tech Challenge WPI #14 robot, MoniVitals.com remote telemedicine platform, and MIT Solve ocean IoT buoy.'
)

projects_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Technical Projects &bull; Autonomous Systems</span>
          <h1 class="inner-hero-title">High-Velocity <span class="italic-serif">Robotic Control</span>, Hardware &amp; Telehealth</h1>
          <p class="inner-hero-lead">
            Architecting high-frequency autonomous navigation routines, designing custom mechanical mechanisms, and deploying production clinical web infrastructure at scale.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">#14 / 108</div>
              <div class="inner-metric-label">WPI Global Rank</div>
              <div class="inner-metric-sub">World US Open Invitational</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Pedro Path</div>
              <div class="inner-metric-label">Bézier Splines</div>
              <div class="inner-metric-sub">Continuous curvature odometry</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">MoniVitals</div>
              <div class="inner-metric-label">Live Telehealth</div>
              <div class="inner-metric-sub">Real-time clinical dashboard</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">1st Place</div>
              <div class="inner-metric-label">MIT Solve Buoy</div>
              <div class="inner-metric-sub">Solar marine telemetry package</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Project 1: FIRST Tech Challenge Autonomous Robotics -->
    <section class="editorial-case-study" id="robotics">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/pic 1 - with robot.jpg" data-title="WPI International Invitational #14" data-badge="FTC Robotics" data-caption="Aadya with competition robot at WPI US Open.">
            <img src="assets/robotics/pic 1 - with robot.jpg" alt="Aadya with FIRST Robotics Robot">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">01 &bull; Autonomous Robotics &bull; FIRST Tech Challenge</p>
            <h2 class="case-title">WPI World Rank #14 &amp; Lead Autonomous Controller</h2>
            <p class="case-subtitle">High-order quintic Bézier splines, 3-wheel odometry &amp; Limelight 3G machine vision.</p>
            <p class="case-body">
              Served as Lead Autonomous Programmer for <em>The LeapcoderZ</em>, leading the team to <strong>Rank #14 of 108 international teams</strong> and Robot Design Finalist honors at the WPI US Open. Currently heading autonomous controls for The Lawrenceville School FTC Team. Designed sub-15ms AprilTag localization pipelines and dead-wheel odometry running at 100 Hz dedicated thread execution to eliminate cumulative wheel slippage during the 30-second autonomous competition period.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">#14 / 108</span>
                <span class="case-metric-desc">WPI World Rank</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Pedro Pathing</span>
                <span class="case-metric-desc">Bézier Splines</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Limelight 3G</span>
                <span class="case-metric-desc">AprilTag 36h11</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="arrow-link">
                <span>View GitHub Repositories</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Project 2: MoniVitals.com Telemedicine Platform -->
    <section class="editorial-case-study" id="monivitals" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">02 &bull; Clinical Telemedicine Platform</p>
            <h2 class="case-title">MoniVitals.com: Remote Patient Telemetry</h2>
            <p class="case-subtitle">Live full-stack production dashboard tracking real-time vitals for underserved cardiac patients.</p>
            <p class="case-body">
              Co-founder and lead engineer of <strong>MoniVitals.com</strong>, an active telemedicine web application designed to connect rural and low-income patients with clinical care teams. Aggregates streaming Bluetooth Low Energy (BLE) sensor data—including heart rate, SpO2, blood pressure, and core temperature—into a physician console with automated clinical threshold alert routing.
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
                <span class="case-metric-num">Clinical Triage</span>
                <span class="case-metric-desc">Threshold Alerts</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="https://monivitals.com" target="_blank" rel="noopener noreferrer" class="arrow-link">
                <span>Visit MoniVitals.com Platform</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/pic 20-devpost.jpg" data-title="MoniVitals Platform Architecture" data-badge="Telemedicine" data-caption="Production telemedicine dashboard submission and architecture.">
            <img src="assets/robotics/pic 20-devpost.jpg" alt="MoniVitals Dashboard Platform">
          </div>
        </div>
      </div>
    </section>

    <!-- Project 3: MIT Solve Ocean Buoy -->
    <section class="editorial-case-study" id="mitBuoy">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/Copy of Engg Device.jpg" data-title="MIT Solve Ocean Buoy Telemetry" data-badge="Climate Tech" data-caption="Solar-powered marine sensor platform with long-range radio.">
            <img src="assets/robotics/Copy of Engg Device.jpg" alt="MIT Solve Marine Environmental Buoy">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">03 &bull; Marine Environmental IoT</p>
            <h2 class="case-title">MIT Solve 1st Place: Ocean Telemetry Buoy</h2>
            <p class="case-subtitle">Solar-powered marine environmental sensor platform monitoring coastal water quality.</p>
            <p class="case-body">
              Won <strong>1st Place</strong> in the MIT Solve regional innovation initiative for developing an autonomous solar-powered marine sensor buoy. Built with underwater probes measuring dissolved oxygen, water temperature, and pH, the system broadcasts real-time telemetry over long-range radio links to coastal research stations without requiring continuous battery replacement.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">1st Place</span>
                <span class="case-metric-desc">MIT Solve Challenge</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Solar Array</span>
                <span class="case-metric-desc">Self-Powered</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Multi-Sensor</span>
                <span class="case-metric-desc">pH, O2 &amp; Temp</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="research.html" class="arrow-link">
                <span>Explore environmental research</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Engineering Photo Stills Section -->
    <section class="stills-section">
      <div class="container">
        <span class="section-meta-label">Verified Engineering Evidence</span>
        <div class="stills-grid">
          <div class="still-item evidence-link" data-src="assets/robotics/Copy of Engg Device.jpg" data-title="Autonomous 3-Wire Odometry Testing" data-badge="Hardware Build" data-caption="Precision dead-wheel tracking with Rev Through Bore encoders on custom aluminum chassis.">
            <img src="assets/robotics/Copy of Engg Device.jpg" alt="Autonomous Odometry Chassis">
            <p class="still-caption">Autonomous 3-wire odometry chassis &amp; dead-wheel tracking testing</p>
          </div>
          <div class="still-item evidence-link" data-src="assets/robotics/Copy of pic 19-award ceremony.jpg" data-title="WPI US Open Award Ceremony" data-badge="Tournament Honors" data-caption="Aadya and team receiving honors at WPI US Open International Invitational.">
            <img src="assets/robotics/Copy of pic 19-award ceremony.jpg" alt="WPI Award Ceremony">
            <p class="still-caption">WPI US Open International Invitational awards ceremony podium</p>
          </div>
          <div class="still-item evidence-link" data-src="assets/robotics/pic 1 - with robot.jpg" data-title="Competition Arena Build" data-badge="FTC Robotics" data-caption="Aadya with the competition robot at tournament arena.">
            <img src="assets/robotics/pic 1 - with robot.jpg" alt="Aadya with FTC Robot">
            <p class="still-caption">Aadya with the autonomous robot ready for match competition</p>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(projects_head + projects_body + footer_block)

print("Generated projects.html successfully")

# ==============================================================================
# 2. RESEARCH.HTML
# ==============================================================================
research_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>Empirical Research &amp; Applied Science — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="Empirical research in environmental biochar water filtration, Stanford AIMI clinical artificial intelligence, and certified wet-bench laboratory science.'
)

research_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Empirical Science &bull; Applied Research</span>
          <h1 class="inner-hero-title">Water Eco-Engineering, <span class="italic-serif">Biochar Filtration</span> &amp; Clinical AI</h1>
          <p class="inner-hero-lead">
            Conducting empirical water remediation trials in partnership with American Biochar Company (featured on Ambiochar.com), investigating clinical machine learning triage as a Stanford AIMI Fellow, and completing certified laboratory genetics.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Ambiochar</div>
              <div class="inner-metric-label">Industry Partner</div>
              <div class="inner-metric-sub">American Biochar Co. feature</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">PFAS &amp; Lead</div>
              <div class="inner-metric-label">Adsorption Targets</div>
              <div class="inner-metric-sub">Stormwater runoff filtration</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Stanford AIMI</div>
              <div class="inner-metric-label">Clinical AI Fellow</div>
              <div class="inner-metric-sub">Multimodal medical telemetry</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Wet-Bench</div>
              <div class="inner-metric-label">BioResearch Certified</div>
              <div class="inner-metric-sub">PCR, cloning &amp; electrophoresis</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Research 1: American Biochar Co. Water Filtration -->
    <section class="editorial-case-study" id="biochar">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/BioResearch Academy Certificate.jpeg" data-title="BioResearch Academy Certification" data-badge="Laboratory Certification" data-caption="Certified laboratory protocols in environmental bio-research and molecular methods.">
            <img src="assets/certificates/BioResearch Academy Certificate.jpeg" alt="Biochar Lab Certification">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">01 &bull; Environmental Engineering &bull; Ambiochar.com</p>
            <h2 class="case-title">American Biochar Co. Water Filtration Research</h2>
            <p class="case-subtitle">Empirical investigation of functionalized biochar mesopores for toxic lead and PFAS sequestration.</p>
            <p class="case-body">
              Partnered with the <strong>American Biochar Company</strong>, who donated commercial biochar substrates and featured Aadya's research on <a href="https://ambiochar.com/what-are-your-desired-outcomes/?srsltid=AU7gw4V0Jv4UopgtnjqFxG-5hjunq52PJQ8GDKwc-Eb0Txs9stcpYchd" target="_blank" style="text-decoration: underline; color: var(--c-dark-olive); font-weight: 700;">Ambiochar.com</a>. Evaluated the adsorption dynamics of engineered eastern white pine biochar for high-affinity sequestration of aqueous lead ions (Pb<sup>2+</sup>) and per- and polyfluoroalkyl substances (PFAS) commonly found in agricultural runoff and municipal stormwater.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Ambiochar.com</span>
                <span class="case-metric-desc">Official Article Feature</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">PFAS &amp; Lead</span>
                <span class="case-metric-desc">Target Contaminants</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Porous Matrix</span>
                <span class="case-metric-desc">High Surface Area</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="https://ambiochar.com/what-are-your-desired-outcomes/?srsltid=AU7gw4V0Jv4UopgtnjqFxG-5hjunq52PJQ8GDKwc-Eb0Txs9stcpYchd" target="_blank" rel="noopener noreferrer" class="arrow-link">
                <span>View Ambiochar.com Publication</span>
                <span class="arrow" aria-hidden="true">&nearr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Research 2: Stanford AIMI Clinical AI Fellowship -->
    <section class="editorial-case-study" id="stanford" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">02 &bull; Clinical Artificial Intelligence &bull; Healthcare</p>
            <h2 class="case-title">Stanford AIMI Fellow: Clinical Machine Learning</h2>
            <p class="case-subtitle">Multimodal telemetry analysis &amp; automated diagnostic anomaly triage for emergency care.</p>
            <p class="case-body">
              Completed the competitive <strong>Stanford AIMI (Center for Artificial Intelligence in Medicine &amp; Imaging) Summer Fellowship</strong>. Explored deep learning architectures applied to clinical decision support systems, evaluating how multi-parameter sensor telemetry (ECG intervals, oxygen plethysmography, pulse transit times) can be aggregated to forecast acute decompensation events hours before clinical presentation.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Stanford AIMI</span>
                <span class="case-metric-desc">Summer Fellowship</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Clinical ML</span>
                <span class="case-metric-desc">Multimodal Models</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Patient Triage</span>
                <span class="case-metric-desc">Anomaly Detection</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="projects.html#monivitals" class="arrow-link">
                <span>View MoniVitals.com platform</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/pic 20-devpost.jpg" data-title="Clinical Telemedicine & AI Triage" data-badge="Stanford AIMI" data-caption="Clinical machine learning models integrated with remote vitals telemetry.">
            <img src="assets/robotics/pic 20-devpost.jpg" alt="Stanford AIMI Clinical Triage">
          </div>
        </div>
      </div>
    </section>

    <!-- Research 3: BioResearch Academy Wet-Bench Certification -->
    <section class="editorial-case-study" id="bioresearch">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" data-title="Academic Distinction Honors" data-badge="Scholarship" data-caption="Academic honors ceremony recognizing multidimensional scholarly rigor.">
            <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Academic Distinction Ceremony">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">03 &bull; Wet-Bench Molecular Biology &bull; Laboratory</p>
            <h2 class="case-title">BioResearch Academy: Hands-On Genetics Laboratory</h2>
            <p class="case-subtitle">Certified wet-bench competence in recombinant DNA plasmid cloning, PCR &amp; electrophoresis.</p>
            <p class="case-body">
              Completed rigorous wet-bench laboratory training at the <strong>BioResearch Academy</strong>, earning official certification across foundational molecular biology protocols. Mastered micropipetting precision, bacterial transformation via heat-shock, restriction enzyme digestion, polymerase chain reaction (PCR) amplification, and agarose gel electrophoresis visualization.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Certified</span>
                <span class="case-metric-desc">Wet-Bench Protocols</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">PCR &amp; Cloning</span>
                <span class="case-metric-desc">Recombinant DNA</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Electrophoresis</span>
                <span class="case-metric-desc">Agarose Gel Assay</span>
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

    <!-- Academic Olympiads & Rigor Grid -->
    <section class="editorial-content-section" id="academics">
      <div class="container">
        <div class="section-head-editorial">
          <span class="eyebrow">Academic Foundation</span>
          <h2 class="title">Coursework Rigor &amp; Competition Distinctions</h2>
          <p class="desc">Pursuing maximum curriculum rigor alongside national STEM Olympiad participation.</p>
        </div>

        <div class="clean-cards-grid">
          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag highlight">Curriculum</span>
              <span class="card-date-badge">15 AP Courses</span>
            </div>
            <h3 class="card-main-title">Pre-Collegiate STEM &amp; Humanities Mastery</h3>
            <p class="card-body-text">
              Enrolled in and completed highest-tier Advanced Placement coursework: AP Computer Science A, AP Physics C, AP Calculus BC, AP Chemistry, AP Biology, AP Environmental Science, AP Statistics, and AP European History.
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">Math &amp; Physics</span>
              <span class="metric-pill">Computer Science</span>
              <span class="metric-pill">Life Sciences</span>
            </div>
          </div>

          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag">Competitions</span>
              <span class="card-date-badge">National Circuit</span>
            </div>
            <h3 class="card-main-title">USABO &amp; USACO Olympiad Circuit</h3>
            <p class="card-body-text">
              Active competitor in the USA Biology Olympiad (USABO) and USA Computing Olympiad (USACO), demonstrating algorithmic problem-solving and deep biological systems knowledge under timed competition settings.
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">USACO Bronze/Silver</span>
              <span class="metric-pill">USABO Semifinalist Prep</span>
            </div>
          </div>

          <div class="clean-editorial-card">
            <div class="card-top-meta">
              <span class="card-tag">Recognition</span>
              <span class="card-date-badge">Honor Award</span>
            </div>
            <h3 class="card-main-title">The John H. Imbrie Award &amp; Honors</h3>
            <p class="card-body-text">
              Recipient of prestigious school academic commendations recognizing interdisciplinary scholarship across both the physical sciences and moral philosophy in the Harkness tradition.
            </p>
            <div class="card-metrics-pill-row">
              <span class="metric-pill">Lawrenceville Honors</span>
              <span class="metric-pill">Interdisciplinary Rigor</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

with open('research.html', 'w', encoding='utf-8') as f:
    f.write(research_head + research_body + footer_block)

print("Generated research.html successfully")

# ==============================================================================
# 3. IMPACT.HTML
# ==============================================================================
impact_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>Civic Leadership &amp; Humanitarian Impact — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="Civic leadership portfolio: STEP LEO Club presidency, United Nations Youth Keynote address, and official New Jersey General Assembly legislative resolution.'
)

impact_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Civic Leadership &bull; Humanitarian Action</span>
          <h1 class="inner-hero-title">Youth Civic Governance, <span class="italic-serif">Direct Aid</span> &amp; UN Advocacy</h1>
          <p class="inner-hero-lead">
            Mobilizing over 150 student volunteers across Central New Jersey to combat local food insecurity, addressing international youth delegates at the United Nations, and earning an official legislative resolution from the State of New Jersey General Assembly.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">3,500+ lbs</div>
              <div class="inner-metric-label">Food Distributed</div>
              <div class="inner-metric-sub">Mercer Street Friends &amp; families</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">420+ lbs</div>
              <div class="inner-metric-label">Shelter Confectionery</div>
              <div class="inner-metric-sub">Anchor House &amp; HomeFront</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">150+</div>
              <div class="inner-metric-label">Student Volunteers</div>
              <div class="inner-metric-sub">Active STEP LEO Club members</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">1 Resolution</div>
              <div class="inner-metric-label">NJ General Assembly</div>
              <div class="inner-metric-sub">Official State Citation</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact 1: STEP LEO Club Food & Candy Drives -->
    <section class="editorial-case-study" id="leo">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/community/Copy of cd - ah- group pic1.jpg" data-title="STEP LEO Club Youth Volunteers" data-badge="Civic Mobilization" data-caption="Aadya with student volunteer team delivering relief supplies to Anchor House.">
            <img src="assets/community/Copy of cd - ah- group pic1.jpg" alt="STEP LEO Club Delivery">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">01 &bull; STEP LEO Club &bull; Community Mobilization</p>
            <h2 class="case-title">Executive Presidency: Mobilizing 150+ Youth Volunteers</h2>
            <p class="case-subtitle">Coordinated multi-town collection drives delivering 3,500+ lbs of food and 420+ lbs of confectionery.</p>
            <p class="case-body">
              As President of the <strong>STEP LEO Club</strong>, Aadya spearheaded county-wide direct aid initiatives to alleviate food insecurity across Central New Jersey. Partnered with Mercer Street Friends, Anchor House youth shelter, and HomeFront to establish high-traffic collection hubs at schools and learning centers. Organized "Operation Sweet Treat" which collected and packaged over 420 lbs of candy and holiday items for children residing in transitional housing.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">3,500+ lbs</span>
                <span class="case-metric-desc">Pounds of Food</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">420+ lbs</span>
                <span class="case-metric-desc">Sweet Treat Candy</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">150+</span>
                <span class="case-metric-desc">Youth Volunteers</span>
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

    <!-- Impact 2: United Nations Keynote Address -->
    <section class="editorial-case-study" id="un" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="case-study-grid reversed">
          <div class="case-study-copy">
            <p class="case-kicker">02 &bull; United Nations Headquarters &bull; Global Advocacy</p>
            <h2 class="case-title">United Nations Youth Keynote: The Future of Service</h2>
            <p class="case-subtitle">Delivered keynote address before international delegates on youth agency in humanitarian action.</p>
            <p class="case-body">
              Invited to address an assembly of youth leaders and non-governmental delegates at the <strong>United Nations Headquarters</strong> in New York City. Her keynote address, titled <em>"The Architecture of Empathy: Scaling Grassroots Youth Mobilization,"</em> outlined actionable frameworks for mobilizing high school students into persistent civic stewardship and community disaster relief.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">United Nations</span>
                <span class="case-metric-desc">Keynote Address</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Global Delegates</span>
                <span class="case-metric-desc">Youth Governance</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Public Oratory</span>
                <span class="case-metric-desc">Keynote Speaker</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="beyond-stem.html#oratory" class="arrow-link">
                <span>View public speaking honors</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
          <div class="case-photo-frame evidence-link" data-src="assets/speaking/speech_stage.jpg" data-title="National Oratory & Public Address" data-badge="UN Keynote" data-caption="Aadya delivering public addresses on youth leadership and civic responsibility.">
            <img src="assets/speaking/speech_stage.jpg" alt="Aadya Speaking on Stage">
          </div>
        </div>
      </div>
    </section>

    <!-- Impact 3: State of New Jersey General Assembly Resolution -->
    <section class="editorial-case-study" id="njAssembly">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" data-title="State Legislative Commendation" data-badge="Legislative Citation" data-caption="Official legislative recognition ceremony.">
            <img src="assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg" alt="Legislative Commendation Citation">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">03 &bull; State Government Commendation</p>
            <h2 class="case-title">State of New Jersey General Assembly Resolution</h2>
            <p class="case-subtitle">Official legislative citation recognizing meritorious civic service and community dedication.</p>
            <p class="case-body">
              Formally commended through an official <strong>Legislative Resolution</strong> enacted by the General Assembly of the State of New Jersey. The bipartisan commendation cited Aadya's exceptional dedication to organizing community food distribution networks, providing ongoing support to homeless shelters, and setting a benchmark for civic responsibility among New Jersey youth.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">NJ Assembly</span>
                <span class="case-metric-desc">Legislative Citation</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Bipartisan</span>
                <span class="case-metric-desc">State Commendation</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Civic Service</span>
                <span class="case-metric-desc">Official Record</span>
              </div>
            </div>
            <div class="case-actions">
              <a href="about.html" class="arrow-link">
                <span>Read personal journey</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Community Field Stills -->
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
          <div class="still-item evidence-link" data-src="assets/community/Copy of cd - ah- group pic1.jpg" data-title="STEP LEO Youth Mobilization" data-badge="Youth Leadership" data-caption="High school volunteers organized for regional distribution logistics.">
            <img src="assets/community/Copy of cd - ah- group pic1.jpg" alt="Volunteer Coalition">
            <p class="still-caption">STEP LEO Club student volunteers coordinating regional food deliveries</p>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

with open('impact.html', 'w', encoding='utf-8') as f:
    f.write(impact_head + impact_body + footer_block)

print("Generated impact.html successfully")

# ==============================================================================
# 4. BEYOND-STEM.HTML
# ==============================================================================
beyond_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>Beyond STEM: Humanities &amp; Fine Arts — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="Humanities, creative writing, and music: Oxford John Locke Commendation, 3x published poetry, and Greenfield Hall recital.'
)

beyond_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Humanities &bull; Fine Arts &bull; Oratory</span>
          <h1 class="inner-hero-title">Moral Philosophy, <span class="italic-serif">Poetic Form</span> &amp; Classical Art</h1>
          <p class="inner-hero-lead">
            Exploring moral agency in autonomous algorithms through the Oxford John Locke Institute (Top 3% worldwide), publishing three award-winning poems, and performing classical piano and 1st chair flute.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Top 3%</div>
              <div class="inner-metric-label">Oxford John Locke</div>
              <div class="inner-metric-sub">Global High Commendation</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">3x Published</div>
              <div class="inner-metric-label">Poetry Broadsides</div>
              <div class="inner-metric-sub">Scholastic Silver Key winner</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">MSM Solo</div>
              <div class="inner-metric-label">Classical Music</div>
              <div class="inner-metric-sub">Greenfield Hall Chopin recital</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">1st Chair</div>
              <div class="inner-metric-label">Woodwinds</div>
              <div class="inner-metric-sub">Concert Band Solo Flute</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Beyond 1: Oxford John Locke Moral Philosophy -->
    <section class="editorial-case-study" id="oratory">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/speaking/speech_stage.jpg" data-title="National Oratory & Public Speaking Stage" data-badge="Oratory Champion" data-caption="Aadya competing on the national oratory stage.">
            <img src="assets/speaking/speech_stage.jpg" alt="National Oratory Stage">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">01 &bull; Moral Philosophy &bull; Oxford John Locke Institute</p>
            <h2 class="case-title">Oxford John Locke Global Commendation (Top 3%)</h2>
            <p class="case-subtitle">Rigorous philosophical inquiry into epistemic humility and autonomous algorithmic agency.</p>
            <p class="case-body">
              Awarded <strong>Global High Commendation (Top 3% worldwide)</strong> in the prestigious Oxford John Locke Institute Global Essay Competition, evaluated by senior Oxford faculty. Her prize treatise investigated whether artificial decision architectures can ever bear authentic moral culpability, or whether ethical weight remains tethered to human intention. Also earned <strong>First Place National Champion</strong> honors in public speaking from the North South Foundation.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Top 3%</span>
                <span class="case-metric-desc">Oxford Global Rank</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Oxford Faculty</span>
                <span class="case-metric-desc">Blind Adjudication</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">NSF Champion</span>
                <span class="case-metric-desc">National Oratory</span>
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

    <!-- Beyond 2: Published Poetry Broadsides -->
    <section class="editorial-content-section" id="poetry" style="background: rgba(239, 232, 222, 0.4);">
      <div class="container">
        <div class="section-head-editorial" style="text-align: center; margin-bottom: 40px;">
          <span class="eyebrow">Literary Arts &bull; Scholastic Silver Key</span>
          <h2 class="title">Three Published Poems</h2>
          <p class="desc" style="margin: 0 auto;">Reflecting on memory, stillness, human vulnerability, and the quiet dignity of the natural world.</p>
        </div>

        <div class="poetry-clean-grid">
          <!-- Poem 1 -->
          <div class="poetry-clean-card">
            <span class="poetry-award-tag">Published Anthology &bull; Selection</span>
            <h3 class="poetry-clean-title">The Celebration of Small</h3>
            <div class="poetry-clean-stanzas">The tea leaves settle softly in the cup,
not in despair, but knowing where to rest.
We measure grandness by what we lift up,
forgetting what remains within the chest.

A pine needle falls silently in shade,
a quiet seed that water learns to keep.
The longest rivers were by raindrops made,
before they taught the ocean how to weep.</div>
            <div class="poetry-footer-note">SCHOLASTIC SILVER KEY WINNER</div>
          </div>

          <!-- Poem 2 -->
          <div class="poetry-clean-card">
            <span class="poetry-award-tag">National Anthology &bull; Featured</span>
            <h3 class="poetry-clean-title">A Shift of Heart</h3>
            <div class="poetry-clean-stanzas">Between the ticking of a rusted clock,
a pendulum that hesitates mid-swing,
the stone gives slowly to the mountain rock,
yet knows the weight of every silent thing.

We walk across the bridges that we burned,
and wonder why the water looks so cold.
A tender truth is never truly learned,
until it breaks the hands that try to hold.</div>
            <div class="poetry-footer-note">NATIONAL LITERARY SELECTION</div>
          </div>

          <!-- Poem 3 -->
          <div class="poetry-clean-card">
            <span class="poetry-award-tag">Published Collection &bull; Folio</span>
            <h3 class="poetry-clean-title">The Frying Pan</h3>
            <div class="poetry-clean-stanzas">The cast iron remembers every flame,
the sizzle of the morning before dawn.
It bears no pride, it carries no sweet name,
yet feeds the living after night is gone.

A kitchen smells of rosemary and rye,
a mother's hand that turns the skillet round.
The greatest devotions do not reach the sky,
they stay right here, close to the humble ground.</div>
            <div class="poetry-footer-note">PUBLISHED POETRY BROADSIDE</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Beyond 3: Classical Music Repertoire -->
    <section class="editorial-case-study" id="music">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/writing_arts/flute_performance.png" data-title="1st Chair Flute Solo Performance" data-badge="Classical Music" data-caption="Aadya performing 1st chair flute at honors concert.">
            <img src="assets/writing_arts/flute_performance.png" alt="Aadya Performing 1st Chair Flute">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">03 &bull; Classical Music &bull; Greenfield Hall &amp; Ensemble</p>
            <h2 class="case-title">Solo Piano Repertoire &amp; 1st Chair Flute</h2>
            <p class="case-subtitle">Performing Chopin solo repertoire at Greenfield Hall and leading wind sections.</p>
            <p class="case-body">
              A classical pianist and flutist for over eight years, Aadya performed solo repertoire—including Chopin's <em>Nocturne in C-sharp Minor, Op. posth.</em>—at Manhattan School of Music's <strong>Greenfield Hall</strong>. She has served as 1st Chair Flutist in competitive wind ensembles, bringing lyrical phrase structure, disciplined rhythmic pulse, and deep ensemble cohesion to the concert stage.
            </p>
            <div class="case-metrics-bar">
              <div class="case-metric-cell">
                <span class="case-metric-num">Greenfield Hall</span>
                <span class="case-metric-desc">Solo Piano Recital</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">1st Chair</span>
                <span class="case-metric-desc">Wind Ensemble Flute</span>
              </div>
              <div class="case-metric-cell">
                <span class="case-metric-num">Chopin Op. Posth</span>
                <span class="case-metric-desc">Classical Repertoire</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""

with open('beyond-stem.html', 'w', encoding='utf-8') as f:
    f.write(beyond_head + beyond_body + footer_block)

print("Generated beyond-stem.html successfully")

# ==============================================================================
# 5. ABOUT.HTML
# ==============================================================================
about_head = header_block.replace(
    '<title>Aadya Agarwal — Autonomous Systems, Eco-Engineering &amp; Applied Research</title>',
    '<title>About &amp; Personal Journey — Aadya Agarwal</title>'
).replace(
    'content="Official portfolio of Aadya Agarwal.',
    'content="About Aadya Agarwal: student scholar at The Lawrenceville School, autonomous robotics engineer, biochar water researcher, and published writer.'
)

about_body = """  <main id="mainContent">
    <!-- Clean Editorial Hero -->
    <section class="inner-page-hero">
      <div class="container">
        <div class="inner-hero-header">
          <span class="inner-hero-eyebrow">Personal Journey &bull; The Lawrenceville School</span>
          <h1 class="inner-hero-title">At the Intersection of <span class="italic-serif">Precision</span>, Empathy &amp; Art</h1>
          <p class="inner-hero-lead">
            I have never believed that one must choose between the cold precision of an autonomous PID control loop, the chemical kinetics of biochar adsorption, and the moral philosophy of civic stewardship.
          </p>

          <div class="inner-hero-metrics">
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Class of '29</div>
              <div class="inner-metric-label">The Lawrenceville School</div>
              <div class="inner-metric-sub">Harkness table scholar</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">8 Years</div>
              <div class="inner-metric-label">STEM &amp; Robotics</div>
              <div class="inner-metric-sub">From FLL to WPI World #14</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">Oxford</div>
              <div class="inner-metric-label">Moral Philosophy</div>
              <div class="inner-metric-sub">John Locke Commendation</div>
            </div>
            <div class="inner-metric-tile">
              <div class="inner-metric-num">President</div>
              <div class="inner-metric-label">Civic Governance</div>
              <div class="inner-metric-sub">STEP LEO Club leader</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Editorial Memoir Feature -->
    <section class="editorial-case-study">
      <div class="container">
        <div class="case-study-grid">
          <div class="case-photo-frame evidence-link" data-src="assets/robotics/pic 1 - with robot.jpg" data-title="Aadya Agarwal" data-badge="Scholar Portrait" data-caption="Aadya Agarwal: student, researcher, and engineer at The Lawrenceville School.">
            <img src="assets/robotics/pic 1 - with robot.jpg" alt="Aadya Agarwal Portrait">
          </div>
          <div class="case-study-copy">
            <p class="case-kicker">Personal Narrative &bull; Ethos &amp; Inquiries</p>
            <h2 class="case-title">Empirical Rigor Grounded in Human Purpose</h2>
            <p class="case-subtitle">Testing hypotheses in the wet lab, measuring wheel slip with odometry, and listening deeply at the Harkness table.</p>
            <p class="case-body">
              Growing up with an insatiable curiosity for how the physical and human world operates, my journey has been defined by an obsession with empirical truth. When our robot drifted during autonomous matches, I didn't blame the carpet—I wrote high-order Bézier splines and integrated dead-wheel encoders. When I learned of heavy metal contamination in local watersheds, I partnered with American Biochar Company to run sorption batch trials.
            </p>
            <p class="case-body">
              At The Lawrenceville School, this ethos thrives through the Harkness pedagogy: no assertion stands without proof, listening is more potent than speaking first, and true scholarship flourishes where technical mastery meets ethical responsibility.
            </p>
            <div class="case-actions">
              <a href="#timeline" class="arrow-link">
                <span>Explore chronological journey</span>
                <span class="arrow" aria-hidden="true">&rarr;</span>
              </a>
              <a href="contact.html" class="arrow-link">
                <span>Counselor &amp; academic inquiry</span>
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
              This philosophy directly informs how I lead engineering and civic teams: intellectual bravery requires testing your hypothesis against thoughtful counterarguments, not seeking quick validation.
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

    <!-- Chronological Milestone Flow (2018 - 2026) -->
    <section class="editorial-content-section" id="timeline">
      <div class="container">
        <div class="section-head-editorial" style="text-align: center; margin-bottom: 48px;">
          <span class="eyebrow">Chronology &bull; Verified Milestones</span>
          <h2 class="title">The Evolution of a Scholar &amp; Builder</h2>
          <p class="desc" style="margin: 0 auto;">Eight years of deliberate exploration, engineering iteration, and community service.</p>
        </div>

        <div class="clean-timeline-flow">
          <div class="timeline-milestone-node">
            <span class="timeline-year-pill">2025 &ndash; 2026</span>
            <h3 class="timeline-node-title">The Lawrenceville School Scholar &amp; FTC Control Lead</h3>
            <p class="timeline-node-text">
              Heading autonomous controls for the Lawrenceville FIRST Tech Challenge robotics team using Pedro Pathing. Earning Oxford John Locke Institute Global High Commendation (Top 3%) in philosophy. Enrolled in 15 AP courses and captaining tennis.
            </p>
          </div>

          <div class="timeline-milestone-node">
            <span class="timeline-year-pill">2024</span>
            <h3 class="timeline-node-title">MoniVitals.com Deployment &amp; UN Youth Keynote</h3>
            <p class="timeline-node-text">
              Co-founded MoniVitals.com remote telemedicine portal. Delivered keynote address on youth service at the United Nations Headquarters. Received State of New Jersey General Assembly legislative resolution commendation.
            </p>
          </div>

          <div class="timeline-milestone-node">
            <span class="timeline-year-pill">2023</span>
            <h3 class="timeline-node-title">WPI World Open #14 &amp; American Biochar Co. Partnership</h3>
            <p class="timeline-node-text">
              Ranked #14 out of 108 international teams at the WPI US Open International Invitational. Initiated biochar water filtration trials with American Biochar Company (featured on Ambiochar.com). Won 1st Place in MIT Solve Marine Buoy challenge.
            </p>
          </div>

          <div class="timeline-milestone-node">
            <span class="timeline-year-pill">2021 &ndash; 2022</span>
            <h3 class="timeline-node-title">STEP LEO Club Presidency &amp; Wet-Bench Certification</h3>
            <p class="timeline-node-text">
              Elected President of STEP LEO Club, mobilizing 150+ youth and 3,500+ lbs of food. Completed BioResearch Academy wet-bench certification in recombinant DNA, PCR, and gel electrophoresis.
            </p>
          </div>

          <div class="timeline-milestone-node">
            <span class="timeline-year-pill">2018 &ndash; 2020</span>
            <h3 class="timeline-node-title">FIRST LEGO League &amp; National Oratory Champion</h3>
            <p class="timeline-node-text">
              Won First Place National Champion in public speaking from the North South Foundation (NSF). Competed in FIRST LEGO League (FLL), discovering a lifelong passion for autonomous systems and embedded control.
            </p>
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

print("Generated about.html successfully")
print("ALL 5 PAGES REBUILT CLEANLY WITH HOME PAGE COLOR THEME AND AUTHENTIC CONTENT!")

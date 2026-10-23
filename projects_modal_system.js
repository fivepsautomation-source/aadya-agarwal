/**
 * projects_modal_system.js
 * Authentic modal dialog & interactive project viewer for Aadya Agarwal Portfolio.
 * Displays clean text 'Explore the work' accordions and dedicated 'Photo Gallery' below it for all cards.
 */
(function() {
  const PROJECTS_DATA = [
  {
    "title": "FIRST Robotics — FLL & FTC",
    "group": "Robotics",
    "category": "Lead Coder & Programming Team · 2020–Present",
    "summary": "From lead coder of an FLL team invited to the WPI US Open to the Lawrenceville FIRST Tech Challenge programming team — building autonomous control and computer-vision pipelines, and teaching robotics to middle schoolers.",
    "cardImage": "assets/robotics/pic 2 - Team award.JPG",
    "heroImage": "assets/robotics/pic 2 - Team award.JPG",
    "badges": [
      {
        "label": "FTC",
        "tone": "plum"
      },
      {
        "label": "FLL",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "Lead coder of an FLL team invited to the prestigious WPI US Open championship",
      "Active member of the Lawrenceville School FIRST Tech Challenge (FTC) programming team",
      "Engineered autonomous driving trajectories and sensory navigation using Java and OpenCV computer-vision pipelines",
      "Designed custom gear-reduction attachments, 3D printed sensor brackets, and closed-loop motor encoders",
      "Mentored and coached younger middle school students in robotics principles, code architecture, and algorithm design"
    ],
    "attachments": [],
    "videos": [],
    "sections": [
      {
        "title": "Autonomous Navigation & Computer-Vision Algorithms",
        "intro": "Implemented autonomous navigation routines utilizing sensor telemetry, AprilTag detection, and OpenCV vision pipelines to achieve high-precision field localization and game element scoring."
      },
      {
        "title": "Mechanical Architecture & Drive-train Iterations",
        "intro": "Prototyped lightweight intake mechanisms and multi-stage lift systems using custom 3D-printed brackets and high-torque motor gearboxes engineered for rapid cycle times."
      },
      {
        "title": "STEM Mentorship & Community Outreach",
        "intro": "Led outreach workshops teaching middle school students foundational Java, robotics concepts, and engineering notebook documentation to expand youth STEM access."
      }
    ],
    "gallerySubtitle": "Competition matches, team awards, robot build iterations, and WPI championship presentation.",
    "gallery": [
      {
        "src": "assets/robotics/pic 2 - Team award.JPG",
        "alt": "FIRST Robotics Team Award",
        "caption": "FIRST Robotics Team Award & Recognition"
      },
      {
        "src": "assets/robotics/pic 1 - with robot.jpg",
        "alt": "Aadya with competition robot",
        "caption": "Hands-on robot tuning and drive-train testing"
      },
      {
        "src": "assets/robotics/pic 10 - wpi award.jpg",
        "alt": "WPI Award Ceremony",
        "caption": "WPI US Open championship award presentation"
      },
      {
        "src": "assets/robotics/pic 11 - WPI goodies.jpg",
        "alt": "WPI Championship Experience",
        "caption": "WPI national tournament participation and badge honors"
      },
      {
        "src": "assets/robotics/pic12 -WPI Team.png",
        "alt": "WPI Championship Team",
        "caption": "Full robotics team celebrating at WPI US Open"
      },
      {
        "src": "assets/robotics/pic 6 - Team Award.JPG",
        "alt": "FIRST LEGO League Award",
        "caption": "Championship banner and trophy honors"
      },
      {
        "src": "assets/robotics/pic 3 - mt olive.JPG",
        "alt": "Mt Olive Regional Event",
        "caption": "Regional tournament field trials and pit demonstrations"
      },
      {
        "src": "assets/robotics/pic 8 - On the board.jpg",
        "alt": "Strategy and Autonomous Mapping",
        "caption": "Field strategy analysis and autonomous game run planning"
      }
    ]
  },
  {
    "title": "MoniVitals: Equitable Vitals Monitor & App",
    "group": "Projects",
    "category": "Health technology",
    "summary": "I brought MoniVitals to our local farmers market and senior outreach events, offering neighbors a free check of their critical vitals in under a minute.",
    "cardImage": "assets/ref_images/projects_monivitals-market.webp",
    "heroImage": "assets/ref_images/projects_monivitals-market.webp",
    "badges": [
      {
        "label": "HealthTech",
        "tone": "plum"
      },
      {
        "label": "ESP32",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "Phone-connected, non-invasive vital screening platform developed for accessible and equitable community health",
      "Measures six vital markers in under a minute, including blood oxygen (SpO2), pulse rate, body temperature, and estimated blood pressure",
      "Private real-time readings transmitted securely to each visitor's smartphone",
      "Python data telemetry backend integrated with edge ESP32 microcontroller, MAX30102 PPG sensor, and MLX90614 infrared optical thermopile",
      "Conducted over 100 free vital screenings across local New Jersey farmers markets, community centers, and senior living facilities"
    ],
    "attachments": [
      {
        "label": "MoniVitals project board (PDF)",
        "href": "docs/monivitals-board.pdf"
      }
    ],
    "videos": [],
    "sections": [
      {
        "title": "Community Field Screening & Senior Care Deployment",
        "intro": "Deployed MoniVitals across local New Jersey farmers markets and senior outreach events, conducting over 100 free vital screenings for community elders and underserved families. Optimized font sizing, high-contrast visual indicators, and voice-assisted telemetry readings for senior accessibility."
      },
      {
        "title": "Hardware Prototype, Custom Enclosure & ESP32 Microcontroller",
        "intro": "Engineered custom 3D printed housing in Fusion 360 with ergonomic fingertip alignment and optical light baffling. Integrated MAX30102 optical sensor and MLX90614 thermopile over I2C multiplexed bus with low-power sleep state management."
      },
      {
        "title": "Pulse Oximetry Optical Bias Mitigation Research",
        "intro": "Investigated wavelength absorption differentials across varying epidermal melanin concentrations in PPG sensors to eliminate systemic bias in non-invasive biometric monitoring, evaluating multi-wavelength calibration curves."
      }
    ],
    "gallerySubtitle": "Community screening drives, senior outreach, hardware enclosure fabrication, and telemetry testing.",
    "gallery": [
      {
        "src": "assets/ref_images/projects_monivitals-market.webp",
        "alt": "MoniVitals: Equitable Vitals Monitor & App",
        "caption": "MoniVitals: Equitable Vitals Monitor & App"
      },
      {
        "src": "assets/monivitals/20260829_100521.jpg",
        "alt": "MoniVitals: Equitable Vitals Monitor & App",
        "caption": "MoniVitals: Equitable Vitals Monitor & App"
      },
      {
        "src": "assets/monivitals/20260829_084022.jpg",
        "alt": "MoniVitals: Equitable Vitals Monitor & App",
        "caption": "MoniVitals: Equitable Vitals Monitor & App"
      },
      {
        "src": "assets/monivitals/20260829_100443.jpg",
        "alt": "MoniVitals: Equitable Vitals Monitor & App",
        "caption": "MoniVitals: Equitable Vitals Monitor & App"
      },
      {
        "src": "assets/monivitals/20260829_084028.jpg",
        "alt": "MoniVitals: Equitable Vitals Monitor & App",
        "caption": "MoniVitals: Equitable Vitals Monitor & App"
      },
      {
        "src": "assets/monivitals/20260829_100506_1_.jpg",
        "alt": "MoniVitals: Equitable Vitals Monitor & App",
        "caption": "MoniVitals: Equitable Vitals Monitor & App"
      },
      {
        "src": "assets/monivitals/20260829_094941_1_.jpg",
        "alt": "MoniVitals: Equitable Vitals Monitor & App",
        "caption": "MoniVitals: Equitable Vitals Monitor & App"
      }
    ]
  },
  {
    "title": "Autonomous Ocean pH Buoy",
    "group": "Projects",
    "category": "Climate technology \u00b7 2025 concept",
    "summary": "A sensor-driven buoy concept designed to detect low water pH and dispense calcium carbonate in response.",
    "cardImage": "projects/ocean-project-presentation.jpg",
    "heroImage": "projects/ocean-project-presentation.jpg",
    "badges": [
      {
        "label": "Climate Tech",
        "tone": "plum"
      },
      {
        "label": "3M Challenge",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "pH sensor feeds real-time water quality readings to an Arduino microcontroller",
      "A servo rotates a 3D-printed dispensing disk below a refillable mineral chamber",
      "Low-pH readings trigger a measured calcium carbonate release in the closed-loop design",
      "3M Young Scientist Challenge concept brief & system architecture submission",
      "Explored predictive dosing with algorithmic feedback and solar-powered continuous runtime"
    ],
    "attachments": [],
    "videos": [
      {
        "type": "local",
        "src": "projects/videos/3m-buoy-preview.mp4",
        "title": "3M Young Scientist Challenge submission",
        "poster": "projects/ocean-project-presentation.jpg"
      }
    ],
    "sections": [
      {
        "title": "System architecture and 3M challenge brief",
        "intro": "A pH sensor, Arduino and servo-operated 3D-printed disk form a closed-loop calcium carbonate dispenser. Next steps include field testing, dispenser calibration, solar power and predictive dosing."
      },
      {
        "title": "Autonomous Closed-Loop Marine Dosing",
        "intro": "Submersible sensor node constantly samples coastal water acidity. Upon detecting localized acidification events, calibrated alkaline reagent is released to protect marine calcifiers and restore pH balance."
      }
    ],
    "gallerySubtitle": "System architecture, Arduino circuit schematics, 3M challenge brief, and 3D dispensing model.",
    "gallery": [
      {
        "src": "projects/ocean-project-presentation.jpg",
        "alt": "Autonomous Ocean pH Buoy",
        "caption": "Autonomous Ocean pH Buoy"
      }
    ]
  },
  {
    "title": "Biochar Water Treatment",
    "group": "Projects",
    "category": "Experimental research \u00b7 2026",
    "summary": "Bench tests comparing waste-derived biochars for water remediation, with pH, filtration and toxicity measurements. Presented peer-reviewed research at IEEE/ISEC at Princeton University.",
    "cardImage": "projects/water-treatment-setup.jpg",
    "heroImage": "projects/water-treatment-setup.jpg",
    "badges": [
      {
        "label": "IEEE/ISEC",
        "tone": "plum"
      },
      {
        "label": "NJWEA",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "Compared softwood and agricultural-waste biochar samples in controlled water-treatment trials",
      "Measured pH and water-quality changes across treatment trials over time",
      "Explored heavy-metal and nutrient removal with a floating treatment device concept",
      "Second place in Earth & Environmental Science at Mercer Science & Engineering Fair (MSEF)",
      "Stockholm Junior Water Prize Regional Award & Acceptance Speech at NJWEA",
      "NOAA Taking the Pulse of the Planet award"
    ],
    "attachments": [],
    "videos": [
      {
        "type": "youtube",
        "src": "ELyxcPwMp3M",
        "title": "NJWEA Stockholm Junior Water Prize Special Award acceptance speech",
        "poster": ""
      }
    ],
    "sections": [
      {
        "title": "IEEE/ISEC 2026 presentation at Princeton University",
        "intro": "Approved abstract: \u201cComparative Analysis of Softwood and Agricultural Waste Biochars for Heavy Metal and Nutrient Remediation in Water.\u201d Presented at the IEEE/ISEC K\u201312 conference at Princeton University."
      },
      {
        "title": "NJWEA & science-fair recognition",
        "intro": "Biochar research earned second place in Earth and Environmental Science at the Mercer Science and Engineering Fair, a Stockholm Junior Water Prize regional award, a NOAA Taking the Pulse of the Planet award, and an invitation to present at the NJWEA Annual Conference."
      },
      {
        "title": "Materials and experimental setup",
        "intro": "Compared softwood and agricultural-waste biochars in controlled water-treatment trials, with sample vessels and pH measurements."
      },
      {
        "title": "Device and filtration design",
        "intro": "Explored a floating device that could carry biochar filtration media and water-quality sensors with end-to-end multi-stage filtration."
      },
      {
        "title": "Measurements and results",
        "intro": "Logged repeated measurements and plotted changes in water quality over time to compare treatment conditions."
      }
    ],
    "gallerySubtitle": "Bench trials, IEEE presentation at Princeton University, NJWEA symposium, and award ceremonies.",
    "gallery": [
      {
        "src": "projects/water-treatment-setup.jpg",
        "alt": "Biochar Water Treatment",
        "caption": "Biochar Water Treatment"
      }
    ]
  },
  {
    "title": "AI for a Better World",
    "group": "Projects",
    "category": "MIT Day of AI \u00b7 July 2026",
    "summary": "One of five national MIT Solve AI for a Better World winners, I presented an AI-powered water-quality node at the MIT Media Lab.",
    "cardImage": "projects/mit-day-ai-stage.jpg",
    "heroImage": "projects/mit-day-ai-stage.jpg",
    "badges": [
      {
        "label": "MIT Solve",
        "tone": "plum"
      },
      {
        "label": "MIT Media Lab",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "The biochar remediation concept combines water-quality sensing, edge machine learning and an actionable treatment response",
      "The presentation proposed training on river, lake and global water-measurement data",
      "Human review, safety limits and decision logs were part of the responsible-AI plan",
      "Named Leopold Scholar in Ecology and Ethics by The Lawrenceville School"
    ],
    "attachments": [],
    "videos": [],
    "sections": [
      {
        "title": "The technical pitch",
        "intro": "The proposed IoT node would pair water-quality sensors with AI-assisted treatment decisions. River, lake and global measurements inform the model plan; human review, fixed safety limits and decision logs govern its use."
      },
      {
        "title": "On stage and recognition at MIT Media Lab",
        "intro": "Presented the water-remediation concept at the MIT Media Lab and received recognition as an AI for a Better World winner and Leopold Scholar."
      }
    ],
    "gallerySubtitle": "On-stage presentation, AI methodology slides, and award recognition at the MIT Media Lab.",
    "gallery": [
      {
        "src": "projects/mit-day-ai-stage.jpg",
        "alt": "AI for a Better World",
        "caption": "AI for a Better World"
      }
    ]
  },
  {
    "title": "FIRST Robotics \u2014 FLL & FTC",
    "group": "Robotics & Coding",
    "category": "Lead Coder & Programming Team \u00b7 2020\u2013Present",
    "summary": "From lead coder of an FLL team invited to the WPI US Open to the Lawrenceville FIRST Tech Challenge programming team \u2014 building autonomous control and computer-vision pipelines, and teaching robotics to middle schoolers.",
    "cardImage": "projects/robotics/team-award.jpg",
    "heroImage": "projects/robotics/team-award.jpg",
    "badges": [
      {
        "label": "FTC",
        "tone": "plum"
      },
      {
        "label": "FLL",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "FTC (2025\u2013Present): autonomous and driver-assisted motion control with Pedro Pathing for the 2026\u20132027 BioBuzz season",
      "Limelight computer-vision pipelines for AprilTag field localization and real-time intake monitoring",
      "Community outreach: teaching robot design, algorithmic thinking and Python basics to 10\u201315 middle-school students across three hands-on sessions",
      "FLL (2020\u20132024): Lead Coder & Innovation Lead for The LeapcoderZ, an eight-person team"
    ],
    "attachments": [],
    "videos": [],
    "sections": [
      {
        "title": "FIRST Tech Challenge \u2014 Lawrenceville (2025\u2013Present)",
        "intro": "On the Lawrenceville School FTC programming team for the 2026\u20132027 BioBuzz season: developing and refining autonomous and driver-assisted motion control with Pedro Pathing, and building Limelight computer-vision pipelines for AprilTag field localization and real-time intake monitoring. Through FTC community outreach, teaching robotics to 10\u201315 students at a local middle school across three hands-on sessions."
      },
      {
        "title": "FIRST Lego League \u2014 The LeapcoderZ (2020\u20132024)",
        "intro": "Lead Coder and Innovation Lead for The LeapcoderZ. Award record: Robot Design Award Finalist at the WPI FLL US Open World (June 2024), Robot Design Award at NJ Regionals (2023\u20132024), Breakthrough Award at NJ State (2023\u20132024), and Robot Design Award at NJ Regionals (2022\u20132023). Architected multi-sensor line-tracking, PID gyro stabilization, and modular attachment quick-swaps."
      },
      {
        "title": "PDS Panther Hackathon, Grade 7th \u2013 Best Beginner Hackathon",
        "intro": "Won Best Beginner Hack at the PDS Panther Hackathon in Grade 7th for \u201cHobbyPals\u201d \u2014 an interactive online platform helping youth pursue creative hobbies while developing healthy screen-time habits. Rapid ideation, front-end interaction flow, and functional web prototype created under hackathon time limits. Delivered technical pitch and live interactive demo to judge panel."
      }
    ],
    "gallerySubtitle": "Moments from FIRST Tech Challenge, WPI US Open World, NJ Regionals, and Panther Hackathon.",
    "gallery": [
      {
        "src": "projects/robotics/with-robot.jpg",
        "alt": "Aadya with the competition robot",
        "caption": "With the competition robot"
      },
      {
        "src": "projects/robotics/on-the-board.jpg",
        "alt": "Aadya coding robot behavior on the board",
        "caption": "Programming on the board"
      },
      {
        "src": "projects/robotics/on-the-board-2.jpg",
        "alt": "Aadya working through robot code",
        "caption": "Refining autonomous routines"
      },
      {
        "src": "projects/robotics/engineering-device.jpg",
        "alt": "Close-up of the engineered robot mechanism",
        "caption": "Engineering the mechanism"
      },
      {
        "src": "projects/robotics/devpost.jpg",
        "alt": "Robotics project submission",
        "caption": "Project submission"
      },
      {
        "src": "projects/robotics/wpi-team.png",
        "alt": "The LeapcoderZ team at the WPI US Open",
        "caption": "The LeapcoderZ at the WPI US Open World"
      },
      {
        "src": "projects/robotics/wpi-opening-ceremony.jpg",
        "alt": "WPI FLL US Open opening ceremony",
        "caption": "WPI US Open opening ceremony"
      },
      {
        "src": "projects/robotics/wpi-award.jpg",
        "alt": "Team receiving a Robot Design award at WPI",
        "caption": "Robot Design Award Finalist \u2014 WPI US Open, 2024"
      },
      {
        "src": "projects/robotics/wpi-pit-visitor-1.jpg",
        "alt": "Presenting the robot to a pit visitor at WPI",
        "caption": "Sharing the robot in the pit"
      },
      {
        "src": "projects/robotics/wpi-pit-visitor-2.jpg",
        "alt": "Explaining the innovation project to a visitor",
        "caption": "Explaining the innovation project"
      },
      {
        "src": "projects/robotics/wpi-field-practice.jpg",
        "alt": "Field practice session at WPI",
        "caption": "Field practice at WPI"
      },
      {
        "src": "projects/robotics/wpi-pit-work.jpg",
        "alt": "Working on the robot in the pit area",
        "caption": "Pit tuning between matches"
      },
      {
        "src": "projects/robotics/fll-award-regional.jpg",
        "alt": "Team with the FLL regional award",
        "caption": "Robot Design Award \u2014 NJ Regionals"
      },
      {
        "src": "projects/robotics/team-board-review.jpg",
        "alt": "Reviewing strategy on the competition board",
        "caption": "Mission run review"
      },
      {
        "src": "projects/robotics/fll-regional-award-2.jpg",
        "alt": "Second regional award presentation",
        "caption": "Breakthrough Award \u2014 NJ State"
      },
      {
        "src": "projects/robotics/fll-regional-ceremony.jpg",
        "alt": "Ceremony photo with judges",
        "caption": "Regional awards ceremony"
      },
      {
        "src": "projects/robotics/fll-field-table.jpg",
        "alt": "Setting up the robot on the field table",
        "caption": "Competition table setup"
      },
      {
        "src": "projects/robotics/team-photo-regional.jpg",
        "alt": "Team photo at the regional tournament",
        "caption": "The LeapcoderZ team"
      },
      {
        "src": "projects/robotics/team-working.jpg",
        "alt": "Team collaborating during practice",
        "caption": "Collaborative practice session"
      },
      {
        "src": "projects/robotics/panther-hackathon-1.jpg",
        "alt": "Panther Hackathon teamwork",
        "caption": "Panther Hackathon \u2014 Best Beginner Hack"
      },
      {
        "src": "projects/robotics/panther-hackathon-2.jpg",
        "alt": "Panther Hackathon presentation",
        "caption": "Pitching HobbyPals to judges"
      }
    ]
  },
  {
    "title": "Writing & Publications",
    "group": "Writing & Arts",
    "category": "Creative & academic writing \u00b7 2021\u2013present",
    "summary": "Commended in the international John Locke Institute Global Essay Prize; multiple published poems exploring environmental consciousness, identity, and ethics.",
    "cardImage": "projects/writing/scholastic-honorable-mention.jpeg",
    "heroImage": "assets/ref_images/projects_john-locke_framed.jpg",
    "badges": [
      {
        "label": "John Locke",
        "tone": "plum"
      },
      {
        "label": "Scholastic",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "Commended in John Locke Global Essay Competition from 19,000+ international entries",
      "Recipient of school annual English and Humanities literary prize",
      "Poetry published in national youth anthologies exploring nature and equity",
      "Contributed essays on ethical technology and environmental stewardship"
    ],
    "attachments": [
      {
        "label": "Selected writing sample (PDF)",
        "href": "docs/writing-sample.pdf"
      }
    ],
    "videos": [],
    "sections": [
      {
        "title": "John Locke Global Essay Commendation",
        "intro": "Selected for High Commendation in the international John Locke Institute Global Essay Competition from over 19,000 international submissions, exploring ethical technology, environmental consciousness, and stewardship."
      },
      {
        "title": "Published Poetry & Literary Anthologies (2021\u2013Present)",
        "intro": "Work published in national youth anthologies including The Telling Room, Skipping Stones magazine, and A Celebration of Poets."
      }
    ],
    "gallerySubtitle": "John Locke Institute commendation, literary journal features, and published poetry anthologies.",
    "gallery": [
      {
        "src": "assets/ref_images/projects_john-locke_framed.jpg",
        "alt": "John Locke Global Essay Prize Commendation",
        "caption": "John Locke Global Essay Commendation"
      },
      {
        "src": "assets/certificates/John Locke 2026 - High Commendation.jpg",
        "alt": "John Locke Institute Certificate of High Commendation",
        "caption": "John Locke High Commendation Certificate"
      },
      {
        "src": "projects/writing/scholastic-honorable-mention.jpeg",
        "alt": "Scholastic Art & Writing Honorable Mention certificate",
        "caption": "Scholastic Art & Writing \u2014 Honorable Mention"
      },
      {
        "src": "projects/writing/when-kindness-is-planted.webp",
        "alt": "Poem 'When Kindness Is Planted' in The Telling Room",
        "caption": "The Telling Room Anthology, 2022"
      },
      {
        "src": "projects/writing/balance-skipping-stones.jpg",
        "alt": "Poem 'Balance' in Skipping Stones",
        "caption": "Skipping Stones Multicultural Magazine"
      },
      {
        "src": "projects/writing/in-a-shift-of-heart.png",
        "alt": "Poem 'In a Shift of Heart'",
        "caption": "Published Poetry Feature, 2023"
      },
      {
        "src": "projects/writing/my-moms-frying-pan.png",
        "alt": "Poem 'My Mom's Frying Pan'",
        "caption": "Anthology Publication, 2024"
      },
      {
        "src": "projects/writing/celebration-of-poets.png",
        "alt": "A Celebration of Poets anthology feature",
        "caption": "A Celebration of Poets Feature"
      },
      {
        "src": "projects/writing/anthology-fall-2024.jpeg",
        "alt": "Anthology feature, Fall 2024",
        "caption": "National Youth Poetry Anthology"
      },
      {
        "src": "projects/writing/pds-feature-2023.webp",
        "alt": "Princeton Day School feature post about Aadya's writing",
        "caption": "Princeton Day School Feature"
      }
    ]
  },
  {
    "title": "Music, Theater & Speaking",
    "group": "Writing & Arts",
    "category": "Piano \u00b7 Flute \u00b7 Theater \u00b7 Public Speaking",
    "summary": "Piano Grand Prize at the Music-Fest International Rising Talent Festival, solo recital at Greenfield Hall at Manhattan School of Music, 1st chair flutist in wind ensemble, technical theater stage crew, and award-winning public speaking.",
    "cardImage": "projects/piano-manhattan-school.jpg",
    "heroImage": "projects/piano-manhattan-school.jpg",
    "badges": [
      {
        "label": "Music-Fest Grand Prize",
        "tone": "plum"
      },
      {
        "label": "Manhattan School of Music",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "Piano Grand Prize \u2014 Music-Fest International Rising Talent Festival with solo recital at Manhattan School of Music",
      "Flute (2021\u2013Present): Middle & High School Jazz Band, 1st Chair Flutist; NJMTA auditions and Honors recitals at Westminster Conservatory and Rutgers University",
      "Theater: backstage technical theater, stage manager and production assistant, with occasional stage performance",
      "Public speaking: Toastmasters YLP Outstanding Communicator, interschool contest semi-finalist, and North South Foundation 1st place"
    ],
    "attachments": [],
    "videos": [],
    "sections": [
      {
        "title": "Piano \u2014 Music-Fest Grand Prize & Manhattan School of Music",
        "intro": "Grand Prize at the Music-Fest International Rising Talent Festival, with a solo classical recital at Greenfield Hall, Manhattan School of Music. Studio recitals and honors recitals at Westminster Conservatory, Princeton."
      },
      {
        "title": "Flute (2021\u2013Present) \u2014 1st Chair & NJMTA Honors",
        "intro": "1st Chair Flutist in competitive school and regional wind ensembles, NJMTA Spring Recital Honors Award winner, and woodwind section leader."
      },
      {
        "title": "Theater \u2014 Technical Stage & Performance",
        "intro": "School and community theater: backstage technical theater, stage manager and production assistant, with stage performance in Lawrenceville Shakespeare\u2019s Much Ado About Nothing."
      },
      {
        "title": "Public Speaking & Debate Honors",
        "intro": "Lawrenceville school-wide and Annual Interschool Public Speaking Contests semi-finalist; ETS Toastmasters Outstanding Communicator Award; 1st place at North South Foundation Public Speaking Contest."
      },
      {
        "title": "Visual Arts Gallery (2020\u20132024)",
        "intro": "Visual art portfolio spanning classical sketch, watercolor, and 3rd-grade yearbook-cover contest winner."
      }
    ],
    "gallerySubtitle": "Piano recitals at Manhattan School of Music, jazz band flute performances, technical theater, and visual art.",
    "gallery": [
      {
        "src": "projects/piano-manhattan-school.jpg",
        "alt": "Aadya performing piano at the Manhattan School of Music",
        "caption": "Music-Fest Recital \u2014 Manhattan School of Music"
      },
      {
        "src": "projects/piano-performance-2.jpg",
        "alt": "Aadya at the piano in classical recital",
        "caption": "Piano Solo Performance"
      },
      {
        "src": "projects/music/musicfest-grand-prize-recital.jpg",
        "alt": "Music-Fest Rising Talent Grand Prize Recital",
        "caption": "Music-Fest Grand Prize Recitalist"
      },
      {
        "src": "projects/music/musicfest-grand-prize.jpeg",
        "alt": "Receiving Music-Fest International Grand Prize",
        "caption": "Music-Fest Grand Prize Trophy"
      },
      {
        "src": "assets/certificates/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg",
        "alt": "Grand Prize Recital Certificate at Greenfield Hall, Manhattan School of Music",
        "caption": "Manhattan School of Music Recital Certificate"
      },
      {
        "src": "projects/music/piano-award.png",
        "alt": "Piano award certificate",
        "caption": "Classical Piano Distinction"
      },
      {
        "src": "projects/music/archive/piano-musicfest-recital.jpg",
        "alt": "Aadya at the Music-Fest recital",
        "caption": "Music-Fest Recital Stage"
      },
      {
        "src": "projects/music/archive/piano-njmta-honors.jpg",
        "alt": "Aadya piano recital performance",
        "caption": "Classical Piano Honors Recital"
      },
      {
        "src": "projects/music/flute-aadya.png",
        "alt": "Aadya performing classical flute",
        "caption": "Wind Ensemble 1st Chair Flutist"
      },
      {
        "src": "projects/music/njmta-flute-honors.jpeg",
        "alt": "NJMTA Flute Honors Recital certificate",
        "caption": "NJMTA Flute Spring Honors Award"
      },
      {
        "src": "assets/writing_arts/flute_performance.png",
        "alt": "Flute solo in concert hall",
        "caption": "Flute Concert Soloist"
      },
      {
        "src": "assets/writing_arts/Aadya Flute Pic1.png",
        "alt": "Aadya with concert flute",
        "caption": "Wind Ensemble Section Leader"
      },
      {
        "src": "assets/certificates/NJMTA Flute Honors Recital.jpeg",
        "alt": "NJMTA Recital Certificate",
        "caption": "Statewide Honors Recognition"
      },
      {
        "src": "projects/flute-1.png",
        "alt": "Aadya playing flute",
        "caption": "Chamber & Jazz Band Flute"
      },
      {
        "src": "projects/flute-2.jpg",
        "alt": "Flute rehearsal",
        "caption": "Sectional Rehearsal"
      },
      {
        "src": "projects/flute-seniors.jpeg",
        "alt": "Playing flute for senior living residents",
        "caption": "Music Therapy for Seniors"
      },
      {
        "src": "projects/music/archive/flute-advanced-band-concert.png",
        "alt": "Advanced band concert first chair",
        "caption": "First Chair \u2014 Advanced Band"
      },
      {
        "src": "projects/theater/much-ado-about-nothing.png",
        "alt": "Much Ado About Nothing theatrical production",
        "caption": "Much Ado About Nothing Production"
      },
      {
        "src": "projects/theater/archive/the-day-the-internet-died.jpg",
        "alt": "Scene from The Day The Internet Died",
        "caption": "Technical Stage Crew & Cast"
      },
      {
        "src": "projects/theater/archive/spring-musical.jpg",
        "alt": "Spring musical production",
        "caption": "Spring Musical Stage"
      },
      {
        "src": "projects/theater/archive/ets-toastmasters-award.png",
        "alt": "ETS Youth Toastmasters Outstanding Communicator Award",
        "caption": "Toastmasters Outstanding Communicator"
      },
      {
        "src": "projects/theater/archive/nsf-learning-journey-excellence.png",
        "alt": "North South Foundation Public Speaking 1st Place",
        "caption": "NSF Public Speaking 1st Place Award"
      },
      {
        "src": "projects/art/art-18-2024.jpg",
        "alt": "Artwork by Aadya, 2024",
        "caption": "Original Artwork, 2024"
      },
      {
        "src": "projects/art/art-20-2024.jpg",
        "alt": "Visual art, 2024",
        "caption": "Mixed Media Artwork, 2024"
      },
      {
        "src": "projects/art/art-16-2023.webp",
        "alt": "Artwork, 2023",
        "caption": "Fine Art Portfolio, 2023"
      },
      {
        "src": "projects/art/artwork-6-2023.jpg",
        "alt": "Original artwork",
        "caption": "Original Sketch, 2023"
      },
      {
        "src": "projects/art/artwork-2-2023.jpg",
        "alt": "Original artwork",
        "caption": "Color Study, 2023"
      },
      {
        "src": "projects/art/artwork-11-2022.jpg",
        "alt": "Original artwork",
        "caption": "Illustration, 2022"
      },
      {
        "src": "projects/art/artwork-7-2022.jpg",
        "alt": "Original artwork",
        "caption": "Nature Drawing, 2022"
      },
      {
        "src": "projects/art/artwork-12-yearbook-cover-2020.jpg",
        "alt": "Yearbook cover contest-winning artwork",
        "caption": "Yearbook Cover Contest Winner"
      }
    ]
  },
  {
    "title": "Mercer County Hunger Relief & Meal Packaging Drives",
    "group": "School & Community",
    "category": "School & Community",
    "summary": "Spearheaded grassroots community drives, packing over 3,500 lbs of shelf-stable food and mobilizing youth volunteers across Mercer County food pantries.",
    "cardImage": "assets/ref_images/projects_hunger-donation_framed.jpg",
    "heroImage": "assets/ref_images/projects_hunger-donation_framed.jpg",
    "badges": [
      {
        "label": "Civic Leadership",
        "tone": "plum"
      },
      {
        "label": "Youth Volunteering",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "Mobilized 150+ youth and student volunteers for regional meal packaging",
      "Coordinated logistics with Mercer County food banks and community shelters",
      "Organized annual holiday candy and non-perishable drives for local children",
      "Direct community leadership recognized by local and state representatives"
    ],
    "attachments": [],
    "videos": [],
    "sections": [
      {
        "title": "Grassroots Logistics & Youth Mobilization",
        "intro": "Organized supply collection points across regional schools, managed volunteer shift scheduling, and ensured safe handling and direct delivery of nutritional meals to local food pantries."
      },
      {
        "title": "Annual Holiday Candy & Nutritional Support",
        "intro": "Created festive care packages and donation boxes distributed through community shelters and underserved youth programs."
      }
    ],
    "gallerySubtitle": "Volunteer meal packaging drives, community food collections, and youth service leadership.",
    "gallery": [
      {
        "src": "assets/ref_images/projects_hunger-donation_framed.jpg",
        "alt": "Mercer County Hunger Relief & Meal Packaging Drives",
        "caption": "Mercer County Hunger Relief & Meal Packaging Drives"
      },
      {
        "src": "assets/community/Copy of cd - boxes - pic5.jpg",
        "alt": "Mercer County Hunger Relief & Meal Packaging Drives",
        "caption": "Mercer County Hunger Relief & Meal Packaging Drives"
      },
      {
        "src": "assets/community/Copy of cd - ah- group pic1.jpg",
        "alt": "Mercer County Hunger Relief & Meal Packaging Drives",
        "caption": "Mercer County Hunger Relief & Meal Packaging Drives"
      },
      {
        "src": "assets/community/Candy donation boxes at AoPs - pic2.jpg",
        "alt": "Mercer County Hunger Relief & Meal Packaging Drives",
        "caption": "Mercer County Hunger Relief & Meal Packaging Drives"
      },
      {
        "src": "assets/certificates/STEP Meals Packaging.jpeg",
        "alt": "Mercer County Hunger Relief & Meal Packaging Drives",
        "caption": "Mercer County Hunger Relief & Meal Packaging Drives"
      }
    ]
  },
  {
    "title": "Senior Living Center Technology & Musical Companionship",
    "group": "School & Community",
    "category": "School & Community",
    "summary": "Weekly volunteer sessions at Artis Senior Living, conducting smartphone/tablet digital literacy workshops, classical music therapy recitals, and intergenerational storytelling.",
    "cardImage": "assets/ref_images/projects_senior-center_framed.jpg",
    "heroImage": "assets/ref_images/projects_senior-center_framed.jpg",
    "badges": [
      {
        "label": "Elder Care",
        "tone": "plum"
      },
      {
        "label": "Music Therapy",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "Conducted one-on-one digital literacy sessions helping seniors connect with family",
      "Performed solo classical flute and piano pieces tailored for cognitive memory therapy",
      "Created handmade holiday cards and seasonal art gifts for memory-care residents",
      "Recognized by Artis Senior Living staff for compassionate intergenerational service"
    ],
    "attachments": [],
    "videos": [],
    "sections": [
      {
        "title": "Digital Literacy & Family Connectivity",
        "intro": "Patiently guided elderly residents through smartphone navigation, FaceTime video calls, accessibility settings, and voice-to-text messaging."
      },
      {
        "title": "Cognitive Music Therapy Recitals",
        "intro": "Performed melodic classical flute and piano repertoire designed to stimulate memory recall, alleviate anxiety, and bring joy to memory-care elders."
      }
    ],
    "gallerySubtitle": "Senior digital workshops, memory-care flute recitals, and intergenerational community care.",
    "gallery": [
      {
        "src": "assets/ref_images/projects_senior-center_framed.jpg",
        "alt": "Senior Living Center Technology & Musical Companionship",
        "caption": "Senior Living Center Technology & Musical Companionship"
      },
      {
        "src": "assets/community/Copy of cd - boxes - pic5.jpg",
        "alt": "Senior Living Center Technology & Musical Companionship",
        "caption": "Senior Living Center Technology & Musical Companionship"
      },
      {
        "src": "assets/community/Copy of cd - aops - pic 4.jpg",
        "alt": "Senior Living Center Technology & Musical Companionship",
        "caption": "Senior Living Center Technology & Musical Companionship"
      },
      {
        "src": "assets/monivitals/20260829_100521.jpg",
        "alt": "Senior Living Center Technology & Musical Companionship",
        "caption": "Senior Living Center Technology & Musical Companionship"
      }
    ]
  },
  {
    "title": "New Jersey Legislative Commendation & Civic Supply Drives",
    "group": "School & Community",
    "category": "School & Community",
    "summary": "Organized regional winter clothing and essential supply drives for unhoused families, receiving official commendation from the New Jersey State Assembly and State Senate.",
    "cardImage": "assets/community/Sock Drive - NJ Assembly Woman House.png",
    "heroImage": "assets/community/Sock Drive - NJ Assembly Woman House.png",
    "badges": [
      {
        "label": "NJ Legislature",
        "tone": "plum"
      },
      {
        "label": "Civic Impact",
        "tone": "berry"
      }
    ],
    "technicalFocus": [
      "Collected and distributed over 1,200 pairs of thermal socks and winter essentials",
      "Coordinated drop-off hubs at local schools, libraries, and community centers",
      "Formal legislative resolution presented by NJ State Assemblywoman",
      "Demonstrated sustainable youth civic engagement model"
    ],
    "attachments": [],
    "videos": [],
    "sections": [
      {
        "title": "Regional Winter Drive Logistics",
        "intro": "Established secure donation collection bins across Mercer County schools and public libraries, coordinating weekly sorting, sanitization, and packaging."
      },
      {
        "title": "Bipartisan Legislative Commendation",
        "intro": "Formally commended on the floor of the New Jersey State Legislature for dedicated grassroots leadership in service of vulnerable families."
      }
    ],
    "gallerySubtitle": "Legislative resolution presentation, thermal supply sorting, and statehouse recognition.",
    "gallery": [
      {
        "src": "assets/community/Sock Drive - NJ Assembly Woman House.png",
        "alt": "New Jersey Legislative Commendation & Civic Supply Drives",
        "caption": "New Jersey Legislative Commendation & Civic Supply Drives"
      },
      {
        "src": "assets/ref_images/projects_hunger-donation_framed.jpg",
        "alt": "New Jersey Legislative Commendation & Civic Supply Drives",
        "caption": "New Jersey Legislative Commendation & Civic Supply Drives"
      },
      {
        "src": "assets/certificates/Service Award - NJ State Assembly.jpeg",
        "alt": "New Jersey Legislative Commendation & Civic Supply Drives",
        "caption": "New Jersey Legislative Commendation & Civic Supply Drives"
      },
      {
        "src": "assets/community/Copy of cd - flyer.jpg",
        "alt": "New Jersey Legislative Commendation & Civic Supply Drives",
        "caption": "New Jersey Legislative Commendation & Civic Supply Drives"
      },
      {
        "src": "assets/community/Copy of cd - ah- group pic1.jpg",
        "alt": "New Jersey Legislative Commendation & Civic Supply Drives",
        "caption": "New Jersey Legislative Commendation & Civic Supply Drives"
      }
    ]
  },
  {
    "title": "Biomedical & AI Scientific Research",
    "group": "Projects",
    "category": "Biomedical & AI",
    "summary": "Stanford AIMI clinical AI research, computational drug discovery with AutoDock Vina, Harvard-mentored molecular biology wet lab, and Cambridge cancer genomics research.",
    "cardImage": "assets/certificates/BioResearch Academy Certificate.jpeg",
    "heroImage": "assets/certificates/BioResearch Academy Certificate.jpeg",
    "badges": [
      {
        "label": "Stanford AIMI",
        "tone": "plum"
      },
      {
        "label": "Harvard Fellow",
        "tone": "berry"
      },
      {
        "label": "AutoDock Vina",
        "tone": "moss"
      }
    ],
    "technicalFocus": [
      "Machine Learning & AI: Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), Random Forest, XGBoost, Predictive Modeling, Data Cleansing, Imbalance Resolution.",
      "Programming & Software: Python, MATLAB, Google Colab, Bash Scripting.",
      "Bioinformatics Tools: AutoDock Vina (Molecular Docking), Computational Structural Biology, Protein Modeling, Graph Theory Networks.",
      "Wet Lab Techniques: Sterile cell culture, CRISPR-Cas9 protocols, gel electrophoresis, PCR preparation, chemical safety."
    ],
    "attachments": [
      {
        "label": "All Pictures & Videos (Google Drive Folder)",
        "href": "https://drive.google.com/drive/folders/1CvGPX-xZhf5QsRUANlcrS7EhEGcuwtv_?usp=drive_link"
      }
    ],
    "videos": [],
    "sections": [
      {
        "title": "Stanford AIMI Academic year Internship (Center for Artificial Intelligence in Medicine & Imaging)",
        "intro": "Stanford University School of Medicine, Center for Artificial Intelligence in Medicine & Imaging (AIMI), Stanford, CA (Remote) &mdash; Academic Year Research Intern | September 2026 \u2013 June 2027.<br><br>\u2022 Selected for a highly competitive 30-week clinical AI research internship (acceptance rate under 5%).<br>\u2022 Developing and evaluating computer vision models for an AI-driven assistive interface for people with visual impairments, utilizing medical imaging.<br>\u2022 Scheduled to present research at a Stanford Health event in summer 2027."
      },
      {
        "title": "Computational Oncology Research, Mentored Independent Research",
        "intro": "Research Co-Author | June 2026 \u2013 Present.<br><br>\u2022 Conducting computational drug discovery research focusing on cervical cancer treatments utilizing a target plant molecule.<br>\u2022 Performed structural bioinformatics modeling and high-throughput molecular docking simulations with AutoDock Vina.<br>\u2022 Publication Status: Co-authoring manuscript currently in preparation for submission to a professional peer-reviewed journal."
      },
      {
        "title": "Biomedical Research Fellow \u2014 Advanced BioResearch Academy, Boston. MA",
        "intro": "Research Trainee | Fall 2025 \u2013 Summer 2026 | Mentor: Professor Sam Kunes, Harvard University.<br><br>\u2022 Completed an intensive 24-week bioresearch program covering cancer cell biology (DNA replication errors, tumor cell identity, cell division regulation), brain organoids, CRISPR genome editing, spatial transcriptomics, advanced microscopy, and synthetic biology in therapy.<br>\u2022 Delivered independent research project presentations at the end of each 12-week session.<br>\u2022 Conducted 3 weeks of hands-on physical wet lab work in Boston under a Harvard University professor, practicing CRISPR, gel electrophoresis, and PCR protocols for Alzheimer's disease research."
      },
      {
        "title": "Research Scholar Program - Independent Cancer Research (12-wks)",
        "intro": "July \u2013 August 2025 | Mentor: Kristina Kordova, PhD, Biological Sciences, University of Cambridge.<br><br>\u2022 Conducted independent research on tumor heterogeneity in cancer biology, with a focus on single-cell RNA sequencing (scRNA-seq) data analysis.<br>\u2022 Performed a literature review to identify current challenges and emerging methods in cancer subtyping.<br>\u2022 Applied data preprocessing, normalization, dimensionality reduction, and clustering using Python to develop a model for breast cancer subtype classification, identified 32 distinct clusters with biomarkers.<br>\u2022 Authored a 6-page research paper detailing methodology, analysis, and biological implications."
      }
    ],
    "gallerySubtitle": "Stanford AIMI fellowship, Harvard bioresearch laboratory sessions, molecular biology certifications, and research presentations.",
    "gallery": [
      {
        "src": "assets/certificates/BioResearch Academy Certificate.jpeg",
        "alt": "Biomedical & AI Scientific Research",
        "caption": "Biomedical & AI Scientific Research"
      },
      {
        "src": "assets/certificates/InspiritAI_AI_Scholars_Certificate.jpg",
        "alt": "Biomedical & AI Scientific Research",
        "caption": "Biomedical & AI Scientific Research"
      },
      {
        "src": "assets/certificates/InspiritAI_AI_Ambassador_Certificate.jpg",
        "alt": "Biomedical & AI Scientific Research",
        "caption": "Biomedical & AI Scientific Research"
      },
      {
        "src": "assets/ref_images/projects_ieee-engineering-conversation.jpg",
        "alt": "Biomedical & AI Scientific Research",
        "caption": "Biomedical & AI Scientific Research"
      },
      {
        "src": "assets/ref_images/projects_lab-setup.jpg",
        "alt": "Biomedical & AI Scientific Research",
        "caption": "Biomedical & AI Scientific Research"
      },
      {
        "src": "assets/science_fairs/ieee_pic4.jpeg",
        "alt": "Biomedical & AI Scientific Research",
        "caption": "Biomedical & AI Scientific Research"
      },
      {
        "src": "assets/science_fairs/pic3.jpeg",
        "alt": "Biomedical & AI Scientific Research",
        "caption": "Biomedical & AI Scientific Research"
      },
      {
        "src": "assets/certificates/Aqua Science Certificate.jpg",
        "alt": "Biomedical & AI Scientific Research",
        "caption": "Biomedical & AI Scientific Research"
      }
    ]
  }
];

  function getProjectIndex(identifier) {
    if (typeof identifier === 'number') return identifier;
    if (!identifier) return 0;
    const lower = identifier.toString().toLowerCase().trim();
    const idx = PROJECTS_DATA.findIndex(p => {
      const titleLower = p.title.toLowerCase();
      return titleLower === lower || titleLower.includes(lower) || lower.includes(titleLower.slice(0, 15));
    });
    return idx >= 0 ? idx : 0;
  }

  function renderModalContent(project) {
    const heroSrc = project.heroImage || project.cardImage || '';

    // Technical focus HTML
    let techFocusHtml = '';
    if (Array.isArray(project.technicalFocus) && project.technicalFocus.length > 0) {
      techFocusHtml = `
        <div class="mt-8 rounded-xl border border-berry/25 bg-[#fff0f6] p-5 sm:p-6 shadow-xs">
          <h3 class="text-sm font-semibold uppercase tracking-widest text-[#ba1f43] font-bold">Technical focus</h3>
          <ul class="mt-4 space-y-3">
            ${project.technicalFocus.map(item => `
              <li class="flex items-start gap-3 text-sm leading-6 text-ink/80">
                <span aria-hidden="true" class="mt-[0.55em] h-1.5 w-1.5 shrink-0 rounded-full bg-[#ba1f43]"></span>
                <span>${item}</span>
              </li>
            `).join('')}
          </ul>
        </div>
      `;
    }

    // Documents HTML
    let docsHtml = '';
    if (Array.isArray(project.attachments) && project.attachments.length > 0) {
      docsHtml = `
        <div class="mt-6 rounded-xl border border-plum/20 bg-[#f8f0fc] p-5 sm:p-6 shadow-xs">
          <h3 class="text-sm font-semibold uppercase tracking-widest text-[#5f3dc4] font-bold">Documents</h3>
          <ul class="mt-3 space-y-2">
            ${project.attachments.map(att => `
              <li>
                <a href="${att.href}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-sm font-semibold text-[#5f3dc4] underline underline-offset-4 hover:text-[#ba1f43] transition">
                  <span aria-hidden="true">📄</span>
                  <span>${att.label}</span>
                  <span aria-hidden="true">↗</span>
                </a>
              </li>
            `).join('')}
          </ul>
        </div>
      `;
    }

    // Sections (Explore the work) HTML - Clean text accordions just like Robotics
    let sectionsHtml = '';
    if (Array.isArray(project.sections) && project.sections.length > 0) {
      sectionsHtml = `
        <div class="mt-10 space-y-4">
          <h3 class="font-display text-2xl font-bold text-plum">Explore the work</h3>
          <div class="space-y-4">
            ${project.sections.map((sec, secIdx) => `
              <details class="group rounded-xl border border-ink/15 bg-white overflow-hidden shadow-xs transition duration-200 open:border-plum/40" ${secIdx === 0 ? 'open' : ''}>
                <summary class="flex min-h-16 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 font-display text-lg font-semibold marker:hidden sm:px-6 [&::-webkit-details-marker]:hidden hover:text-plum transition select-none">
                  <span>${sec.title}</span>
                  <span aria-hidden="true" class="text-2xl leading-none text-[#ba1f43] transition-transform duration-200 group-open:rotate-45 font-light">+</span>
                </summary>
                <div class="border-t border-ink/10 px-5 pb-6 pt-5 sm:px-6 bg-[#FAFBF9]">
                  <p class="max-w-3xl leading-relaxed text-ink/75 text-sm sm:text-base">${sec.intro}</p>
                </div>
              </details>
            `).join('')}
          </div>
        </div>
      `;
    }

    // Photo Gallery HTML - Rendered cleanly below Explore the work with phone photo grid for all cards
    let galleryPhotos = [];
    if (Array.isArray(project.gallery) && project.gallery.length > 0) {
      galleryPhotos = project.gallery;
    } else if (Array.isArray(project.images) && project.images.length > 0) {
      galleryPhotos = project.images.map(img => typeof img === 'string' ? { src: img, alt: project.title, caption: project.title } : img);
    } else if (Array.isArray(project.sections) && project.sections.length > 0) {
      const collected = [];
      project.sections.forEach(sec => {
        if (Array.isArray(sec.photos)) {
          sec.photos.forEach(ph => {
            if (ph && ph.src && !collected.some(c => c.src === ph.src)) {
              collected.push(ph);
            }
          });
        }
      });
      galleryPhotos = collected;
    }

    let galleryHtml = '';
    if (galleryPhotos.length > 0) {
      const subtitle = project.gallerySubtitle || `Documented photographs, research trials, and field milestones for ${project.title}.`;
      galleryHtml = `
        <div class="photo-gallery-section">
          <div class="mb-4 flex items-center justify-between">
            <h3 class="font-display text-2xl font-bold text-plum">Photo Gallery</h3>
            <span class="text-xs font-semibold uppercase tracking-wider text-[#ba1f43]">${galleryPhotos.length} Photos</span>
          </div>
          <p class="mb-6 text-sm text-ink/65 leading-relaxed">${subtitle}</p>
          <div class="phone-photo-grid">
            ${galleryPhotos.map(ph => `
              <a href="${ph.src}" target="_blank" rel="noopener noreferrer" aria-label="${ph.alt || 'View photo'}" class="phone-gallery-thumb">
                <img src="${ph.src}" alt="${ph.alt || project.title + ' photo'}" loading="lazy">
              </a>
            `).join('')}
          </div>
        </div>
      `;
    }

    // Video Recording Section HTML - Rendered at the end, only when real videos exist (zero placeholders)
    let videosHtml = '';
    if (Array.isArray(project.videos) && project.videos.length > 0) {
      const validVideos = project.videos.filter(v => v && v.src && typeof v.src === 'string' && v.src.trim() !== '');
      if (validVideos.length > 0) {
        videosHtml = `
          <div class="video-recording-section mt-10">
            <div class="mb-4 flex items-center justify-between">
              <h3 class="font-display text-2xl font-bold text-plum">Featured Video</h3>
              <span class="text-xs font-semibold uppercase tracking-wider text-[#ba1f43]">${validVideos.length === 1 ? 'Video Recording' : validVideos.length + ' Videos'}</span>
            </div>
            <div class="space-y-6">
              ${validVideos.map(vid => {
                const vidTitle = vid.title || `${project.title} Video Recording`;
                const isYouTube = vid.type === 'youtube' || (!vid.src.endsWith('.mp4') && !vid.src.endsWith('.mov') && !vid.src.endsWith('.webm') && !vid.src.includes('/'));

                if (isYouTube) {
                  const ytId = vid.src.replace(/^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)/, '').split(/[^a-zA-Z0-9_-]/)[0];
                  return `
                    <div class="overflow-hidden rounded-2xl border border-ink/15 bg-black shadow-lg">
                      <div class="relative aspect-video w-full bg-black">
                        <iframe 
                          src="https://www.youtube.com/embed/${ytId}?rel=0" 
                          title="${vidTitle}"
                          class="absolute inset-0 h-full w-full border-0" 
                          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                          allowfullscreen>
                        </iframe>
                      </div>
                      <div class="bg-paper px-5 py-3 border-t border-ink/10 flex items-center justify-between">
                        <span class="text-sm font-semibold text-ink">${vidTitle}</span>
                        <a href="https://www.youtube.com/watch?v=${ytId}" target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-plum hover:text-berry underline underline-offset-2">Watch on YouTube ↗</a>
                      </div>
                    </div>
                  `;
                } else {
                  const videoSrc = vid.src.startsWith('/') ? vid.src.slice(1) : vid.src;
                  return `
                    <div class="overflow-hidden rounded-2xl border border-ink/15 bg-black shadow-lg">
                      <div class="relative aspect-video w-full bg-black">
                        <video 
                          src="${videoSrc}" 
                          controls 
                          playsinline 
                          preload="metadata" 
                          poster="${vid.poster || ''}" 
                          class="h-full w-full object-contain">
                          Your browser does not support the video tag.
                        </video>
                      </div>
                      <div class="bg-paper px-5 py-3 border-t border-ink/10 flex items-center justify-between">
                        <span class="text-sm font-semibold text-ink">${vidTitle}</span>
                        <span class="text-xs font-mono font-medium text-ink/50">MP4 Video</span>
                      </div>
                    </div>
                  `;
                }
              }).join('')}
            </div>
          </div>
        `;
      }
    }

    return `
      <!-- Hero Banner with Title Overlay -->
      <div class="modal-hero-banner">
        ${heroSrc ? `<img src="${heroSrc}" alt="${project.title}" class="modal-hero-image" style="object-position: center !important;">` : ''}
        <div class="modal-hero-overlay px-5 py-5 text-white sm:px-8 sm:py-7 pointer-events-none">
          ${project.category ? `<span class="mb-2 inline-block rounded-full bg-[#ba1f43] px-3 py-1 text-xs font-semibold uppercase tracking-wider text-white shadow-sm">${project.category}</span>` : ''}
          <h2 class="font-display text-xl font-bold tracking-tight text-white leading-tight sm:text-3xl">${project.title}</h2>
        </div>
      </div>

      <!-- Main Modal Body -->
      <div class="mx-auto max-w-5xl px-5 py-8 sm:px-8 sm:py-10 bg-paper">
        <p class="max-w-3xl text-sm leading-relaxed text-ink/80 sm:text-base md:text-lg">${project.summary}</p>
        ${techFocusHtml}
        ${docsHtml}
        ${sectionsHtml}
        ${galleryHtml}
        ${videosHtml}
      </div>
    `;
  }

  function setupModalDOM() {
    let modal = document.getElementById('projectModal');
    if (!modal) {
      modal = document.createElement('dialog');
      modal.id = 'projectModal';
      document.body.appendChild(modal);
    }

    modal.className = 'm-auto max-h-[90dvh] w-[95vw] max-w-6xl overflow-hidden rounded-2xl border border-ink/15 bg-paper p-0 text-ink shadow-2xl backdrop:bg-ink/70';
    modal.setAttribute('aria-label', 'Project details');

    modal.innerHTML = `
      <div class="relative">
        <!-- Pinned Close Button (Exact Vercel Spec) -->
        <button type="button" id="modalCloseBtn" aria-label="Close project" class="absolute right-4 top-4 z-50 flex h-10 w-10 items-center justify-center rounded-full border border-white/40 bg-[#ba1f43] text-2xl font-bold leading-none text-white shadow-lg transition hover:bg-[#9e1736] cursor-pointer">
          <span aria-hidden="true">&times;</span>
        </button>

        <!-- Scrollable Modal Viewport -->
        <div id="modalScrollArea" class="max-h-[90dvh] overflow-y-auto">
          <div id="modalDynamicRoot"></div>
        </div>
      </div>
    `;

    const closeBtn = document.getElementById('modalCloseBtn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => modal.close());
    }

    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.close();
    });

    return modal;
  }

  window.openProjectModal = function(identifier) {
    const modal = setupModalDOM();
    let project = null;

    if (typeof identifier === 'object' && identifier !== null) {
      const title = (identifier.title || '').trim();
      const matchedIdx = PROJECTS_DATA.findIndex(p => {
        const t1 = p.title.toLowerCase();
        const t2 = title.toLowerCase();
        return t1 === t2 || t1.includes(t2) || t2.includes(t1.slice(0, 15));
      });

      if (matchedIdx >= 0) {
        project = JSON.parse(JSON.stringify(PROJECTS_DATA[matchedIdx]));
        if (Array.isArray(identifier.images) && identifier.images.length > 0) {
          const existingSrcs = new Set((project.gallery || []).map(g => g.src));
          identifier.images.forEach(img => {
            const src = typeof img === 'string' ? img : img.src;
            if (src && !existingSrcs.has(src)) {
              project.gallery = project.gallery || [];
              project.gallery.push({ src: src, alt: project.title, caption: project.title });
              existingSrcs.add(src);
            }
          });
        }
        if (Array.isArray(identifier.videos) && identifier.videos.length > 0) {
          project.videos = identifier.videos;
        }
      } else {
        const imgs = Array.isArray(identifier.images) ? identifier.images : (identifier.img ? [identifier.img] : []);
        project = {
          title: identifier.title || 'Project Detail',
          category: identifier.category || '',
          summary: identifier.desc || '',
          heroImage: identifier.img || imgs[0] || '',
          technicalFocus: identifier.highlights || [],
          sections: [
            {
              title: "Project Highlights & Methodology",
              intro: identifier.desc || ""
            }
          ],
          gallery: imgs.map(img => typeof img === 'string' ? { src: img, alt: identifier.title, caption: identifier.title } : img),
          gallerySubtitle: "Field captures, research documentation, and presentation materials.",
          videos: Array.isArray(identifier.videos) ? identifier.videos : (identifier.video ? [identifier.video] : [])
        };
      }
    } else {
      const idx = getProjectIndex(identifier);
      project = PROJECTS_DATA[idx];
    }

    if (!project) return;

    const root = document.getElementById('modalDynamicRoot');
    if (root) {
      root.innerHTML = renderModalContent(project);
    }

    const scrollArea = document.getElementById('modalScrollArea');
    if (scrollArea) {
      scrollArea.scrollTop = 0;
    }

    modal.showModal();
  };

  document.addEventListener('DOMContentLoaded', () => {
    setupModalDOM();
    setupCardImageSwitchers();
    document.querySelectorAll('.portfolio-cards-grid').forEach((grid) => {
      const cardObserver = new MutationObserver(() => setupCardImageSwitchers());
      cardObserver.observe(grid, { childList: true });
    });

    // Bind click handlers: entering card is done via content below image or "Read more" button
    const cards = document.querySelectorAll('.portfolio-card');
    cards.forEach((card, i) => {
      const contentBox = card.querySelector('.p-5') || card.children[1];
      if (contentBox) {
        contentBox.style.cursor = 'pointer';
        contentBox.addEventListener('click', (e) => {
          if (e.target.closest('a') && !e.target.closest('.card-read-more')) return;
          const title = card.querySelector('h3')?.textContent?.trim() || '';
          const dataProject = card.getAttribute('data-project');
          let projectObj = null;
          if (dataProject) {
            try { projectObj = JSON.parse(dataProject); } catch(err) {}
          }
          window.openProjectModal(projectObj || title || i);
        });
      }

      // Card-level fallback (ignores image area)
      card.addEventListener('click', (e) => {
        if (e.target.closest('.aspect-video') || e.target.closest('.card-media-box')) return;
        if (e.target.closest('a') && !e.target.closest('.card-read-more')) return;
        
        const title = card.querySelector('h3')?.textContent?.trim() || '';
        const dataProject = card.getAttribute('data-project');
        let projectObj = null;
        if (dataProject) {
          try {
            projectObj = JSON.parse(dataProject);
          } catch(err) {}
        }
        window.openProjectModal(projectObj || title || i);
      });
    });

  function setupCardImageSwitchers() {
    const cards = document.querySelectorAll('.portfolio-card');
    cards.forEach((card) => {
      const mediaBox = card.querySelector('.aspect-video');
      if (!mediaBox || mediaBox.dataset.hasSwitcher) return;
      mediaBox.dataset.hasSwitcher = 'true';
      mediaBox.classList.add('card-media-box');

      const imgEl = mediaBox.querySelector('img');
      if (!imgEl) return;
      imgEl.classList.add('card-image-foreground');

      let images = [];
      const dataProjectStr = card.getAttribute('data-project');
      if (dataProjectStr) {
        try {
          const pObj = JSON.parse(dataProjectStr);
          if (Array.isArray(pObj.images) && pObj.images.length > 0) {
            images = pObj.images;
          } else if (pObj.img) {
            images = [pObj.img];
          }
        } catch(e) {}
      }

      if (images.length === 0 && card.getAttribute('data-is-robotics')) {
        images = [
          "assets/robotics/pic 2 - Team award.JPG",
          "assets/robotics/fll_team_wpi.jpg",
          "assets/robotics/pic 1 - 2024.jpg",
          "assets/robotics/ftc_match_focus.jpg"
        ];
      }

      if (images.length > 1) {
        let curIdx = 0;

        const changeImage = (newIdx) => {
          curIdx = (newIdx + images.length) % images.length;
          imgEl.style.transition = 'opacity 0.15s ease';
          imgEl.style.opacity = '0.35';
          setTimeout(() => {
            imgEl.src = images[curIdx];
            imgEl.style.opacity = '1';
          }, 150);
        };

        mediaBox.addEventListener('click', (e) => {
          if (e.target.closest('a')) return;
          e.stopPropagation();
          e.preventDefault();
          changeImage(curIdx + 1);
        });
      } else {
        // Prevent opening modal when clicking single image
        mediaBox.addEventListener('click', (e) => {
          e.stopPropagation();
        });
      }
    });
  }

    // National Memberships Carousel Auto-advance (index.html)
    const membershipCarousel = document.querySelector('[aria-label="National memberships carousel"]');
    if (membershipCarousel) {
      const track = membershipCarousel.querySelector('.flex.transition-transform');
      const dots = membershipCarousel.querySelectorAll('.mt-4.flex span');
      const itemsCount = 4; // NCWIT, NJWEA, STEP, AWD
      let curIdx = 0;
      let isHovered = false;

      membershipCarousel.addEventListener('mouseenter', () => isHovered = true);
      membershipCarousel.addEventListener('mouseleave', () => isHovered = false);

      setInterval(() => {
        if (isHovered) return;
        curIdx = (curIdx + 1) % itemsCount;
        if (track) {
          track.style.transform = `translateX(calc(var(--card-step) * -${curIdx}))`;
        }
        if (dots && dots.length > 0) {
          dots.forEach((dot, idx) => {
            if (idx === curIdx) {
              dot.className = 'h-1.5 rounded-full transition-all w-5 bg-plum';
            } else {
              dot.className = 'h-1.5 rounded-full transition-all w-1.5 bg-ink/20';
            }
          });
        }
      }, 3000);
    }

    // CMS Synchronization: Expose global updater & load cached updates
    window.updateProjectsDataFromCMS = function(cmsPortfolio) {
      if (!Array.isArray(cmsPortfolio) || !cmsPortfolio.length) return;
      cmsPortfolio.forEach(item => {
        const idx = PROJECTS_DATA.findIndex(p => p.title.toLowerCase() === (item.title || '').toLowerCase());
        if (idx >= 0) {
          PROJECTS_DATA[idx].title = item.title;
          if (item.desc) PROJECTS_DATA[idx].summary = item.desc;
          if (item.img) {
            PROJECTS_DATA[idx].cardImage = item.img;
            PROJECTS_DATA[idx].heroImage = item.img;
          }
          if (Array.isArray(item.images) && item.images.length > 0) {
            PROJECTS_DATA[idx].gallery = item.images.map(img => typeof img === 'string' ? { src: img, alt: item.title, caption: item.title } : img);
          }
          if (Array.isArray(item.highlights)) {
            PROJECTS_DATA[idx].technicalFocus = item.highlights;
          }
          if (Array.isArray(item.videos)) {
            PROJECTS_DATA[idx].videos = item.videos;
          }
        } else {
          PROJECTS_DATA.push({
            title: item.title,
            category: item.category_name || '',
            summary: item.desc || '',
            cardImage: item.img || '',
            heroImage: item.img || '',
            technicalFocus: item.highlights || [],
            sections: [{ title: "Project Overview", intro: item.desc || "" }],
            gallery: (item.images || []).map(img => typeof img === 'string' ? { src: img, alt: item.title, caption: item.title } : img),
            videos: Array.isArray(item.videos) ? item.videos : []
          });
        }
      });
    };

    try {
      const stored = localStorage.getItem('aadya_cms_content');
      if (stored) {
        const parsed = JSON.parse(stored);
        if (parsed && Array.isArray(parsed.portfolio)) {
          window.updateProjectsDataFromCMS(parsed.portfolio);
        }
      }
    } catch(e) {}
  });
})();

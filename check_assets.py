import os

paths_to_check = [
    "assets/robotics/pic 1 - with robot.jpg",
    "assets/robotics/pic12 -WPI Team.png",
    "assets/community/Copy of cd - ah- group pic1.jpg",
    "assets/speaking/speech_stage.jpg",
    "assets/athletics/tennis_action.jpg",
    "assets/writing_arts/flute_performance.png",
    "assets/community/Candy donation boxes at AoPs - pic2.jpg",
    "assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg",
    "assets/robotics/pic 10 - wpi award.jpg",
    "assets/certificates/Day of AI Certificate - MIT RAISE.jpeg",
    "assets/certificates/Service Award - NJ State Assembly.jpeg",
    "assets/certificates/Award Certificate - NSF PS1 contest .jpg",
    "assets/certificates/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg",
    "assets/community/STEP Meals Packaging.jpeg"
]

for p in paths_to_check:
    print(f"{p}: {'EXISTS' if os.path.exists(p) else 'MISSING'}")

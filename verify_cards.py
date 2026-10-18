import os

cards = [
    ("assets/robotics/pic 10 - wpi award.jpg", "WPI US Open World #14 Trophy"),
    ("assets/certificates/Day of AI Certificate - MIT RAISE.jpeg", "MIT Solve Top 5 National Winner"),
    ("assets/certificates/Receiving THE JOHN H IMBRIE HUMANITIES AWARD.jpg", "John H. Imbrie Humanities Award"),
    ("assets/certificates/Service Award - NJ State Assembly.jpeg", "NJ Legislative Resolution"),
    ("assets/certificates/STEP Meals Packaging.jpeg", "150,624 Meals Packaged"),
    ("assets/certificates/Award Certificate - NSF PS1 contest .jpg", "1st Place National Speech Champion"),
    ("assets/certificates/Grand Prize Recital - Music-Fest International Rising Talent Festival_.jpg", "Music-Fest Grand Prize Winner"),
    ("assets/robotics/pic 1 - with robot.jpg", "FTC BioBuzz Autonomous Robot")
]

for path, title in cards:
    exists = os.path.exists(path)
    size = os.path.getsize(path) if exists else 0
    print(f"{path}: {exists} ({size} bytes)")

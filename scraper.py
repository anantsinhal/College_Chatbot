import requests
from bs4 import BeautifulSoup

urls = {

    # Admissions
    "admissions_overview": "https://www.smu.edu.in/admissions-majitar-campus.php",
    "eligibility": "https://www.smu.edu.in/smit/eligibility-criteria.php",
    "fee_structure": "https://www.smu.edu.in/smit/fee-structure.php",
    "scholarship": "https://www.smu.edu.in/smit/scholarship.php",
    "contact": "https://www.smu.edu.in/contact-us.php",

    # Departments
    "cse_department": "https://www.smu.edu.in/smit/dept-of-computer-science-engineering-smit-sikkim-manipal.php",
    "it_department": "https://www.smu.edu.in/smit/dept-of-information-technology.php",
    "civil_department": "https://www.smu.edu.in/smit/dept-of-civil-engineering.php",
    "ece_department": "https://www.smu.edu.in/smit/dept-of-Electronics-communication-engineering.php",
    "mechanical_department": "https://www.smu.edu.in/smit/dept-of-mechanical-engineering.php",
    "ai_ds_department": "https://www.smu.edu.in/smit/dept-of-Artificial-intelligence-and-Data-science.php",

    # Placements
    "placements": "https://www.smu.edu.in/smit/placement.php",
    "practice_school": "https://www.smu.edu.in/smit/practice-school.php",

    # Student Life
    "student_clubs": "https://www.smu.edu.in/smit/student-clubs.php",
    "library": "https://www.smu.edu.in/smit/library.php",
    "hostel": "https://www.smu.edu.in/smit/hostel-smit-smu.php",
    "student_support": "https://www.smu.edu.in/smit/student-support.php",

    # Events & News
    "events": "https://www.smu.edu.in/smit/events.php",
    "news": "https://www.smu.edu.in/smit/news.php",
    "notice_board": "https://www.smu.edu.in/smit/notice-board.php",

    # About SMIT
    "history": "https://www.smu.edu.in/smit/history.php",
    "vision_mission": "https://www.smu.edu.in/smit/vision-mission.php",
    "leadership": "https://www.smu.edu.in/smit/leadership.php",
    "rankings": "https://www.smu.edu.in/smit/rankings.php",
    "achievements": "https://www.smu.edu.in/smit/achievements.php",

    # Faculty
    "faculty": "https://www.smu.edu.in/smit/faculty.php"
}

for name, url in urls.items():

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")

            text = soup.get_text(separator=" ", strip=True)

            with open(f"data/{name}.txt", "w", encoding="utf-8") as f:
                f.write(text)

            print(f"Saved: {name}.txt")

        else:
            print(f"Failed: {name} ({response.status_code})")

    except Exception as e:
        print(f"Error with {name}: {e}")
# scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from course import Course 

PROG_PAGE_URL = "https://programs-courses.uq.edu.au/requirements/program/2350/2023"
SOFT_ENG_PAGE_URL = "https://programs-courses.uq.edu.au/requirements/plan/SOFTEX2350/2023"

PROG_PAGE_MAP = {"Core": "part-A", 
                "Prep": "part-C",
                "FYElec": "part-D"} 

SOFT_ENG_PAGE_MAP = {"FOS Compulsory": "part-A", 
                     "FOS Elective": "part-B",
                     "FOS Masters": "part-C",
                     "FOS Breadth": "part-D",
                     "FOS Breadth": "part-D"} 
COURSE_BASE_URL = "https://programs-courses.uq.edu.au/course.html?course_code="

def start_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(2)

    return driver


def parse_section(section, category, courses):
    subjects = section.find_elements(By.CLASS_NAME, "curriculum-reference")
    
    for subject in subjects:
        courses.append(Course(subject.get_attribute("href").split('=')[1],
                              subject.get_attribute("title"), 2, category))


def scrape_course_list(driver, url, pageMap, courses):
    driver.get(url)

    for key in pageMap:
        section = driver.find_element(By.ID, pageMap[key])
        parse_section(section, key, courses)
    

def scrape_course_details(driver, courses):
    for course in courses:
        driver.get(COURSE_BASE_URL + course.get_code())
        level = driver.find_element(By.ID, "course-level").text
        faculty = driver.find_element(By.ID, "course-faculty").text
        school = driver.find_element(By.ID, "course-school").text
        prereqList = driver.find_elements(By.ID, "course-prerequisite")
        prereq = None if prereqList == [] else prereqList[0].text
        course.set_details(level, faculty, school, prereq)
        
def get_courses():
    driver = start_driver()
    
    courses = []
    
    scrape_course_list(driver, PROG_PAGE_URL, PROG_PAGE_MAP, courses)
    scrape_course_list(driver, SOFT_ENG_PAGE_URL, SOFT_ENG_PAGE_MAP, courses)
    scrape_course_details(driver, courses)

    driver.close()
    return courses

if __name__ == "__main__":
    courses = get_courses()
    for course in courses:
        course.print_full()
        print("=======================================================")
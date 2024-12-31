# scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



def start_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    driver.get("https://programs-courses.uq.edu.au/requirements/program/2350/2023")

    return driver

if __name__ == "__main__":
    driver = start_driver()

    section = driver.find_element(By.ID, "part-A")
    subjects= section.find_elements(By.CLASS_NAME, "curriculum-reference")

    for subject in subjects:
        print(subject.get_attribute("href"))
        print(subject.get_attribute("title"))
        
    driver.close()

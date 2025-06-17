import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environmental variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
COMPANY_ID = os.getenv("COMPANY_ID")
USER = os.getenv("USER")
KEY = os.getenv("KEY")

# Load Firefox driver and get web data for login page
driver = webdriver.Firefox()
driver.get(BASE_URL)

# Find login text inputs and add text
elem = WebDriverWait(driver, 100).until(
    EC.visibility_of(driver.find_element(By.ID, 'txtDashId')))
elem.send_keys(COMPANY_ID)
elem = driver.find_element(By.ID, 'txtUserName')
elem.send_keys(USER)
elem = driver.find_element(By.ID, 'txtPassword')
elem.send_keys(KEY)

# Click login
elem = driver.find_element(By.ID, "btnLogIn")
elem.click()

# Search for job by job number
elem = WebDriverWait(elem, 100).until(
    EC.visibility_of(driver.find_element(By.NAME, "ctl00_RadSearchBox1")))

elem.send_keys("145-7666-CON")

# wait for results to populate
search_form = driver.find_element(By.ID, "aspnetForm")
result_box = WebDriverWait(search_form, 100).until(
    EC.visibility_of(search_form.find_element(By.CLASS_NAME, "rsbSlide")))

search_results = result_box.find_elements(By.TAG_NAME, "li")

url_anchor = search_results[1].find_element(By.TAG_NAME, "a")
driver.get(url_anchor.get_attribute("href"))

# click on job
# job_url = search_results[1].find_element(
#     By.PARTIAL_LINK_TEXT, "https://frsteam-ngs.net/Enterprise/Module/Job/jJobSlideBoard.aspx?")
# print(job_url)

# Find all info

# Print info


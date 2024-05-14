# Automated LinkedIn job application program

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

MY_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")
PHONE_NUMBER = os.environ.get("PHONE_NUM")

# Starting webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3915033791&f_LF=f_AL&f_WT"
               "=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true")

# Sign In to LinkedIn
time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, value='/html/body/div[4]/a[1]')
sign_in_button.click()

email_bar = driver.find_element(By.XPATH, value='//*[@id="username"]')
email_bar.send_keys(MY_EMAIL)

password_bar = driver.find_element(By.XPATH, value='//*[@id="password"]')
password_bar.send_keys(LINKEDIN_PASSWORD)

sign_in_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()


# Apply for a job
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(PHONE_NUMBER)

# Submit the application
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()

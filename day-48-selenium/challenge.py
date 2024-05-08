from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

# Filling up first name
first_name_input = driver.find_element(By.NAME, value="fName")
first_name_input.send_keys("John")

# Filling up last name
last_name_input = driver.find_element(By.NAME, value="lName")
last_name_input.send_keys("Don")

# Filling up e-mail
e_mail_input = driver.find_element(By.NAME, value="email")
e_mail_input.send_keys("john.don@gmail.com")

# Click to Sign Up button
sign_up_button = driver.find_element(By.CLASS_NAME, value="btn")
sign_up_button.click()

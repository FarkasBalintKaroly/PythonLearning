from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# Amazon price
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# Python.org
driver.get("https://www.python.org/")

# Amazon price
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# price = f"{price_dollar}.{price_cents}"
# print(price)

# Python.org
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a").text
# print(documentation_link)
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Challenge for python.org
# Searching for dates
dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li time")

# Searching for event names
names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu a")

events = {}

for n in range(len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": names[n].text,
    }
print(events)

# Close the active tab
# driver.close()

# Quit will quit the program
driver.quit()

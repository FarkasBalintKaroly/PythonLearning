from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

article_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_number.text)

# Click on anchor tag
# article_number.click()

# Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Using search bar
search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python", Keys.ENTER)

# driver.quit()

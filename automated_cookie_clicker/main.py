# Automated cookie clicker program

from selenium import webdriver
from selenium.webdriver.common.by import By


def check_money():
    """Checking, how much money do we have - return an int."""
    money = driver.find_element(By.ID, value="money")
    cookies = int(money.text)
    return cookies


# Starting webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# Clicking on the cookie
cookie = driver.find_element(by=By.ID, value="cookie")
for i in range(0, 100):
    cookie.click()

# Checking how much cookie the bot got
print(check_money())

# Checking, which upgrade can we buy


# Quit the driver
driver.quit()

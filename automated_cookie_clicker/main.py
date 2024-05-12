# Automated cookie clicker game bot

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


BUY_MINUTE = 0.5
GAME_MINUTE = 3


def check_money():
    """Checking, how much money do we have - return an int."""
    money = driver.find_element(By.ID, value="money")
    cookies = int(money.text.replace(",", ""))
    return cookies


def buy():
    """Checking, what the bot can buy, and buy the upgrade."""

    money = check_money()

    prices_str = []
    elements_to_buy = ['//*[@id="buyCursor"]', '//*[@id="buyGrandma"]', '//*[@id="buyFactory"]',
                       '//*[@id="buyMine"]', '//*[@id="buyShipment"]', '//*[@id="buyAlchemy lab"]',
                       '//*[@id="buyPortal"]', '//*[@id="buyTime machine"]']

    # Get price for all elements
    for element in elements_to_buy:
        price_element = driver.find_element(By.XPATH, value=f"{element}/b")
        try:
            price = price_element.text.split(" ")[3]
        except IndexError:
            price = price_element.text.split(" ")[2]
        prices_str.append(price)
    prices = [int(price.replace(",", "")) for price in prices_str]

    # Decide what to buy
    buying_price = 0
    for price in reversed(prices):
        if price <= money:
            buying_price = price
            break

    # Buying upgrade
    index_to_buy = prices.index(buying_price)
    buy_button = driver.find_element(By.XPATH, value=elements_to_buy[index_to_buy])
    buy_button.click()


# Starting webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# timer starts
game_timeout = time.time() + 60 * GAME_MINUTE  # 5 minutes from now
buying_timeout = time.time() + 60 * BUY_MINUTE

cookie = driver.find_element(by=By.ID, value="cookie")
# Running for 5 minutes
while True:
    if time.time() > game_timeout:
        break
    # Click to cookie
    if time.time() > buying_timeout:
        # Check which item to buy
        buy()
        buying_timeout = buying_timeout + 60 * BUY_MINUTE
    cookie.click()

# Quit the driver
# driver.quit()

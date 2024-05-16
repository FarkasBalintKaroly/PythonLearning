from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

WEBSITE_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = ("https://docs.google.com/forms/d/e/1FAIpQLSdXtthiN-fCUdJ2uJ6b775hM5r7AQMPVGorBEF9CzBexK6Lgg/"
            "viewform?usp=sf_link")
ADDRESS_BAR = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
PRICE_BAR = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
LINK_BAR = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
SUBMIT_BUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
ANOTHER_ANSWER = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'


# TODO 1: BeautifulSoup to scrape listings from website
response = requests.get(url=WEBSITE_URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

# TODO 2: Create a list of links for all the listings
# Saving links to links list
listing_links = soup.find_all(name="a", class_="property-card-link")
links = []
for link in listing_links:
    link_href = link.get("href")
    links.append(link_href)

# TODO 3: Create a list of prices for all the listings + clean up
# Saving prices to prices list
listing_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = []
for price in listing_prices:
    price_text = price.text
    formatted_price = price_text.split("+")[0].split("/")[0]
    prices.append(formatted_price)

# TODO 4: Create a list of addresses for all the listings + clean up
# Saving addresses to addresses list
listing_addresses = soup.find_all(name="address")
addresses = []
for address in listing_addresses:
    address_text = address.text
    formatted_address = address_text.strip().replace("|", "")
    addresses.append(formatted_address)


# Starting Selenium webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(FORM_URL)
time.sleep(4)

# TODO 5: Fill in the form
for i in range(0, len(links)):

    # Filling in address
    address_bar = driver.find_element(by=By.XPATH, value=ADDRESS_BAR)
    address_bar.send_keys(addresses[i])

    # Filling in price
    price_bar = driver.find_element(by=By.XPATH, value=PRICE_BAR)
    price_bar.send_keys(prices[i])

    # Filling in link
    link_bar = driver.find_element(by=By.XPATH, value=LINK_BAR)
    link_bar.send_keys(links[i])

    # Hit submit button
    submit_button = driver.find_element(by=By.XPATH, value=SUBMIT_BUTTON)
    submit_button.click()

    # Hit another answer button
    another_answer = driver.find_element(by=By.XPATH, value=ANOTHER_ANSWER)
    another_answer.click()

driver.quit()
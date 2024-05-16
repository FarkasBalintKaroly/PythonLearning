from bs4 import BeautifulSoup
import requests

website_url = "https://appbrewery.github.io/Zillow-Clone/"

# TODO 1: BeautifulSoup to scrape listings from website
response = requests.get(url=website_url)
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
# Saving prices to prices list ---- continue here
listing_prices = soup.find_all(name="a", class_="property-card-link")
prices = []
for price in listing_prices:
    price_text = price.get("")
    prices.append(price_text)

# TODO 4: Create a list of addresses for all the listings + clean up


# Use selenium
form_url = ("https://docs.google.com/forms/d/e/1FAIpQLSdXtthiN-fCUdJ2uJ6b775hM5r7AQMPVGorBEF9CzBexK6Lgg/"
            "viewform?usp=sf_link")
# TODO 5: Fill in the form

# TODO 6: Open excel from the form

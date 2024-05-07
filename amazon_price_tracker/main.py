# Amazon price tracker project
# Web scraping the price from amazon
# Send an e-mail to myself, about the price

import requests
from bs4 import BeautifulSoup
import smtplib
import os

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGET_PRICE = 100.00
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_EMAIL_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "hu-HU,hu;q=0.6"
}

# Get the website html
response = requests.get(url=PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

# Get the price of the product
price_whole = soup.find(class_="a-price-whole").getText()
price_fraction = soup.find(class_="a-price-fraction").getText()
price = float(f"{price_whole}{price_fraction}")

product_name = soup.find(class_="a-size-large product-title-word-break").getText()

# Compare to target price and send an e-mail, if below target price
if price <= TARGET_PRICE:
    message = f"Subject: Amazon Price Alert!\n\nProduct: {product_name} is now {price}$\nLink to Buy: {PRODUCT_URL}"
    new_message = message.encode("utf-8", "ignore")

    # Sending e-mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=new_message)

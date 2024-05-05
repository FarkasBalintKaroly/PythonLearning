# Amazon price tracker project
# Web scraping the price from amazon
# Send an e-mail to myself, about the price

import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "hu-HU,hu;q=0.6"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
website_html = response.text
print(website_html)

# Web scraping the date, which the user give in console
# Then creating a spotify playlist of it

import requests
from bs4 import BeautifulSoup

# Get the data from the user - which date to webscraping
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

date_url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=date_url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_name_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_name_spans]
print(song_names)

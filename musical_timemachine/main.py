# Web scraping the date, which the user give in console
# Then creating a spotify playlist of it

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")


# Get the data from the user - which date to webscraping
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
#
# date_url = f"https://www.billboard.com/charts/hot-100/{date}/"
#
# response = requests.get(url=date_url)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
# song_name_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_name_spans]
# print(song_names)

# Auth with spotipy
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME,
    )
)

user_id = sp.current_user()["id"]

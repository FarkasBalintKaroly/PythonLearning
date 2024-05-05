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
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

# Webscraping - save 100 songs name to a list
date_url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=date_url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_name_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_name_spans]


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


# Get the URI for top 100 songs
song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print(f"Song: {song} not in Spotify - Skipped")

# Create playlist to add music
playlist_name = f"Top 100 songs in {date}"
description = f"Python project for webscraping top 100 songs in {date} and creating a Spotify playlist."

playlist_create = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=description)
print(playlist_create)

playlist_id = playlist_create["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

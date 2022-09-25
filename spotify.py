import json
import re
from os import environ

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


def generate_playlist_tracks(date):
    """
    web scrape Billboard site


    return list of song titles/artists as dict
    """

    URL = f"https://www.billboard.com/charts/hot-100/{date}/"
    response = requests.get(URL)
    # raw html content
    billboard_data = response.text
    # specifying html parser
    soup = BeautifulSoup(billboard_data, "html.parser")
    # soup.find_all finds all divs with same class
    songs = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")

    song_titles = [title.getText().strip("\n\t") for title in songs]

    artists = soup.find_all(name="span", class_="u-max-width-330")

    artist_names = [name.getText().strip("\n\t") for name in artists]
    song_and_artist = dict(zip(song_titles, artist_names))

    return song_and_artist


def add_playlist_to_database():
    # takes playlist dict as arg
    # sticks it into playlist table in model.py
    pass


def add_song_and_artist_list_to_database(song_and_artist_dict):
    # come back to this later -- pass in return from func above
    # put it into playlist_contents table in model.py
    pass


def build_spotify_playlist(sp, song_and_artist, date):
    """
    generate playlist from song data using Spotify API

    """

    user_id = sp.current_user()["id"]

    playlist = sp.user_playlist_create(
        user=user_id,
        name=f"{date} Billboard 100",
        public=False,
    )

    return playlist


def add_songs_to_spotify_playlist(sp, playlist, song_and_artist):

    user_id = sp.current_user()["id"]
    song_uris = []
    for (song, artist) in song_and_artist.items():
        try:
            result = sp.search(q=f"track:{song} artist:{artist}", type="track")
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except:
            pass

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

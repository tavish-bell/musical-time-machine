import json
import re
from os import environ

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

from crud import *
from model import *


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

    print(f"song and artist: {song_and_artist}")
    return song_and_artist


def build_spotify_playlist(sp, songs_and_artists, date):
    """
    generate playlist from song data using Spotify API

    """

    user_id = sp.current_user()["id"]

    playlist = sp.user_playlist_create(
        user=user_id,
        # TODO: add msg?
        name=f"{date} Billboard 100",
        public=False,
    )

    return playlist


def add_songs_to_spotify_playlist(
    sp, playlist, song_and_artist, selected_date, dB_user_id, db, message
):

    user_id = sp.current_user()["id"]
    song_uris = []
    db_playlist = make_playlist(selected_date, dB_user_id, message=message)
    for (song, artist) in song_and_artist.items():
        try:
            result = sp.search(q=f"track:{song} artist:{artist}", type="track")
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)

            new_track = make_track(song=song, artist=artist)
            db_playlist.tracks.append(new_track)

        except:
            pass

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    db.session.add(db_playlist)
    db.session.commit()

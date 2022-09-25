"""Server for musical time machine """
from os import environ

import crud
import spotipy
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from jinja2 import StrictUndefined
from model import connect_to_db, db
from spotify import (
    add_songs_to_spotify_playlist,
    build_spotify_playlist,
    generate_playlist_tracks,
)
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/users", methods=["POST"])
def create_user():
    """Create a new user account"""

    email = request.form.get("email")
    password = request.form.get("password")
    # print(email, password)
    user = crud.get_user_by_email(email)

    if user:
        flash("An account with that email already exists. Please try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def user_login():
    """Show login form.

    Pull data from login form"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("The email or password you entered was incorrect, please try again.")
    else:
        # Log in user by storing the user email in session
        session["user_email"] = user.email
        flash("Logged In!")

    return redirect("/profile")


@app.route("/profile")
def show_profile():
    """Display user profile page"""

    if "user_email" in session:
        email = session["user_email"]
        user = crud.get_user_by_email(email)
        return render_template("profile.html")

    else:
        flash("User not logged in")
        return redirect("/")


@app.route("/api/generate-playlist")
def initiate_web_scrape():
    OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
    OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
    SPOTIPY_REDIRECT_URI = "http://example.com"
    SPOTIPY_SCOPE = "playlist-modify-private"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=environ["SPOTIPY_CLIENT_ID"],
            client_secret=environ["SPOTIPY_CLIENT_SECRET"],
            redirect_uri="https://example.com/callback",
            scope=SPOTIPY_SCOPE,
            show_dialog=True,
            cache_path="token.txt",
        )
    )
    date = request.args.get("date")
    songs_and_artists = generate_playlist_tracks(date)
    playlist = build_spotify_playlist(sp, songs_and_artists, date)
    add_songs_to_spotify_playlist(sp, playlist, songs_and_artists)
    # double-check / debug if necessary
    url = playlist["external_urls"]["spotify"]
    return redirect(url)

    # url from temp.py -- url that will take user to spotify
    # url = "https: //open.spotify.com/playlist/1rl8dWuLImIrRrOUT1pHmp"
    # create empty playlist, add dict items in--


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

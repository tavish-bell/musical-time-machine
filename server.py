"""Server for musical time machine """
import random
from os import environ

import spotipy
from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   session)
from jinja2 import StrictUndefined
from spotipy.oauth2 import SpotifyOAuth

import crud
from model import connect_to_db, db
from spotify import (add_songs_to_spotify_playlist, build_spotify_playlist,
                     generate_playlist_tracks)

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
        session["user_id"] = user.user_id
        flash("Logged In!")

    return redirect("/profile")


@app.route("/profile")
def show_profile():
    """Display user profile page"""

    if "user_email" in session:
        email = session["user_email"]
        user = crud.get_user_by_email(email)
        
        TODO: create func in crud, 
        TODO: import choice from random
        TODO: pass playlist via jinja & render template
        
        playlist = choice(crud.get_playlists_by_user(arg=user))


        return render_template("profile.html")

    else:
        flash("User not logged in")
        return redirect("/")


@app.route("/api/generate-playlist")
def initiate_web_scrape():
    """generate playlist given user selected date"""
    print("*" * 20)
    spotipy_scope = "playlist-modify-private"
    date = request.args.get("date")
    message = request.args.get("message")
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=environ["SPOTIPY_CLIENT_ID"],
            client_secret=environ["SPOTIPY_CLIENT_SECRET"],
            redirect_uri="https://example.com/callback",
            scope=spotipy_scope,
            show_dialog=True,
            cache_path="token.txt",
        )
    )

    songs_and_artists = generate_playlist_tracks(date)
    playlist = build_spotify_playlist(sp, songs_and_artists, date)
    add_songs_to_spotify_playlist(
        sp, playlist, songs_and_artists, date, session["user_id"], db, message
    )

    url = playlist["external_urls"]["spotify"]
    return {"spotify_url": url}
    # return redirect(url)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

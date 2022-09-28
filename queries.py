from flask import Flask

from model import Playlist, Track, User, connect_to_db, db

app = Flask(__name__)
connect_to_db(app)

# get all the playlists for a user
user_playlist_query = db.session.query(User.playlists).all()

"""Models for musical time machine"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    playlists = db.relationship("Playlist", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Playlist(db.Model):
    """a playlist"""

    __tablename__ = "playlists"

    playlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    selected_date = db.Column(db.DateTime)
    # message = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", back_populates="playlists")

    # tracks = db.relationship("Track", back_populates="playlist")

    def __repr__(self):
        return f"<Playlist playlist_id={self.playlist_id} date created={self.date_created}>"


class PlaylistContents(db.Model):
    """contents of playlist"""

    # when this stuff is needed, add some relationships that will get playlist objects & tracks when querying for playlist contents --
    # relationships will help when putting items into db, just need to create playlist object & track object for each song
    # create playlist contents object, set playlist property to new playlist
    # set tracks object to list of tracks
    # session.add(playlist_contents)

    __tablename__ = "playlist_contents"
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.playlist_id"))
    track_id = db.Column(db.Integer, db.ForeignKey("tracks.track_id"))


class Track(db.Model):
    """a song track"""

    __tablename__ = "tracks"

    track_id = db.Column(db.Integer, primary_key=True, nullable=False)
    track_title = db.Column(db.String, nullable=False)
    track_artist = db.Column(db.String, nullable=False)
    track_album = db.Column(db.String, nullable=True)
    track_year = db.Column(db.Integer, nullable=True)
    # playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.playlist_id"))
    # playlist = db.relationship("Playlist", back_populates="tracks")

    def __repr__(self):
        return (
            f"<Track track title={self.track_title} track artist={self.track_artist}>"
        )


def connect_to_db(flask_app, db_uri="postgresql:///timemachine", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)

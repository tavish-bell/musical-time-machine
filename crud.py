"""Create Replace Update Delete operations."""


import datetime

from model import Playlist, Track, User, connect_to_db, db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def get_user_by_id(user_id):
    """Return user by user_id/"""

    return User.query.get(user_id)

    # user_id is primary key


def get_user_by_email(email):
    """Return user by email"""

    return User.query.filter(User.email == email).first()

    # return a user with that email if it exists; otherwise return None


# TODO:add optional param for msg, if it exists
def make_playlist(selected_date, user_id, message):
    """Return playlist object"""
    date_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
    playlist = Playlist(selected_date=date_obj, user_id=user_id)

    return playlist


def make_track(song, artist):
    """Return track object"""
    track_title = song
    track_artist = artist
    track = Track(track_title=song, track_artist=artist)

    return track


if __name__ == "__main__":
    from server import app

    connect_to_db(app)

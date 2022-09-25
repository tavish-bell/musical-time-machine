"""Create Replace Update Delete operations."""


from model import Playlist, Track, User, connect_to_db


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


if __name__ == "__main__":
    from server import app

    connect_to_db(app)

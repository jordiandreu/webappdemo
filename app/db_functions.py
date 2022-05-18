from typing import Optional

from app.db_conf import db_session
from app.models import User

db = db_session.session_factory()


def get_users():
    users = db.query(User).all()
    return users


def add_user(username: str, email: str):
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(id: int, username: Optional[str] = None, email: Optional[str] = None):
    user2update = db.query(User).filter(User.id == id).first()
    if username:
        user2update.username = username
    if email:
        user2update.email = email
    db.commit()
    # db.refresh(user2update)
    return user2update


def delete_user(id: int):
    user2delete = db.query(User).filter(User.id == id).first()
    if user2delete:
        db.delete(user2delete)
        db.commit()
        return user2delete
    else:
        raise Exception("User does not exist!")

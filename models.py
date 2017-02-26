from database import db
from sqlalchemy import Column, Integer, String, Sequence


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User(username={}, email={})>'.format(
            self.username, self.email
        )

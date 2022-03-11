from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    post = db.relationship("Pitch", backref="user", lazy="dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__='posts'


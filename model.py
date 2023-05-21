from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class User(db.Model):
    """Makes a user in the database that takes in the values for a password and username."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password = password

class Post(db.Model):
    
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    header = db.Column(db.String)
    body = db.Column(db.Text)

    def __init__(self,user_id,header,body):
        self.user_id = user_id
        self.header = header
        self.body = body

class Reaction(db.Model):

    __tablename__ = 'reactions'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    is_liked = db.Column(db.Boolean)
    is_disliked = db.Column(db.Boolean)

    def __init__(self,user_id,post_id,is_liked,is_disliked):
        self.user_id = user_id
        self.post_id = post_id
        self.is_liked = is_liked
        self.is_disliked = is_disliked

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    comment_text = db.Column(db.Text)

    def __init__(self,user_id,post_id,comment_text):

        self.user_id = user_id
        self.post_id = post_id
        self.comment_text = comment_text

def connect_to_db(app, db_uri="postgresql:///capstone", echo=True):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to db...")
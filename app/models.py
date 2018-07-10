from datetime import datetime
from .ext import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    regist_time = db.Column(db.DateTime, datetime=datetime.utcnow())
    is_delete = db.Column(db.Boolean, default=False)


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    content = db.Column(db.Text)
    is_delete = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, datetime=datetime.utcnow())
    update_time = db.Column(db.DateTime, datetime=datetime.utcnow())
    tag = db.Column(db.String(16))
    user_id = db.Column(db.Integer, unique=True, nullable=False)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    content = db.Column(db.Text)
    is_delete = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, datetime=datetime.utcnow())
    update_time = db.Column(db.DateTime, datetime=datetime.utcnow())
    user_id = db.Column(db.Integer, unique=True, nullable=False)




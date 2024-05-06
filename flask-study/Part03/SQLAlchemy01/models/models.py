#model -> 테이블 생성
from db import db

#user
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')

#board
class Board(db.Model):
    __tablename__="boards"

    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship('User', back_populates='boards')

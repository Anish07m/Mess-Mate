from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(50), default='user')  # Added role field

    def __repr__(self):
        return f"<User {self.username}>"




class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Feedback {self.name}>'

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room = db.Column(db.String(20), nullable=False)
    issue = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship back to the User
    user = db.relationship('User', backref='complaints', lazy=True)

    def __repr__(self):
        return f"<Complaint {self.id} by User {self.user_id}>"
    
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    items = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Menu {self.day}>'


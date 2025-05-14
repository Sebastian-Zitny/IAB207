import os

from flask_sqlalchemy import SQLAlchemy



# Configure SQLite database
base_dir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()


# --- Models ---
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    events = db.relationship('Event', backref='owner', lazy=True)
    bookings = db.relationship('Booking', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)


class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    venue = db.Column(db.String(200))
    image_url = db.Column(db.String(300))
    category = db.Column(db.String(50))
    status = db.Column(db.String(20))  # Open, Cancelled, Sold Out, Inactive
    owner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    bookings = db.relationship('Booking', backref='event', lazy=True)
    comments = db.relationship('Comment', backref='event', lazy=True)


class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)
    date_booked = db.Column(db.DateTime, default=datetime.utcnow)


class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)





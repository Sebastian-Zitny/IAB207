from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

<<<<<<< HEAD
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    bookings = db.relationship('Booking', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    events = db.relationship('Event', backref='owner', lazy=True)
=======

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
>>>>>>> 2cad1d684b0d978cb9e88a804e0c548abb944f6a

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    venue = db.Column(db.String(200))
    image_url = db.Column(db.String(300))
    category = db.Column(db.String(50))
    status = db.Column(db.String(20))  # Open, Cancelled, Sold Out, Inactive
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bookings = db.relationship('Booking', backref='event', lazy=True)
    comments = db.relationship('Comment', backref='event', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)
    date_booked = db.Column(db.DateTime, default=datetime.utcnow)

<<<<<<< HEAD
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
=======
Base.metadata.create_all(engine)
>>>>>>> 2cad1d684b0d978cb9e88a804e0c548abb944f6a

with app.app_context():
    db.create_all()
    print("✅ Database created successfully.")

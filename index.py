from flask import Blueprint, render_template, redirect, url_for
from databaseCreator import db, Event  # Adjust if your Event model is defined elsewhere

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def default():
    events = Event.query.order_by(Event.date.asc()).all()
    return render_template('index.html', events=events)

@index_bp.route('/index.html')
def home():
    return redirect('/')

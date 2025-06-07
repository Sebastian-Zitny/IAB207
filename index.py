from flask import Blueprint, render_template, redirect, url_for, request
from databaseCreator import db, Event

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def default():
    keyword = request.args.get('keyword', '').strip()
    selected_categories = request.args.getlist('category')
    selected_cities = request.args.getlist('city')

    query = Event.query

    if keyword:
        query = query.filter(
            (Event.title.ilike(f'%{keyword}%')) |
            (Event.venue.ilike(f'%{keyword}%'))
        )

    if selected_categories:
        query = query.filter(Event.category.in_(selected_categories))

    if selected_cities:
        query = query.filter(Event.venue.in_(selected_cities))

    created_events = query.order_by(Event.date.asc()).all()

    return render_template('index.html', created_events=created_events)

@index_bp.route('/index.html')
def home():
    return redirect(url_for('index.default'))
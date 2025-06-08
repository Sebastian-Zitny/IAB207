import os
from flask import Flask, render_template, session, flash, redirect, request
from createEvents import init_createEvents
from checkOut import init_checkOut
from myBooking import init_myBooking
from eventDetail import init_eventDetail
from Register import init_Register
from logIn import init_logIn, init_logOut
from databaseCreator import db, Event
from sqlalchemy import or_

app = Flask(__name__)
app.secret_key = 'secret'

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db_path = os.path.join(base_dir, 'database.db')
    if not os.path.exists(db_path):
        db.create_all()

init_createEvents(app)
init_checkOut(app)
init_myBooking(app)
init_eventDetail(app)
init_Register(app)
init_logIn(app)

@app.route('/')
@app.route('/index.html')
def home():
    keyword = request.args.get('keyword', '').strip()
    selected_categories = request.args.getlist('category')
    selected_cities = request.args.getlist('city')

    query = Event.query.filter(Event.date.isnot(None))

    if keyword:
        like_pattern = f"%{keyword}%"
        query = query.filter(
            or_(
                Event.title.ilike(like_pattern),
                Event.venue.ilike(like_pattern)
            )
        )

    if selected_categories:
        query = query.filter(Event.category.in_(selected_categories))

    if selected_cities:
        city_filters = [Event.venue.ilike(f"%{c}%") for c in selected_cities]
        query = query.filter(or_(*city_filters))

    created_events = query.order_by(Event.date.asc()).all()

    return render_template('index.html', created_events=created_events)

@app.route('/logout')
def logOut():
    session.clear()
    flash("You’ve been logged out.", "success")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
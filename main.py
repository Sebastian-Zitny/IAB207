import os
from flask import Flask, render_template, session, flash, redirect
from createEvents import init_createEvents
from checkOut import init_checkOut
from myBooking import init_myBooking
from eventDetail import init_eventDetail
from Register import init_Register
from logIn import init_logIn, init_logOut
from databaseCreator import db 
from databaseCreator import Event 


app = Flask(__name__)
app.secret_key = 'secret'

base_dir = os.path.abspath(os.path.dirname(__file__))

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'database.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind SQLAlchemy to app
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

from sqlalchemy import and_

@app.route('/')
@app.route('/index.html')
def home():
    created_events = Event.query.filter(Event.date.isnot(None)).order_by(Event.event_id.asc()).all()
    return render_template('index.html', created_events=created_events)



@app.route('/logout')
def logOut():
    session.clear()
    flash("You’ve been logged out.", "success")
    return redirect('/')   # back to Home


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)

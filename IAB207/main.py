import os
from flask import Flask, render_template
from createEvents import init_createEvents
from checkOut import init_checkOut
from myBooking import init_myBooking
from eventDetail import init_eventDetail
from Register import init_Register
from logIn import init_logIn
from databaseCreator import db 



app = Flask(__name__)
app.secret_key = 'secret'

base_dir = os.path.abspath(os.path.dirname(__file__))

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'database.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind SQLAlchemy to app
db.init_app(app)

with app.app_context():
    db.create_all()

init_createEvents(app)

init_checkOut(app)

init_myBooking(app)

init_eventDetail(app)

init_Register(app)

init_logIn(app)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html')
def Home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

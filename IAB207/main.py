from flask import Flask, render_template
from createEvents import init_createEvents
from checkOut import init_checkOut
from myBooking import init_myBooking
from eventDetail import init_eventDetail
from Register import init_Register
from logIn import init_logIn

app = Flask(__name__)

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
    app.run(debug=False, use_reloader=False)

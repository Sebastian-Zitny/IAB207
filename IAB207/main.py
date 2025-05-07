from flask import Flask, render_template


app = Flask(__name__)




@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html')
def Home():
    return render_template('index.html')

@app.route('/createEvents.html')
def createEvents():
    return render_template('createEvents.html')

@app.route('/eventDetail.html')
def eventDetail():
    return render_template('eventDetail.html')

@app.route('/myBooking.html')
def myBooking():
    return render_template('myBooking.html')

@app.route('/checkOut.html')
def checkOut():
    return render_template('checkOut.html')




if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)

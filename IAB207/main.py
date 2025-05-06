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

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)

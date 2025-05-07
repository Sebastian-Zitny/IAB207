from flask import Flask, render_template


def init_checkOut(app):
    @app.route('/checkOut.html')
    def checkOut():
        return render_template('checkOut.html')


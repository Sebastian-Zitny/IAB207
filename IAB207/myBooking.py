from flask import Flask, render_template


def init_myBooking(app):
    @app.route('/myBooking.html')
    def myBooking():
        return render_template('myBooking.html')


from flask import Flask, render_template


def init_logIn(app):
    @app.route('/logIn.html')
    def logIn():
        return render_template('logIn.html')


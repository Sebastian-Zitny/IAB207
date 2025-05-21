from flask import Flask, render_template


def init_index(app):
    @app.route('/index.html')
    def index():
        return render_template('index.html')


from flask import Flask, render_template


def init_createEvents(app):
    @app.route('/createEvents.html')
    def createEvents():
        return render_template('createEvents.html')


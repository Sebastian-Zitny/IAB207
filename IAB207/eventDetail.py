from flask import Flask, render_template


def init_eventDetail(app):
    @app.route('/eventDetail.html')
    def eventDetail():
        return render_template('eventDetail.html')


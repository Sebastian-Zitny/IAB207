from flask import Flask, render_template


def init_Register(app):
    @app.route('/Register.html')
    def Register():
        return render_template('Register.html')


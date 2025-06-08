from flask import render_template, request, redirect, url_for, flash, session
from databaseCreator import db, User

def init_logIn(app):
    @app.route('/logIn.html', methods=['GET', 'POST'])
    def logIn():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = User.query.filter_by(username=username, password=password).first()

            if user:
                session['user_id'] = user.user_id
                session['username'] = user.username
                flash("Login successful!", "success")
                return redirect(url_for('myBooking'))
            else:
                flash("Invalid username or password.", "error")
                return redirect(url_for('logIn'))

        return render_template('logIn.html')
    
def init_logOut(app):
    @app.route('/logout')
    def logOut():
        session.clear()
        flash("You’ve been logged out.", "success")
        return redirect('/')
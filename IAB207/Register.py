from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from databaseCreator import db, User 

def init_Register(app):
    @app.route('/Register.html', methods=['GET', 'POST'])
    def Register():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            # Check if user already exists
            existing_user = User.query.filter(
                (User.username == username) | (User.email == email)
            ).first()
            if existing_user:
                flash("Username or email already exists", "error")
                return redirect(url_for('Register'))


            # Create and save new user
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            flash("Registration successful!", "success")
            return redirect(url_for('logIn'))  # Assuming you have a login route

        return render_template('register.html')
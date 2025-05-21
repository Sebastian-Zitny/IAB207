from flask import request, render_template, redirect, url_for, session, flash
import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_createEvents(app):
    @app.route('/createEvents.html', methods=['GET', 'POST'])
    def createEvents():
        if 'user_id' not in session:
            flash("You must be logged in to create an event.", "danger")
            return redirect(url_for('logIn'))

        if request.method == 'POST':
            try:
                title = request.form['title']
                date = request.form['date']
                start_time = request.form['start_time']
                end_time = request.form['end_time']
                venue = request.form['venue']
                image_url = request.form['image_url']
                category = request.form['category']
                status = 'Open'
                owner_id = session['user_id']

                conn = get_db_connection()
                conn.execute("""
                    INSERT INTO event (title, date, start_time, end_time, venue, image_url, category, status, owner_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (title, date, start_time, end_time, venue, image_url, category, status, owner_id))
                conn.commit()
                conn.close()

                flash("✅ Event created successfully!", "success")
                return redirect('/createEvents.html')
            except Exception as e:
                flash(f"❌ Error creating event: {e}", "danger")
                return redirect('/createEvents.html')

        # 🟢 Fetch existing events created by the current user
        conn = get_db_connection()
        events = conn.execute('SELECT * FROM event WHERE owner_id = ?', (session['user_id'],)).fetchall()
        conn.close()

        return render_template('createEvents.html', events=events)

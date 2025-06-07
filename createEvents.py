from flask import request, render_template, redirect, url_for, session, flash
import sqlite3
import os
from werkzeug.utils import secure_filename

IMG_UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(IMG_UPLOAD_FOLDER, exist_ok=True)

DATABASE = os.path.join(os.path.dirname(__file__), 'database.db')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
                category = request.form.get('category', '')
                description = request.form.get('description', '')
                status = 'Open'
                owner_id = session['user_id']

                # handle image upload
                image_file = request.files.get('image_url')
                image_url = None
                if image_file and allowed_file(image_file.filename):
                    image_url = secure_filename(image_file.filename)
                    image_path = os.path.join(IMG_UPLOAD_FOLDER, image_url)
                    image_file.save(image_path)
                elif image_file and image_file.filename != '':
                    flash("❌ Invalid image file type.", "danger")
                    return redirect(url_for('createEvents'))

                # save to DB
                conn = get_db_connection()
                conn.execute("""
                    INSERT INTO event (
                        title, date, start_time, end_time,
                        venue, category, status, owner_id,
                        image_url, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    title, date, start_time, end_time,
                    venue, category, status, owner_id,
                    image_url, description
                ))
                conn.commit()
                conn.close()

                flash("✅ Event created successfully!", "success")
                return redirect(url_for('createEvents'))

            except Exception as e:
                flash(f"❌ Error creating event: {e}", "danger")
                return redirect(url_for('createEvents'))

        conn = get_db_connection()
        events = conn.execute('SELECT * FROM event WHERE owner_id = ?', (session['user_id'],)).fetchall()
        conn.close()
        return render_template('createEvents.html', events=events)

from flask import render_template, request, redirect, url_for, session, flash
import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_checkOut(app):
    @app.route('/checkOut/<int:event_id>', methods=['GET', 'POST'])
    def checkOut(event_id):
        if 'user_id' not in session:
            flash("Please log in to book tickets.", "warning")
            return redirect(url_for('logIn'))

        conn = get_db_connection()

        if request.method == 'POST':
            qty = request.form.get('quantity', '').strip()
            try:
                qty_int = int(qty)
                if qty_int < 1:
                    raise ValueError
            except ValueError:
                flash("Please enter a valid ticket quantity.", "danger")
                conn.close()
                return redirect(url_for('checkOut', event_id=event_id))

            conn.execute(
                """
                INSERT INTO booking (user_id, event_id, quantity, date_booked)
                VALUES (?, ?, ?, datetime('now'))
                """,
                (session['user_id'], event_id, qty_int)
            )
            conn.commit()
            conn.close()

            flash("Your booking was successful!", "success")
            return redirect(url_for('myBooking'))

        event = conn.execute(
            """
            SELECT event_id, title, date, start_time AS time, image_url AS image, venue, status, description
            FROM event
            WHERE event_id = ?
            """,
            (event_id,)
        ).fetchone()
        conn.close()

        if event is None:
            flash("Event not found.", "warning")
            return redirect(url_for('Home'))

        return render_template('checkOut.html', event=event)
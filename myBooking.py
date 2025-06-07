from flask import render_template, request, redirect, url_for, session
import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_myBooking(app):
    @app.route('/myBooking.html')
    def myBooking():
        if 'user_id' not in session:
            return redirect(url_for('logIn'))

        conn = get_db_connection()
        bookings = conn.execute("""
            SELECT
                b.booking_id,
                e.event_id,
                e.title,
                e.date,
                e.start_time,
                e.image_url,
                e.venue,
                b.quantity,
                b.date_booked
            FROM booking b
            JOIN event e ON b.event_id = e.event_id
            WHERE b.user_id = ?
            ORDER BY b.date_booked DESC
        """, (session['user_id'],)).fetchall()
        conn.close()

        return render_template('myBooking.html', bookings=bookings)
from flask import Flask, render_template
from flask import request, render_template, redirect, url_for, session
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
        events = conn.execute("""
            SELECT event_id, title, date, image_url, venue
            FROM event
            WHERE owner_id = ?
            ORDER BY date DESC
        """, (session['user_id'],)).fetchall()
        conn.close()

        return render_template('myBooking.html', bookings=events)



# eventDetail.py
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,    # ← add this
    flash       # ← and this if you want to flash the error
)
from datetime import datetime
from app.forms import CommentForm
from databaseCreator import db, Comment as DBComment

# Event and Comment Classes
class Comment:
    def __init__(self, user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at

class Event:
    def __init__(self, id, title, city, date, time, speaker, image, status, description):
        self.id = id
        self.title = title
        self.city = city
        self.date = date
        self.time = time
        self.speaker = speaker
        self.image = image
        self.status = status
        self.description = description
        self.comments = []

# Dummy Event Data
# eventDetail.py (or wherever you define your dummy data)
events = {
    "1": Event(
        "1",
        "Technology Executive Summit",
        "Brisbane, Australia",
        "14 Mar, 2025",
        "7:00 PM – 10:00 PM",
        "Steve Jobs",
        "img/Tech image.jpg",
        "Booking Available",
        "Join us at the Technology Executive Summit, an exclusive gathering..."
    ),
    "2": Event(
        "2",
        "FutureTech Innovation Forum",
        "New York, U.S",
        "21 Mar, 2025",
        "10:00 AM – 4:00 PM",
        "Elon Musk",
        "img/Tech image6.jpg",
        "Booking Available",
        "Dive into future tech innovations..."
    ),
    "3": Event(
        "3",
        "AI & Automation Expo 2025",
        "Boston, U.S",
        "18 Apr, 2025",
        "9:00 AM – 5:00 PM",
        "Ada Lovelace",
        "img/Tech image5.jpg",
        "Booking Available",
        "Explore the power of AI and automation..."
    ),

    # ——— three new entries below ———

    "4": Event(
        "4",
        "Global Blockchain Summit",
        "London, U.K.",
        "05 Jun, 2025",
        "9:00 AM – 5:00 PM",
        "Satoshi Nakamoto",
        "img/Tech image7.jpg",
        "Booking Available",
        "Discover the latest trends in blockchain, DeFi, and decentralized systems."
    ),
    "5": Event(
        "5",
        "Cybersecurity Essentials Workshop",
        "Sydney, Australia",
        "12 Jun, 2025",
        "10:00 AM – 1:00 PM",
        "Bruce Schneier",
        "img/Tech image8.jpg",
        "Booking Available",
        "A hands-on workshop covering modern threats, defence strategies, and best practices."
    ),
    "6": Event(
        "6",
        "AI Ethics Forum",
        "San Francisco, U.S",
        "20 Jun, 2025",
        "2:00 PM – 6:00 PM",
        "Timnit Gebru",
        "img/Tech image9.jpg",
        "Booking Available",
        "Join experts discussing the ethical implications and governance of AI."
    ),
}


def init_eventDetail(app):
    @app.route('/event/<event_id>', methods=['GET', 'POST'])
    def event_detail(event_id):
        form = CommentForm()
        event = events.get(event_id)
        if not event:
            return "Event not found", 404

        if form.validate_on_submit():
            # **Only** on POST do we require login
            if 'user_id' not in session:
                flash("You must be logged in to leave a comment.", "error")
                return redirect(url_for('logIn'))
            
            # save the comment
            new_comment = DBComment(
                user_id     = session['user_id'],
                event_id    = int(event_id),
                content     = form.text.data,
                date_posted = datetime.utcnow()
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('event_detail', event_id=event_id))

        # Always load persisted comments
        db_comments = DBComment.query.filter_by(
            event_id=int(event_id)
        ).all()
        comments = [
            Comment(c.user.username, c.content, c.date_posted.strftime("%b %d, %Y"))
            for c in db_comments
        ]

        # Render page: if user logged-in, show the form; otherwise prompt them
        return render_template(
            'eventDetail.html',
            event     = event,
            comments  = comments,
            form      = form,
            can_comment = ('user_id' in session)
        )
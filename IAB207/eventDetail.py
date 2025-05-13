# eventDetail.py
from flask import render_template, request, redirect, url_for
from datetime import datetime
from app.forms import CommentForm

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
events = {
    "1": Event("1", "Technology Executive Summit", "Brisbane, Australia", "14 Mar, 2025", "7:00 PM – 10:00 PM", "Steve Jobs", "img/Tech image.jpg", "Booking Available", "Join us at the Technology Executive Summit, an exclusive gathering..."),
    "2": Event("2", "FutureTech Innovation Forum", "New York, U.S", "21 Mar, 2025", "10:00 AM – 4:00 PM", "Elon Musk", "img/Tech image6.jpg", "Booking Available", "Dive into future tech innovations..."),
    "3": Event("3", "AI & Automation Expo 2025", "Boston, U.S", "18 Apr, 2025", "9:00 AM – 5:00 PM", "Ada Lovelace", "img/Tech image5.jpg", "Booking Available", "Explore the power of AI and automation...")
}

def init_eventDetail(app):
    @app.route('/event/<event_id>', methods=['GET', 'POST'])
    def event_detail(event_id):
        form = CommentForm()
        event = events.get(event_id)

        if not event:
            return "Event not found", 404

        if form.validate_on_submit():
            comment = Comment("Anonymous", form.text.data, datetime.now().strftime("%b %d, %Y"))
            event.comments.append(comment)
            return redirect(url_for('event_detail', event_id=event_id))

        return render_template('eventDetail.html', event=event, comments=event.comments, form=form)

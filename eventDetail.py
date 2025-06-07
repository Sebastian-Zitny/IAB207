from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
from datetime import datetime
from app.forms import CommentForm
from databaseCreator import db, Comment as DBComment, Event as DBEvent, User as DBUser

# Comment class for passing formatted data to template
class Comment:
    def __init__(self, user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at

def init_eventDetail(app):
    @app.route('/event/<int:event_id>', methods=['GET', 'POST'])
    def event_detail(event_id):
        form = CommentForm()

        # Fetch event from the DB
        event = DBEvent.query.get(event_id)
        if not event:
            return "Event not found", 404

        # Comment form submission
        if form.validate_on_submit():
            if 'user_id' not in session:
                flash("You must be logged in to leave a comment.", "error")
                return redirect(url_for('logIn'))

            new_comment = DBComment(
                user_id=session['user_id'],
                event_id=event_id,
                content=form.text.data,
                date_posted=datetime.utcnow()
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('event_detail', event_id=event_id))

        # Load comments
        db_comments = DBComment.query.filter_by(event_id=event_id).order_by(DBComment.date_posted.desc()).all()
        comments = [
            Comment(c.user.username, c.content, c.date_posted.strftime("%b %d, %Y"))
            for c in db_comments
        ]

        return render_template(
            'eventDetail.html',
            event=event,
            comments=comments,
            form=form,
            can_comment=('user_id' in session)
        )
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.forms import CreateEventForm
from databaseCreator import db, Event  

def init_createEvents(app):

    @app.route('/create-event', methods=['GET', 'POST'])
    @login_required  
    def create_event():
        form = CreateEventForm()

        if form.validate_on_submit():
            new_event = Event(
                title=form.title.data,
                description=form.description.data,
                date=form.date.data,
                start_time=form.start_time.data,
                end_time=form.end_time.data,
                venue=form.venue.data,
                image_url=form.image_url.data,
                category=form.category.data,
                status='Open',
                owner_id=current_user.id
            )

            db.session.add(new_event)
            db.session.commit()
            flash('✅ Event created successfully!', 'success')
            return redirect(url_for('Home'))

        return render_template('createEvents.html')

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, SubmitField
from wtforms.validators import InputRequired, DataRequired

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Add Comment')

class CreateEventForm(FlaskForm):
    title = StringField('Event Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    date = DateField('Date', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])
    venue = StringField('Venue', validators=[DataRequired()])
    image_url = StringField('Image URL')
    category = StringField('Category')
    submit = SubmitField('Submit Event')

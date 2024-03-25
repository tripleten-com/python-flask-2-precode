from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
    title = StringField(
        'Enter the title of the movie',
        validators=[DataRequired(message='Required field'),
                    Length(1, 128)]
    )
    text = TextAreaField(
        'Write a short review',
        validators=[DataRequired(message='Required field')]
    )
    source = URLField(
        'Add a link to a detailed movie review',
        validators=[Length(1, 256), Optional()]
    )
    submit = SubmitField('Add')

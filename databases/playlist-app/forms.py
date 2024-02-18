"""Forms for playlist app."""

from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[Length(max=255)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    artist = StringField('Artist', validators=[InputRequired(), Length(max=100)])
    duration = IntegerField('Duration (seconds)', validators=[InputRequired(), NumberRange(min=1)])
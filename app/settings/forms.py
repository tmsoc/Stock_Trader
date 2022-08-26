from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email
from app.models import User


class PreferencesForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    phone_number = StringField('Phone Number')
    email = StringField('Email', validators=[DataRequired(), Email()])
    dob = DateField('Date Of Birth')
    contact_preference = RadioField('Contact Preference', choices=[('1', 'Email'), ('2', 'Text')], default='1', validators=[DataRequired()])
    submit = SubmitField('Save Changes')

    def validate_username(self, username):
        # Need to validate that username is not already used.
        pass

    def validate_email(self, email):
        # Need to validate that email is not already used.
        pass


class NotificationForm(FlaskForm):
    account_change = BooleanField('Account Changes')
    holds = BooleanField('Holdings')
    watchlist = BooleanField('Watch List', default='checked')
    submit = SubmitField('Save Changes')

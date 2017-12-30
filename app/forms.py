from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password', message='Passwords must match'),
        Length(min=6)
    ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6)])
    email_address = StringField('email_address', validators=[DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[DataRequired()])

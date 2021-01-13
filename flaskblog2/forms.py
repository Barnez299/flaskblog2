from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog2.models import User, Post



class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember = BooleanField(label='Remember Me')
    submit = SubmitField(label='Login')

class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label='Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=2, max=16)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exist. Please create another one")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exist. Please create another one")

class UpdateAccountForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label='Email',validators=[DataRequired(), Email()])
    picture = FileField(label='Update Profile Pic', validators=[FileAllowed(['png','jpg'])])
    submit = SubmitField(label='Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username already exist. Please create another one")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email already exist. Please create another one")
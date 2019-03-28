from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4,max=12)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),Length(min=4,max=12), EqualTo('password')])
    pic_filename = "default"
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4,max=12)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import mysql.connector

recipe_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Recipease"
)

cur = recipe_db.cursor()

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4,max=12)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),Length(min=4,max=12), EqualTo('password')])
    pic_filename = "default"
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        mysql_command = "SELECT Username FROM users WHERE Username = %s;"
        cur.execute(mysql_command,username)
        existing_username = cur.fetchone()
        print(existing_username)
        print(type(existing_username))

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4,max=12)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

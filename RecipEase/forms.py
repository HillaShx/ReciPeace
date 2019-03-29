from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
# import mysql.connector
from RecipEase import recipe_db

cur = recipe_db.cursor()

class RegistrationForm(FlaskForm):
    username = TextField('Username',validators=[DataRequired(),Length(min=3,max=15)])
    email = TextField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4,max=12)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),Length(min=4,max=12), EqualTo('password')])
    pic_filename = "default"
    submit = SubmitField('Sign Up')

    def validate_username(self,new_username):
        mysql_command = "SELECT Username FROM users WHERE Username = %s;"
        if type(new_username) == str:
            cur.execute(mysql_command, (new_username,))
            existing_username = cur.fetchone()
            if existing_username:
                return False
        return True

    def validate_email(self,new_email):
        mysql_command = "SELECT Email FROM users WHERE Email = %s;"
        if type(new_email) == str:
            cur.execute(mysql_command, (new_email,))
            existing_email = cur.fetchone()
            if existing_email:
                return False
        return True

class LoginForm(FlaskForm):
    email = TextField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4,max=12)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_login_info(self,email,password):
        mysql_command = "SELECT Username, Email, AES_DECRYPT(Password,'PaSswOrD') FROM Recipease.users WHERE (AES_DECRYPT(Password,'PaSswOrD') = %s) AND (Email = %s);"
        cur.execute(mysql_command,(password,email))
        existing_record = cur.fetchone()
        if existing_record:
            username = existing_record[0]
            if existing_record[2] == password:
                return True, username
        return False, ""

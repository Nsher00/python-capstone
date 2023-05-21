from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, EmailField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class PostForm(FlaskForm):
    header = StringField('header', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])

class NewUserForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    repassword = PasswordField('repassword', validators=[DataRequired()])
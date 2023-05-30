from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class PostForm(FlaskForm):
    header = StringField('header', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])
    delete = SubmitField('delete')
    like = SubmitField('like')
    dislike = SubmitField('dislike')

class NewUserForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    repassword = PasswordField('repassword', validators=[DataRequired()])

class CommentForm(FlaskForm):
    text = TextAreaField('text', validators=[DataRequired()])
    submit = SubmitField('submit')
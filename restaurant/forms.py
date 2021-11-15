from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class RegisterForm(FlaskForm):
    username = StringField(label = 'username')

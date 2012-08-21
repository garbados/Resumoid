from db import db
from flask_login import UserMixin
from flask.ext.wtf import Form, TextField, Required, Email
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Document, UserMixin):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True, primary_key=True)
    pass_hash = db.StringField(required=True)

class ValidateLogin(object):
    """Attaches to the form's password field. Validates the user exists and the credentials are correct."""
    def __init__(self, pass_message=None, user_message=None):
        self.user_message = user_message or u'No user by that email.'
        self.pass_message = pass_message or u'Incorrect password.'

    def __call__(self, form, field):
        user = User.objects(email=form.email.data).first()
        if not user:
            return ValidationError(self.user_message)
        elif bcrypt.check_password_hash(field, user.pass_hash)):
            return ValidationError(self.pass_message)

class ValidateSignup(object):
    """Attaches to the form's pass_check field. Validates no user with the form's email exists, and that the passwords match."""
    def __init__(self, pass_message=None, user_message=None):
        self.user_message = user_message or u'User with that email already exists.'
        self.pass_message = pass_message or u'Passwords don\'t match.'

    def __call__(self, form, field):
        user = User.objects(email=form.email.data).first()
        if user:
            return ValidationError(self.user_message)
        if form.password.data != field:
            return ValidationError(self.pass_message)

def validate_signup(email, password, pass_check):

class LoginForm(Form):
    email = TextField(validators=[Email()])
    password = PasswordField(validators=[Required(), ValidateLogin()])

class SignupForm(Form):
    name = TextField(validators=[Required()])
    email = TextField(validators=[Email()])
    password = PasswordField(validators=[Required()])
    pass_check = PasswordField(validators=[Required(), ValidateSignup()])

class ForgotForm(Form):
    email = TextField(validators=[Email()])
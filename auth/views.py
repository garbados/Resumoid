from flask_login import LoginManager, current_user, login_user
from flask import Blueprint, request, redirect, g
from models import User

login_manager = LoginManager()
views = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(userid):
    return User.objects(id=userid).first()

@views.route('/login', methods=["GET", "POST"])
def login():
    """
    WARNING: This method currently suffers from a security vulnerability.
    A user could fake their login by sending requests to this function
    without actually logging in. We would create a user from the request,
    and log the user in. No good.
    TODO: Fix this security hole.
    """
    if request.method == 'POST':
        if not current_user.is_authenticated():
            user_data = dict(id = 'id')
            for key, value in user_data.iteritems():
                user_data[key] = request.args[value][0]
            user = User.objects.first(**user_data)
            if not user:
                user = User(**user_data)
            login_user(user)
            g['user'] = current_user
            user.set_profile()
        return ''
    else:
        return redirect('/')

login_manager.login_view = 'login'

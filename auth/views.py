from flask_login import LoginManager, current_user, login_user
from flask import Blueprint, request, redirect, g, flash
from models import User, LoginForm, SignupForm, ForgotForm

login_manager = LoginManager()
views = Blueprint('auth', __name__)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(email):
    return User.objects(email=email).first()

@views.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    elif form.errors:
        for error in form.errors:
            flash(error, "error")
    return render_template('login.html', form=form)

@views.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.save()
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    elif form.errors:
        for error in form.errors:
            flash(error, "error")
    return render_template('signup.html', form=form)
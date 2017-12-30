from flask import Blueprint, render_template, current_app, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user

from app.forms import LoginForm, RegisterForm
from app.handlers.user_handler import UserHandler

home_bp = Blueprint('home', __name__)


@home_bp.route('/user/trips')
@login_required
def user_index():
    return render_template('user/home.html',
                           basil_api_endpoint=current_app.config['BASIL_API_ENDPOINT'],
                           gmaps_api_key=current_app.config['GMAPS_API_KEY'])


@home_bp.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('home.user_index'))

    login_form = LoginForm()
    return render_template('homepage.html', form=login_form)


@home_bp.route("/login", methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserHandler.validate_user(form.username.data, form.password.data)
        if user:
            login_user(user)
            return redirect(url_for('home.user_index'))

    flash('Invalid credentials :(')
    return redirect(url_for('home.home'))


@home_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.user_index'))

    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = UserHandler.create(
                username=form.username.data,
                email=form.username.data,
                password=form.password.data
            )
            login_user(user)
            return redirect(url_for('home.user_index'))
        else:
            flash('Dude, get your shit together')

    return render_template('register.html', form=form)


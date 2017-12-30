from flask import Blueprint, render_template, current_app, redirect, url_for, flash, request

from app.forms import LoginForm, RegisterForm
from app.handlers.user_handler import UserHandler

home_bp = Blueprint('home', __name__)


@home_bp.route('/user/trips')
def user_index():
    return render_template('user/home.html',
                           basil_api_endpoint=current_app.config['BASIL_API_ENDPOINT'],
                           gmaps_api_key=current_app.config['GMAPS_API_KEY'])


@home_bp.route('/')
def home():
    login_form = LoginForm()
    return render_template('homepage.html', form=login_form)


@home_bp.route("/login", methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if UserHandler.validate_user(form.username.data, form.password.data):
            return redirect(url_for('home.user_index'))

    flash('Invalid credentials :(')
    return redirect(url_for('home.home'))


@home_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = UserHandler.create(
                username=form.username.data,
                email=form.username.data,
                password=form.password.data
            )
            return redirect(url_for('home.user_index'))
        else:
            flash('Dude, get your shit together')

    return render_template('register.html', form=form)

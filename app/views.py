from flask import request, Blueprint, render_template, current_app


home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def home():
    return render_template('home.html',
                           basil_api_endpoint=current_app.config['BASIL_API_ENDPOINT'],
                           gmaps_api_key=current_app.config['GMAPS_API_KEY'])

from flask import Flask
from flask_login import LoginManager

from app.database import db
from config import config
from app.views import home_bp
from app.finders.user_finder import UserFinder
from .api.routes import api_v1, api


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    api.init_app(app)
    app.register_blueprint(api_v1)
    app.register_blueprint(home_bp)
    login_manager = LoginManager(app)

    if app.debug:
        app.logger.setLevel("DEBUG")
    else:
        app.logger.setLevel("INFO")

    login_manager.login_view = "home.home"
    login_manager.user_loader(UserFinder.get_from_id)
    app.app_context().push()
    return app

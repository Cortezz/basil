from flask import Flask

from app.database import db
from config import config
from app.views import home_bp
from .api.routes import api_v1, api


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    api.init_app(app)
    app.register_blueprint(api_v1)
    app.register_blueprint(home_bp)

    if app.debug:
        app.logger.setLevel("DEBUG")
    else:
        app.logger.setLevel("INFO")

    app.app_context().push()
    return app

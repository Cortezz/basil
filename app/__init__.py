from flask import Flask

from config import config
from app.views import home_bp


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.register_blueprint(home_bp)

    if app.debug:
        app.logger.setLevel("DEBUG")
    else:
        app.logger.setLevel("INFO")

    app.app_context().push()
    return app

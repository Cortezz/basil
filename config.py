import os
import logging

from dotenv import load_dotenv

log = logging.getLogger(__name__)

if os.path.isfile('.env'):
    load_dotenv('.env')


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    BASIL_API_ENDPOINT = os.environ.get("BASIL_API_ENDPOINT")
    GMAPS_API_KEY = os.environ.get('GMAPS_API_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @classmethod
    def init_app(cls, app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


config = {
    '_baseconfig': BaseConfig,
    'development': DevelopmentConfig
}


__all__ = ['config']

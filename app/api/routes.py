from flask import Blueprint, make_response
from flask_restful import Api

from app.api.resources import Trip, Trips

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(api_v1)

api.add_resource(Trip, '/trips/<trip_id>')
api.add_resource(Trips, '/trips')

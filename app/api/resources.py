from flask_restful import Resource, reqparse

from app.handlers.trip_handler import TripHandler
from app.values.trip_value import TripValue
from app.values.trip_values import TripValues
from .common import coordinate_pair


class Trip(Resource):

    def get(self, trip_id):
        trip = TripHandler.get(trip_id)

        if not trip:
            return {"error": "Task not found"}
        trip_value = TripValue(trip).raw

        return trip_value


class Trips(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=False, location='json')
        parser.add_argument('coordinates', type=coordinate_pair, required=True, location='json', action='append')

        args = parser.parse_args(strict=True)
        trip = TripHandler.create(**args)
        trip_value = TripValue(trip).raw

        return trip_value

    def get(self):
        trips = TripHandler.get_all()
        trip_values = TripValues(trips).raw

        return trip_values

    def delete(self):
        trips = TripHandler.delete_all()

        if trips:
            return {"message": "Trips were successfully deleted"}, 200
        else:
            return {"message": "An unexpected error occurred"}, 500

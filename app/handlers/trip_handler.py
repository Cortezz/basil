from app.services.trips.create_trip_service import CreateTripService
from app.services.trips.delete_all_trips_service import DeleteAllTripsService
from app.finders.trip_finder import TripFinder


class TripHandler(object):

    @classmethod
    def create(cls, **kwargs):
        return CreateTripService(**kwargs).call()

    @classmethod
    def get(cls, task_id):
        return TripFinder.get_from_id(task_id)

    @classmethod
    def get_all(cls):
        return TripFinder.get_all()

    @classmethod
    def delete_all(cls):
        return DeleteAllTripsService().call()

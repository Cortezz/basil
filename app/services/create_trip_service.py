from app.models.trip import Trip


class CreateTripService(object):

    def __init__(self, coordinates, name=None):
        self.coordinates = coordinates
        self.name = name

    def call(self):
        trip = Trip(coordinates=self.coordinates, name=self.name)

        trip.create()
        trip.reload()

        return trip

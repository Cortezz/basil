from app.models.trip import Trip


class CreateTripService(object):

    def __init__(self, coordinates, name=None, color=None):
        self.coordinates = coordinates
        self.name = name
        self.color = color

    def call(self):
        trip = Trip(coordinates=self.coordinates, name=self.name, color=self.color)

        trip.create()
        trip.reload()

        return trip

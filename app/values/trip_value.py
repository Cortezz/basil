from .value_composite import ValueComposite


class TripValue(ValueComposite):

    def __init__(self, trip):
        super(TripValue, self).initialize({})
        self.trip = trip

        self.serialize_with(coordinates=self.trip.coordinates)
        self.serialize_with(id=str(trip.id))

        if self.trip.name:
            self.serialize_with(name=self.trip.name)
        if self.trip.color:
            self.serialize_with(color=self.trip.color)

from .value_composite import ValueComposite
from .trip_value import TripValue


class TripValues(ValueComposite):

    def __init__(self, trips):
        super(TripValues, self).initialize([])
        self.trips = trips

        trip_values = []
        for trip in self.trips:
            trip_values.append(TripValue(trip))
        self.serialize_and_append_from_values(trip_values)

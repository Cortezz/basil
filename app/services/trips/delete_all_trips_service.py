from app.models.trip import Trip


class DeleteAllTripsService(object):

    def call(self):
        Trip.delete_all()

        return True


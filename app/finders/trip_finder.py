from app.models.trip import Trip


class TripFinder(object):

    @classmethod
    def get_from_id(cls, task_id):
        return Trip.query.get(task_id)

    @classmethod
    def get_all(cls):
        return Trip.query.all()

from app.models.user import User


class UserFinder(object):

    @classmethod
    def get_from_id(cls, user_id):
        return User.query.get(user_id)

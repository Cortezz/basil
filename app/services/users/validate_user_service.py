from app.finders.user_finder import UserFinder


class ValidateUserService(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def call(self):
        user = UserFinder.get_from_username(self.username)

        if user and self.password == user.password:
            return user
        else:
            return None

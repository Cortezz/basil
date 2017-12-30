from app.services.users.create_user_service import CreateUserService


class UserHandler(object):

    @classmethod
    def create(cls, **kwargs):
        return CreateUserService(**kwargs).call()

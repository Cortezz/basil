from app.services.users.create_user_service import CreateUserService
from app.services.users.validate_user_service import ValidateUserService


class UserHandler(object):

    @classmethod
    def create(cls, **kwargs):
        return CreateUserService(**kwargs).call()

    @classmethod
    def validate_user(cls, username, password):
        return ValidateUserService(username,password).call()

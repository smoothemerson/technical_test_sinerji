from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from src.models.interface.user_repository import UserRepositoryInterface

from .interfaces.login_creator import LoginCreatorInterface


class LoginCreator(LoginCreatorInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()

    def create(self, email: str, password: str) -> dict:
        user = self.__find_user(email)
        user_id, nome, hashed_password = user[0], user[1], user[3]

        self.__verify_password(password, hashed_password)
        token = self.__jwt_handler.create_jwt_token({"user_id": user_id})

        return {"access": True, "nome": nome, "email": email, "token": token}

    def __find_user(self, email: str) -> tuple:
        user = self.__user_repository.get_user_by_email(email)
        if not user:
            raise HttpNotFoundError("User not found")
        return user

    def __verify_password(self, password: str, hashed_password: bytes) -> None:
        if not self.__password_handler.check_password(password, hashed_password):
            raise HttpBadRequestError("Wrong password")

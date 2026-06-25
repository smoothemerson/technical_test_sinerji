from src.drivers.password_handler import PasswordHandler
from src.models.interface.user_repository import UserRepositoryInterface

from .interfaces.user_register import UserRegisterInterface


class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def registry(self, nome: str, email: str, password: str) -> dict:
        hashed_password = self.__password_handler.encrypt_password(password)
        self.__user_repository.insert_user(nome, email, hashed_password)
        return {"type": "User", "count": 1, "nome": nome, "email": email}

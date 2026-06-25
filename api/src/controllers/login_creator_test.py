from pytest import raises

from src.drivers.password_handler import PasswordHandler
from src.models.interface.user_repository import UserRepositoryInterface

from .login_creator import LoginCreator

email = "joao@email.com"
password = "minhasenha"
hashed_password = PasswordHandler().encrypt_password(password)


class MockUserRepository(UserRepositoryInterface):
    def insert_user(self, nome: str, email: str, password: bytes) -> None:
        pass

    def get_user_by_email(self, email: str) -> tuple[int, str, str, bytes]:
        return (10, "João Silva", email, hashed_password)


class MockUserRepositoryNotFound(UserRepositoryInterface):
    def insert_user(self, nome: str, email: str, password: bytes) -> None:
        pass

    def get_user_by_email(self, email: str) -> tuple[int, str, str, bytes]:
        return None


def test_create_login():
    controller = LoginCreator(MockUserRepository())
    response = controller.create(email, password)

    assert response["access"] is True
    assert response["email"] == email
    assert response["token"] is not None


def test_create_with_wrong_password():
    controller = LoginCreator(MockUserRepository())

    with raises(Exception):
        controller.create(email, "senha_errada")


def test_create_with_user_not_found():
    controller = LoginCreator(MockUserRepositoryNotFound())

    with raises(Exception):
        controller.create("naoexiste@email.com", password)

from src.models.interface.user_repository import UserRepositoryInterface

from .user_register import UserRegister


class MockUserRepository(UserRepositoryInterface):
    def __init__(self) -> None:
        self.insert_user_attributes = {}

    def insert_user(self, nome: str, email: str, password: bytes) -> None:
        self.insert_user_attributes["nome"] = nome
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["password"] = password

    def get_user_by_email(self, email: str) -> tuple[int, str, str, bytes]:
        return (1, "João", email, b"")


def test_registry():
    repository = MockUserRepository()
    controller = UserRegister(repository)

    nome = "João Silva"
    email = "joao@email.com"
    password = "minhasenha"

    response = controller.registry(nome, email, password)

    assert response["type"] == "User"
    assert response["nome"] == nome
    assert response["email"] == email
    assert repository.insert_user_attributes["nome"] == nome
    assert repository.insert_user_attributes["email"] == email
    assert repository.insert_user_attributes["password"] is not None
    assert repository.insert_user_attributes["password"] != password.encode()

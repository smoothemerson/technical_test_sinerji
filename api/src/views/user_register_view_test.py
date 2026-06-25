from pytest import raises

from src.controllers.interfaces.user_register import UserRegisterInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from .user_register_view import UserRegisterView


class MockController(UserRegisterInterface):
    def registry(self, nome: str, email: str, password: str) -> dict:
        return {"type": "User", "nome": nome, "email": email}


def test_handle_user_register():
    body = {"nome": "João Silva", "email": "joao@email.com", "password": "senha123"}
    request = HttpRequest(body=body)

    response = UserRegisterView(MockController()).handle(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body["data"]["nome"] == "João Silva"
    assert response.body["data"]["email"] == "joao@email.com"


def test_handle_missing_nome():
    body = {"email": "joao@email.com", "password": "senha123"}
    with raises(Exception):
        UserRegisterView(MockController()).handle(HttpRequest(body=body))


def test_handle_missing_email():
    body = {"nome": "João Silva", "password": "senha123"}
    with raises(Exception):
        UserRegisterView(MockController()).handle(HttpRequest(body=body))


def test_handle_missing_password():
    body = {"nome": "João Silva", "email": "joao@email.com"}
    with raises(Exception):
        UserRegisterView(MockController()).handle(HttpRequest(body=body))


def test_handle_empty_body():
    with raises(Exception):
        UserRegisterView(MockController()).handle(HttpRequest(body={}))

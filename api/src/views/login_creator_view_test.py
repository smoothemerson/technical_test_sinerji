from pytest import raises

from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from .login_creator_view import LoginCreatorView


class MockController(LoginCreatorInterface):
    def create(self, email: str, password: str) -> dict:
        return {"access": True, "email": email, "token": "fake-token"}


def test_handle_login_creator():
    body = {"email": "joao@email.com", "password": "minhasenha"}
    response = LoginCreatorView(MockController()).handle(HttpRequest(body=body))

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]["access"] is True
    assert response.body["data"]["email"] == "joao@email.com"
    assert response.body["data"]["token"] == "fake-token"


def test_handle_missing_email():
    body = {"password": "minhasenha"}
    with raises(Exception):
        LoginCreatorView(MockController()).handle(HttpRequest(body=body))


def test_handle_missing_password():
    body = {"email": "joao@email.com"}
    with raises(Exception):
        LoginCreatorView(MockController()).handle(HttpRequest(body=body))


def test_handle_empty_body():
    with raises(Exception):
        LoginCreatorView(MockController()).handle(HttpRequest(body={}))

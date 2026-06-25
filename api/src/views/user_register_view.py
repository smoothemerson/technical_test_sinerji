from src.controllers.interfaces.user_register import UserRegisterInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from .interfaces.view_interface import ViewInterface


class UserRegisterView(ViewInterface):
    def __init__(self, controller: UserRegisterInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body or {}
        nome = body.get("nome")
        email = body.get("email")
        password = body.get("password")
        self.__validate_inputs(nome, email, password)
        assert isinstance(nome, str) and isinstance(email, str) and isinstance(password, str)

        response = self.__controller.registry(nome, email, password)
        return HttpResponse(body={"data": response}, status_code=201)

    def __validate_inputs(self, nome, email, password) -> None:
        if (
            not nome
            or not email
            or not password
            or not isinstance(nome, str)
            or not isinstance(email, str)
            or not isinstance(password, str)
        ):
            raise HttpBadRequestError("Invalid inputs")

from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from .interfaces.view_interface import ViewInterface


class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body or {}
        email = body.get("email")
        password = body.get("password")
        self.__validate_inputs(email, password)
        assert isinstance(email, str) and isinstance(password, str)

        response = self.__controller.create(email, password)
        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_inputs(self, email, password) -> None:
        if (
            not email
            or not password
            or not isinstance(email, str)
            or not isinstance(password, str)
        ):
            raise HttpBadRequestError("Invalid inputs")

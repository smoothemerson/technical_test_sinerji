from fastapi import Request

from src.drivers.jwt_handler import JwtHandler
from src.errors.types.http_unauthorized import HttpUnauthorizedError


def auth_jwt_verify(request: Request) -> dict:
    jwt_handler = JwtHandler()
    token = request.cookies.get("access_token")

    if not token:
        raise HttpUnauthorizedError("Token ausente")

    return jwt_handler.decode_jwt_token(token)

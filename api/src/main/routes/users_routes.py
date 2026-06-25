from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.errors.error_handler import handle_errors
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.user_register_composer import user_register_composer
from src.main.routes.schemas import (
    ErrorResponse,
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
)
from src.views.http_types.http_request import HttpRequest

user_router = APIRouter(prefix="/auth", tags=["Auth"])


@user_router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Dados inválidos"},
    },
)
async def register_user(body: RegisterRequest):
    try:
        http_request = HttpRequest(body=body.model_dump())
        http_response = user_register_composer().handle(http_request)
        return JSONResponse(content=http_response.body, status_code=http_response.status_code)
    except Exception as exception:
        http_response = handle_errors(exception)
        return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@user_router.post(
    "/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": ErrorResponse, "description": "Senha incorreta"},
        404: {"model": ErrorResponse, "description": "Usuário não encontrado"},
    },
)
async def login(body: LoginRequest):
    try:
        http_request = HttpRequest(body=body.model_dump())
        http_response = login_creator_composer().handle(http_request)
        return JSONResponse(content=http_response.body, status_code=http_response.status_code)
    except Exception as exception:
        http_response = handle_errors(exception)
        return JSONResponse(content=http_response.body, status_code=http_response.status_code)

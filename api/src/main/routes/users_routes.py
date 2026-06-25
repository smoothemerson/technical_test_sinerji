from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from src.errors.error_handler import handle_errors
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.user_register_composer import user_register_composer
from src.views.http_types.http_request import HttpRequest

bank_router = APIRouter(prefix="/auth")


@bank_router.post("/register")
async def register_user(request: Request):
    try:
        body = await request.json()
        http_request = HttpRequest(body=body)
        http_response = user_register_composer().handle(http_request)
        return JSONResponse(content=http_response.body, status_code=http_response.status_code)
    except Exception as exception:
        http_response = handle_errors(exception)
        return JSONResponse(content=http_response.body, status_code=http_response.status_code)


@bank_router.post("/login")
async def login(request: Request):
    try:
        body = await request.json()
        http_request = HttpRequest(body=body)
        http_response = login_creator_composer().handle(http_request)
        return JSONResponse(content=http_response.body, status_code=http_response.status_code)
    except Exception as exception:
        http_response = handle_errors(exception)
        return JSONResponse(content=http_response.body, status_code=http_response.status_code)

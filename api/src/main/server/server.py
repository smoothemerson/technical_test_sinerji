from fastapi import FastAPI

from src.main.routes.users_routes import bank_router
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

app = FastAPI()

app.include_router(bank_router)

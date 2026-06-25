from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.main.routes.users_routes import bank_router
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bank_router)

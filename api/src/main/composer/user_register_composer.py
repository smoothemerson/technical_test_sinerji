from src.controllers.user_register import UserRegister
from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
from src.views.user_register_view import UserRegisterView


def user_register_composer():
    conn = db_connection_handler.get_connection()
    assert conn is not None
    model = UserRepository(conn)
    controller = UserRegister(model)
    view = UserRegisterView(controller)
    return view

from typing import cast
from unittest.mock import Mock

from psycopg2.extensions import connection as PgConnection

from .user_repository import UserRepository


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_insert_user():
    nome = "João Silva"
    email = "joao@email.com"
    password = b"hashed_password"

    mock_connection = MockConnection()
    repo = UserRepository(cast(PgConnection, mock_connection))

    repo.insert_user(nome, email, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(nome, email, password)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (nome, email, password)
    mock_connection.commit.assert_called_once()


def test_get_user_by_email():
    email = "joao@email.com"

    mock_connection = MockConnection()
    repo = UserRepository(cast(PgConnection, mock_connection))

    repo.get_user_by_email(email)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, nome, email, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE email = %s" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (email,)
    cursor.fetchone.assert_called_once()

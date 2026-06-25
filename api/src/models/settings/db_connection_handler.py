from os import getenv
from typing import Optional

import psycopg2
from dotenv import load_dotenv

load_dotenv()

_CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password TEXT NOT NULL
);
"""


class __DbConnectionHandler:
    def __init__(self) -> None:
        self.__conn: Optional[psycopg2.extensions.connection] = None

    def connect(self) -> None:
        self.__conn = psycopg2.connect(
            user=getenv("POSTGRES_USER"),
            password=getenv("POSTGRES_PASS"),
            host=getenv("POSTGRES_HOST"),
            port=getenv("POSTGRES_PORT"),
            dbname=getenv("POSTGRES_DB"),
        )
        self.__run_migrations()

    def get_connection(self) -> Optional[psycopg2.extensions.connection]:
        return self.__conn

    def __run_migrations(self) -> None:
        with self.__conn.cursor() as cursor:
            cursor.execute(_CREATE_USERS_TABLE)
        self.__conn.commit()


db_connection_handler = __DbConnectionHandler()

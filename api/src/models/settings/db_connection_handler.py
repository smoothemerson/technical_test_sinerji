from os import getenv
from typing import Optional

import psycopg2
from dotenv import load_dotenv

load_dotenv()


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

    def get_connection(self) -> Optional[psycopg2.extensions.connection]:
        return self.__conn


db_connection_handler = __DbConnectionHandler()

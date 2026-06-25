from psycopg2.extensions import connection as PgConnection

from src.models.interface.user_repository import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: PgConnection) -> None:
        self.__conn = conn

    def insert_user(self, nome: str, email: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO users
                (nome, email, password)
            VALUES
                (%s, %s, %s)
            """,
            (nome, email, password),
        )
        self.__conn.commit()

    def get_user_by_email(self, email: str) -> tuple[int, str, str, str]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT id, nome, email, password
            FROM users
            WHERE email = %s
            """,
            (email,),
        )
        return cursor.fetchone()

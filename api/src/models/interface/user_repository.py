from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, nome: str, email: str, password: bytes) -> None:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> tuple[int, str, str, bytes]:
        pass

from abc import ABC, abstractmethod


class UserRegisterInterface(ABC):
    @abstractmethod
    def registry(self, nome: str, email: str, password: str) -> dict:
        pass

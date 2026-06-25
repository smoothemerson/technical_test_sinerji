from abc import ABC, abstractmethod


class LoginCreatorInterface(ABC):
    @abstractmethod
    def create(self, email: str, password: str) -> dict:
        pass

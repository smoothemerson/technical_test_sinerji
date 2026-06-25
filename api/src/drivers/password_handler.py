from bcrypt import checkpw, gensalt, hashpw


class PasswordHandler:
    def encrypt_password(self, password: str) -> str:
        salt = gensalt()
        hashed_password = hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    def check_password(self, password: str, hashed_password: str) -> bool:
        return checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

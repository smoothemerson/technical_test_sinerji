from bcrypt import checkpw, gensalt, hashpw


class PasswordHandler:
    def encrypt_password(self, password: str) -> bytes:
        salt = gensalt()
        hashed_password = hashpw(password.encode("utf-8"), salt)
        return hashed_password

    def check_password(self, password: str, hashed_password: bytes) -> bool:
        return checkpw(password.encode("utf-8"), hashed_password)

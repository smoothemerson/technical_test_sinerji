from datetime import datetime, timedelta, timezone

from jwt import decode, encode

from src.configs.jwt_configs import jwt_infos


class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = encode(
            payload={
                "exp": datetime.now(timezone.utc)
                + timedelta(hours=int(jwt_infos["JWT_HOURS"])),
                **body,
            },
            key=jwt_infos["KEY"],
            algorithm=jwt_infos["ALGORITHM"],
        )

        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = decode(
            token,
            key=jwt_infos["KEY"],
            algorithms=jwt_infos["ALGORITHM"],
        )

        return token_information

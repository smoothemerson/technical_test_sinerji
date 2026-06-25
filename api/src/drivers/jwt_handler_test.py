from .jwt_handler import JwtHandler


def test_jwt_handler():
    jwt_handler = JwtHandler()
    body = {"username": "olaMundo"}

    token = jwt_handler.create_jwt_token(body)
    token_informations = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_informations["username"] == body["username"]

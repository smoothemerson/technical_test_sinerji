from typing import Optional


class HttpRequest:
    def __init__(
        self,
        body: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        token_infos: Optional[dict] = None,
    ) -> None:
        self.body = body
        self.headers = headers
        self.params = params
        self.token_infos = token_infos

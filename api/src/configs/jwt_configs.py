import os

jwt_infos = {
    "KEY": os.getenv("KEY", ""),
    "ALGORITHM": os.getenv("ALGORITHM", "HS256"),
    "JWT_HOURS": os.getenv("JWT_HOURS", "10"),
}

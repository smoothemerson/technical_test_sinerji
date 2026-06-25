from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    nome: str
    email: EmailStr
    password: str


class RegisterData(BaseModel):
    type: str
    count: int
    nome: str
    email: str


class RegisterResponse(BaseModel):
    data: RegisterData


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginData(BaseModel):
    access: bool
    nome: str
    email: str


class LoginResponse(BaseModel):
    data: LoginData


class ErrorDetail(BaseModel):
    title: str
    detail: str


class ErrorResponse(BaseModel):
    errors: list[ErrorDetail]

from pydantic import BaseModel

from datetime import date

class UserInfos(BaseModel):
    nome: str
    cpf: int
    data_nascimento: date


class UserID(UserInfos):
    id: int


class UserPublic(BaseModel):
    id: int
    nome: str
    data_nascimento: date


class UserList(BaseModel):
    users: list[UserPublic]
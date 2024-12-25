from Pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str

from Pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str

from pydantic import BaseModel
import datetime


class UserCreate(BaseModel):
    username: str
    password: str


class UserFromDB(UserCreate):
    id: int
    created_at: datetime.datetime

import datetime

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    password: str


class UserFromDB(UserCreate):
    id: int
    created_at: datetime.datetime

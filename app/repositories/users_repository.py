from abc import ABC, abstractmethod
from sqlalchemy import select
from app.api.schemas.users import UserCreate, UserFromDB
from app.db.models import User


class UserRepository(ABC):
    @abstractmethod
    async def get_user(self, user: UserFromDB) -> User:
        pass

    @abstractmethod
    async def create_user(self, user: UserCreate) -> User:
        pass

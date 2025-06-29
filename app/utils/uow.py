from abc import ABC, abstractmethod

from app.db.database import async_session_maker
from app.repositories.users_repository import UserRepository


class IUnitOfWork(ABC):
    """An abstract basic class, a base pattern to apply 
    to specific repositories and transactions.
    """
    user: UserRepository

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, *args):
        pass

    @abstractmethod
    async def rollback(self):
        pass


class UnitOfWork(IUnitOfWork):
    """An implementation of the UoW pattern
    to work with databases.
    """
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.user = UserRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

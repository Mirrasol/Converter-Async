from abc import ABC, abstractmethod
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_one_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_one_by_name(self, name: str):
        raise NotImplementedError


class Repository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        query = insert(self.model).values(**data).returning(self.model)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def get_one_by_id(self, id: int):
        query = select(self.model).where(self.model.id == id)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def get_one_by_name(self, name: str):
        query = select(self.model).where(self.model.username == name)
        result = await self.session.execute(query)
        return result.scalar_one()

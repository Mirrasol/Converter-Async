from app.api.schemas.users import UserCreate, UserFromDB
from app.utils.uow import IUnitOfWork


class UserService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_user(self, user_data: UserCreate):
        user_dict = user_data.model_dump()
        async with self.uow:
            user_from_db = await self.uow.user.add_one(user_dict)
            user_result = UserFromDB.model_validate(user_from_db)
            await self.uow.commit()
            return user_result

    async def get_user(self, user_data: dict):
        async with self.uow:
            user_result = await self.uow.user.find_one(user_data)
            return user_result

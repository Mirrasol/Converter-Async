from app.api.schemas.users import UserCreate, UserFromDB
from app.utils.uow import IUnitOfWork
from app.core.security import create_token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import NoResultFound
from app.core.exception_handlers import InvalidCredentialsException, UserExistsException


class UserService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_user(self, user_data: UserCreate):
        user_dict = user_data.model_dump()
        async with self.uow:
            try:
                user_from_db = await self.uow.user.add_one(user_dict)
            except:
                raise UserExistsException
            user_result = UserFromDB.model_validate(user_from_db)
            await self.uow.commit()
            return user_result

    async def get_user_by_name(self, username: str):
        async with self.uow:
            user_result = await self.uow.user.get_one_by_name(username)
            if user_result is None:
                raise InvalidCredentialsException
            return user_result

    async def get_jwt_token(self, data: OAuth2PasswordRequestForm):
        async with self.uow:
            try:
                user_from_db = await self.uow.user.get_one_by_name(data.username)
            except (NoResultFound):
                raise InvalidCredentialsException
            if user_from_db.password != data.password:
                raise InvalidCredentialsException
            current_token = create_token({"sub": data.username})
            return current_token

from fastapi import APIRouter, Depends
from app.api.schemas.users import UserCreate
from app.services.users_service import UserService
from app.utils.uow import UnitOfWork, IUnitOfWork
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

auth_router = APIRouter(
    prefix='/auth',
    tags=['Authenticate'],
)


async def get_user_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> UserService:
    return UserService(uow)


@auth_router.post('/register/')
async def register_user(
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service),
):
    await user_service.add_user(user_data)
    return {'message': 'User added successfully'}


@auth_router.post('/login/')
async def login(
    user_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: UserService = Depends(get_user_service),
):
    current_token = await user_service.get_jwt_token(user_data)
    return {'access_token': current_token}

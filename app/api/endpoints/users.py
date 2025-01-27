from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.api.schemas.users import UserCreate, UserFromDB
from app.db.database import get_async_session
from app.db.models import User
from app.core.security import create_token

auth_router = APIRouter(
    prefix='/auth',
    tags=['Authenticate'],
)


@auth_router.post('/register/', response_model=UserFromDB)
async def register_user(user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    new_user = User(**user.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


#    @auth_router.post('/login/', response_model=UserFromDB)
#   async def login(
#       user_data: Annotated[OAuth2PasswordRequestForm, Depends()],
#       session: AsyncSession = Depends(get_async_session),
#   ):
#       user_check = await session.execute(select(user_data))
#       if user_check is None or 


#    @auth_router.post('/login/')
#    def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#        user_data_from_db = get_user(user_data.username)
#        if user_data_from_db is None or user_data.password != user_data_from_db.password:
#            raise HTTPException(
#                status_code=status.HTTP_401_UNAUTHORIZED,
#                detail='Invalid credentials',
#                headers={'WWW-Authenticate': 'Bearer'},
#            )
#        return {'access_token': create_token({'sub': user_data.username})}

#   def register_user(user: User):
#       username_to_check = user.username
#       if get_user(username_to_check):
#           raise HTTPException(
#               status_code=status.HTTP_401_UNAUTHORIZED,
#               detail='User already exists',
#               headers={'WWW-Authenticate': 'Bearer'},
#           )
#       else:
#           add_user(user)
#           return {'message': 'You have successfully registered!'}

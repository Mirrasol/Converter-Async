from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.api.schemas.users import User
from app.db.db_manager import add_user, get_user, get_users_list
from app.core.security import create_token

auth_router = APIRouter(
    prefix='/auth',
    tags=['Authenticate'],
)


@auth_router.post('/register/')
def register_user(user: User):
    username_to_check = user.username
    if get_user(username_to_check):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User already exists',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    else:
        add_user(user)
        return {'message': 'You have successfully registered!'}


@auth_router.post('/login/')
def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_data_from_db = get_user(user_data.username)
    if user_data_from_db is None or user_data.password != user_data_from_db.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return {'access_token': create_token({'sub': user_data.username})}

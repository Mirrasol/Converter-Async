from fastapi import APIRouter

auth_router = APIRouter(
    prefix='/auth',
    tags=['Authenticate'],
)


@auth_router.post('/auth/login')
def login():
    pass


@auth_router.post('/auth/register')
def register_user():
    pass

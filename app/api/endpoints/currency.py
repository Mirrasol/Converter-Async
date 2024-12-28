from fastapi import APIRouter, Depends
from app.core.security import get_user_from_token
from app.utils.external_api import get_currencies_list

currency_router = APIRouter(
    prefix='/currency',
    tags=['Currency'],
)


@currency_router.get('/list')
def show_currencies_list(user: str = Depends(get_user_from_token)):
    currencies = get_currencies_list()
    return currencies


@currency_router.post('/exchange')
def exchange_currency():
    pass

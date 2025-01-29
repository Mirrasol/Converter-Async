from fastapi import APIRouter, Depends
from app.core.security import get_user_from_token
from app.utils.external_api import get_currencies_list, get_current_exchange_rates
from app.api.schemas.currency import Currencies

currency_router = APIRouter(
    prefix='/currency',
    tags=['Currency'],
)


@currency_router.get('/list')
def show_currencies_list(user: str = Depends(get_user_from_token)):
    currencies = get_currencies_list()
    return currencies


@currency_router.post('/exchange')
def exchange_currency(currencies: Currencies, user: str = Depends(get_user_from_token)):
    result = get_current_exchange_rates(currencies)
    return result

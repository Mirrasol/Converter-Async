from fastapi import APIRouter, Depends

from app.api.schemas.currency import Currencies
from app.core.security import get_user_from_token
from app.utils.external_api import get_currencies_list, get_current_exchange_rates

currency_router = APIRouter(
    prefix='/currency',
    tags=['Currency'],
)


@currency_router.get('/list')
async def show_currencies_list(user: str = Depends(get_user_from_token)):
    currencies = await get_currencies_list()
    return currencies


@currency_router.post('/exchange')
async def exchange_currency(currencies: Currencies, user: str = Depends(get_user_from_token)):
    result = await get_current_exchange_rates(currencies)
    return result

from fastapi import APIRouter

currency_router = APIRouter(
    prefix='/currency',
    tags=['Currency'],
)


@currency_router.post('/currency/exchange')
def exchange_currency():
    pass


@currency_router.get('/currency/list')
def get_currencies_list():
    pass

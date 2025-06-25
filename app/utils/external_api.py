import aiohttp
from app.core.config import get_settings
from app.api.schemas.currency import Currencies
from app.core.exception_handlers import InvalidCurrencyException, ExternalAPIException

settings = get_settings()


async def get_currencies_list():
    async with aiohttp.ClientSession() as session:
        url = 'https://api.apilayer.com/currency_data/list'
        headers = {'apikey': settings.API_KEY}
        async with session.get(url=url, headers=headers) as response:
            if response.status != 200:
                raise ExternalAPIException(status_code=response.status)
            currencies_list = await response.json()
            return currencies_list.get('currencies')        


async def get_current_exchange_rates(currencies_data: Currencies):
    async with aiohttp.ClientSession() as session:
        url = 'https://api.apilayer.com/currency_data/convert'
        params = {
            'from': currencies_data.from_currency,
            'to': currencies_data.to_currency,
            'amount': currencies_data.amount,
        }
        headers = {'apikey': settings.API_KEY}
        async with session.get(url=url, headers=headers, params=params) as response:
            if response.status != 200:
                raise InvalidCurrencyException(status_code=response.status)
            exchange_result = await response.json()
            return exchange_result.get('result')

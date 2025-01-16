import requests
from app.core.config import get_settings
from app.api.schemas.currency import Currencies

settings = get_settings()


def get_currencies_list():
    url = 'https://api.apilayer.com/currency_data/list'
    headers = {'apikey': settings.API_KEY}
    response_data = requests.get(url, headers=headers)
    currencies_list = response_data.json().get('currencies')
    return currencies_list


def get_current_exchange_rates(currencies_data: Currencies):
    url = 'https://api.apilayer.com/currency_data/convert'
    params = {
        'from': currencies_data.from_currency,
        'to': currencies_data.to_currency,
        'amount': currencies_data.amount,
    }
    headers = {'apikey': settings.API_KEY}
    response_data = requests.get(url, params=params, headers=headers)
    exchange_result = response_data.json().get('result')
    return exchange_result

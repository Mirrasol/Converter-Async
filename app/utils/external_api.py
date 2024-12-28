import requests
from app.core.config import get_settings

settings = get_settings()


def get_currencies_list():
    url = 'https://api.apilayer.com/currency_data/list'
    headers = {'apikey': settings.API_KEY}
    response_data = requests.get(url, headers=headers)
    currencies_list = response_data.json()['currencies']
    return currencies_list


def get_current_exchange_rates():
    pass

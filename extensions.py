import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class get_price:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/348181eb1a9b07e273a79dc5/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate'] * amount

        return total_base



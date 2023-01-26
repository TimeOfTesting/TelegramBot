import requests
import json
from keys import keys

class APIException(Exception):
    pass
class PriceConverter:
    @staticmethod
    def get_price(quote: float, base: float, amound: float):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        quote_tiker = keys[quote]
        base_tiker = keys[base]

        try:
            quote_tiker == keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')

        try:
            amound == float(amound)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amound}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')
        total_base = round(float(json.loads(r.content)[keys[base]]) * float(amound), 2)
        return total_base
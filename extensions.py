import json
import requests
from config import keys
import telebot

class ConvertionException(Exception):
    pass

# #Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и возвращает нужную сумму в валюте:
# - имя валюты, цену на которую надо узнать, — base;
# - имя валюты, цену в которой надо узнать, — quote;
# - количество переводимой валюты — amount.
class Convertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты:\n {base}!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту: \n{quote}!")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту: \n{base}!")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]

        return total_base







        # r = requests.get(f"https://api.exchangeratesapi.io/latest?base={base_key}&symbols={quote_key}")
        # resp = json.loads(r.content)
        # new_price = resp['rates'][quote_key] * amount
        # new_price = round(new_price, 3)
        # message = f"Цена {amount} {base} в {quote} : {new_price}"
        # return message

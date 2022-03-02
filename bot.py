import telebot
from config import keys, TOKEN
from extensions import ConvertionException, Convertor

bot = telebot.TeleBot(TOKEN)

# "Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать>
# имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>."

@bot.message_handler(commands=['start', 'help'])
def help_welcome(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\
\n<имя валюты, цену на которую надо узнать>  \
\n<в какую валюту перевести> \
\n<количество переводимой валюты>\
\nУвидеть список доступных валют можно по команде:/values\
\n <Пример запроса: "доллар рубль 1">'
    bot.reply_to(message, text)

# При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)
"""
- имя валюты, цену на которую надо узнать, — base;
- имя валюты, цену в которой надо узнать, — quote;
- количество переводимой валюты — amount.
"""

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
       values = message.text.split(' ')

       if len(values) != 3:
          raise ConvertionException('Слишком много параметров!')

       quote, base, amount = values
       total_base = Convertor.get_price(quote, base, amount)

    except ConvertionException as e:
         bot.reply_to(message, f"Ошибка пользователя:\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду:\n{e}")
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.infinity_polling()
# Telegram Currency Converter Bot

### Описание
**Telegram Currency Converter Bot** — это телеграм-бот, который позволяет пользователям быстро узнавать курс валют на заданное количество. Бот поддерживает три основных валюты: евро, доллар и рубль. Пользователь отправляет запрос в виде: `<имя валюты, цену которой он хочет узнать> <имя валюты, в которой он хочет узнать цену первой валюты> <количество первой валюты>`, а бот отвечает актуальной стоимостью запрашиваемой валюты. Также бот поддерживает команды `/start`, `/help` и `/values` для получения инструкций и доступных валют.

### Функционал
- Получение цены на указанное количество валюты по запросу.
- Поддержка основных валют: евро, доллар и рубль.
- Команды `/start` и `/help` для вывода инструкций по работе с ботом.
- Команда `/values` для вывода всех доступных валют.
- Обработка пользовательских ошибок и выдача пояснений в случае некорректного ввода.
- Логирование запросов и ошибок для отладки.

### Используемые технологии
- **Python 3.9+**
- **PyTelegramBotAPI** — библиотека для взаимодействия с Telegram API.
- **Requests** — библиотека для отправки HTTP-запросов к стороннему API.
- **JSON** — библиотека для парсинга данных.
- **Custom Exceptions** — для обработки ошибок ввода пользователем.


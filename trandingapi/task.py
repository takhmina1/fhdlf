# import requests
# from celery import shared_task

# @shared_task
# def update_trading_data():
#     url = 'https://api.binance.com/api/v3/ticker/bookTicker'
#     response = requests.get(url)
#     data = response.json()

#     if 'symbols' in data:
#         symbols = [symbol_data['symbol'] for symbol_data in data['symbols']]
#         print("Список актуальных криптовалют на Binance:")
#         print(symbols)
#     else:
#         print("Не удалось получить данные с Binance API")

#     # Дополнительные действия с данными, например, сохранение в базу данных или отправка на другой сервис


# a = update_trading_data()
# print(a)




# import requests
# from celery import shared_task

# @shared_task
# def get_binance_symbols():
#     url = 'https://api.binance.com/api/v3/exchangeInfo'
#     response = requests.get(url)
#     data = response.json()

#     if 'symbols' in data:
#         symbols = [symbol_data['symbol'] for symbol_data in data['symbols']]
#         return symbols
#     else:
#         print("Failed to retrieve symbols from Binance API")
#         return []

# # Пример использования
# symbols = get_binance_symbols()
# print("Список актуальных криптовалют на Binance:")
# print(symbols)





# from celery import shared_task

# @shared_task
# def update_trading_data():
#     url = 'https://api.binance.com/api/v3/ticker/bookTicker'
#     response = requests.get(url)
#     data = response.json()

#     if data:
#         print("Список актуальных криптовалют на Binance:")
#         for symbol_data in data:
#             print("Символ:", symbol_data['symbol'])
#             print("Цена покупки (bidPrice):", symbol_data['bidPrice'])
#             print("Количество покупки (bidQty):", symbol_data['bidQty'])
#             print("Цена продажи (askPrice):", symbol_data['askPrice'])
#             print("Количество продажи (askQty):", symbol_data['askQty'])
#             print()
#     else:
#         print("Не удалось получить данные с Binance API")
#         return []

# a = update_trading_data()







# from .models import CryptocurrencyQuote

# @shared_task
# def update_trading_data():
#     url = 'https://api.binance.com/api/v3/ticker/bookTicker'
#     response = requests.get(url)
#     data = response.json()

#     if data:
#         for symbol_data in data:
#             symbol = symbol_data['symbol']
#             bid_price = symbol_data['bidPrice']
#             bid_qty = symbol_data['bidQty']
#             ask_price = symbol_data['askPrice']
#             ask_qty = symbol_data['askQty']
            
#             # Сохранение данных в базу данных
#             CryptocurrencyQuote.objects.update_or_create(
#                 symbol=symbol,
#                 defaults={
#                     'bid_price': bid_price,
#                     'bid_qty': bid_qty,
#                     'ask_price': ask_price,
#                     'ask_qty': ask_qty
#                 }
#             )
#     else:
#         print("Не удалось получить данные с Binance API")









# from celery import shared_task
# from .models import CryptocurrencyQuote
# import requests

# @shared_task
# def update_trading_data():
#     url = 'https://api.binance.com/api/v3/ticker/bookTicker'
#     response = requests.get(url)
#     data = response.json()

#     if data:
#         for symbol_data in data:
#             symbol = symbol_data['symbol']
#             bid_price = symbol_data['bidPrice']
#             bid_qty = symbol_data['bidQty']
#             ask_price = symbol_data['askPrice']
#             ask_qty = symbol_data['askQty']
            
#             # Сохранение данных в базу данных
#             CryptocurrencyQuote.objects.update_or_create(
#                 symbol=symbol,
#                 defaults={
#                     'bid_price': bid_price,
#                     'bid_qty': bid_qty,
#                     'ask_price': ask_price,
#                     'ask_qty': ask_qty
#                 }
#             )
#     else:
#         print("Не удалось получить данные с Binance API")

# @shared_task
# def update_trading_data_periodic():
#     update_trading_data.delay()









# # tradingapi/tasks.py
# from celery import shared_task
# import requests

# @shared_task
# def fetch_binance_data():
#     binance_api_url = 'https://api.binance.com/api/v3/ticker/bookTicker'
#     # Выполнение запроса к API Binance и обработка данных здесь
#     response = requests.get(binance_api_url)
#     data = response.json()
#     # Обработка полученных данных

#     return data
    






import requests
from celery import shared_task

# @shared_task
# def update_fiat_data():
#     # Получаем данные о фиатных валютах из другого API и сохраняем их в базе данных
#     fiats_data = requests.get('https://api.binance.com/api/v3/ticker/bookTicker').json()
#     for fiat in fiats_data:
#         symbol = fiat['symbol']
#         price = fiat['askPrice']
#         FiatCurrency.objects.update_or_create(symbol=symbol, defaults={'price': price})





# tradingapi/tasks.py
@shared_task
def update_fiat_data():
    cryptos_data = requests.get('https://api.binance.com/api/v3/ticker/bookTicker').json()
    for crypto in cryptos_data:
        symbol = crypto['symbol']
        price = crypto['askPrice']
        Cryptocurrency.objects.update_or_create(symbol=symbol, defaults={'price': price})

    return cryptos_data 
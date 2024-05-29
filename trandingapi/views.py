# tradingapi/views.py

# from .models import TriggeredMessage
# from .tasks import fetch_binance_data

# def trigger_binance_data(request):
#     message = 'Task has been triggered successfully'
#     TriggeredMessage.objects.create(message=message)
#     fetch_binance_data.delay()
    #     return JsonResponse({'message': message})




from django.http import JsonResponse
from .task import *

# def update_fiat_currencies(request):
#         update_fiat_data.delay()
#         return JsonResponse({'message': 'Fiat currency data update task has been triggered successfully'})









# # tradingapi/views.py
from django.http import JsonResponse
from .models import FiatCurrency

# from .tasks import update_fiat_data

def update_fiat_currencies(request):
    # Выполняем задачу обновления данных фиатных валют
    update_fiat_data.delay()
    
    # Здесь вы должны получить актуальные данные из вашей базы данных или API,
    # чтобы отобразить их в JSON-ответе.
    # Предположим, что у вас есть модель FiatCurrency для хранения данных о фиатных валютах.
    # Вам нужно получить эти данные из базы данных и создать список словарей,
    # содержащих информацию о каждой фиатной валюте.
    fiat_currencies = list(FiatCurrency.objects.all().values())
    
    # Возвращаем JSON-ответ с данными о фиатных валютах
    return JsonResponse({'fiat_currencies': fiat_currencies})

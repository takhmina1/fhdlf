# tradingapi/urls.py
from django.urls import path
from .views import update_fiat_currencies  # Исправленный импорт

urlpatterns = [
    path('update-fiat-currencies/', update_fiat_currencies, name='update_fiat_currencies'),
    # Другие URL-адреса вашего приложения
]

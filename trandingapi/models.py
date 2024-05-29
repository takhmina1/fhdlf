from django.db import models

# class CryptocurrencyQuote(models.Model):
#     symbol = models.CharField(max_length=50, unique=True)
#     bid_price = models.DecimalField(max_digits=20, decimal_places=10)
#     bid_qty = models.DecimalField(max_digits=20, decimal_places=10)
#     ask_price = models.DecimalField(max_digits=20, decimal_places=10)
#     ask_qty = models.DecimalField(max_digits=20, decimal_places=10)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.symbol

#     class Meta:
#         verbose_name = 'Cryptocurrency Quote'
#         verbose_name_plural = 'Cryptocurrency Quotes'


# # tradingapi/models.py
# from django.db import models

# class TriggeredMessage(models.Model):
#     message = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.message




# tradingapi/models.py
from django.db import models

class FiatCurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.symbol
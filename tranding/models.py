from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext_lazy as _


class Bank(models.Model):
    name = models.CharField(max_length=100)
    api_url = models.URLField()
    exchange_rate_to_usd = models.DecimalField(max_digits=20, decimal_places=10, default=0)


    def __str__(self):
        return self.name

    def clean(self):
        # Проверяем, что обменный курс не отрицательный
        if self.exchange_rate_to_usd < 0:
            raise ValidationError("Exchange rate cannot be negative.")

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"



class BankCredentials(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True, null=True)  
    password = models.CharField(max_length=100, blank=True, null=True)  


    def __str__(self):
        return f"{self.bank} - API Credentials"


    def clean(self):
        # Проверяем, что оба username и password указаны либо оба отсутствуют
        if bool(self.username) != bool(self.password):
            raise ValidationError("Both username and password must be provided or both should be empty.")

    class Meta:
        verbose_name = "Bank Credentials"
        verbose_name_plural = "Bank Credentials"



class FiatWallet(models.Model):
    fiat_currency = models.ForeignKey(Bank, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=10, default=0)


    def __str__(self):
        return f"Wallet for {self.fiat_currency}: {self.balance}"


    # def clean(self):
    #     # Проверяем, что баланс положителен
    #     if self.balance < 0:
    #         raise ValidationError("Balance cannot be negative.")

    class Meta:
        verbose_name = "Fiat Wallet"
        verbose_name_plural = "Fiat Wallets"



class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    api_url = models.URLField()


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Cryptocurrency"
        verbose_name_plural = "Cryptocurrencies"



    # def clean(self):
    #     # Проверяем символ криптовалюты на допустимые символы
    #     if not re.match(r'^[a-zA-Z0-9]+$', self.symbol):
    #         raise ValidationError("Symbol can only contain letters and numbers.")




class CryptoCurrencyCredentials(models.Model):
    cryptocurrency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=100, blank=True, null=True)
    api_key = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)  
    password = models.CharField(max_length=100, blank=True, null=True) 


    def __str__(self):
        return f"{self.cryptocurrency} - API Credentials"


    class Meta:
        verbose_name = "Crypto Currency Credentials"
        verbose_name_plural = "Crypto Currency Credentials" 


    # def clean(self):
    #     # Проверка, что secret_key и api_key не могут быть оба пустыми
    #     if not self.secret_key and not self.api_key:
    #         raise ValidationError("At least one of secret_key or api_key must be provided.")




class CryptoWallet(models.Model):
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=20, decimal_places=10, default=0)


    def __str__(self):
        return f"Wallet for {self.cryptocurrency}: {self.balance}"


    def clean(self):
        # Проверка длины адреса кошелька
        if len(self.address) != 100:
            raise ValidationError("Address length must be 100 characters.")


class Transaction(models.Model):
    sender_crypto_wallet = models.ForeignKey(
        CryptoWallet, related_name='sender_crypto_wallet',
        on_delete=models.CASCADE
    )
    receiver_crypto_wallet = models.ForeignKey(
        CryptoWallet, related_name='receiver_crypto_wallet',
        on_delete=models.CASCADE
    )
    sender_fiat_wallet = models.ForeignKey(
        FiatWallet, related_name='sender_fiat_wallet',
        on_delete=models.CASCADE, null=True, blank=True
    )
    receiver_fiat_wallet = models.ForeignKey(
        FiatWallet, related_name='receiver_fiat_wallet',
        on_delete=models.CASCADE, null=True, blank=True
    )
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    commission = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.amount} from {self.sender_crypto_wallet} to {self.receiver_crypto_wallet}"

    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ["-timestamp"]


    def clean(self):
        # Проверка суммы транзакции
        if self.amount <= 0:
            raise ValidationError("Transaction amount must be greater than zero.")

        # Проверка суммы комиссии
        if self.commission < 0:
            raise ValidationError("Commission must be non-negative.")

        # Проверка типа транзакции (криптокошелек к криптокошельку или фиатный к фиатному)
        if not (self.sender_crypto_wallet_id and self.receiver_crypto_wallet_id) and not (self.sender_fiat_wallet_id and self.receiver_fiat_wallet_id):
            raise ValidationError("Transaction must be either crypto to crypto or fiat to fiat.")




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    has_orders = models.BooleanField(default=True)  # Для отображения раздела "Мои заявки"
    has_payouts = models.BooleanField(default=False)  # Для отображения раздела "Выплаты"
    has_referral_program = models.BooleanField(default=False)  # Для отображения раздела "Реферальная программа"
    has_promo_codes = models.BooleanField(default=False)  # Для отображения раздела "Мои промокоды"
    has_discounts = models.BooleanField(default=False)  # Для отображения раздела "Скидки"
    has_settings = models.BooleanField(default=True)  # Для отображения раздела "Настройки"


    def __str__(self):
        return f"Profile for {self.user.username}"


    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"



class OperationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ссылка на пользователя, который совершил операцию
    operation_type = models.CharField(max_length=100)  # Тип операции (например, "Вход в систему", "Создание записи" и т. д.)
    timestamp = models.DateTimeField(auto_now_add=True)  # Время совершения операции
    description = models.TextField(blank=True, null=True)  # Дополнительное поле для описания операции

    def clean(self):
        # Пример валидации для поля operation_type
        if not self.operation_type:
            raise ValidationError(_('Operation type cannot be empty'))

    def __str__(self):
        """Строковое представление объекта OperationLog."""
        return f"{self.operation_type} by {self.user.username} at {self.timestamp}"

    class Meta:
        verbose_name = _("Operation Log")
        verbose_name_plural = _("Operation Logs")





class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    from_currency = models.CharField(max_length=100)
    from_amount = models.DecimalField(max_digits=20, decimal_places=10)
    to_currency = models.CharField(max_length=100)
    to_amount = models.DecimalField(max_digits=20, decimal_places=10)
    status = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.date}"

class OrderStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



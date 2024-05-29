from rest_framework import serializers
from .models import Bank, BankCredentials, FiatWallet, Cryptocurrency, CryptoCurrencyCredentials, CryptoWallet, Transaction, UserProfile, OperationLog


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class BankCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCredentials
        fields = '__all__'


class FiatWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiatWallet
        fields = '__all__'


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'


class CryptoCurrencyCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrencyCredentials
        fields = '__all__'


class CryptoWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoWallet
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    # Дополнительные поля для представления адресов криптокошельков отправителя и получателя
    sender_crypto_wallet_address = serializers.CharField(source='sender_crypto_wallet.address', read_only=True)
    receiver_crypto_wallet_address = serializers.CharField(source='receiver_crypto_wallet.address', read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        """
        Проверка валидности транзакции.
        """
        # Проверка наличия достаточного баланса на счете отправителя
        sender_wallet = data['sender_crypto_wallet']
        amount = data['amount']
        if sender_wallet.balance < amount:
            raise serializers.ValidationError("Недостаточно средств на счете отправителя.")
        return data

    def to_representation(self, instance):
        """
        Кастомная сериализация объекта транзакции.
        """
        representation = super().to_representation(instance)
        # Добавление кастомного поля с отформатированной суммой транзакции
        representation['amount_formatted'] = "{:.2f}".format(instance.amount)
        return representation



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        

    # def validate_phone_number(self, value):
    #     """
    #     Проверка валидности номера телефона.
    #     """
    #     if not value:
    #         raise serializers.ValidationError("Номер телефона не может быть пустым.")
    #     # Добавьте здесь дополнительные проверки валидности номера телефона, если необходимо
    #     return value



class OperationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationLog
        fields = '__all__'  # Включаем все поля модели в сериализацию

    def validate(self, data):
        """
        Проверка валидности данных операционного журнала.
        Можно добавить дополнительные проверки валидности данных здесь.
        """
        # Пример: Проверяем, что поле operation_type не пустое
        if not data.get('operation_type'):
            raise serializers.ValidationError("Тип операции не может быть пустым.")
        return data

    def to_representation(self, instance):
        """
        Кастомная сериализация объекта операционного журнала.
        Можно кастомизировать представление объекта перед его сериализацией здесь.
        """
        representation = super().to_representation(instance)
        # Пример: Добавляем кастомное поле, содержащее строковое представление даты и времени
        representation['timestamp_str'] = instance.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return representation

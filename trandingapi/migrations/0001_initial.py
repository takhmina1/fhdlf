# Generated by Django 5.0.6 on 2024-05-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptocurrencyQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50, unique=True)),
                ('bid_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('bid_qty', models.DecimalField(decimal_places=10, max_digits=20)),
                ('ask_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('ask_qty', models.DecimalField(decimal_places=10, max_digits=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cryptocurrency Quote',
                'verbose_name_plural': 'Cryptocurrency Quotes',
            },
        ),
    ]

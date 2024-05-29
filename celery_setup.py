# import os
# from celery import Celery

# # Указываем Django settings модуль для Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onemoment.settings')

# # Создаем экземпляр Celery
# app = Celery('onemoment')

# # Загружаем конфигурацию из настроек Django
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Автоматически находим и регистрируем задачи из приложений Django
# app.autodiscover_tasks()


# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onemoment.settings')

# app = Celery('onemoment')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()



# # celery_setup.py
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onemoment.settings')

app = Celery('tradingapi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



# # celery.py

# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onemoment.settings')

# app = Celery('onemoment')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# # Установите новый параметр broker_connection_retry_on_startup на True
# app.conf.broker_connection_retry_on_startup = True

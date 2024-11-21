# dfrsite/dfrsite/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установка настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dfrsite.settings')

app = Celery('dfrsite')

# Загрузка конфигурации из settings.py с префиксом 'CELERY_'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач (tasks.py) в установленных приложениях
app.autodiscover_tasks()

# applicationvault_main/celery.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'applicationvault_main.settings')

app = Celery('applicationvault')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

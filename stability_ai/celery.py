
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stability_ai.settings')
app = Celery('stability_ai')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
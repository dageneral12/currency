from celery import app as celery_app, Celery
import os

__all__ = ('celery_app',)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

app = Celery('currency_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

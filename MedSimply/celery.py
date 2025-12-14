import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MedSimply.settings')

app = Celery('MedSimply')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.autodiscover_tasks()

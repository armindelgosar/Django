from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')
app = Celery('Yektanet')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-1-hour-clicks': {
        'task': 'advertiser_management.tasks.count_total_clicks_per_hour',
        'schedule': crontab(hour='*/1'),
    },
    'every-1-hour-views': {
        'task': 'advertiser_management.tasks.count_total_views_per_hour',
        'schedule': crontab(hour='*/1'),
    },
    'every-1-day-clicks': {
        'task': 'advertiser_management.tasks.count_total_clicks_per_day',
        'schedule': crontab(hour='*/24'),
    },
    'every-1-day-views': {
        'task': 'advertiser_management.tasks.count_total_views_per_day',
        'schedule': crontab(hour='*/24'),
    }
}
app.autodiscover_tasks()

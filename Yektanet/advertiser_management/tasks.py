from __future__ import absolute_import, unicode_literals

from celery import Celery
from .models import Ad

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def count_total_views_per_hour():
    list1 = Ad.objects.all()
    for ad in list1:
        ad.make_hourly_views()


@app.task
def count_total_clicks_per_hour():
    list1 = Ad.objects.all()
    for ad in list1:
        ad.make_hourly_clicks()


@app.task
def count_total_views_per_day():
    list1 = Ad.objects.all()
    for ad in list1:
        ad.make_daily_views()


@app.task
def count_total_clicks_per_day():
    list1 = Ad.objects.all()
    for ad in list1:
        ad.make_daily_clicks()

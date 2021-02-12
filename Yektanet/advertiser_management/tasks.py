from __future__ import absolute_import, unicode_literals

from celery import Celery
from .models import Ad

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def count_total_views_per_hour():
    list1 = Ad.objects.all()
    dict = {}
    for ad in list1:
        dict[ad.id] = ad.hourly_views
        ad.make_hourly_views_zero()
        ad.daily_views += ad.hourly_views
    return list1


@app.task
def count_total_clicks_per_hour():
    list1 = Ad.objects.all()
    dict = {}
    for ad in list1:
        dict[ad.id] = ad.hourly_clicks
        ad.make_hourly_clicks_zero()
        ad.daily_clicks += ad.hourly_clicks
    return list1


@app.task
def count_total_views_per_day():
    list1 = Ad.objects.all()
    dict = {}
    for ad in list1:
        dict[ad.id] = ad.daily_views
        ad.make_daily_views_zero()
    return list1


@app.task
def count_total_clicks_per_day():
    list1 = Ad.objects.all()
    dict = {}
    for ad in list1:
        dict[ad.id] = ad.daily_clicks
        ad.make_daily_clicks_zero()
    return list1

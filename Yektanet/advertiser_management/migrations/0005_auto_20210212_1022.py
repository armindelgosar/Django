# Generated by Django 3.1.6 on 2021-02-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0004_createadview'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='daily_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ad',
            name='daily_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ad',
            name='hourly_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ad',
            name='hourly_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='advertiser',
            name='daily_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='advertiser',
            name='daily_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='advertiser',
            name='hourly_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='advertiser',
            name='hourly_views',
            field=models.IntegerField(default=0),
        ),
    ]

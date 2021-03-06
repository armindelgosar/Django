# Generated by Django 3.1.6 on 2021-02-05 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0002_auto_20210205_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='views',
        ),
        migrations.AlterField(
            model_name='ad',
            name='approve',
            field=models.CharField(choices=[('a', 'APPROVED'), ('d', 'Disapproved'), ('n', 'Not checked')], default='n', max_length=1),
        ),
        migrations.AlterField(
            model_name='click',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='view',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

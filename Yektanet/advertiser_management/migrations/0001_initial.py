# Generated by Django 3.1.5 on 2021-02-02 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('clicks', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('clicks', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.advertiser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

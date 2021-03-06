# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-05 01:53
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict_app', '0002_auto_20171005_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(null=True, upload_to='sheets/%Y/%m/%d')),
                ('weather', models.CharField(choices=[('Use', 'Using weather data'), ('Not', 'Not using weather data')], max_length=5)),
                ('timestep', models.CharField(choices=[('year', 'year'), ('month', 'month'), ('week', 'week'), ('day', 'day')], max_length=10)),
                ('result', django.contrib.postgres.fields.jsonb.JSONField(default='{"result":"Not Yet"}')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='weather',
            field=models.CharField(choices=[('Use', 'Using weather data'), ('Use', 'Using weather data'), ('Not', 'Not using weather data')], max_length=5),
        ),
    ]

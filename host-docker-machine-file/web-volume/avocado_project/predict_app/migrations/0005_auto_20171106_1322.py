# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-06 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict_app', '0004_auto_20171106_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='palletdata',
            name='department',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='palletdata',
            name='manager',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='palletdata',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='predict_app.Company'),
        ),
        migrations.AlterField(
            model_name='palletdata',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webInfo', '0003_auto_20170802_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='filequery',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fileresults',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('passwoerd', models.CharField(max_length=100, null=True)),
                ('mail', models.EmailField(max_length=254)),
                ('n_targeta', models.PositiveIntegerField()),
                ('n_secret', models.PositiveSmallIntegerField()),
                ('contact_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(auto_now=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webInfo.Client')),
            ],
        ),
        migrations.CreateModel(
            name='FileQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_style', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='Query_csv/')),
                ('engine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webInfo.Engine')),
            ],
        ),
        migrations.CreateModel(
            name='FileResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_style', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='Results_csv/%Y/%m')),
                ('engine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webInfo.Engine')),
            ],
        ),
    ]

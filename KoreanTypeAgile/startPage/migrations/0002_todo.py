# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=20)),
                ('todoName', models.CharField(max_length=40)),
                ('todoContents', models.CharField(max_length=40)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
            ],
        ),
    ]
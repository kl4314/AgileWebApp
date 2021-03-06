# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brainstorm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=40)),
                ('ideas', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=40)),
                ('issue_name', models.CharField(max_length=40)),
                ('issue_contents', models.CharField(max_length=40)),
                ('person_created', models.CharField(max_length=40)),
                ('commit', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=40)),
                ('project_leader', models.CharField(default='', max_length=40)),
                ('project_member', models.CharField(default='', max_length=40)),
                ('project_contents', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=40)),
                ('todoName', models.CharField(default='', max_length=40)),
                ('todoContents', models.CharField(default='', max_length=40)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('todo', models.BooleanField(default=True)),
                ('do', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('progress', models.FloatField(default=0.0)),
                ('person_created', models.CharField(default='', max_length=40)),
                ('performer', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(default=' ', max_length=40)),
            ],
        ),
    ]

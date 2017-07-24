# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startPage', '0002_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userPassword',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userId',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-13 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20160908_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email_verification_code',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
        migrations.AddField(
            model_name='person',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
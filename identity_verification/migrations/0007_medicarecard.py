# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-09 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity_verification', '0006_auto_20160908_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicareCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('reference_number', models.CharField(blank=True, max_length=16)),
                ('expiry_date', models.DateField(null=True)),
                ('colour', models.CharField(max_length=16)),
            ],
        ),
    ]

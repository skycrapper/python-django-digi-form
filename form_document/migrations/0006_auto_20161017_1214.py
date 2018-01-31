# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-17 01:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_document', '0005_formdocumentlink_receiver_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentsignature',
            old_name='signer_person',
            new_name='person',
        ),
        migrations.RemoveField(
            model_name='documentsignature',
            name='is_witnessed',
        ),
        migrations.RemoveField(
            model_name='documentsignature',
            name='require_witness',
        ),
        migrations.RemoveField(
            model_name='documentsignature',
            name='witness_person',
        ),
    ]
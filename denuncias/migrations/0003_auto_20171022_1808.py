# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-22 21:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0002_auto_20171022_0727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='denuncia',
            old_name='denuncedDate',
            new_name='denouncedDate',
        ),
    ]

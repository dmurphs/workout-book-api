# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170605_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liftentry',
            name='entry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='runentry',
            name='entry_date',
            field=models.DateField(),
        ),
    ]

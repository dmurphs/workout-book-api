# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-11 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20170719_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='weight',
            field=models.SmallIntegerField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_queue', '0004_auto_20171127_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventqueuemodel',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Opened'), (1, 'Closed'), (2, 'Cancelled')], default=0),
        ),
    ]

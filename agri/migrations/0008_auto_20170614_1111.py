# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0007_auto_20170614_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalregistraion',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='rentalregistraion',
            name='kebele',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='rentalregistraion',
            name='phone_no_2',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]

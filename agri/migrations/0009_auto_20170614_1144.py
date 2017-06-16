# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0008_auto_20170614_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalregistraion',
            name='rental_type',
            field=models.CharField(max_length=20, choices=[('Person', 'person'), ('Organization', 'organization')]),
        ),
    ]

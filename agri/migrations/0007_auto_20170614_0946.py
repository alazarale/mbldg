# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0006_rentalregistraion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalregistraion',
            name='rental_type',
            field=models.CharField(max_length=20),
        ),
    ]

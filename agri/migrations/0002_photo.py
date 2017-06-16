# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('category', models.CharField(max_length=30, choices=[('Commercial building', 'commercial_building'), ('Dairy farm', 'dairy_farm'), ('Farm', 'farm'), ('Poultry', 'poultry')])),
                ('description', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='gallery/image/%Y/%m')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0005_auto_20160912_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalRegistraion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('rental_type', models.BooleanField()),
                ('region', models.CharField(max_length=30)),
                ('zone', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('kebele', models.CharField(max_length=30)),
                ('phone_no_1', models.CharField(max_length=10)),
                ('phone_no_2', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('floor', models.CharField(choices=[('Under Ground FLoor', 'under_ground_floor'), ('Ground Floor', 'ground_floor'), ('First Floor', 'first_floor'), ('Second Floor', 'second_floor'), ('3rd Floor', '3rd_floor'), ('Top Floor', 'top_floor')], max_length=20)),
                ('business_type', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

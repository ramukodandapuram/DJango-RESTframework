# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Employee_Name', models.CharField(max_length=50)),
                ('Department_Name', models.CharField(max_length=50)),
            ],
        ),
    ]

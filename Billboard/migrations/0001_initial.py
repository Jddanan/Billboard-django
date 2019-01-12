# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-12 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=4000)),
                ('author', models.CharField(max_length=50)),
                ('date', models.CharField(default='2019/01/12', max_length=20)),
            ],
        ),
    ]

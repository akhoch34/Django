# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160102_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='input_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='options',
            name='summary_text',
            field=models.TextField(),
        ),
    ]

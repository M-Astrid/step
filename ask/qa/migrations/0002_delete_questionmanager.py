# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-31 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionManager',
        ),
    ]
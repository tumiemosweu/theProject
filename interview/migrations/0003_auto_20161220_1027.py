# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_auto_20161220_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(max_length=1),
        ),
    ]
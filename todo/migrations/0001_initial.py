# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-14 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('detail', models.CharField(blank=True, max_length=255, verbose_name='detail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='DATE')),
                ('memo', models.TextField(null=True)),
                ('dones', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
    ]

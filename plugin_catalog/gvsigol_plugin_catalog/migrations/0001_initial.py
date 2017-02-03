# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-01 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gvsigol_services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayerMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata_uuid', models.CharField(blank=True, max_length=100, null=True)),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_services.Layer')),
            ],
        ),
    ]

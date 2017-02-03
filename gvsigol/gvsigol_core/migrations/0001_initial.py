# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-01 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gvsigol_services', '0001_initial'),
        ('gvsigol_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, default='/gvsigonline/static/img/no_project.png', null=True, upload_to='images')),
                ('center_lat', models.CharField(max_length=100)),
                ('center_lon', models.CharField(max_length=100)),
                ('zoom', models.IntegerField(default=10)),
                ('extent', models.CharField(max_length=250)),
                ('toc_order', models.TextField(blank=True, null=True)),
                ('created_by', models.CharField(max_length=100)),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLayerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layer_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_services.LayerGroup')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_core.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_core.Project')),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvsigol_auth.UserGroup')),
            ],
        ),
    ]

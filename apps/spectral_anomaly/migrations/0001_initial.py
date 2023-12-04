# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2021-01-26 10:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dc_algorithm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpectralAnomalyTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('execution_start', models.DateTimeField(default=datetime.datetime.now, verbose_name='execution_start')),
                ('execution_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='execution_end')),
                ('area_id', models.CharField(max_length=100)),
                ('time_start', models.DateField(verbose_name='time_start')),
                ('time_end', models.DateField(verbose_name='time_end')),
                ('latitude_min', models.FloatField()),
                ('latitude_max', models.FloatField()),
                ('longitude_min', models.FloatField()),
                ('longitude_max', models.FloatField()),
                ('pixel_drill_task', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('pixel_count', models.IntegerField(default=0)),
                ('clean_pixel_count', models.IntegerField(default=0)),
                ('percentage_clean_pixels', models.FloatField(default=0)),
                ('acquisition_list', models.CharField(default='', max_length=100000)),
                ('clean_pixels_per_acquisition', models.CharField(default='', max_length=100000)),
                ('clean_pixel_percentages_per_acquisition', models.CharField(default='', max_length=100000)),
                ('status', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=100)),
                ('scenes_processed', models.IntegerField(default=0)),
                ('total_scenes', models.IntegerField(default=0)),
                ('result_path', models.CharField(default='', max_length=250)),
                ('baseline_time_start', models.DateField(default=datetime.datetime.now, verbose_name='baseline_time_start')),
                ('baseline_time_end', models.DateField(default=datetime.datetime.now, verbose_name='baseline_time_end')),
                ('analysis_time_start', models.DateField(default=datetime.datetime.now, verbose_name='analysis_time_start')),
                ('analysis_time_end', models.DateField(default=datetime.datetime.now, verbose_name='analysis_time_end')),
                ('composite_threshold_min', models.FloatField(default=-1)),
                ('composite_threshold_max', models.FloatField(default=1)),
                ('change_threshold_min', models.FloatField(blank=True, null=True)),
                ('change_threshold_max', models.FloatField(blank=True, null=True)),
                ('data_netcdf_path', models.CharField(default='', max_length=250)),
                ('data_path', models.CharField(default='', max_length=250)),
                ('plot_path', models.CharField(default='', max_length=250)),
                ('compositor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dc_algorithm.Compositor')),
                ('query_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spectral_anomaly.ResultType')),
                ('satellite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dc_algorithm.Satellite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ToolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=100)),
                ('image_title', models.CharField(max_length=50)),
                ('image_description', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('task_id', models.UUIDField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='spectralanomalytask',
            unique_together=set([('satellite', 'area_id', 'time_start', 'time_end', 'latitude_max', 'latitude_min', 'longitude_max', 'longitude_min', 'title', 'description', 'query_type', 'compositor', 'baseline_time_start', 'baseline_time_end', 'analysis_time_start', 'analysis_time_end', 'composite_threshold_min', 'composite_threshold_max', 'change_threshold_min', 'change_threshold_max')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2021-01-26 10:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.CharField(default='', max_length=250, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=250)),
                ('color_scale', models.CharField(blank=True, default='', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.CharField(default='', max_length=250, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=250)),
                ('latitude_min', models.FloatField(default=0)),
                ('latitude_max', models.FloatField(default=0)),
                ('longitude_min', models.FloatField(default=0)),
                ('longitude_max', models.FloatField(default=0)),
                ('thumbnail_imagery', models.CharField(default='', max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AreaProductsMap',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('product_names', models.CharField(default='', max_length=240)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dc_algorithm.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Compositor',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datacube_platform', models.CharField(help_text='This should correspond with a Data Cube platform. Combinations should be comma seperated with no spaces, e.g. LANDSAT_7,LANDSAT_8', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('date_min', models.DateField(default=datetime.date.today, verbose_name='date_min')),
                ('date_max', models.DateField(default=datetime.date.today, verbose_name='date_min')),
                ('data_min', models.FloatField(default=0, help_text='Define the minimum of the valid range of this dataset. This is used for image creation/scaling.')),
                ('data_max', models.FloatField(default=4096, help_text='Define the maximum of the valid range of this dataset. This is used for image creation/scaling.')),
                ('measurements', models.CharField(default='blue,green,red,nir,swir1,swir2,pixel_qa', help_text="Comma seperated list (no spaces) representing the list of measurements. e.g. 'red,green,blue,nir'", max_length=250)),
                ('no_data_value', models.FloatField(default=-9999, help_text='No data value to be used for all outputs/masking functionality.')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='satellite',
            unique_together=set([('datacube_platform',)]),
        ),
        migrations.AddField(
            model_name='areaproductsmap',
            name='satellite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dc_algorithm.Satellite'),
        ),
        migrations.AddField(
            model_name='area',
            name='satellites',
            field=models.ManyToManyField(to='dc_algorithm.Satellite'),
        ),
        migrations.AddField(
            model_name='application',
            name='application_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dc_algorithm.ApplicationGroup'),
        ),
        migrations.AddField(
            model_name='application',
            name='areas',
            field=models.ManyToManyField(to='dc_algorithm.Area'),
        ),
        migrations.AddField(
            model_name='application',
            name='satellites',
            field=models.ManyToManyField(to='dc_algorithm.Satellite'),
        ),
        migrations.AlterUniqueTogether(
            name='areaproductsmap',
            unique_together=set([('area', 'satellite')]),
        ),
    ]

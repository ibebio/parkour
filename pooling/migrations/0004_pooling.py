# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pooling', '0003_librarypreparationfile'),
        ('library', '0019_sample_is_converted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pooling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concentration_c1', models.FloatField(blank=True, null=True, verbose_name='Concentration C1')),
                ('concentration_c2', models.FloatField(blank=True, null=True, verbose_name='Concentration C2')),
                ('sample_volume', models.FloatField(blank=True, null=True, verbose_name='Sample Volume V1')),
                ('percentage_library', models.IntegerField(blank=True, null=True, verbose_name='% library in Pool')),
                ('volume_to_pool', models.FloatField(blank=True, null=True, verbose_name='Volume to Pool')),
                ('library', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Library', verbose_name='Library')),
                ('sample', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Sample', verbose_name='Sample')),
                ('buffer_volume', models.FloatField(blank=True, null=True, verbose_name='Buffer Volume V2')),
            ],
        ),
    ]
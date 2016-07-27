# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_load_concentration_methods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_name', models.CharField(max_length=200, verbose_name='Library Name')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('enrichment_cycles', models.IntegerField(verbose_name='No. of Enrichment Cycles')),
                ('index_reads', models.IntegerField(verbose_name='Index Reads')),
                ('index_i7', models.CharField(max_length=200, verbose_name='Index I7')),
                ('index_i5', models.CharField(max_length=200, verbose_name='Index I5')),
                ('equal_representation_nucleotides', models.BooleanField()),
                ('dna_dissolved_in', models.CharField(max_length=200, verbose_name='DNA Dissolved in')),
                ('concentration', models.FloatField(verbose_name='Concentration')),
                ('sample_volume', models.IntegerField(verbose_name='Sample Volume')),
                ('qpcr_result', models.FloatField(verbose_name='qPCR Result')),
                ('sequencing_depth', models.IntegerField(verbose_name='Sequencing Depth')),
                ('comments', models.TextField(verbose_name='Comments')),
                ('concentration_determined_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.ConcentrationMethod', verbose_name='Concentration Determined by')),
                ('index_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.IndexType', verbose_name='Index Type')),
                ('library_protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.LibraryProtocol', verbose_name='Library Protocol')),
                ('library_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.LibraryType', verbose_name='Library Type')),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Organism', verbose_name='Organism')),
                ('sequencing_run_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.SequencingRunCondition', verbose_name='Sequencing Run Condition')),
            ],
            options={
                'verbose_name_plural': 'Libraries',
                'verbose_name': 'Library',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-11 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='CostUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Cost Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Organization')),
            ],
        ),
        migrations.CreateModel(
            name='PrincipalInvestigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Organization')),
            ],
            options={
                'ordering': ['organization__name', 'name'],
                'verbose_name': 'Principal Investigator',
                'verbose_name_plural': 'Principal Investigators',
            },
        ),
        migrations.AddField(
            model_name='costunit',
            name='pi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.PrincipalInvestigator', verbose_name='Principal Investigator'),
        ),
        migrations.AddField(
            model_name='user',
            name='cost_unit',
            field=models.ManyToManyField(blank=True, to='common.CostUnit', verbose_name='Cost Unit'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='pi',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.PrincipalInvestigator', verbose_name='Principal Investigator'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterModelOptions(
            name='costunit',
            options={'ordering': ['name'], 'verbose_name': 'Cost Unit', 'verbose_name_plural': 'Cost Units'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterField(
            model_name='costunit',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Organization', verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.PrincipalInvestigator', verbose_name='Principal Investigator'),
        ),
    ]

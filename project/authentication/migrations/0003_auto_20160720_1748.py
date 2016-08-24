# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20160720_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='University',
            new_name='City',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='university',
        ),
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='city',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.City', verbose_name='город'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('male', 'мужской'), ('female', 'женский')], default=None, max_length=20, null=True, verbose_name='пол'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(default=None, max_length=20, null=True, verbose_name='номер телефона'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='faculty',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Faculty', verbose_name='факультет'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('answer', models.TextField(verbose_name='Текст статьи')),
            ],
            options={
                'verbose_name_plural': 'FAQ',
                'ordering': ['-id'],
                'verbose_name': 'FAQ',
            },
        ),
    ]

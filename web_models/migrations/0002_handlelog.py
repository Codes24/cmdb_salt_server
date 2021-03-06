# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 02:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandleLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle_type', models.CharField(blank=True, max_length=256, verbose_name='\u5904\u7406\u7c7b\u578b')),
                ('summary', models.CharField(blank=True, max_length=256, verbose_name='\u5904\u7406\u7684\u603b\u6570')),
                ('detail', models.TextField(blank=True, verbose_name='\u5904\u7406\u7684\u8be6\u7ec6\u4fe1\u606f')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.User')),
            ],
            options={
                'verbose_name': '\u65e5\u5fd7\u8bb0\u5f55',
            },
        ),
    ]

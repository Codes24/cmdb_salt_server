# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-22 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0002_cpuinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u6743\u9650\u6807\u9898')),
                ('urls', models.URLField(max_length=255, verbose_name='URL\u63a7\u5236\u6743\u9650')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u6743\u9650\u8868',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u89d2\u8272\u540d\u79f0')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('permissions', models.ManyToManyField(blank=True, to='web_models.Permission', verbose_name='\u5177\u6709\u7684\u6240\u6709\u6743\u9650')),
            ],
            options={
                'verbose_name_plural': '\u89d2\u8272\u8868',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=255, verbose_name='\u5bc6\u7801')),
                ('is_admin', models.BooleanField(verbose_name='\u662f\u5426\u4e3a\u7ba1\u7406\u5458')),
                ('email', models.EmailField(max_length=255, verbose_name='\u90ae\u7bb1')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('roles', models.ManyToManyField(blank=True, to='web_models.Role', verbose_name='\u5177\u6709\u7684\u6240\u6709\u89d2\u8272')),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
#测试表Test
class Test(models.Model):

    UserName = models.CharField(max_length=255)

    PassWord = models.CharField(max_length=255)

#测试表CpuInfo
class CpuInfo(models.Model):

    cpu_module = models.CharField(max_length=255)

    cpu_physical = models.CharField(max_length=255)

    cpu_cores = models.CharField(max_length=255)

    cpu_processor = models.CharField(max_length=255)

#用户表
class User(models.Model):

    username = models.CharField(verbose_name="用户名",max_length=255)
    password = models.CharField(verbose_name="密码",max_length=255)
    is_admin = models.BooleanField(verbose_name="是否为管理员",blank=True)
    email = models.EmailField(verbose_name="邮箱",max_length=255)
    roles = models.ManyToManyField(verbose_name="具有的所有角色",to="Role",blank=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", blank=True, auto_now=True)
    created_time = models.DateTimeField(verbose_name="创建时间",blank=True,auto_now_add=True)

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.username

#角色表
class Role(models.Model):

    name = models.CharField(verbose_name="角色名称",max_length=255)
    permissions = models.ManyToManyField(verbose_name="具有的所有权限",to="Permission",blank=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", blank=True, auto_now=True)
    created_time = models.DateTimeField(verbose_name="创建时间",blank=True,auto_now_add=True)

    class Meta:
        verbose_name_plural = "角色表"

    def __str__(self):
        return self.name

#权限表
class Permission(models.Model):

    title = models.CharField(verbose_name="权限标题",max_length=255)
    urls = models.URLField(verbose_name="URL控制权限",max_length=255)
    updated_time = models.DateTimeField(verbose_name="更新时间", blank=True, auto_now=True)
    created_time = models.DateTimeField(verbose_name="创建时间", blank=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = "权限表"

    def __str__(self):
        return self.title


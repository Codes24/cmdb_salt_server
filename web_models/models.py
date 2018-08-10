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

#设备类型表(网络设备，服务器设备，虚拟机)
class DeviceType(models.Model):

    name = models.CharField(u'类型名称',max_length=255)
    memo = models.TextField(u'备注',null=True,blank=True)

#设备状态表(运行，闲置，报废)
class DeviceStatus(models.Model):

    name = models.CharField(u'状态名称',max_length=255)
    memo = models.TextField(u'备注',null=True,blank=True)

#设备所属表(点对点，会议，CDN，个人，项目)
class Business(models.Model):

    name = models.CharField(u'业务线名称',max_length=255)
    memo = models.TextField(u'备注',null=True,blank=True)

#服务器设备型号表(DELL，HP，IBM，曙光)
class ServerModel(models.Model):

    name = models.CharField(u'服务器型号名称', max_length=255)
    memo = models.TextField(u'备注', null=True, blank=True)

#设备属性表(现网，测试网)
class Purpose(models.Model):

    name = models.CharField(u'用途表名称', max_length=255)
    memo = models.TextField(u'备注', null=True, blank=True)

#网络类型表(裸公网，NAT)
class NetworkType(models.Model):

    name = models.CharField(u'网络类型名称', max_length=255)
    memo = models.TextField(u'备注', null=True, blank=True)

#网络线路表(BGP线路，双线，三线)
class NetworkCircuit(models.Model):

    name = models.CharField(u'网络线路名称', max_length=255)
    memo = models.TextField(u'备注', null=True, blank=True)

#机房地域表(北京，上海，广州等地)
class IDCArea(models.Model):

    name = models.CharField(u'区域名称', max_length=255)
    memo = models.TextField(u'备注', null=True, blank=True)

#操作系统表(linux，windows)
class OperatingSystem(models.Model):

    name = models.CharField(u'操作系统名称', max_length=255)
    memo = models.TextField(u'备注', null=True, blank=True)



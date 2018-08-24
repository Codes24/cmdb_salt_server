# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import time

# Create your models here.
#用户表
class User(models.Model):

    username = models.CharField(verbose_name="用户名",max_length=255)
    password = models.CharField(verbose_name="密码",max_length=255)
    is_admin = models.BooleanField(verbose_name="是否为管理员",blank=True)
    email = models.EmailField(verbose_name="邮箱",max_length=255)
    roles = models.ManyToManyField(verbose_name="具有的所有角色",to="Role",blank=True)
    created_time = models.DateTimeField(verbose_name="创建时间", blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", blank=True, auto_now=True)

    class Meta:
        verbose_name = "用户表"

    def __str__(self):
        return self.username

#角色表
class Role(models.Model):

    name = models.CharField(verbose_name="角色名称",max_length=255)
    permissions = models.ManyToManyField(verbose_name="具有的所有权限",to="Permission",blank=True)
    created_time = models.DateTimeField(verbose_name="创建时间", blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", blank=True, auto_now=True)

    class Meta:
        verbose_name = "角色表"

    def __str__(self):
        return self.name

#权限表
class Permission(models.Model):

    title = models.CharField(verbose_name="权限标题",max_length=255)
    urls = models.URLField(verbose_name="URL控制权限",max_length=255)
    created_time = models.DateTimeField(verbose_name="创建时间", blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", blank=True, auto_now=True)

    class Meta:
        verbose_name = "权限表"

    def __str__(self):
        return self.title

#设备类型表(网络设备，服务器设备，虚拟机)
class DeviceType(models.Model):

    name = models.CharField(u'类型名称',max_length=255)
    memo = models.TextField(u'备注',null=True,blank=True)

#设备型号表(DELL，HP，IBM，曙光)
class DeviceModel(models.Model):

    name = models.CharField(u'设备型号名称',max_length=255)
    memo = models.TextField(u'备注',null=True,blank=True)

#设备状态表(运行，闲置，报废)
class DeviceStatus(models.Model):

    name = models.CharField(u'状态名称',max_length=255)
    memo = models.TextField(u'备注',null=True,blank=True)

#设备属性表(现网，测试网)
class DeviceAttribute(models.Model):

    name = models.CharField(u'用途表名称', max_length=255)
    memo = models.TextField(u'备注', null=True, blank=True)

#设备所属表(点对点，会议，CDN，个人，项目)
class DeviceBusiness(models.Model):

    name = models.CharField(u'业务线名称',max_length=255)
    memo = models.TextField(u'备注',null=True,blank=True)

#设备用途表(具体用途表)
class DevicePurpose(models.Model):

    name = models.CharField(u'设备用途名称',max_length=255)
    memo = models.TextField(u'备注',null=True,blank=True)

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

#合同单
class Contract(models.Model):

    sn = models.CharField(u'合同号',max_length=64,unique=True)
    name = models.CharField(u'合同名',max_length=64)
    cost = models.IntegerField(u'合同金额')
    start_date = models.DateTimeField(u'合同起始时间',blank=True)
    end_date = models.DateTimeField(u'合同结束时间',blank=True)
    license_number = models.IntegerField(u'license数量',blank=True)
    created_time = models.DateTimeField(blank=True,auto_now_add=True)
    updated_time = models.DateTimeField(blank=True,auto_now=True)
    memo = models.TextField(u'备注',blank=True)

    class Meta:
        verbose_name = '合同'

    def __unicode__(self):
        return self.name

# 存储变更的日志记录表
class HandleLog(models.Model):

    handle_type = models.CharField(u'处理类型', max_length=255, blank=True)
    summary = models.CharField(u'处理的总数', max_length=255, blank=True)
    detail = models.TextField(u'处理的详细信息',blank=True)
    creater = models.ForeignKey('User')
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, auto_now=True)
    memo = models.TextField(u'备注', blank=True)

    class Meta:
        verbose_name = '日志记录'

    def __unicode__(self):
        return self.handle_type

#设备资产表
class Asset(models.Model):

    hostname = models.CharField(u'主机名',max_length=255,unique=True,blank=False)
    device_type = models.ForeignKey('DeviceType')
    status = models.ForeignKey('DeviceStatus')
    attribute = models.ForeignKey('DeviceAttribute')
    business = models.ForeignKey('DeviceBusiness')
    purpose = models.ForeignKey('DevicePurpose')
    network_type = models.ForeignKey('NetworkType')
    network_circuit = models.ForeignKey('NetworkCircuit')
    operatingsystem = models.ForeignKey('OperatingSystem')
    bandwidth_limit = models.BooleanField(u'带宽是否有限制')
    limit_size = models.IntegerField(u'带宽限制大小')
    idcarea = models.ForeignKey('IDCArea')
    room = models.CharField(u'机房号',max_length=32,null=True,blank=True)
    cabinet_number = models.CharField(u'机柜号',max_length=32,null=True,blank=True)
    cabinet_order = models.CharField(u'机柜中序号',max_length=32,null=True,blank=True)
    contract = models.ForeignKey('Contract')
    created_time = models.DateTimeField(blank=True,auto_now_add=True)
    updated_time = models.DateTimeField(blank=True,auto_now=True)
    user = models.ForeignKey('User')
    memo = models.TextField(u'备注', null=True, blank=True)

    class Meta:
        verbose_name = '资产总表'

    def __unicode__(self):
        return self.hostname


#服务器表
class Server(models.Model):

    asset = models.ForeignKey('Asset')
    sn = models.CharField(u'SN号', max_length=64)
    manufactory = models.CharField(verbose_name=u'制造商', max_length=64, null=True, blank=True)
    model = models.CharField(u'型号', max_length=128, null=True, blank=True)
    asset_number = models.CharField(u'资产编号',max_length=64)
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, auto_now=True)
    memo = models.TextField(u'备注', blank=True)

    class Meta:
        verbose_name = '服务器'

    def __unicode__(self):
        return self.asset.hostname,self.sn

#网络设备表
class Network(models.Model):

    asset = models.ForeignKey('Asset')
    port_number = models.IntegerField(u'端口数量')
    capacity = models.IntegerField(u'吞吐能力')
    sn = models.CharField(u'SN号', max_length=64)
    manufactory = models.CharField(verbose_name=u'制造商', max_length=64, null=True, blank=True)
    model = models.CharField(u'型号', max_length=128, null=True, blank=True)
    asset_number = models.CharField(u'资产编号', max_length=64)
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, auto_now=True)
    memo = models.TextField(u'备注', blank=True)

    class Meta:
        verbose_name = '网络设备'

    def __unicode__(self):
        return self.asset.hostname, self.sn

#CPU详细信息表
class Cpu(models.Model):

    model = models.CharField(u'cpu型号',max_length=255)
    frequency = models.CharField(u'频率',max_length=255)
    physical_cores = models.CharField(u'物理核数',max_length=64)
    logic_cores = models.CharField(u'逻辑核数',max_length=64)
    hyper_threading = models.BooleanField(u'是否超线程')
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, auto_now=True)
    memo = models.TextField(u'备注', blank=True)
    server_info = models.ForeignKey('Server')

    class Meta:
        verbose_name = 'CPU'

    def __unicode__(self):
        return self.model

#内存详细信息表
class Memory(models.Model):

    total = models.IntegerField(u'内存总数')
    capacity = models.IntegerField(u'单个内存条大小')
    memory_number = models.IntegerField(u'内存条数量')
    frequency = models.IntegerField(u'内存条频率')
    slot_total = models.IntegerField(u'内存槽总数')
    slot_residue = models.IntegerField(u'内存槽剩余数量')
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, auto_now=True)
    memo = models.TextField(u'备注', blank=True)
    server_info = models.ForeignKey('Server')

    class Meta:
        verbose_name = '内存'

    def __unicode__(self):
        return self.total

#RAID详细信息表
class Raid(models.Model):

    model = models.CharField(u'Raid型号',max_length=255)
    is_onboard = models.BooleanField(u'是否板载')
    raid_group = models.IntegerField(u'Raid是0，1，5还是10')
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, auto_now=True)
    memo = models.TextField(u'备注', blank=True)
    server_info = models.ForeignKey('Server')

    class Meta:
        verbose_name = 'RAID'

    def __unicode__(self):
        return self.model

#硬盘详细信息表
class Disk(models.Model):

    model = models.CharField(u'磁盘型号', max_length=128, blank=True)
    capacity = models.IntegerField(u'硬盘容量')
    disk_number = models.IntegerField(u'硬盘数量')
    iface_type = models.CharField(u'接口类型',max_length=128,blank=True)
    slot = models.CharField(u'插槽位数量',max_length=128,blank=True)
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, auto_now=True)
    memo = models.TextField(u'备注', blank=True)
    server_info = models.ForeignKey('Server')

    class Meta:
        verbose_name = '硬盘'

    def __unicode__(self):
        return self.model

#网卡详细信息表
class Nic(models.Model):

    name = models.CharField(u'网卡名称', max_length=128, blank=True)
    model = models.CharField(u'网卡型号', max_length=128, blank=True)
    ipaddrs = models.GenericIPAddressField(u'IP地址')
    mac = models.CharField(u'网卡mac地址', max_length=128, blank=True)
    netmask = models.CharField(u'子网掩码', max_length=128, blank=True)
    gateway = models.CharField(u'网关', max_length=128, blank=True)
    dns1 = models.CharField(u'DNS1地址',max_length=128,blank=True)
    dns2 = models.CharField(u'DNS2地址',max_length=128,blank=True)
    memo = models.TextField(u'备注', blank=True)
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    updated_time = models.DateTimeField(blank=True, auto_now=True)
    server_info = models.ForeignKey('Server')

    class Meta:
        verbose_name = '网卡'

    def __unicode__(self):
        return self.name
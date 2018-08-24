# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,redirect
from django.http.response import HttpResponse
from web_models import models
from django.db import connection
from django.core import serializers
from web_manage import forms
import hashlib
import json
import urllib
# Create your views here.
#ajax测试
def ajax(request):

    if request.method == 'POST':

        print request.POST
        data={'msg':'a','bbb':'b'}
        return HttpResponse(json.dumps(data))

    else:

        return render(request, 'web_manage/../templates/backup/ajax.html')

#主页
def index(request):

    return render_to_response('web_manage/index.html')

#用户注册
def register(request):

    obj = forms.Verification()

    if request.method == "GET":

        return render(request,'web_manage/register.html',{"data":obj})

    if request.method == "POST":

        checkForm = forms.Verification(request.POST)
        checkResult = checkForm.is_valid()
        if checkResult:
            username_form = checkForm.cleaned_data.get('username')
            username_model = models.User.objects.filter(username=username_form)
            print username_model

            if username_model.exists():
                return render(request,"web_manage/register.html",{"data":obj,"username":"用户名已经存在"})
            else:
                user_table = models.User()
                user_table.username = checkForm.cleaned_data.get('username')
                user_table.password = hashlib.md5(checkForm.cleaned_data.get('password')).hexdigest()
                user_table.email = checkForm.cleaned_data.get('email')
                user_table.is_admin = 0
                user_table.save()
                return render(request,'web_manage/register_success.html')
        else:
            errorForm = checkForm.errors

    return render(request,"web_manage/register.html",{"data":obj,"errordata":checkForm.errors})

#用户登录
def login(request):

    obj = forms.login_forms()

    if request.method == 'GET':

        return render(request,"web_manage/login.html",{"data":obj})

    if request.method == 'POST':

        checkForm = forms.login_forms(request.POST)
        checkResult = checkForm.is_valid()
        if checkResult:

            username_form = checkForm.cleaned_data.get('username')
            password_form = hashlib.md5(checkForm.cleaned_data.get('password')).hexdigest()
            username_model = models.User.objects.filter(username=username_form)
            if username_model.exists():
                user_pwd_model = models.User.objects.filter(username=username_form,password=password_form)
                if user_pwd_model:
                    return render(request,'web_manage/index.html')
                else:
                    return render(request, 'web_manage/login.html', {'data': obj, 'errordata1': '用户名或密码错误'})
            else:
                return render(request,'web_manage/login.html',{'data':obj,'errordata2':'用户不存在'})
        else:
            errorForm = checkForm.errors
    return render(request, "web_manage/login.html", {"data": obj, "errordata": checkForm.errors})

#物理设备资源汇总
def physical_device_count(request):

    user = models.User.objects.all().values('id','username','password')
    user_count = models.User.objects.filter(id__gt='10').count()

    return render_to_response('web_manage/asset/asset_1/physical_device_count.html',{'data':user_count})

#虚拟设备资源汇总
#def virtual_device_count(request):

#网络设备信息
#def network_device_info(request):

#虚拟设备信息
def server_device_info(request):

    return render_to_response('web_manage/asset/asset_2/server_device_info.html')

#添加设备信息
def server_add(request):

    if request.method == 'GET':
        return render_to_response('web_manage/asset/asset_2/server_add.html')

    if request.method == 'POST':
        hostname_data = request.POST.get('hostname')
        hostname_devicetype = request.POST.get('devicetype_s')
        hostname_obj = models.Asset.objects.filter(hostname=hostname_data)
        if hostname_obj.exists():
            print 'ok'
        else:
            asset_table = models.Asset()
            asset_table.hostname = hostname_data
            asset_table.device_type_id = hostname_devicetype
            asset_table.save()
            asset_id = models.Server.objects.create(asset_id=models.Asset.objects.get(hostname=hostname_data).id)
            server_id_asset_id = models.Server.objects.filter(asset_id=models.Asset.objects.get(hostname=hostname_data))
            asset_id_s = serializers.serialize("json",server_id_asset_id)
            asset_id_json = json.loads(asset_id_s)
            asset_id_json_list = asset_id_json[0]
            asset_id_json_id = str(asset_id_json_list['pk']).decode()
            print type(asset_id_json)
            print asset_id_json_list
            print asset_id_json_id
            print type(asset_id_json_id)
            server_id = models.Cpu.objects.create(server_info_id=asset_id_json_id)
        return HttpResponse('ok')
#查询设备类型信息
def show_devicetype(request):

    if request.method == 'GET':

        devicetype_list = []
        devicetype_all = models.DeviceType.objects.all()

        for item in devicetype_all:
            devicetype_dict = {}
            devicetype_dict['id'] = item.id
            devicetype_dict['name'] = item.name
            devicetype_list.append(devicetype_dict)

        return HttpResponse(json.dumps(devicetype_list))
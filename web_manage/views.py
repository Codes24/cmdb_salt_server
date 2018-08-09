# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,redirect
from django.http.response import HttpResponse
from web_models import models
from django.db import connection
from web_manage import forms
import hashlib
import json
# Create your views here.
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

#ajax测试
def ajax(request):

    if request.method == 'POST':

        print request.POST
        data={'msg':'a','bbb':'b'}
        return HttpResponse(json.dumps(data))

    else:

        return render(request, 'web_manage/ajax.html')

#物理设备资源汇总
def physical_device_count(request):

    user = models.User.objects.all().values('id','username','password')

    return render_to_response('web_manage/asset/asset_1/physical_device_count.html',{'data':1})
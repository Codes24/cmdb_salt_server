# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render,render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
import json
import urllib
from web_models import models

# Create your views here.
def receive_server_info(request):

    server_info = request.POST.get('data')
    #将url编码的字符进行转换
    server_info = urllib.unquote(server_info)
    server_info_dict = json.loads(server_info)
    hostname = server_info_dict['hostname']
    if server_info_dict['modify'] == 0:
        pass
    else:
        asset_id = models.Asset.objects.filter(hostname=hostname)
        #将查询出来的结果类型由models.class转换为json
        asset_id_s = serializers.serialize("json",asset_id)
        asset_id_json = json.loads(asset_id_s)
        asset_id_json_list = asset_id_json[0]
        asset_id_json_dict = str(asset_id_json_list['pk']).decode()
        server_id = models.Server.objects.filter(asset_id=asset_id_json_dict)
        server_id_s = serializers.serialize("json",server_id)
        server_id_json = json.loads(server_id_s)
        server_id_json_list = server_id_json[0]
        server_id_json_dict = str(server_id_json_list['pk']).decode()
        cpu_info_list = models.Cpu.objects.filter(server_info_id=server_id_json_dict)
        for item in cpu_info_list:
            print item.memo
            for new_key,new_value in server_info_dict.items():
                if item.memo == new_key:
                    if item.model != new_value['cpu_module']:
                        item.model = new_value['cpu_module']
                        item.save()
                    else:
                        print '相等'
    return HttpResponse('123')
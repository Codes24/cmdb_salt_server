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
    server_info = urllib.unquote(server_info)
    server_info_dict = json.loads(server_info)
    print server_info_dict
    print server_info_dict['cpu']
    print type(server_info_dict)
    print type(server_info_dict['cpu'])
    hostname = server_info_dict['hostname']
    print hostname
    if server_info_dict['modify'] == 0:
        pass
    else:
        asset_id = models.Asset.objects.filter(hostname=hostname)
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
            for new_key,new_value in server_info_dict['cpu'].items():
                print new_value[0][1]
                #if item.model != new_value['model']:
                #print item.model
                #print new_value[]
                #else:
                 #   print 'no'
                  #  item.model = new_value['model']
                   # item.save()
                #print new_key,new_value
        #models.Server.objects.create(asset_id=asset_id)
        #old_cpu_list = models.Cpu.objects.filter(server__id=server_id)
        #print old_cpu_list

    return HttpResponse('123')
    '''
    try:
        method = request.method
        if method == 'POST':
            server_info = request.POST.get('data')
            server_info_dict = json.loads(server_info)
            print server_info_dict
    except Exception,e:
        print e
    
    cpu_status = server_info_dict['cpu']['modify']
    cpu_data = server_info_dict['cpu']['data']
    print cpu_data
    if cpu_status == 0:
        pass
    else:
        cpu_models = models.CpuInfo.objects.create(**cpu_data)
        cpu_models.save()
    return Response('ok')
    '''
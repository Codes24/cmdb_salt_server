# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render,render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from web_models import models

# Create your views here.
def test(request):

    return HttpResponse('ok')

#@api_view(['POST','GET'])
def receive_server_info(request):

    server_info = request.POST.get('data')
    print server_info
    '''
    server_info = server_info.encode('utf-8')
    server_info_dict = json.loads(server_info)
    print server_info_dict
    '''
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
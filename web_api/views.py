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

def receive_server_info(request):

    server_info = request.POST.get('data')
    server_info = server_info.encode('utf-8')
    server_info_dict = json.loads(server_info)
    print server_info_dict

def a(request):

    return re
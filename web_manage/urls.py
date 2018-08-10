"""cmdb_salt_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from web_manage.views import index,register,login,ajax,physical_device_count,server_device_info

urlpatterns = [
    url(r'^index/',index),
    url(r'^register/',register),
    url(r'^login/',login),
    url(r'^ajax/',ajax),
    url(r'^physical_device_count/',physical_device_count),
    url(r'^server_device_info/',server_device_info),
]

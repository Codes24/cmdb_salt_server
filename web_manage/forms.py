#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: forms.py
@time: 2018/7/12 10:35
'''
from django import forms
from django.core.validators import RegexValidator

class Verification(forms.Form):

    username = forms.CharField(
        required=True,
        max_length=15,
        min_length=6,
        widget=forms.TextInput(attrs={'class':"form-control","placeholder":u"username"}),
        validators=[RegexValidator(r'[a-zA-Z0-9_]$', '只支持数字,字母大小写和下划线', 'invalid')],
        error_messages={
            'requeried':'用户名不能为空',
            'max_length':'最大长度不得超过15个字符',
            'min_length':'最小长度不得小于6个字符'
        }
    )

    password = forms.CharField(
        required=True,
        max_length=15,
        min_length=6,
        widget=forms.widgets.PasswordInput(attrs={'class':'form-control',"placeholder":u"password"}),
        error_messages={
            'required':'密码不能为空'
        }
    )

    re_password = forms.CharField(
        required=True,
        max_length=15,
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": u"re_password"}),
        error_messages={
            'required': '密码不能为空'
        }
    )

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd != re_pwd:
            self.add_error('re_password','两次输入密码不一致')
        else:
            return self.cleaned_data

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control',"placeholder":u"email"}),
        error_messages={
            'required':'邮箱不能为空',
            'invalid':'邮箱格式不正确'
        }
    )

class login_forms(forms.Form):

    username = forms.CharField(
        required=True,
        max_length=15,
        min_length=6,
        widget=forms.TextInput(attrs={'class':"form-control","placeholder":u"username"}),
        validators=[RegexValidator(r'[a-zA-Z0-9_]$', '只支持数字,字母大小写和下划线', 'invalid')],
        error_messages={
            'requeried':'用户名不能为空',
            'max_length':'最大长度不得超过15个字符',
            'min_length':'最小长度不得小于6个字符'
        }
    )

    password = forms.CharField(
        required=True,
        max_length=15,
        min_length=6,
        widget=forms.widgets.PasswordInput(attrs={'class':'form-control',"placeholder":u"password"}),
        error_messages={
            'required':'密码不能为空'
        }
    )
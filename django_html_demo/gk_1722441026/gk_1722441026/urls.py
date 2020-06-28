'''
@Author: randolph
@Date: 2020-06-24 09:17:45
@LastEditors: randolph
@LastEditTime: 2020-06-24 18:27:26
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 
'''
"""gk_1722441026 URL Configuration

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
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from app_1722441026.views_1722441026 import index, login, redirect_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),   # 登录
    path('', redirect_login),            # 重定向
    path('index/', index, name='index'),   # 主页
]

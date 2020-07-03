'''
@Author: randolph
@Date: 2020-07-01 03:38:12
@LastEditors: randolph
@LastEditTime: 2020-07-03 10:05:53
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 
'''
from django.conf.urls import url

from apps.Information.views import ais_classmate_view

urlpatterns = [
    url(r'^ais_classmate_view/', ais_classmate_view, name='ais_classmate_view'),
]

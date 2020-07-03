'''
@Author: randolph
@Date: 2020-07-01 03:38:12
@LastEditors: randolph
@LastEditTime: 2020-07-03 10:06:27
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 
'''
from django.contrib import admin

from apps.Information.models import AisClassmate


# Register your models here.

admin.site.register(AisClassmate)

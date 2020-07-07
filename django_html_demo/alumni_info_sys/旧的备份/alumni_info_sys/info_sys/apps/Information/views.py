# -*- coding : utf-8 -*-
import json
import os
import re

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core.paginator import (EmptyPage, InvalidPage, PageNotAnInteger,
                                   Paginator)
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from apps.Information.models import *
from apps.User.models import UserProfile

# Create your views here.

TABLE_SIZE = 9                  # 注册审批页面表格行数
PAGE_SIZE = 10                  # 每页显示行数


@csrf_exempt
@transaction.atomic
@login_required(login_url="/login/")
def ais_classmate_view(request):
    current_user = request.user         # 当前登录用户
    # print(current_user)
    classmate_name = request.GET.get("classmate_name", "")
    page = int(request.GET.get("page", 1))
    keys = ""   # 搜索参数
    search = dict()
    user_profile_base = UserProfile.objects.get(auth_user=current_user)
    # print(user_profile.cla_id)        # 当前登录用户所在班级
    search["cla_id"] = str(user_profile_base.cla_id)
    keys += "cla_id=" + str(user_profile_base.cla_id) + "&"
    if classmate_name:
        search["user_real_name__contains"] = classmate_name
        keys += "user_real_name=" + classmate_name + "&"
    user_profile = UserProfile.objects.filter(**search).exclude(auth_user=current_user).order_by('-user_id')        # 排除自己
    # user_profile = UserProfile.objects.filter(**search).order_by('-user_id')
    # ais_cla = AisCla.objects.filter(**search).order_by('-id')      # 根据st_id倒序
    print("接口测试")
    # 调用自定义分页方法
    zip_obj, pages, page_obj, page, paginator = paginator_interface(user_profile, page, TABLE_SIZE)
    print({"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                               'page': page, 'paginator': paginator, 'pages': pages})
    return render(request, 'classmates.html', {"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                               'page': page, 'paginator': paginator, 'pages': pages})


@csrf_exempt
@transaction.atomic
@login_required(login_url="/login/")
def ais_msg_view(request):
    current_user = request.user         # 当前登录用户
    user_profile_base = UserProfile.objects.get(auth_user=current_user)  
      
    msg_content = request.GET.get("msg_content", "")
    page = int(request.GET.get("page", 1))
    keys = ""   # 搜索参数
    search = dict()
    search["cla_id"] = str(user_profile_base.cla_id)        # 当前登录用户所在班级 去过滤留言
    keys += "cla_id=" + str(user_profile_base.cla_id) + "&"
    if msg_content:
        search["msg_content__contains"] = msg_content
        keys += "msg_content=" + msg_content + "&"
    ais_msg = AisMsg.objects.filter(**search).order_by('-id')
    # 调用自定义分页方法
    zip_obj, pages, page_obj, page, paginator = paginator_interface(ais_msg, page, TABLE_SIZE)
    print("接口测试")
    print({"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                        'page': page, 'paginator': paginator, 'pages': pages})
    return render(request, 'msg.html', {"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                        'page': page, 'paginator': paginator, 'pages': pages})


@csrf_exempt
@login_required(login_url="/login/")
@transaction.atomic
def clean_user(request):
    if request.method == "GET":
        return HttpResponse("Nothing...")
    if request.method == "POST":
        user_real_name = request.POST.get("user_real_name", "")
        user_profile = UserProfile.objects.get(user_real_name=user_real_name)
        user_profile.cla_id = 0  # 班级清空     # ais_cla预留一个班级id为0的用来存放无班级用户
        user_profile.save()
        return HttpResponse(content="success")

@csrf_exempt
@login_required(login_url="/login/")
@transaction.atomic
def publish_msg(request):
    if request.method == "GET":
        return HttpResponse("Nothing...")
    if request.method == "POST":
        current_user = request.user         # 当前登录用户
        user_profile_base = UserProfile.objects.get(auth_user=current_user)  
        # 获得前端传过来的数据
        pub_msg_content = request.POST.get("pub_msg_content", "")
        print(pub_msg_content)
        ais_msg = AisMsg()
        ais_msg.msg_content = "各位老同学好啊"
        import datetime
        ais_msg.msg_publish_date = datetime.datetime.now()
        ais_msg.cla_id = user_profile_base.cla_id
        ais_msg.user_id = user_profile_base.user_id
        ais_msg.save()
        # user_profile = UserProfile.objects.get(auth_user=username)
        # user_profile.cla_id = 0  # 班级清空     # ais_cla预留一个班级id为0的用来存放无班级用户
        # user_profile.save()
        return HttpResponse(content="success")

@csrf_exempt
@transaction.atomic
@login_required(login_url="/login/")
def ais_cla_view(request):      
    cla_name = request.GET.get("cla_name", "")
    page = int(request.GET.get("page", 1))
    keys = ""   # 搜索参数
    search = dict()
    if cla_name:
        search["cla_name__contains"] = cla_name
        keys += "cla_name=" + cla_name + "&"
    ais_cla = AisCla.objects.filter(**search).exclude(id=0).order_by('-id')
    # 调用自定义分页方法
    zip_obj, pages, page_obj, page, paginator = paginator_interface(ais_cla, page, TABLE_SIZE)
    print("后端接口测试")
    print({"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                        'page': page, 'paginator': paginator, 'pages': pages})
    return render(request, 'cla.html', {"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                        'page': page, 'paginator': paginator, 'pages': pages})
    
    
@csrf_exempt
@transaction.atomic
@login_required(login_url="/login/")
def ais_profession_view(request):      
    profession_name = request.GET.get("profession_name", "")
    page = int(request.GET.get("page", 1))
    keys = ""   # 搜索参数
    search = dict()
    if profession_name:
        search["profession_name__contains"] = profession_name
        keys += "profession_name=" + profession_name + "&"
    ais_profession = AisProfession.objects.filter(**search).order_by('id')
    # 调用自定义分页方法
    zip_obj, pages, page_obj, page, paginator = paginator_interface(ais_profession, page, TABLE_SIZE)
    print("获取专业接口")
    print({"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                        'page': page, 'paginator': paginator, 'pages': pages})
    return render(request, 'profession.html', {"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                        'page': page, 'paginator': paginator, 'pages': pages})    


@csrf_exempt
@login_required(login_url="/login/")
@transaction.atomic
def join_cla(request):
    if request.method == "GET":
        return HttpResponse("Nothing...")
    if request.method == "POST":
        current_user = request.user         # 当前登录用户
        # 获得前端传过来的数据
        cla_name = request.POST.get("cla_name", "")
        print(cla_name)
        ais_cla_base = AisCla.objects.get(cla_name=cla_name)  
        print(ais_cla_base.id)
        user_profile = UserProfile.objects.get(auth_user=current_user)
        user_profile.cla_id = ais_cla_base.id
        user_profile.cla = ais_cla_base.id
        user_profile.save()
        return HttpResponse(content="success")
    

def paginator_interface(object_list, page, table_size):
    """
    分页接口函数，创建分页的规则，返回给函数表格序号，页数对象
    :param object_list: 搜索结果列表
    :param page: 前端返回的页数
    :param table_size: 表格长度
    :return:
    """
    paginator = Paginator(object_list, table_size)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数, 返回第一页。
        page_obj = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        page_obj = paginator.page(paginator.num_pages)
    except InvalidPage:
        return HttpResponseRedirect(next)  # 如果请求的页数不存在, 重定向页面
    index = [table_size * (page - 1) + x for x in [x + 1 for x in list(range(table_size))]]  # 页内列表序号
    zip_obj = zip(page_obj, index)
    # 页数控制
    num_pages = paginator.num_pages
    if num_pages <= 11:     # 总页数小于11
        pages = [x for x in range(1, min(num_pages + 1, 12))]
    elif num_pages > 11 and page <= 6:  # 总页数大于11，激活页面为前6页
        pages = [x for x in range(1, min(num_pages + 1, 8))] + [None] + list(range(num_pages + 1))[-3:]
    elif page > num_pages - 6:      # 总页数大于11，激活页面为后6页
        pages = list(range(4))[1:] + [None] + [x for x in range(num_pages - 6, num_pages + 1)]
    else:       # 总页数大于11，激活页面为中间其他页
        pages_front = [x for x in range(1, min(num_pages + 1, 4))]  # 前3
        pages_behind = list(range(num_pages + 1))[-3:]  # 后3
        pages_mid = [page - 1, page, page + 1]  # 中3
        pages = pages_front + [None] + pages_mid + [None] + pages_behind
    return zip_obj, pages, page_obj, page, paginator

'''
@Author: randolph
@Date: 2020-07-01 03:38:12
@LastEditors: randolph
@LastEditTime: 2020-07-03 12:12:16
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 
'''
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

from apps.Information.models import AisClassmate
from apps.User.models import UserProfile

# Create your views here.

TABLE_SIZE = 9                  # 注册审批页面表格行数
PAGE_SIZE = 10                  # 每页显示行数


@csrf_exempt
@transaction.atomic
@login_required(login_url="/login/")
def ais_classmate_view(request):
    # classmate_id = int(request.GET.get("classmate_id", ""))
    page = int(request.GET.get("page", 1))
    keys = ""   # 搜索参数
    search = dict()
    search["user_id__contains"] = 8
    # if classmate_id:
    #     search["classmate_id__contains"] = classmate_id
    #     keys += "classmate_id=" + classmate_id + "&"
    # user_profile = UserProfile.objects.get(user_id=8)
    user_profile = UserProfile.objects.filter(**search).order_by('-user_id')
    # ais_classmate = AisClassmate.objects.filter(**search).order_by('-id')      # 根据st_id倒序
    # 调用自定义分页方法
    zip_obj, pages, page_obj, page, paginator = paginator_interface(user_profile, page, TABLE_SIZE)
    return render(request, 'classmates.html', {"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                               'page': page, 'paginator': paginator, 'pages': pages})



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

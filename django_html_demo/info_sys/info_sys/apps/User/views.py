import json
import re

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import (EmptyPage, InvalidPage, PageNotAnInteger,
                                   Paginator)
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from apps.User.models import UserProfile

# Create your views here.
TABLE_SIZE = 5                      # 注册审批页面表格行数


@csrf_exempt
def login_view(request):
    next_url = request.GET.get('next', '/index/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'info': '账号或密码错误!', 'next': next_url})
    else:
        return render(request, 'login.html', {'next': next_url})


def logout_view(request):
    logout(request)
    return redirect("/login/")


def redirect_login(request):
    return redirect('/login/')


@login_required(login_url="/login/")
def index_view(request):
    return redirect("/user/index/")


@login_required(login_url="/login/")
def user_profile_view(request):
    user = User.objects.get(username=request.user.username)
    try:
        user_profile = UserProfile.objects.get(auth_user=user)
    except Exception as e:
        if user.is_superuser:
            user_profile = {
                "user_real_name": "超级管理员",
                "email": user.email,
                "user_stu_num": "123456",
            }
        else:
            return redirect("/login/")
    return render(request, 'index.html',
                  {"user": user, "user_profile": user_profile, })


@csrf_exempt
def registration(request):
    if request.method == "GET":
        return HttpResponse("Nothing...")
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        real_name = request.POST.get("real_name", "")
        email = request.POST.get("email", "")
        if not re.match(r'[a-zA-z]\w{5,15}', username):
            return HttpResponse(content=json.dumps({"result": "请正确填写用户名（以字母开头）!"}))
        if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
            return HttpResponse(content=json.dumps({"result": "请正确填写用户邮箱!"}))
        if username and password and real_name and email:
            is_username_existed = User.objects.filter(username=username)
            is_email_existed = User.objects.filter(email=email)
            if is_username_existed:
                return HttpResponse(content=json.dumps({"result": "用户名已存在,请使用其他用户名!"}))
            elif is_email_existed:
                return HttpResponse(content=json.dumps({"result": "邮箱已被注册,请更换邮箱注册!"}))
            try:
                user = User.objects.create_user(username=username,
                                                password=password,
                                                email=email,
                                                is_active=0)
                UserProfile.objects.create(user_real_name=real_name,
                                           auth_user=user,
                                           is_approval=0,
                                           is_manager=0)  # 提交注册给未处理状态
            except Exception as e:
                return HttpResponse(content=json.dumps({"result": e}), status=400)
            return HttpResponse(content="success")
        else:
            return HttpResponse(content=json.dumps({"result": "必填项不能为空!"}))


@login_required(login_url="/login/")
def registration_dispatch(request):
    from apps.Information.views import paginator_interface
    username = request.GET.get("username", "")
    user_real_name = request.GET.get("user_real_name", "")
    email = request.GET.get("email", "")
    page = int(request.GET.get("page", 1))
    keys = ""  # 搜索参数
    search = dict()
    search["is_approval"] = 0
    if username:
        search["auth_user__username__contains"] = username
        keys += "username=" + username + "&"
    if user_real_name:
        search["user_real_name__contains"] = user_real_name
        keys += "user_real_name=" + user_real_name + "&"
    if email:
        search["auth_user__email__contains"] = email
        keys += "email=" + email + "&"
    profile = UserProfile.objects.filter(**search).order_by('user_id')
    # 调用自定义分页方法
    zip_obj, pages, page_obj, page, paginator = paginator_interface(profile, page, TABLE_SIZE)
    return render(request, 'approval.html', {"page_obj": page_obj, 'zip_obj': zip_obj, "keys": keys,
                                             'page': page, 'paginator': paginator, 'pages': pages})


@csrf_exempt
@login_required(login_url="/login/")
@transaction.atomic
def reject_user(request):
    if request.method == "GET":
        return HttpResponse("Nothing...")
    if request.method == "POST":
        username = request.POST.get("username", "")
        user_profile = UserProfile.objects.get(auth_user__username=username)
        user_profile.is_approval = -2  # 拒绝注册，比停用状态低一级别
        user_profile.save()
        return HttpResponse(content="success")


@csrf_exempt
@login_required(login_url="/login/")
@transaction.atomic
def pass_user(request):
    if request.method == "GET":
        return HttpResponse("Nothing...")
    if request.method == "POST":
        username_list = json.loads(request.POST.get("username_list", []))
        for username in username_list:
            user_profile = UserProfile.objects.get(auth_user__username=username)
            user_profile.is_approval = 1                # 正常用户
            user_profile.auth_user.is_active = 1        # 活动帐户，不决定能否登陆
            user_profile.save()
            user_profile.auth_user.save()
            user_profile.save()
        return HttpResponse(content="success")


@csrf_exempt
@login_required(login_url="/login/")
@transaction.atomic
def pass_manager_user(request):
    if request.method == "GET":
        return HttpResponse("Nothing...")
    if request.method == "POST":
        username = request.POST.get('username', '')
        user_real_name = request.POST.get('user_real_name', '')
        email = request.POST.get('email', '')
        user_profile = UserProfile.objects.get(auth_user__username=username)
        user_profile.auth_user.is_active = 1        # 注册通过
        user_profile.is_approval = 1                # 正常用户
        user_profile.is_manager = 1                 # 是管理
        user_profile.save()
        user_profile = UserProfile.objects.get(auth_user__username=username)
        user_profile.save()
        return HttpResponse(content="success")


@csrf_exempt
@login_required(login_url="/login/")
@transaction.atomic
def change_pwd(request):
    if request.method == "GET":
        return HttpResponse("Nothing...")
    if request.method == "POST":
        username = request.POST.get("username", "")
        oldpassword = request.POST.get("oldPassword", "")
        newpassword = request.POST.get("newPassword", "")
        user = User.objects.get(username=username)
        user.set_password(newpassword)
        user.save()
    return HttpResponse(content="success")

from django.conf.urls import url
from apps.User.views import *

urlpatterns = [
    url(r'^index/', user_profile_view),                 # 首页展示用户个人信息表user_profile
    url(r'^registration/', registration),               # 提交注册
    url(r'^approval/', registration_dispatch),          # 审批注册
    url(r'^pass_user/', pass_user),                     # 通过审计员用户
    url(r'^reject_user/', reject_user),                 # 拒绝通过用户
    url(r'^pass_manager_user/', pass_manager_user),     # 通过管理员用户
    url(r'^change_pwd/', change_pwd),
]

from django.conf.urls import url

from apps.Information.views import ais_classmate_view, ais_msg_view, clean_user, publish_msg, ais_cla_view, ais_profession_view, join_cla

urlpatterns = [
    url(r'^ais_classmate_view/', ais_classmate_view, name='ais_classmate_view'),        # 班级同学列表
    url(r'^ais_msg_view/', ais_msg_view, name='ais_msg_view'),                          # 班级留言列表
    url(r'^clean_user/', clean_user, name='clean_user'),                                # 踢出用户
    url(r'^publish_msg/', publish_msg, name='publish_msg'),                             # 发布留言
    url(r'^ais_cla_view/', ais_cla_view, name='ais_cla_view'),                          # 班级列表
    url(r'^ais_profession_view/', ais_profession_view, name='ais_profession_view'),     # 专业列表
    url(r'^join_cla/', join_cla, name='join_cla'),                                      # 加入班级
]

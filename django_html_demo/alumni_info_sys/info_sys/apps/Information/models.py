'''
@Author: randolph
@Date: 2020-07-01 03:38:12
@LastEditors: randolph
@LastEditTime: 2020-07-03 12:08:44
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 
'''
from django.db import models
from django.utils import timezone

from apps.User.models import UserProfile

# Create your models here.


class AisClassmate(models.Model):
    classmate = models.ForeignKey(UserProfile, models.DO_NOTHING)
    classmate_desc = models.TextField()

    class Meta:
        db_table = 'ais_classmate'
        permissions = (
            ('view_ais_classmate', 'View ais_classmate'),
            ('modify_ais_classmate', 'Modify ais_classmate'),
        )
        verbose_name = 'cla_mate数据'

class AisCla(models.Model):
    id = models.IntegerField(primary_key=True)
    cla_name = models.CharField(max_length=255, blank=True, null=True)
    cla_desc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ais_cla'
        verbose_name = '班级表'
        
class AisMsg(models.Model):
    id = models.IntegerField(primary_key=True)
    msg_publish_date = models.DateField(blank=True, null=True)
    msg_content = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ais_msg'
        verbose_name = '留言表'


class AisProfession(models.Model):
    id = models.IntegerField(primary_key=True)
    profession_name = models.CharField(max_length=255, blank=True, null=True)
    profession_desc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ais_profession'
        verbose_name = '专业表'


class AisUniversity(models.Model):
    id = models.IntegerField(primary_key=True)
    university_name = models.CharField(max_length=255, blank=True, null=True)
    university_desc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ais_university'
        verbose_name = '学校表'
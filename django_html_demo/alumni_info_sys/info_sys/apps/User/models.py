#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    is_approval_set = (
        (-2, "拒绝注册"),
        (-1, "停用"),
        (0, "待通过"),
        (1, "注册通过"),
    )
    user_id = models.AutoField(primary_key=True)
    user_real_name = models.CharField(max_length=255, blank=True, null=True)
    user_stu_num = models.IntegerField(blank=True, null=True)
    user_phone = models.IntegerField(blank=True, null=True)
    user_desc = models.TextField(blank=True, null=True)
    auth_user = models.OneToOneField(User, models.DO_NOTHING)
    is_approval = models.IntegerField(choices=is_approval_set)
    is_manager = models.IntegerField()
    university = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    cla = models.CharField(max_length=255)
    is_cla_manager = models.IntegerField()
    university_id = models.IntegerField(blank=True, null=True)
    procession_id = models.IntegerField(blank=True, null=True)
    cla_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户信息'
        permissions = (
            ('view_user_profile', 'View User Profile'),
            ('modify_user_profile', 'Modify User Profile'),
            ('can_approval_user', 'Can approval user')
        )

    def __str__(self):
        return self.auth_user.username

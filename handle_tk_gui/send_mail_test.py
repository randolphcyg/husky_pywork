#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author: randolph
@Date: 2020-06-16 09:48:28
@LastEditors: randolph
@LastEditTime: 2020-06-16 10:04:05
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 
'''
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import time
import datetime


def send_email(from_addr, to_addr, subject, password):
    msg = MIMEText("Ding !", 'html', 'utf-8')
    msg['From'] = u'<%s>' % from_addr
    msg['To'] = u'<%s>' % to_addr
    msg['Subject'] = subject

    smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtp.set_debuglevel(1)
    smtp.ehlo("smtp.qq.com")
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())


if __name__ == "__main__":
    # 这里的密码是开启smtp服务时输入的客户端登录授权码，并不是邮箱密码
    # 现在很多邮箱都需要先开启smtp才能这样发送邮件
    today = datetime.date.today().isoweekday()
    # 周六周天不发送邮件提醒当前时间
    if today != 6 or today != 7:
        send_email(u"957531442@qq.com", u"1466429534@qq.com", u"Time reminder", u"ifbqurunnvdpbeej")
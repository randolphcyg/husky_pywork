from django import template
from django.http import HttpResponse

register = template.Library()           # 注册自定义模板


@register.filter(name='time_format')
def time_format(second_time):
    if second_time is None:     # if none then set zero
        second_time = 0
    m, s = divmod(second_time, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)        # 考虑到天数
    try:
        if d == h == m == s == 0:
            return '无'
        if d == h == 0:
            return '%d分%d秒' % (m, s)
        if d == 0:
            return '%d时%d分%d秒' % (h, m, s)
        else:
            return '%d天%d时%d分%d秒' % (d, h, m, s)
    except Exception as e:
        return HttpResponse(content="wrong in 'apps/Information/templatetags/user_extras.py/time_format' ! ")

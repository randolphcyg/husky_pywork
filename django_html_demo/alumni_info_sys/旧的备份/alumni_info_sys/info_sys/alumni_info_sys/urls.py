"""alumni_info_sys URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.User.views import index_view, login_view, logout_view, redirect_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login'),
    url(r'^index/', index_view, name='index'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^$', redirect_login),
    url(r'^info/', include("apps.Information.urls")),
    url(r'^user/', include("apps.User.urls")),
] + staticfiles_urlpatterns()

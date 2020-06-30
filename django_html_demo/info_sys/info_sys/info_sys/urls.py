"""info_sys URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.User.views import login_view, index_view, logout_view, redirect_login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view),
    url(r'^index/', index_view),
    url(r'^logout/', logout_view),
    url(r'^$', redirect_login),
    url(r'^info/', include("apps.Information.urls")),
    url(r'^user/', include("apps.User.urls")),
]

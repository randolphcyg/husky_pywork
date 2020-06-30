from django.conf.urls import url
from apps.Information.views import stock_stat_view, import_csv_view

urlpatterns = [
    url(r'^stock/', stock_stat_view),
    url(r'^import_csv/', import_csv_view),
]

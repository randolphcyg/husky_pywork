from django.conf.urls import url

from apps.Information.views import import_csv_view, stock_stat_view, predict_stock

urlpatterns = [
    url(r'^predict_stock/', predict_stock, name='predict_stock'),
    url(r'^stock/', stock_stat_view, name='stock'),
    url(r'^import_csv/', import_csv_view, name='import_csv'),
]

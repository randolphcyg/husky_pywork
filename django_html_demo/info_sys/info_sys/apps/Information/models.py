from django.db import models
from apps.User.models import UserProfile
from django.utils import timezone

# Create your models here.


class StockStat(models.Model):
    st_id = models.AutoField(primary_key=True) 
    st_code = models.CharField(max_length=6)
    st_desc = models.CharField(max_length=2000)

    class Meta:
        db_table = 'stock_stat'
        permissions = (
            ('view_stock_stat', 'View stock_stat'),
            ('modify_stock_stat', 'Modify stock_stat'),
        )
        verbose_name = 'stock数据'
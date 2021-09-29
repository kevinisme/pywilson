from django.db import models

# Create your models here.
# import datetime
from twinbird.models import Twinbird


class Receipt(models.Model):
    twinbirdy = models.ForeignKey(
        Twinbird, on_delete=models.CASCADE, null=True, blank=True,
    )



    ydate = models.DateField('收據日期')
    itemname = models.CharField('項目名稱', max_length=200)
    code = models.CharField('收據號碼', max_length=200, null=True, blank=True)
    shop = models.CharField('店家名稱', max_length=200, null=True, blank=True)
    price = models.IntegerField('價格')


    class Meta:
        db_table = 'receipts'

from django.db import models

# Create your models here.
# import datetime
from twinbird.models import Twinbird


class Wonder(models.Model):
    twinbirdx = models.OneToOneField(Twinbird,on_delete=models.CASCADE,null=True, blank=True,)



    xdate = models.DateField('評估日期')
    note = models.CharField('項目名稱', max_length=200)
    source = models.CharField('需求來源', max_length=200, null=True, blank=True)
    xrange = models.CharField('價格區間', max_length=200, null=True, blank=True)



    class Meta:
        db_table = 'wonders'

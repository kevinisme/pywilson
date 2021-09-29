from django.db import models

# Create your models here.
# import datetime


class Twinbird(models.Model):
    wonderid = models.IntegerField('評估id')
    wondernote = models.CharField('評估備註', max_length=200, null=True, blank=True)
    dogid = models.IntegerField('收據日期id')
    dogitemname = models.CharField('收據日期備註', max_length=200, null=True, blank=True)
    catid = models.IntegerField('收據店家欄位id', null=True, blank=True)
    catitemname = models.CharField('收據店家欄位備註', max_length=200, null=True, blank=True)
    eggid = models.IntegerField('收據價錢欄位id', null=True, blank=True)
    eggitemname = models.CharField('收據價錢欄位備註', max_length=200, null=True, blank=True)



    class Meta:
        db_table = 'twinbirds'


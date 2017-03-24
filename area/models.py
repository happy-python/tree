#coding:utf-8
from django.db import models
from mptt.models import MPTTModel


class Area(MPTTModel):
    name = models.CharField('名称', max_length=50, unique=True)
    parent_area = models.ForeignKey('self', verbose_name='上级区域', null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'area'
        verbose_name = verbose_name_plural = '省/市/地区(县)'

    class MPTTMeta:
        parent_attr = 'parent_area'


    def __unicode__(self):
        return self.name

#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Test(models.Model):   #这里的类名代表了数据库的表名
    name = models.CharField(max_length=20)
    #def __unicode__(self):
    #	return self.name	#this fuction is to help you when you check it in database normally instead of garbled	
class temperature(models.Model):
	value_of_temperature = models.FloatField(max_length = 20)
	date_time = models.DateTimeField(auto_now_add = True)
	#date_time = models.DateTimeField(default = timezone.now)


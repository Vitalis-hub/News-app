from __future__ import unicode_literals #reads all languages possible
from django.db import models

# Create your models here.

class Newsapp(models.Model):
    
    name = models.CharField(max_length=150)  #string 
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default="0")
    picname = models.TextField()
    picurl = models.TextField(default='-')
    writer = models.CharField(max_length=30)
    catname = models.CharField(max_length=30, default="-")
    catid= models.IntegerField(default=0)
    ocatid= models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tag = models.TextField(default="")


    def __str__(self):
        return self.name
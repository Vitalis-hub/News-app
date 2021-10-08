from __future__ import unicode_literals #reads all languages possible
from django.db import models

# Create your models here.

class Main(models.Model):
    
    name = models.CharField(max_length=30)  #string 
    about = models.TextField()
    abouttxt = models.TextField(default="")
    #models.IntegerField()
    #models.CharField()
    #def __str__(self):
    #    return self.name

    fb = models.CharField(default='-', max_length=30)
    tw = models.CharField(default='-', max_length=30)
    ig = models.CharField(default='-', max_length=30)
    tell = models.CharField(default='-', max_length=30)
    seo_txt = models.CharField(default='-', max_length=200)
    seo_keywords = models.TextField(default='-', max_length=30)
    link = models.CharField(default='-', max_length=30)
    set_name = models.CharField(default='-', max_length = 30)

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")

    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    def __str__(self):
        return self.set_name + ' | ' + str(self.pk)
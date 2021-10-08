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
<<<<<<< HEAD
    act = models.IntegerField(default=0)
    rand = models.IntegerField(default=0)
=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c


    def __str__(self):
        return self.name
from __future__ import unicode_literals #reads all languages possible
from django.db import models

# Create your models here.

class Comment(models.Model):
    
    name = models.CharField(max_length=30)  #string
    email = models.CharField(max_length=30)  #string
    cm = models.TextField()  #string
    news_id = models.IntegerField()
    date = models.CharField(max_length=12)  #string
    time = models.CharField(max_length=10)  #string
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

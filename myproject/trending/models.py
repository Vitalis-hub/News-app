from __future__ import unicode_literals #reads all languages possible
from django.db import models

# Create your models here.

class Trending(models.Model):
    
    txt = models.CharField(max_length=200, default="")  #string
     
    

    def __str__(self):
        return self.txt


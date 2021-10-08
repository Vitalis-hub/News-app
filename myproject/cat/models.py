from __future__ import unicode_literals #reads all languages possible
from django.db import models

# Create your models here.

class Cat(models.Model):
    
    name = models.CharField(max_length=50)  #string 
    count = models.IntegerField(default=0)


    def __str__(self):
        return self.name
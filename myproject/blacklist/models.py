from __future__ import unicode_literals #reads all languages possible
from django.db import models

# Create your models here.

class Blacklist(models.Model):
    
    ip = models.CharField(max_length=30)  #string
    
    def __str__(self):
        return self.ip

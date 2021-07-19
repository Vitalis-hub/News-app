from __future__ import unicode_literals #reads all languages possible
from django.db import models

# Create your models here.

class ContactForm(models.Model):
    
    name = models.CharField(max_length=50)  #string 
    email = models.CharField(max_length=50)
    sub = models.TextField(default = "")
    txt = models.TextField()
    date = models.CharField(max_length=12, default="")
    time = models.CharField(max_length=12, default="")

    def __str__(self):
        return self.name
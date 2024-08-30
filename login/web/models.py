from django.db import models

# Create your models here.
class WangUser(models.Model):
    username = models.CharField(max_length=32, unique=True) # its primary key
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

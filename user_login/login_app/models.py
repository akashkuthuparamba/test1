import email
from django.db import models

# Create your models here.

class Log_in(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    phone_no=models.IntegerField()
    
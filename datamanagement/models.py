from django.db import models
from django.db.models.fields import DateField, IntegerField
from django.contrib.auth.models import User
# Create your models here.



class Admin(models.Model):
    status=models.BooleanField(default=True)
    paraphrase=models.CharField(max_length=20)
    Live=models.BooleanField(default=True)

class positions(models.Model):

    symbol=models.CharField(max_length=20,default='NA')
    time=models.DateTimeField(auto_now_add = True)
    price=models.FloatField(default=0)
    order_type = models.CharField(max_length=20,default='NA')



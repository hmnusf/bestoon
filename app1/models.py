from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return "{} - {} - {}".format(self.date,self.amount,self.text)

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return "{} - {} - {}".format(self.date,self.amount,self.text)
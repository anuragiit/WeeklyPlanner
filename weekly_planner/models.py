from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class toDoList(models.Model):
    userdetails = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    taskName = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200,default = "TODO")
    ts = models.DateTimeField(auto_now_add=True)

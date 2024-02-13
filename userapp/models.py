from django.db import models

# Create your models here.

class registerdb(models.Model):
    username=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)

class favdb(models.Model):
    uname=models.CharField(max_length=50,null=True,blank=True)
    recipe=models.CharField(max_length=50,null=True,blank=True)
    ingredients=models.CharField(max_length=500,null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
class downloaddb(models.Model):
    rname=models.CharField(max_length=50,null=True,blank=True)
    ringredients=models.CharField(max_length=500,null=True,blank=True)
    rdesc=models.CharField(max_length=500,null=True,blank=True)
class feedbackdb(models.Model):
    uname=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    feedback=models.CharField(max_length=100,null=True,blank=True)



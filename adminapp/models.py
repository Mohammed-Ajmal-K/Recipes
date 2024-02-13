from django.db import models

# Create your models here.

class cuisinedb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to="fooditems",null=True,blank=True)
    description=models.CharField(max_length=50,null=True,blank=True)

class recipedb(models.Model):
    item=models.CharField(max_length=20,null=True,blank=True)
    recipe_name=models.CharField(max_length=50,null=True,blank=True)
    about=models.CharField(max_length=500,null=True,blank=True)
    recipe_image=models.ImageField(upload_to="recipes",null=True,blank=True)
    ingredients=models.CharField(max_length=500,null=True,blank=True)
    recipe_desc=models.CharField(max_length=1000,null=True,blank=True)


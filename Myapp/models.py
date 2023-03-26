from django.db import models

# Create your models here.
class variety(models.Model):
    food_variety=models.CharField(max_length=50)

class Foodtype(models.Model):
    type=models.CharField(max_length=50)   

class Meals(models.Model):
    meals_type=models.CharField(max_length=50) 
from django.db import models

# Create your models here.


class CafeDetails(models.Model):
   cafe_name = models.CharField(max_length=50)


class FoodItems(models.Model):
   name = models.CharField(max_length=50)
   vegan = models.BooleanField()
   vegetarian = models.BooleanField()
   gluten_free = models.BooleanField()
   kosher = models.BooleanField()
   halal = models.BooleanField()
   humane = models.BooleanField()
   seafood_watch = models.BooleanField()

   
class MealPeriodDetails(models.Model):
   period_time = models.DateField()
   period_name = models.CharField(max_length=50)
   cafe = models.ForeignKey(CafeDetails, on_delete=models.CASCADE)
   






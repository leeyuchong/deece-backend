from django.db import models


class CafeDetails(models.Model):
   cafe_name = models.CharField(max_length=50)


class FoodItems(models.Model):
   name = models.CharField(max_length=50)
   vegan = models.BooleanField(default=False)
   vegetarian = models.BooleanField(default=False)
   gluten_free = models.BooleanField(default=False)
   kosher = models.BooleanField(default=False)
   halal = models.BooleanField(default=False)
   humane = models.BooleanField(default=False)
   seafood_watch = models.BooleanField(default=False)
   farmToFork = models.BooleanField(default=False)


class StationDetails(models.Model):
    station_name = models.CharField(max_length=50)
    cafe = models.ForeignKey(CafeDetails, on_delete=models.CASCADE)

   
class MealPeriodDetails(models.Model):
   period_name = models.CharField(max_length=50)
   period_time = models.TimeField()
   cafe = models.ForeignKey(CafeDetails, on_delete=models.CASCADE)
   

class Menu(models.Model):
    food_item = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    cafe = models.ForeignKey(CafeDetails, on_delete=models.CASCADE)
    station = models.ForeignKey(StationDetails, on_delete=models.CASCADE)
    meal_period = models.ForeignKey(MealPeriodDetails, on_delete=models.CASCADE)
    date = models.DateField()

from django.db import models

# Create your models here.

class StationDetails(models.Model):
    station_name = models.CharField(max_length=50)
    cafe = models.ForeignKey(CafeDetails, on_delete=models.CASCADE)

class Menu(models.Model):
    cafe = models.ForeignKey(CafeDetails, on_delete=models.CASCADE)
    station = models.ForeignKey(Stations, on_delete=models.CASCADE)
    meal_period = models.CharField(MealPeriodDetails, on_delete=models.CASCADE)
    food_item = models.CharField(FoodItems, on_delete=models.CASCADE)
    date = models.DateField()
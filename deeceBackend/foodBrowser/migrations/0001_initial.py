# Generated by Django 4.0.3 on 2022-03-24 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CafeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vegan', models.BooleanField()),
                ('vegetarian', models.BooleanField()),
                ('gluten_free', models.BooleanField()),
                ('kosher', models.BooleanField()),
                ('halal', models.BooleanField()),
                ('humane', models.BooleanField()),
                ('seafood_watch', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MealPeriodDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_name', models.CharField(max_length=50)),
                ('period_time', models.TimeField()),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodBrowser.cafedetails')),
            ],
        ),
        migrations.CreateModel(
            name='StationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=50)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodBrowser.cafedetails')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodBrowser.cafedetails')),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodBrowser.fooditems')),
                ('meal_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodBrowser.mealperioddetails')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodBrowser.stationdetails')),
            ],
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-24 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodBrowser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditems',
            name='farmToFork',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='gluten_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='halal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='humane',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='kosher',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='seafood_watch',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='vegan',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]

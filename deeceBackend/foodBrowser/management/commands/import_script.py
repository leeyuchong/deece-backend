from django.core.management.base import BaseCommand
import requests
from dataclasses import dataclass
import random
from foodBrowser.models import FoodItems

@dataclass
class FoodItem:
    item_id: int = 0
    name: str = ""
    vegetarian: bool = False
    vegan: bool = False
    glutenFree: bool = False
    halal: bool = False
    kosher: bool = False
    humane: bool = False
    seafood: bool = False
    farmToFork: bool = False
    cafe: str = ""
    date: str = ""
    station: str = ""
    meal_label: str = ""


class Command(BaseCommand):
    help = "Populates the database with data from the Cafe BonAppetit website"

    def handle(self, *args, **kwargs):
        response = requests.get(
            "https://legacy.cafebonappetit.com/api/2/menus?cafe=1626,1627,1628,1629,1630&date=2022-03-23"
        )
        response_dict = response.json()
        food_items = []
        for item_id, item in response_dict["items"].items():
            curr_item = FoodItems(
                item_id = item_id,
                name = item["label"],
                vegan = False,
                vegetarian = False,
                gluten_free = False,
                kosher = False,
                halal = False,
                humane = False,
                seafood_watch = False,
                farmToFork = False
            )
            if type(item["cor_icon"]) == dict:
                for key in item["cor_icon"].keys():
                    if key == "1":
                        curr_item.vegetarian = True
                    if key == "4":
                        curr_item.vegan = True
                    if key == "9":
                        curr_item.gluten_free = True
                    if key == "10":
                        curr_item.halal = True
                    if key == "11":
                        curr_item.kosher = True
                    if key == "6":
                        curr_item.farmToFork = True
                    if key == "18":
                        curr_item.humane = True
                    if key == "3":
                        curr_item.seafood_watch = True
            food_items.append(curr_item)
        # for day in response_dict["days"]:
        #     for cafe, cafeInfo in day["cafes"].items():
        #         for daypart in cafeInfo["dayparts"][0]:
        #             # print(daypart['label'])
        #             for station in daypart["stations"]:
        #                 # print(station['label'])
        #                 for item in station["items"]:
        #                     item_info = response_dict["items"][item]
        #                     food_items.append(
        #                         FoodItems(
        #                             item_id=item,
        #                             name=item_info["label"],
        #                             # date="2021-04-22",
        #                             # cafe=cafe,
        #                             # station=station["label"],
        #                             # meal_label=daypart["label"],
        #                         )
        #                     )
        #                     if type(item_info["cor_icon"]) == dict:
        #                         for key in item_info["cor_icon"].keys():
        #                             if key == "1":
        #                                 food_items[-1].vegetarian = True
        #                             elif key == "4":
        #                                 food_items[-1].vegan = True
        #                             elif key == "9":
        #                                 food_items[-1].glutenFree = True
        #                             elif key == "10":
        #                                 food_items[-1].halal = True
        #                             elif key == "11":
        #                                 food_items[-1].kosher = True
        #                             elif key == "6":
        #                                 food_items[-1].farmToFork = True
        #                             elif key == "18":
        #                                 food_items[-1].humane = True
        #                             elif key == "3":
        #                                 food_items[-1].seafood = True
        # sample = random.sample(food_items, 10)
        # for i in sample:
        #     print(i)
        # print(len(food_items))
        FoodItems.objects.bulk_create(food_items)

from django.db import models
from RestaurantLogin.models import Restaurant, RestaurantManager

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    # menu_included
    restaurant = models.ManyToManyField(Restaurant,related_name="items")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
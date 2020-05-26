from django.db import models
from RestaurantLogin.models import Restaurant, RestaurantManager

class Item(models.Model):
    item_title = models.CharField(max_length=255)
    item_description = models.TextField()
    item_price = models.IntegerField()
    # menu_included
    restaurant = models.ManyToManyField(Restaurant,related_name="items")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
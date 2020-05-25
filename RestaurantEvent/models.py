from django.db import models
from RestaurantLogin.models import Restaurant, RestaurantManager
from RestaurantMenu.models import Menu

class Event(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    spots_available = models.IntegerField()

    menu = models.ForeignKey(Menu,related_name="events_included",on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models
from RestaurantLogin.models import Restaurant, RestaurantManager

class Event(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    spots_available = models.IntegerField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
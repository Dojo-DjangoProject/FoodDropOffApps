from django.db import models
from RestaurantLogin.models import Restaurant, RestaurantManager
from RestaurantMenu.models import Menu

class Event(models.Model):
    restaurant_id =  models.ForeignKey(Restaurant, related_name="restaurant_events", on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,related_name="events_included",on_delete=models.CASCADE)
    
    date_time = models.DateTimeField()
    notes = models.TextField()
    # location = models.ForeignKey(Location, related_name="location_events", on_delete=models.CASCADE)
    minimum_orders = models.IntegerField()
    maximum_orders = models.IntegerField()
    minimum_amount_per_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # restaurant = models.ManyToManyField(Restaurant,related_name="events")  Not now
from django.db import models

class Order(models.Model):
    # user_id =  models.ForeignKey(User, related_name="user_orders", on_delete=models.CASCADE)
    # item_id = models.ManyToManyField(Item, related_name="item_orders")
    # event_id = models.ForeignKey(Event, related_name="event_orders", on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderQuantity(models.Model):
    # item_id =  models.ForeignKey(Item, related_name="item_quantities", on_delete=models.CASCADE)
    # order_id =  models.ForeignKey(Order, related_name="order_quantities", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    # event_id =  models.ForeignKey(Event, related_name="event_items", on_delete=models.CASCADE)
    item_title = models.CharField(max_length=255)
    item_description = models.TextField()
    item_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

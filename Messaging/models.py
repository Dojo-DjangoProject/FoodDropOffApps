from django.db import models

# Create your models here.
class Message(models.Model):
    # order_id =  models.ForeignKey(Order, related_name="order_messages", on_delete=models.CASCADE)
    sent_by = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
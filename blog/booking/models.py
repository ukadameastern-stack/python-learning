import uuid

from django.db import models

# Create your models here.

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campsite_name = models.CharField(max_length=60)
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
    email = models.EmailField(max_length=254)
    total_price= models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
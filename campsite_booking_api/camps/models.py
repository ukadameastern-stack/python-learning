from django.db import models
from .mixins import TimestampMixin
from django.contrib.auth.models import User

# Create your models here.

class Campsite(TimestampMixin, models.Model):
    name = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self) -> str:
        return self.name + f" (${self.price_per_night}/night, capacity: {self.capacity})"
    
    def __repr__(self) -> str:
        return f"Campsite(name={self.name}, price={self.price_per_night}, capacity={self.capacity})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Campsite) and self.id == other.id
    

class Booking(TimestampMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campsite = models.ForeignKey(Campsite, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guests = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user} - {self.campsite}"
    
    def __repr__(self) -> str:
        return f"Booking(user={self.user}, campsite={self.campsite}, start_date={self.start_date}, end_date={self.end_date})"

    @property
    def total_days(self) -> int:
        return (self.end_date - self.start_date).days

    @staticmethod
    def validate_dates(start_date, end_date) -> bool:
        return start_date < end_date

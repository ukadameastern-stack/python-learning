from django.db import models
from .mixins import TimestampMixin
from django.contrib.auth.models import User
from typing import Optional


class Campsite(TimestampMixin, models.Model):
    """
    Model representing a campsite.

    A campsite has a name, price per night, and capacity for guests.
    """
    name = models.CharField(max_length=100, help_text="Name of the campsite")
    price_per_night = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Price per night in USD"
    )
    capacity = models.IntegerField(help_text="Maximum number of guests")

    def __str__(self) -> str:
        return self.name + f" (${self.price_per_night}/night, capacity: {self.capacity})"

    def __repr__(self) -> str:
        return f"Campsite(name={self.name}, price={self.price_per_night}, capacity={self.capacity})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Campsite) and self.id == other.id

    class Meta:
        verbose_name = "Campsite"
        verbose_name_plural = "Campsites"
        ordering = ["name"]


class Booking(TimestampMixin, models.Model):
    """
    Model representing a booking.

    A booking links a user to a campsite for specific dates with a number of guests.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User who made the booking"
    )
    campsite = models.ForeignKey(
        Campsite,
        on_delete=models.CASCADE,
        help_text="Campsite being booked"
    )
    start_date = models.DateField(help_text="Start date of the booking")
    end_date = models.DateField(help_text="End date of the booking")
    guests = models.IntegerField(help_text="Number of guests")

    def __str__(self) -> str:
        return f"{self.user} - {self.campsite}"

    def __repr__(self) -> str:
        return f"Booking(user={self.user}, campsite={self.campsite}, start_date={self.start_date}, end_date={self.end_date})"

    @property
    def total_days(self) -> int:
        return (self.end_date - self.start_date).days

    @property
    def total_cost(self) -> float:
        """Calculate the total cost for this booking."""
        return float(self.total_days * self.campsite.price_per_night)

    @staticmethod
    def validate_dates(start_date, end_date) -> bool:
        return start_date < end_date

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-created_at"]
        unique_together = []  # Could add constraints if needed

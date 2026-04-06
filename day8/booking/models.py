import uuid

from django.db import models
from .mixins import TimestampMixin
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import DateRangeField
from django.contrib.postgres.indexes import GinIndex, GistIndex
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields.ranges import RangeOperators
from django.db.models import F

from simple_history.models import HistoricalRecords

# Create your models here.

User = get_user_model()

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campsite = models.ForeignKey("Campsite", on_delete=models.CASCADE)

    start_date = models.DateField()
    end_date = models.DateField()
    guests = models.IntegerField()

    # ✅ NEW: provider fields (for payments / external systems)
    provider_id = models.CharField(max_length=50, null=True, blank=True)
    provider_booking_id = models.CharField(max_length=100, null=True, blank=True)

    # ✅ NEW: JSONB fields
    payment_details = models.JSONField(default=dict, blank=True)
    extra_data = models.JSONField(default=dict, blank=True)

    # ✅ Optional (for PostgreSQL range queries)
    date_range = DateRangeField(null=True, blank=True)

    # ✅ Audit trail
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.user} - {self.campsite}"

    def __repr__(self):
        return (
            f"Booking(user={self.user}, campsite={self.campsite}, "
            f"start_date={self.start_date}, end_date={self.end_date})"
        )

    @property
    def total_days(self):
        return (self.end_date - self.start_date).days

    @staticmethod
    def validate_dates(start_date, end_date):
        return start_date < end_date

    def save(self, *args, **kwargs):
        # Keep range field in sync
        if self.start_date and self.end_date:
            from psycopg.types.range import DateRange
            self.date_range = DateRange(self.start_date, self.end_date, bounds="[)")
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            # ✅ Prevent duplicate external bookings
            models.UniqueConstraint(
                fields=["provider_id", "provider_booking_id"],
                name="unique_provider_booking"
            ),

            # ✅ Prevent overlapping bookings (PostgreSQL ONLY)
            ExclusionConstraint(
                name="prevent_overlapping_bookings",
                expressions=[
                    (F("campsite_id"), RangeOperators.EQUAL),
                    (F("date_range"), RangeOperators.OVERLAPS),
                ],
                index_type="GIST",
            )
        ]

        indexes = [
            # ✅ Fast JSON queries
            GinIndex(fields=["extra_data"], name="booking_extra_gin"),
            GistIndex(fields=["date_range"], name="booking_range_gist"), 
        ]
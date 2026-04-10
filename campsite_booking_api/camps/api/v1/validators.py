import logging
from abc import ABC, abstractmethod
from typing import Optional
from django.db import models
from ...dataclasses import BookingInput
from ...models import Booking, Campsite

# Get logger for this module
logger = logging.getLogger(__name__)


class BookingValidator(ABC):
    """Abstract base class for booking validators."""

    @abstractmethod
    def validate(self, booking: BookingInput) -> Optional[str]:
        """Validate a booking input. Return error message or None if valid."""
        pass


class OverlapValidator(BookingValidator):
    """
    Validator for checking booking overlaps.

    Ensures that the number of overlapping bookings doesn't exceed
    the campsite's capacity for the given date range.
    """

    def validate(self, booking: BookingInput) -> Optional[str]:
        """
        Check if the booking would exceed campsite capacity for the date range.

        Args:
            booking: BookingInput dataclass with booking details

        Returns:
            Error message if validation fails, None if valid
        """
        start = booking.start_date
        end = booking.end_date
        campsite_id = booking.campsite_id
        new_guests = booking.guests

        logger.debug(f"Checking overlap for campsite {campsite_id}, dates {start} to {end}, guests: {new_guests}")

        # Find overlapping bookings (excluding current booking if updating)
        overlapping_bookings = Booking.objects.filter(
            campsite_id=campsite_id,
            start_date__lt=end,
            end_date__gt=start
        )

        campsite = Campsite.objects.get(id=campsite_id)

        # Calculate total guests from overlapping bookings
        total_overlapping_guests = overlapping_bookings.aggregate(
            total_guests=models.Sum('guests')
        )['total_guests'] or 0

        logger.debug(f"Found {overlapping_bookings.count()} overlapping bookings with {total_overlapping_guests} total guests for campsite {campsite.name} (capacity: {campsite.capacity})")

        # Check if adding this booking would exceed capacity
        if total_overlapping_guests + new_guests > campsite.capacity:
            error_msg = f"Campsite '{campsite.name}' would be over capacity (Existing booking guest total: {total_overlapping_guests} + New guests: {new_guests} > Capacity: {campsite.capacity})"
            logger.warning(f"Overlap validation failed: {error_msg}")
            return error_msg

        logger.debug(f"Overlap validation passed for campsite {campsite.name}")
        return None
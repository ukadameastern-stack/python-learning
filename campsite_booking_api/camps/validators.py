import logging
from abc import ABC, abstractmethod
from typing import Optional
from .dataclasses import BookingInput
from .models import Booking, Campsite

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

        logger.debug(f"Checking overlap for campsite {campsite_id}, dates {start} to {end}")

        # Find overlapping bookings (excluding current booking if updating)
        overlapping_bookings = Booking.objects.filter(
            campsite_id=campsite_id,
            start_date__lt=end,
            end_date__gt=start
        )

        campsite = Campsite.objects.get(id=campsite_id)
        overlap_count = overlapping_bookings.count()

        logger.debug(f"Found {overlap_count} overlapping bookings for campsite {campsite.name} (capacity: {campsite.capacity})")

        # Check if adding this booking would exceed capacity
        if overlap_count >= campsite.capacity:
            error_msg = f"Campsite '{campsite.name}' is fully booked for the selected dates"
            logger.warning(f"Overlap validation failed: {error_msg} (found {overlap_count} bookings, capacity {campsite.capacity})")
            return error_msg

        logger.debug(f"Overlap validation passed for campsite {campsite.name}")
        return None
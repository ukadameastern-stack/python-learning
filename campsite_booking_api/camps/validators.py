from abc import ABC, abstractmethod
from typing import Optional
from .dataclasses import BookingInput
from .models import Booking, Campsite

class BookingValidator(ABC):

    @abstractmethod
    def validate(self, booking: BookingInput) -> Optional[str]:
        pass


class OverlapValidator(BookingValidator):

    def validate(self, booking: BookingInput) -> Optional[str]:

        start = booking.start_date
        end = booking.end_date
        campsite_id = booking.campsite_id

        # Date validation
        validate_dates = Booking.validate_dates(start, end)
        if not validate_dates:
            return "End date must be greater than start date"

        # Overlap validation
        overlapping_bookings = Booking.objects.filter(
            campsite_id=campsite_id,
            start_date__lt=end,
            end_date__gt=start
        )

        campsite = Campsite.objects.get(id=campsite_id)

        if overlapping_bookings.count() >= campsite.capacity:
            return "Campsite is fully booked for selected dates"

        return None
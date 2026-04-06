from dataclasses import dataclass, field
from datetime import date
from typing import Optional, Dict, Any


@dataclass
class PaymentDetails:
    amount: int
    currency: str
    status: str
    method: str

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("amount must be greater than 0")

        if self.currency not in ["INR", "USD", "EUR"]:
            raise ValueError("unsupported currency")

        if self.status not in ["paid", "pending", "failed"]:
            raise ValueError("invalid payment status")

@dataclass
class BookingInput:
    campsite: int

    start_date: date
    end_date: date

    # Provider fields
    provider_id: str
    provider_booking_id: str

    # JSON fields
    payment_details: PaymentDetails = field(default_factory=PaymentDetails)
    extra_data: Dict[str, Any] = field(default_factory=dict)


    guests: int = 1
    user: Optional[str] = None   # UUID as string

    def __post_init__(self):
        # ✅ Validate dates
        if self.start_date and self.end_date:
            if self.start_date >= self.end_date:
                raise ValueError("start_date must be before end_date")

        # ✅ Optional: validate guests
        if self.guests <= 0:
            raise ValueError("guests must be greater than 0")
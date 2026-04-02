from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class BookingInput:
    campsite_id: int
    start_date: date
    end_date: date
    guests: int
    user_id: Optional[int] = None
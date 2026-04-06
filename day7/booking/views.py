from django.db import IntegrityError

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Campsite
from .serializers import CampsiteSerializer, RegisterSerializer, BookingSerializer
from .pagination import CustomPagination
from .validators import OverlapValidator
from .dataclasses import BookingInput, PaymentDetails 
from .models import Booking


class CampsiteListAPI(ListAPIView):
    queryset = Campsite.objects.all()
    serializer_class = CampsiteSerializer
    pagination_class = CustomPagination

class BookingListAPI(ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class RegisterAPI(CreateAPIView):
    serializer_class = RegisterSerializer


class BookingCreateAPI(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        data = serializer.validated_data

        payment_data = data.get("payment_details")

        payment_details = (
            PaymentDetails(**payment_data)
            if payment_data else None
        )

        # dataclass instance
        booking_input = BookingInput(
            campsite=data["campsite"].id,
            start_date=data["start_date"],
            end_date=data["end_date"],
            guests=data["guests"],
            provider_id=data["provider_id"],
            provider_booking_id=data["provider_booking_id"],
            user=self.request.user.id,
            payment_details=payment_details
        )

        # dataclass to validator
        validator = OverlapValidator()
        error = validator.validate(booking_input)

        if error:
            raise ValidationError(error)

        try:
            serializer.save(user=self.request.user)

        except IntegrityError as e:
            error_msg = str(e)

            if "prevent_overlapping_bookings" in error_msg:
                raise ValidationError({
                    "error": "This campsite is already booked for the selected dates."
                })

            elif "unique_provider_booking" in error_msg:
                raise ValidationError({
                    "error": "This provider booking already exists.",
                    "details": {
                        "provider_id": serializer.validated_data.get("provider_id"),
                        "provider_booking_id": serializer.validated_data.get("provider_booking_id")
                    }
                })

            else:
                raise ValidationError({
                    "error": "Database constraint error."
                })
        
            
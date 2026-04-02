from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Campsite
from .serializers import CampsiteSerializer, RegisterSerializer, BookingSerializer
from .pagination import CustomPagination
from .validators import OverlapValidator
from .dataclasses import BookingInput 
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

        # dataclass instance
        booking_input = BookingInput(
            campsite_id=data["campsite"].id,
            start_date=data["start_date"],
            end_date=data["end_date"],
            guests=data["guests"],
            user_id=self.request.user.id
        )

        # dataclass to validator
        validator = OverlapValidator()
        error = validator.validate(booking_input)

        if error:
            raise ValidationError(error)

        serializer.save(user=self.request.user)  
        
            
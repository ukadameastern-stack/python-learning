import logging
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from ...models import Campsite
from .serializers import CampsiteSerializer, RegisterSerializer, BookingSerializer
from ...pagination import CustomPagination
from ...models import Booking

# Get logger for this module
logger = logging.getLogger(__name__)


class CampsiteListAPI(ListAPIView):
    """
    API endpoint for listing campsites.

    Returns paginated list of available campsites with their details.
    """
    queryset = Campsite.objects.all()
    serializer_class = CampsiteSerializer
    pagination_class = CustomPagination


class BookingListAPI(ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return bookings for the current user."""
        return Booking.objects.filter(user=self.request.user)


class RegisterAPI(CreateAPIView):
    serializer_class = RegisterSerializer


class BookingCreateAPI(CreateAPIView):
    """
    API endpoint for creating bookings.

    Creates new bookings for authenticated users with validation.
    All validation is handled in the serializer.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Override create method to add comprehensive logging."""
        user = request.user
        campsite_id = request.data.get('campsite')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        guests = request.data.get('guests')

        logger.info(f"User {user.username} (ID: {user.id}) attempting to create booking: "
                   f"campsite={campsite_id}, dates={start_date} to {end_date}, guests={guests}")

        try:
            response = super().create(request, *args, **kwargs)
            booking_id = response.data.get('id')
            logger.info(f"Successfully created booking ID {booking_id} for user {user.username}")
            return response
        except ValidationError as e:
            logger.warning(f"Booking validation failed for user {user.username}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error creating booking for user {user.username}: {str(e)}")
            raise

    def perform_create(self, serializer):
        """Save the booking with the current user."""
        serializer.save(user=self.request.user)  
        
            
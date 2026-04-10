import logging
from camps.dataclasses import BookingInput
from rest_framework import serializers
from .models import Campsite, Booking
from django.contrib.auth.models import User
from .validators import OverlapValidator

# Get logger for this module
logger = logging.getLogger(__name__)


class CampsiteSerializer(serializers.ModelSerializer):
    # Note: Just to show how to use source to rename fields in the serializer.
    pricePerNight = serializers.DecimalField(
        source='price_per_night',
        max_digits=6,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Campsite
        fields = ["id", "name", "capacity", "price_per_night", "pricePerNight"]


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.

    Handles booking creation with validation for:
    - Date validity (end > start)
    - Guest capacity vs campsite capacity
    - Booking overlaps
    """
    campsite = serializers.PrimaryKeyRelatedField(
        queryset=Campsite.objects.all(),
        error_messages={
            "required": "Campsite is required.",
            "does_not_exist": "Campsite not found.",
            "incorrect_type": "Campsite ID must be an integer."
        }
    )

    class Meta:
        model = Booking
        fields = ["id", "campsite", "start_date", "end_date", "guests"]

    def validate(self, data):
        """
        Validate booking data including guest capacity and overlap checks.
        """
        campsite = data["campsite"]
        guests = data["guests"]
        start_date = data["start_date"]
        end_date = data["end_date"]

        logger.info(f"Validating booking: campsite={campsite.id}, dates={start_date}-{end_date}, guests={guests}")

        # Validate guest capacity against campsite capacity
        if guests > campsite.capacity:
            error_msg = f"Number of guests ({guests}) exceeds campsite capacity ({campsite.capacity})"
            logger.warning(f"Guest capacity validation failed: {error_msg}")
            raise serializers.ValidationError(error_msg)

        # Validate date range
        if start_date >= end_date:
            error_msg = "End date must be after start date"
            logger.warning(f"Date validation failed: {error_msg}")
            raise serializers.ValidationError(error_msg)

        # Check for overlapping bookings
        validator = OverlapValidator()
        booking_input = BookingInput(
            campsite_id=campsite.id,
            start_date=start_date,
            end_date=end_date,
            guests=guests
        )

        error = validator.validate(booking_input)
        if error:
            logger.warning(f"Overlap validation failed: {error}")
            raise serializers.ValidationError(error)

        logger.info("Booking validation successful")
        return data


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Creates new user accounts with username and password.
    """
    password = serializers.CharField(
        write_only=True, # Password should not be returned in the API response
        min_length=8,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        """Create and return a new user."""
        return User.objects.create_user(**validated_data)
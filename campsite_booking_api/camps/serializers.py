from camps.dataclasses import BookingInput
from rest_framework import serializers
from .models import Campsite, Booking
from django.contrib.auth.models import User
from .validators import OverlapValidator

class CampsiteSerializer(serializers.ModelSerializer):
    # Note: Just to show how to use source to rename fields in the serializer.
    pricePerNight = serializers.DecimalField(
        source='price_per_night', 
        max_digits=6, 
        decimal_places=2
    )
    
    class Meta:
        model = Campsite
        fields = ["id", "name", "capacity", "price_per_night", "pricePerNight"] # Fields to define what data gets sent to the client.


class BookingSerializer(serializers.ModelSerializer):
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
        fields = ["id", "campsite", "start_date", "end_date", "guests"] # Fields to define what data gets sent to the client.

    def validate(self, data):
        validator = OverlapValidator()

        booking_input = BookingInput(
            campsite_id=data["campsite"].id,
            start_date=data["start_date"],
            end_date=data["end_date"],
            guests=data["guests"]
        )

        error = validator.validate(booking_input)

        if error:
            raise serializers.ValidationError(error)

        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
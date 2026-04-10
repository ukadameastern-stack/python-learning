"""
URL configuration for camps application.

This module defines all API endpoints for the campsite booking system.
All endpoints are prefixed with /api/ as defined in the main urls.py

Available endpoints:
- GET /api/campsites : List all campsites (paginated)
- POST /api/register/ : Register new user
- POST /api/token/ : Obtain JWT authentication token
- POST /api/bookings/create/ : Create a new booking (authenticated)
- GET /api/bookings/ : List user's bookings (authenticated)
"""

# Import path() function for URL routing
from django.urls import path

# Import TokenObtainPairView from simplejwt for JWT token generation
# This provides the token/ endpoint for user authentication
from rest_framework_simplejwt.views import TokenObtainPairView

# Import API view classes from camps app
# CampsiteListAPI: ListAPIView for retrieving paginated campsites
# RegisterAPI: CreateAPIView for user registration
# BookingCreateAPI: CreateAPIView for booking creation with validation
# BookingListAPI: ListAPIView for retrieving user's bookings
from .views import CampsiteListAPI, RegisterAPI, BookingCreateAPI, BookingListAPI

# Define URL patterns for camps application
urlpatterns = [
    path("campsites", CampsiteListAPI.as_view(), name="campsite-list"),
    path("register/", RegisterAPI.as_view(), name="register"),
    
    # JWT Token Obtain Endpoint
    # Route: /api/token/
    # Method: POST
    # Purpose: Authenticate user and obtain JWT tokens
    # Authentication: Not required (username/password based)
    # Request: { "username": "string", "password": "string" }
    # Response: { "access": "token", "refresh": "token" }
    # Usage: Include access token in Authorization header for protected endpoints
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("bookings/create/", BookingCreateAPI.as_view(), name="booking-create"),
    path("bookings/", BookingListAPI.as_view(), name="booking-list"),
]
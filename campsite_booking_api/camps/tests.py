from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Campsite, Booking
from datetime import date


class CampsiteModelTest(TestCase):
    """Test cases for Campsite model."""

    def setUp(self):
        self.campsite = Campsite.objects.create(
            name="Test Campsite",
            price_per_night=50.00,
            capacity=4
        )

    def test_campsite_creation(self):
        """Test campsite creation and string representation."""
        self.assertEqual(str(self.campsite), "Test Campsite ($50.0/night, capacity: 4)")
        self.assertEqual(self.campsite.capacity, 4)
        self.assertEqual(float(self.campsite.price_per_night), 50.00)


class BookingModelTest(TestCase):
    """Test cases for Booking model."""

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.campsite = Campsite.objects.create(
            name="Test Campsite",
            price_per_night=50.00,
            capacity=4
        )

    def test_booking_creation(self):
        """Test booking creation and properties."""
        booking = Booking.objects.create(
            user=self.user,
            campsite=self.campsite,
            start_date=date(2024, 12, 25),
            end_date=date(2024, 12, 27),
            guests=2
        )

        self.assertEqual(str(booking), f"{self.user} - {self.campsite}")
        self.assertEqual(booking.total_days, 2)
        self.assertEqual(booking.total_cost, 100.00)

    def test_date_validation(self):
        """Test date validation static method."""
        self.assertTrue(Booking.validate_dates(date(2024, 12, 25), date(2024, 12, 27)))
        self.assertFalse(Booking.validate_dates(date(2024, 12, 27), date(2024, 12, 25)))


class CampsiteAPITest(APITestCase):
    """Test cases for Campsite API endpoints."""

    def setUp(self):
        self.campsite = Campsite.objects.create(
            name="API Test Campsite",
            price_per_night=75.00,
            capacity=6
        )

    def test_campsite_list(self):
        """Test retrieving campsite list."""
        response = self.client.get('/api/campsites')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "API Test Campsite")


class AuthenticationAPITest(APITestCase):
    """Test cases for authentication endpoints."""

    def test_user_registration(self):
        """Test user registration."""
        data = {
            "username": "newuser",
            "password": "securepass123"
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('username', response.data)

    def test_token_obtain(self):
        """Test JWT token obtain."""
        # Create user first
        User.objects.create_user(username="testuser", password="testpass")

        data = {
            "username": "testuser",
            "password": "testpass"
        }
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class BookingAPITest(APITestCase):
    """Test cases for Booking API endpoints."""

    def setUp(self):
        self.user = User.objects.create_user(username="bookuser", password="bookpass")
        self.campsite = Campsite.objects.create(
            name="Booking Test Campsite",
            price_per_night=60.00,
            capacity=4
        )
        self.client.force_authenticate(user=self.user)

    def test_booking_creation_valid(self):
        """Test creating a valid booking."""
        data = {
            "campsite": self.campsite.id,
            "start_date": "2024-12-25",
            "end_date": "2024-12-27",
            "guests": 2
        }
        response = self.client.post('/api/bookings/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_creation_invalid_guests(self):
        """Test booking creation with too many guests."""
        data = {
            "campsite": self.campsite.id,
            "start_date": "2024-12-25",
            "end_date": "2024-12-27",
            "guests": 6  # Exceeds capacity of 4
        }
        response = self.client.post('/api/bookings/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_booking_creation_invalid_dates(self):
        """Test booking creation with invalid date range."""
        data = {
            "campsite": self.campsite.id,
            "start_date": "2024-12-27",
            "end_date": "2024-12-25",  # End before start
            "guests": 2
        }
        response = self.client.post('/api/bookings/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_booking_list_authenticated(self):
        """Test retrieving user's bookings."""
        # Create a booking first
        Booking.objects.create(
            user=self.user,
            campsite=self.campsite,
            start_date=date(2024, 12, 25),
            end_date=date(2024, 12, 27),
            guests=2
        )

        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that we have at least one booking
        self.assertGreater(len(response.data), 0)

    def test_booking_list_unauthenticated(self):
        """Test that unauthenticated users cannot access bookings."""
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

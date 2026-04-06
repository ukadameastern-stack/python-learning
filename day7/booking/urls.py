from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

urlpatterns = [
    path("campsites", views.CampsiteListAPI.as_view(), name="campsite-list"),
    path("register/", views.RegisterAPI.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("bookings/create/", views.BookingCreateAPI.as_view(), name="booking-create"),
    path("bookings/", views.BookingListAPI.as_view(), name="booking-list"),
]
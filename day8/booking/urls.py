from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

urlpatterns = [
    path("campsites", views.CampsiteListAPI.as_view(), name="campsite-list"),
    path("register/", views.RegisterAPI.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("bookings/create/", views.BookingCreateAPI.as_view(), name="booking-create"),
    path("bookings/", views.BookingListAPI.as_view(), name="booking-list"),
    path("jobs/waiting/", views.JobsWaitingAPI.as_view(), name="jobs-waiting"),
    path("jobs/execute/", views.ExecuteJobAPI.as_view(), name="jobs-execute"),
    path("jobs/failed/", views.JobsFailedAPI.as_view(), name="jobs-failed"),
    path("jobs/finished/", views.JobsFinishedAPI.as_view(), name="jobs-finished"),
]
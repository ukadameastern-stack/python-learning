from django.contrib import admin
from .models import Campsite, Booking

# Register your models here.

@admin.register(Campsite)
class CampsiteAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["capacity"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ["start_date"]
    search_fields = ["user__username"]

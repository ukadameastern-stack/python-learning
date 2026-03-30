from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['campsite_name', 'arrival', 'departure', 'email', 'total_price', 'timestamp']
    list_filter = ['arrival', 'departure', 'timestamp']
    search_fields = ['campsite_name', 'email']
    ordering = ['-timestamp']

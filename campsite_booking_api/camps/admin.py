from django.contrib import admin
from .models import Campsite, Booking

# Register your models here.

@admin.register(Campsite)
class CampsiteAdmin(admin.ModelAdmin):
    search_fields = ["name", "price_per_night"]
    list_filter = ["capacity"]
    list_display = ["name", "price_per_night", "capacity"]  


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ["start_date"]
    search_fields = ["user__username", "campsite__name"]
    list_display = ["user_name", "campsite_name", "start_date", "end_date", "guests"] 

    @admin.display(description="Campsite")
    def campsite_name(self, obj):
        return obj.campsite.name + f" ({obj.campsite.capacity})"

    @admin.display(description="User")
    def user_name(self, obj):
        return obj.user.username.upper()
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related("campsite")

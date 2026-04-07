from django.contrib import admin

# Register your models here.
from .models import Husband, Wife
admin.site.register(Husband)
admin.site.register(Wife)

from django.contrib import admin

# Register your models here.
from .models import Location , PickupRequest

admin.site.register(Location)
admin.site.register(PickupRequest)
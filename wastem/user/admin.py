from django.contrib import admin

# Register your models here.
from .models import Profile
# from .models import Location

admin.site.register(Profile)
# admin.site.register(Location)
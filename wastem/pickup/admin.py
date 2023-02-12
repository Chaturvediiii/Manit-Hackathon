from django.contrib import admin

# Register your models here.
from .models import Location , PickupRequest
from django.contrib import admin

@admin.register(PickupRequest)
class PickupRequestAdmin(admin.ModelAdmin):
    list_display = ( 'location', 'status','description','phone_number')
    list_filter = ('status',)
    search_fields = ('location','description','phone_number')
    
    def has_add_permission(self, request):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Location)

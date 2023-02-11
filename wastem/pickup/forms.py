from django import forms
from .models import Location, PickupRequest

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name','address',]


class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = PickupRequest
        fields = ['location', 'date', 'time', 'description']
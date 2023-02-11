from django import forms
from .models import PickupRequest

class PickupRequestForm(forms.ModelForm):
    # type = forms.MultipleChoiceField(label='TYPE OF WASTE', choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = PickupRequest
        fields = ['location', 'date', 'time', 'description']
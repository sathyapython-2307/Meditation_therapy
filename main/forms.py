from django import forms
from .models import Approach

class ApproachForm(forms.ModelForm):
    class Meta:
        model = Approach
        fields = ['first_name', 'last_name', 'mobile', 'email', 'therapy_days', 'family_count', 'address', 'time_availability', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'therapy_days': forms.Select(attrs={'class': 'form-select'}),
            'family_count': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'required': True}),
            'time_availability': forms.Select(attrs={'class': 'form-select'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
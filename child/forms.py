from django import forms
from .models import  Guardian,Child
from location.models import Location
import re

class GuardianRegistrationForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'location','phone_number']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        # Check if first name contains only letters
        if not re.match(r'^[a-zA-Z]+$', first_name):
            raise forms.ValidationError('First name should only contain letters.')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        # Check if last name contains only letters
        if not re.match(r'^[a-zA-Z]+$', last_name):
            raise forms.ValidationError('Last name should only contain letters.')

        return last_name
    
    def clean(self):
        cleaned_data = super().clean()

        # Clear the form fields after submission
        self.cleaned_data = {}

        return cleaned_data

class ChildRegistrationForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'guardian']
        

    def __init__(self, *args, **kwargs):
        guardian_id = kwargs.pop('guardian_id', None)
        super().__init__(*args, **kwargs)
        if guardian_id:
            self.fields['guardian'].initial = guardian_id
# forms.py
from django import forms
from vaccine.models import Vaccine
from .models import VaccineAdministration, Immunization_Record
from child.models import Child
class VaccineAdministrationForm(forms.ModelForm):
    class Meta:
        model = VaccineAdministration
        exclude = ['id', 'record']

    date_of_administration = forms.DateField(
        required=True,
        widget=forms.SelectDateWidget(),
        error_messages={'required': 'Please enter a date of administration.'}
    )

class ImmunizationRecordForm(forms.ModelForm):
    child = forms.IntegerField(widget=forms.HiddenInput(), required=False)  # Make the child field hidden and not required

    class Meta:
        model = Immunization_Record
        fields = ['child', 'status', 'next_date_of_administration']

    vaccineadministration_set = forms.inlineformset_factory(
        Immunization_Record,
        VaccineAdministration,
        form=VaccineAdministrationForm,
        extra=1,
        can_delete=False,
        can_order=False
    )
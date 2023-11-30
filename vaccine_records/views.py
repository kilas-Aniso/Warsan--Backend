from django.shortcuts import render, redirect
from .models import Immunization_Record
from .forms import ImmunizationRecordForm, VaccineAdministrationForm

from django.shortcuts import render, redirect
from .forms import ImmunizationRecordForm, VaccineAdministrationForm
from child.models import Child


# views.py
from django.shortcuts import render, redirect
from .forms import ImmunizationRecordForm

def create_immunization_record(request, child_id):
    if request.method == 'POST':
        immunization_form = ImmunizationRecordForm(request.POST)
        if immunization_form.is_valid():
            record = immunization_form.save(commit=False)
            record.child_id = child_id  # Set the child_id from the URL
            record.save()

            VaccineAdministrationFormSet = immunization_form.vaccineadministration_set
            formset = VaccineAdministrationFormSet(request.POST, instance=record)

            if formset.is_valid():
                formset.save()
                return redirect('immunization_detail', child_id=record.child_id)  # Assuming 'child_id' is the expected argument

    else:
        immunization_form = ImmunizationRecordForm(initial={'child': child_id})  # Initialize the form with the child_id

    return render(request, 'create_immunization_record.html', {'form': immunization_form})

# View to update an existing immunization record with inline Vaccine Administration
def update_immunization_record(request, record_id):
    record = Immunization_Record.objects.get(pk=record_id)
    
    if request.method == 'POST':
        form = ImmunizationRecordForm(request.POST, instance=record)
        formset = VaccineAdministrationForm(request.POST, instance=record)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('immunization_detail')  # Redirect to the list view
    else:
        form = ImmunizationRecordForm(instance=record)
        formset = VaccineAdministrationForm(instance=record)
    
    return render(request, 'update_immunization_record.html', {'form': form, 'formset': formset, 'record': record})


from django.shortcuts import render
from .models import Immunization_Record
from django.shortcuts import render, get_object_or_404

# View to list immunization records
def immunization_detail(request, child_id):
    record = get_object_or_404(Immunization_Record, child__id=child_id)
    return render(request, 'immunization_detail.html', {'record': record})
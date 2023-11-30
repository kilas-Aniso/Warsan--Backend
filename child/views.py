from django.shortcuts import get_object_or_404, redirect, render

from api.serializers import GuardianSerializer
from api.views import guardian_list
from .forms import GuardianRegistrationForm, ChildRegistrationForm
from  child.models import Guardian
from location.models import Location

# def retrieve_guardian(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         try:
#             guardian = Guardian.objects.get(phone_number=phone_number)
#             return render(request, 'guardian_details.html', {'guardian': guardian})
#         except Guardian.DoesNotExist:
#             return render(request, 'guardian_not_found.html')
#     return render(request, 'guardian/retrieve_guardian.html')
def retrieve_guardian(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        try:
            guardian = Guardian.objects.get(phone_number=phone_number)
            return redirect('guardian_detail', guardian_id=guardian.id)
        except Guardian.DoesNotExist:
            # Guardian not found, redirect to the guardian registration form
            return redirect('retrieve_guardian')  # Replace 'register_guardian' with your URL name for the registration form
    return render(request, 'guardian/retrieve_guardian.html')
def guardian_detail(request, guardian_id):
    guardian = get_object_or_404(Guardian, pk=guardian_id)
    children = guardian.child_set.all()
    children_with_age = []
    for child in children:
        child_age = child.age()
        children_with_age.append({'child': child, 'age': child_age})
    context = {
        'guardian': guardian,
        'children_with_age': children_with_age,
    }
    return render(request, 'guardian/guardian_detail.html', context)


def register_guardian(request):
    if request.method == 'POST':
        form = GuardianRegistrationForm(request.POST)
        if form.is_valid():
            guardian = form.save(commit=False)
            # Save the guardian
            guardian.save()
            # Redirect to the guardian details page
            return redirect('guardian_detail', guardian_id=guardian.id)  # Redirect to the guardian details page
    else:
        form = GuardianRegistrationForm()
    
    return render(request, 'guardian/register_guardian.html', {'form': form})


# 




def register_child(request, guardian_id):
    guardian = Guardian.objects.get(id=guardian_id)
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST, guardian_id=guardian_id)
        if form.is_valid():
            child = form.save(commit=False)
            child.guardian = guardian
            child.save()
            return redirect('create_immunization_record',child_id=child.id)
    else:
        form = ChildRegistrationForm(guardian_id=guardian_id)
    return render(request, 'child/register_child.html', {'form': form, 'guardian': guardian})

def welcome_view(request):
    return render(request, 'welcome.html')
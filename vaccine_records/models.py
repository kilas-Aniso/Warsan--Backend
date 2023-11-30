from django.db import models
from django.forms import ValidationError
from vaccine.models import Vaccine
from child.models import Child

class Immunization_Record(models.Model):
    child = models.OneToOneField(Child, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, choices=[('Taken', 'Taken'), ('Missed', 'Missed')], default='Not administered')
    next_date_of_administration = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Immunization Record - {self.child.first_name} {self.child.last_name}'



class VaccineAdministration(models.Model):
    record = models.ForeignKey(Immunization_Record, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    date_of_administration = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('record', 'vaccine')

    def __str__(self):
        return f'Vaccine Administration - {self.vaccine.vaccine_choice} - Date: {self.date_of_administration}'

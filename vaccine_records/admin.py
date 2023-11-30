from django.contrib import admin
from .models import Immunization_Record, VaccineAdministration

class VaccineAdministrationInline(admin.TabularInline):
    model = VaccineAdministration
    extra = 1  # Number of inline forms to display

class Immunization_RecordAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    search_fields = ('child__first_name', 'child__last_name')
    inlines = [VaccineAdministrationInline]

    def display_vaccine_administrations(self, obj):
        vaccine_administrations = VaccineAdministration.objects.filter(record=obj)
        administrations_str = ", ".join([f"{administration.vaccine} ({administration.date_of_administration})" for administration in vaccine_administrations])
        return administrations_str

    display_vaccine_administrations.short_description = 'Vaccine Administrations'

    list_display = ('child', 'next_date_of_administration', 'status', 'display_vaccine_administrations')

admin.site.register(Immunization_Record, Immunization_RecordAdmin)

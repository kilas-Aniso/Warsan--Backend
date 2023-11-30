from django.contrib import admin
from .models import Vaccine

class VaccineAdmin(admin.ModelAdmin):
    list_display = ['vaccine_choice',]


admin.site.register(Vaccine, VaccineAdmin)
from django.contrib import admin
from .models import Location
class LocationAdmin(admin.ModelAdmin):
    list_display = ('region',)
admin.site.register(Location, LocationAdmin)
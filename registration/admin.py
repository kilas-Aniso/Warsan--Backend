
from django.contrib import admin
from .models import CustomUser, Healthworker



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


class HealthworkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email', 'hospital', 'phone_number')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Healthworker, HealthworkerAdmin)
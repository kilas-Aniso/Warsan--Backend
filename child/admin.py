from django.contrib import admin
from .models import Child, Guardian

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','age', 'date_of_birth', 'gender', 'guardian', 'location', 'phone_number')
    search_fields = ('first_name', 'last_name')
    list_filter = ('gender', 'status')
    def get_readonly_fields(self, request, obj=None):
        
        return ['location', 'phone_number']
    def save_model(self, request, obj, form, change):
        
        if obj.guardian:
            obj.location = obj.guardian.location
            obj.phone_number = obj.guardian.phone_number
        super().save_model(request, obj, form, change)
        
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'Full Name'


@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'location')

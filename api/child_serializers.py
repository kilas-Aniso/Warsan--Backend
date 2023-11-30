from child.models import Child, Guardian
from rest_framework import serializers


class ChildSerializer(serializers.ModelSerializer):
    guardian_name = serializers.ReadOnlyField(source='guardian.first_name')
    location_name = serializers.ReadOnlyField(source='location.region')

    class Meta:
        model = Child
        fields = ['id', 'first_name', 'last_name', 'date_of_birth','age', 'gender', 'status', 'guardian_name', 'phone_number', 'location_name', 'guardian']
        read_only_fields = ['phone_number']
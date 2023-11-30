from django.urls import path
from . import views

urlpatterns = [
    # URL for creating a new immunization record
    path('create/<int:child_id>/', views.create_immunization_record, name='create_immunization_record'),

    # URL for updating an existing immunization record with the record_id parameter
    path('update/<int:record_id>/', views.update_immunization_record, name='update_immunization_record'),

    # URL for listing immunization records
    path('detail/<int:child_id>/', views.immunization_detail, name='immunization_detail'),
    
    # Other URL patterns if needed
]

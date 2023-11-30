from django.urls import path
from . import views

urlpatterns = [
    path('ngo/signup/', views.ngo_signup, name='ngo-signup'),
    path('ngo/logout/', views.ngo_logout, name='ngo-logout'),
    path('customusers/', views.custom_user_list, name='customuser-list'),    
    path('customusers/<int:pk>/', views.custom_user_detail, name='customuser-detail'),
    path('healthworkers/', views.healthworker_list, name='healthworker-list'),
    path('healthworkers/<int:pk>/', views.healthworker_detail, name='healthworker-detail'),
    path('healthworker/signup/', views.healthworker_signup, name='healthworker-signup'),
    path('healthworker/login/', views.healthworker_login, name='healthworker-login'),
    path('ngo/login/', views.ngo_login, name='ngo-login'),
    path('vaccines/', views.vaccine_list, name='vaccine-list'),
    path('vaccines/<str:vaccine_choice>/', views.vaccine_detail, name='vaccine-detail'),
    path('locations/', views.location_list, name='location-list'),
    path('children/', views.child_list, name='child-list'),
    path('children/<int:pk>/', views.child_detail, name='child-detail'),
    path('guardians/', views.guardian_list, name='guardian-list'),
    path('guardians/<int:pk>/', views.guardian_detail, name='guardian-detail'),
    path('guardian/<str:phone_number>/', views.get_guardian_by_phone, name='get_guardian_by_phone'),
    path('immunization-records/<int:child_id>/', views.child_immunization_records, name='immunization_record_detail'),
    path('immunization-records/', views.list_immunization_records, name='immunization_record_list'),
    path('child-vaccine-count/<int:child_id>/', views.child_vaccines_count_api_view, name='child-vaccine-count'),
    path('region_rate/<str:region_name>/',views.immunization_rate,name='immunization-rate'),
    path('regions_rates/',views.all_regions_rates,name='regions_rates')
]

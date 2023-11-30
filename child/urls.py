# from .views import guardian_detail,retrieve_guardian,register_child,register_guardian
# from django.urls import path


# urlpatterns=[
#     # path('guardian/upload/',guardian_upload_form,name='guardian_upload_view'),
#     path('guardian/<int:guardian_id>/', guardian_detail, name='guardian_detail'),
#     path('guardian/retrieve/',retrieve_guardian, name='retrieve_guardian'),
#     path('guardian/register_guardian/', register_guardian, name='register_guardian'),
#     path('register_child/<int:guardian_id>/', register_child, name='register_child'),
  
# ]
from .views import guardian_detail,retrieve_guardian,register_child,register_guardian, welcome_view
from django.urls import path
urlpatterns=[
    # path('guardian/upload/',guardian_upload_form,name='guardian_upload_view'),
    path('guardian/<int:guardian_id>/', guardian_detail, name='guardian_detail'),
    # path('child/guardian/<int:guardian_id>/', guardian_detail, name='guardian_detail'),
    path('guardian/retrieve/',retrieve_guardian, name='retrieve_guardian'),
    path('guardian/register_guardian/', register_guardian, name='register_guardian'),
    path('child/guardian/<int:guardian_id>/register/', register_child, name='register_child'),    # path('register_child/<int:guardian_id>/', register_child, name='register_child'),
    path('welcome/', welcome_view, name='welcome'),  # Define a URL pattern for the welcome view


]
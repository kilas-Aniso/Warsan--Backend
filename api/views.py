from tokenize import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from location.models import Location
from vaccine_records.models import Immunization_Record
from registration.models import CustomUser, Healthworker
from vaccine.models import Vaccine
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password
from child.models import Child, Guardian
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render
from django.utils.crypto import get_random_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from .serializers import *
from .permissions import IsAdminOrNGO, IsHealthworker, IsOwnerOrAdmin, IsAdminOrReadOnly
from . utils import send_emails

@api_view(['GET', 'POST'])
def location_list(request):
    locations = Location.objects.all()
    data = []
    for location in locations:
        data.append({
            'id': location.id,  # Include the 'id' field
            'region': location.region,
            'longitude': location.longitude,
            'latitude': location.latitude
        })
    return Response(data)



# @api_view(['GET', 'POST', 'PUT'])
# @permission_classes([IsAdminOrNGO])
# def immunization_record_list(request):
#     if request.method == 'GET':
#         immunization_records = Immunization_Record.objects.all()
#         serializer = Immunization_RecordSerializer(immunization_records, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = Immunization_RecordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    


@api_view(['POST'])
@permission_classes([IsAdminOrNGO])
def healthworker_signup(request):
    serializer = HealthworkerSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        healthworker = serializer.save(password=password)  # Save the password as provided by the user

        return Response({'message': 'Health worker registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsHealthworker])
def healthworker_login(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    user = Healthworker.objects.filter(phone_number=phone_number).first()
    print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<{user}>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if user is not None and user.password == password:  # Compare the password without hashing
        login(request, user)
        token = default_token_generator.make_token(user)
        print(user)
        return Response({'token': token}, status=status.HTTP_200_OK)
    elif user is None:
        return Response({'message': 'User with this phone number does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)




@api_view(['GET'])
@permission_classes([IsAdminOrNGO])
def healthworker_list(request):
    if request.method == 'GET':
        healthworkers = Healthworker.objects.all()
        serializer = HealthworkerSerializer(healthworkers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrAdmin])
def healthworker_detail(request, pk):
    try:
        healthworker = Healthworker.objects.get(pk=pk)
    except Healthworker.DoesNotExist:
        return Response({'message': 'Health worker not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HealthworkerSerializer(healthworker)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = HealthworkerSerializer(healthworker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        healthworker.delete()
        return Response("Health worker deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAdminOrNGO])
def ngo_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = CustomUser.objects.filter(username=username).first()
    
    if user is not None and user.check_password(password):
        login(request, user)
        token = default_token_generator.make_token(user)
        return Response({'token': token}, status=status.HTTP_200_OK)
    
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
@permission_classes([IsAdminOrNGO])
def vaccine_list(request):
    if request.method == 'GET':
        vaccines = Vaccine.objects.all()
        serializer = VaccineSerializer(vaccines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VaccineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST',])
@permission_classes([IsAdminOrNGO])
def custom_user_list(request):
    if request.method == 'GET':
        custom_users = CustomUser.objects.all()
        serializer = CustomUserSerializer(custom_users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response({'message': 'Custom user created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminOrNGO])
def custom_user_detail(request, pk):
    try:
        custom_user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response({'message': 'Custom user not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(custom_user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CustomUserSerializer(custom_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        custom_user.delete()
        return Response("Custom user deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAdminOrNGO])
def vaccine_list(request):
    if request.method == 'GET':
        vaccines = Vaccine.objects.all()
        serializer = VaccineSerializer(vaccines, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VaccineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminOrNGO])
def vaccine_detail(request, vaccine_choice):
    vaccine = get_object_or_404(Vaccine, vaccine_choice=vaccine_choice)

    if request.method == 'GET':
        serializer = VaccineSerializer(vaccine)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT'])
def child_list(request):
    if request.method == 'GET':
        children = Child.objects.all()
        serialized_children = ChildSerializer(children, many=True) 
        return Response(serialized_children.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminOrNGO])
def child_detail(request, pk):
    try:
        child = Child.objects.get(pk=pk)
    except Child.DoesNotExist:
        return Response({'message': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChildSerializer(child)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ChildSerializer(child, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        child.delete()
        return Response("Child deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAdminOrNGO])
def guardian_list(request):
    if request.method == 'GET':
        guardians = Guardian.objects.filter(status='A')
        serializer = GuardianSerializer(guardians, many=True) 
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GuardianSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_guardian_by_phone(request, phone_number):
    try:
        guardian = Guardian.objects.get(phone_number=phone_number)
    except Guardian.DoesNotExist:
        return Response(
            {"error": "Guardian not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # Serialize the guardian
    guardian_serializer = GuardianSerializer(guardian)

    # Get the related children for the guardian
    children = guardian.child_set.all()

    # Serialize the related children using the ChildSerializer
    children_serializer = ChildSerializer(children, many=True)

    # Combine the guardian and children data
    response_data = {
        'guardian': guardian_serializer.data,
        'children': children_serializer.data,
    }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminOrNGO])
def guardian_detail(request, pk):
    try:
        guardian = Guardian.objects.get(pk=pk)
    except Guardian.DoesNotExist:
        return Response({'message': 'Guardian not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Use the GuardianSerializer with related children
        serializer = GuardianSerializer(guardian)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = GuardianSerializer(guardian, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        guardian.delete()
        return Response("Guardian deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAdminOrNGO])
def ngo_signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hashed_password = make_password(password) 
        serializer.validated_data['password'] = hashed_password
        user = serializer.save()
        return Response({'message': 'NGO user created successfully'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminOrNGO])
def ngo_logout(request):
    logout(request)
    return Response({'message': 'NGO user logged out successfully'}, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def immunization_status_api_view(request):
#     fully_immunized_records = Immunization_Record.objects.filter(next_date_of_administration__isnull=True)
#     incomplete_immunized_records = Immunization_Record.objects.exclude(next_date_of_administration__isnull=True)

#     fully_immunized_serializer = Immunization_RecordSerializer(fully_immunized_records, many=True)
#     incomplete_immunized_serializer = Immunization_RecordSerializer(incomplete_immunized_records, many=True)

#     response_data = {
#         'fully_immunized_records': fully_immunized_serializer.data,
#         'incomplete_immunized_records': incomplete_immunized_serializer.data
#     }

#     return Response(response_data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def child_vaccines_count_api_view(request, child_id):
    try:
        child = Child.objects.get(id=child_id)
    except Child.DoesNotExist:
        return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)

    vaccine_count = Immunization_Record.objects.filter(child=child).count()

    response_data = {
        'child_id': child.id,
        'vaccine_count': vaccine_count
    }

    return Response(response_data, status=status.HTTP_200_OK)



@api_view(['GET'])
def child_vaccines_count_api_view(request, child_id):
    try:
        child = Child.objects.get(id=child_id)
    except Child.DoesNotExist:
        return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)

    vaccine_count = Immunization_Record.objects.filter(child=child).count()

    response_data = {
        'child_id': child.id,
        'vaccine_count': vaccine_count
    }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def child_vaccines_count_api_view(request, child_id):
    try:
        child = Child.objects.get(id=child_id)
    except Child.DoesNotExist:
        return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)

    
    vaccine_count = Immunization_Record.objects.filter(child=child).count()

    response_data = {
        'child_id': child.id,
        'vaccine_count': vaccine_count
    }

    return Response(response_data, status=status.HTTP_200_OK)





@api_view(['GET'])
@permission_classes([IsAdminOrNGO])
def immunization_rate(request, region_name):
    try:
        total_children = 100
        immunized_children = Child.objects.filter(location__region=region_name, immunization_record__isnull=False).distinct().count()
        immunization_rate = (immunized_children / total_children) * 100 if total_children > 0 else 0
        response_data = {
            'region_name': region_name,
            'total_children': total_children,
            'immunized_children': immunized_children,
            'immunization_rate': immunization_rate,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAdminOrNGO])
def all_regions_rates(request):
    try:
        region_names = Location.objects.values_list('region', flat=True).distinct()
        immunization_rates = []
        for region_name in region_names:
            total_children = 100
            immunized_children = Child.objects.filter(location__region=region_name, immunization_record__isnull=False).distinct().count()
            immunization_rate = (immunized_children / total_children) * 100 if total_children > 0 else 0
            region_data = {
                'region_name': region_name,
                'total_children': total_children,
                'immunized_children': immunized_children,
                'immunization_rate': immunization_rate,
            }
            immunization_rates.append(region_data)
        return Response(immunization_rates, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST', 'PUT'])
def list_immunization_records(request):
    if request.method == 'GET':
        immunization_records = Immunization_Record.objects.all()
        serializer = ImmunizationRecordSerializer(immunization_records, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ImmunizationRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        try:
            child_id = request.data['child']
            immunization_record = Immunization_Record.objects.get(child_id=child_id)
        except Immunization_Record.DoesNotExist:
            return Response({"error": "Immunization Record not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ImmunizationRecordSerializer(immunization_record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def child_immunization_records(request, child_id):
    try:
        immunization_records = Immunization_Record.objects.filter(child_id=child_id)
        serializer = ImmunizationRecordSerializer(immunization_records, many=True)
        return Response(serializer.data)
    except Immunization_Record.DoesNotExist:
        return Response({"error": "Immunization Records not found for the specified child."}, status=status.HTTP_404_NOT_FOUND)

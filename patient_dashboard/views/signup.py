from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from patient_dashboard.models.models import Patient

@api_view(['POST'])
def patient_signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({"message": "Username, password, and email are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Check if username or email already exists
    if Patient.objects.filter(username=username).exists():
        return Response({"message": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
    if Patient.objects.filter(email=email).exists():
        return Response({"message": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

    # Create the patient
    patient = Patient.objects.create_user(username=username, email=email, password=password)
    patient.save()

    return Response({"message": "Patient created successfully."}, status=status.HTTP_201_CREATED)

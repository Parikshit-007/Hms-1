from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from appointment.models.models import Appointment
from appointment.serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

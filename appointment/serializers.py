# serializers.py
from rest_framework import serializers
from appointment.models.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

from patient_dashboard.models.models import CNFT
from rest_framework import serializers


class CNFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNFT
        fields = ['token', 'image', 'uploaded_at']
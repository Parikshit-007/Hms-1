from patient_dashboard.models.models import CNFT
from rest_framework import serializers


class CNFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNFT
        fields = '__all__'
# class ImageSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Image
        # fields = '__all__'        
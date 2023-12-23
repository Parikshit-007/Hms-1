# patient/serializers.py
from rest_framework import serializers
from patient.models.models import Patient, PatientBilling, PatientHistory, PatientLedger, PatientReminder, PatientVisitList

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientBilling
        fields = '__all__'

class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = '__all__'

class PatientLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientLedger
        fields = '__all__'

class PatientReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientReminder
        fields = '__all__'

class PatientVisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVisitList
        fields = '__all__'

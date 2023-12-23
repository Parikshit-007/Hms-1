# patient/views/views.py
from rest_framework import generics
from patient.models.models import Patient, PatientBilling, PatientHistory, PatientLedger, PatientReminder, PatientVisitList
from patient.serializers import (
    PatientSerializer, 
    PatientBillingSerializer, 
    PatientHistorySerializer, 
    PatientLedgerSerializer, 
    PatientReminderSerializer, 
    PatientVisitListSerializer
)

# Patient API views
class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# PatientBilling API views
class PatientBillingListCreateView(generics.ListCreateAPIView):
    queryset = PatientBilling.objects.all()
    serializer_class = PatientBillingSerializer

class PatientBillingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientBilling.objects.all()
    serializer_class = PatientBillingSerializer

# PatientHistory API views
class PatientHistoryListCreateView(generics.ListCreateAPIView):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer

class PatientHistoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer

# PatientLedger API views
class PatientLedgerListCreateView(generics.ListCreateAPIView):
    queryset = PatientLedger.objects.all()
    serializer_class = PatientLedgerSerializer

class PatientLedgerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientLedger.objects.all()
    serializer_class = PatientLedgerSerializer

# PatientReminder API views
class PatientReminderListCreateView(generics.ListCreateAPIView):
    queryset = PatientReminder.objects.all()
    serializer_class = PatientReminderSerializer

class PatientReminderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientReminder.objects.all()
    serializer_class = PatientReminderSerializer

# PatientVisitList API views
class PatientVisitListListCreateView(generics.ListCreateAPIView):
    queryset = PatientVisitList.objects.all()
    serializer_class = PatientVisitListSerializer

class PatientVisitListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientVisitList.objects.all()
    serializer_class = PatientVisitListSerializer

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from opd.models.models import (
    OPD_REGISTER,
    OPD_Billing,
    OPD_REPORT,
    OPD_PRESCRIPTION,
    OPDTOIPDTRANSFER,
    OPDPatientSummary,
    Depwisereport,
    RefDoctorReport,
    ConsultantDoctorReport,
)
from opd.serializers import (
    OPD_REGISTERSerializer,
    OPD_BillingSerializer,
    OPD_REPORTSerializer,
    OPD_PRESCRIPTIONSerializer,
    OPDTOIPDTRANSFERSerializer,
    OPDPatientSummarySerializer,
    DepwisereportSerializer,
    RefDoctorReportSerializer,
    ConsultantDoctorReportSerializer,
)

class OPD_REGISTERViewSet(viewsets.ModelViewSet):
    queryset = OPD_REGISTER.objects.all()
    serializer_class = OPD_REGISTERSerializer

class OPD_BillingViewSet(viewsets.ModelViewSet):
    queryset = OPD_Billing.objects.all()
    serializer_class = OPD_BillingSerializer

class OPD_REPORTViewSet(viewsets.ModelViewSet):
    queryset = OPD_REPORT.objects.all()
    serializer_class = OPD_REPORTSerializer

class OPD_PRESCRIPTIONViewSet(viewsets.ModelViewSet):
    queryset = OPD_PRESCRIPTION.objects.all()
    serializer_class = OPD_PRESCRIPTIONSerializer

class OPDTOIPDTRANSFERViewSet(viewsets.ModelViewSet):
    queryset = OPDTOIPDTRANSFER.objects.all()
    serializer_class = OPDTOIPDTRANSFERSerializer

class OPDPatientSummaryViewSet(viewsets.ModelViewSet):
    queryset = OPDPatientSummary.objects.all()
    serializer_class = OPDPatientSummarySerializer

class DepwisereportViewSet(viewsets.ModelViewSet):
    queryset = Depwisereport.objects.all()
    serializer_class = DepwisereportSerializer

class RefDoctorReportViewSet(viewsets.ModelViewSet):
    queryset = RefDoctorReport.objects.all()
    serializer_class = RefDoctorReportSerializer

class ConsultantDoctorReportViewSet(viewsets.ModelViewSet):
    queryset = ConsultantDoctorReport.objects.all()
    serializer_class = ConsultantDoctorReportSerializer

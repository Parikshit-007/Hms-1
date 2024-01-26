from rest_framework import serializers
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

class OPD_REGISTERSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPD_REGISTER
        fields = '__all__'

class OPD_BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPD_Billing
        fields = '__all__'

class OPD_REPORTSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPD_REPORT
        fields = '__all__'

class OPD_PRESCRIPTIONSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPD_PRESCRIPTION
        fields = '__all__'

class OPDTOIPDTRANSFERSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPDTOIPDTRANSFER
        fields = '__all__'

class OPDPatientSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = OPDPatientSummary
        fields = '__all__'

class DepwisereportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depwisereport
        fields = '__all__'

class RefDoctorReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefDoctorReport
        fields = '__all__'

class ConsultantDoctorReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantDoctorReport
        fields = '__all__'

from opd.models.models import OPD_REGISTER, OPD_PRESCRIPTION, OPD_Billing, OPD_REPORT, OPDPatientSummary, OPDTOIPDTRANSFER, RefDoctorReport, ConsultantDoctorReport, Depwisereport
from rest_framework import serializers

class OPD_REGISTERSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPD_REGISTER
        fields = '__all__'

class OPD_PRESCRIPTIONSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPD_PRESCRIPTION
        fields = '__all__'

class OPD_BillingSerializers(serializers.ModelSerializer):
    class Meta:
        model = OPD_Billing
        fields = '__all__'

class OPD_REPORTSerializers(serializers.ModelSerializer):
    class Meta:
        model = OPD_REPORT
        fields = '__all__'

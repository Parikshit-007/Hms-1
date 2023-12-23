# ipd/serializers.py
from rest_framework import serializers
from ipd.models.models import  IPDRegistration, IPDDeposit, IPDDischarge, IPDAdmitReport, IPDDepositReport, IPDDischargeReport, DepartmentReport, WardWiseReport, DoctorWiseReport, TPAReport

class IPDRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDRegistration
        fields = '__all__'

class IPDDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDDeposit
        fields = '__all__'

class IPDDischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDDischarge
        fields = '__all__'

class IPDAdmitReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDAdmitReport
        fields = '__all__'

class IPDDepositReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDDepositReport
        fields = '__all__'

class IPDDischargeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPDDischargeReport
        fields = '__all__'

class DepartmentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentReport
        fields = '__all__'

class WardWiseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardWiseReport
        fields = '__all__'

class DoctorWiseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorWiseReport
        fields = '__all__'

class TPAReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPAReport
        fields = '__all__'
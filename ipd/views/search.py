from rest_framework import generics
from ipd.models.models import (
    IPDRegistration, IPDDeposit, IPDDischarge, IPDAdmitReport, 
    IPDDepositReport, IPDDischargeReport, DepartmentReport, 
    WardWiseReport, DoctorWiseReport, TPAReport
)
from ipd.serializers import (
    IPDRegistrationSerializer, IPDDepositSerializer, IPDDischargeSerializer, 
    IPDAdmitReportSerializer, IPDDepositReportSerializer, IPDDischargeReportSerializer,
    DepartmentReportSerializer, WardWiseReportSerializer, DoctorWiseReportSerializer, TPAReportSerializer
)



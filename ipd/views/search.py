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


def search(self):
    qs= IPDRegistration.objects.all()
    title = self.request.qery_params.get('title')
    if title is not None:
        qs= qs.filter(title__icontains=title)
    return qs    
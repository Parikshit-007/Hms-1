# ipd/views.py
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

class IPDRegistrationListCreateView(generics.ListCreateAPIView):
    queryset = IPDRegistration.objects.all()
    serializer_class = IPDRegistrationSerializer

class IPDRegistrationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDRegistration.objects.all()
    serializer_class = IPDRegistrationSerializer

class IPDDepositListCreateView(generics.ListCreateAPIView):
    queryset = IPDDeposit.objects.all()
    serializer_class = IPDDepositSerializer

class IPDDepositRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDeposit.objects.all()
    serializer_class = IPDDepositSerializer

class IPDDischargeListCreateView(generics.ListCreateAPIView):
    queryset = IPDDischarge.objects.all()
    serializer_class = IPDDischargeSerializer

class IPDDischargeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDischarge.objects.all()
    serializer_class = IPDDischargeSerializer

class IPDAdmitReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDAdmitReport.objects.all()
    serializer_class = IPDAdmitReportSerializer

class IPDAdmitReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDAdmitReport.objects.all()
    serializer_class = IPDAdmitReportSerializer

class IPDDepositReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDDepositReport.objects.all()
    serializer_class = IPDDepositReportSerializer

class IPDDepositReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDepositReport.objects.all()
    serializer_class = IPDDepositReportSerializer

class IPDDischargeReportListCreateView(generics.ListCreateAPIView):
    queryset = IPDDischargeReport.objects.all()
    serializer_class = IPDDischargeReportSerializer

class IPDDischargeReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPDDischargeReport.objects.all()
    serializer_class = IPDDischargeReportSerializer

class DepartmentReportListCreateView(generics.ListCreateAPIView):
    queryset = DepartmentReport.objects.all()
    serializer_class = DepartmentReportSerializer

class DepartmentReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepartmentReport.objects.all()
    serializer_class = DepartmentReportSerializer

class WardWiseReportListCreateView(generics.ListCreateAPIView):
    queryset = WardWiseReport.objects.all()
    serializer_class = WardWiseReportSerializer

class WardWiseReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WardWiseReport.objects.all()
    serializer_class = WardWiseReportSerializer

class DoctorWiseReportListCreateView(generics.ListCreateAPIView):
    queryset = DoctorWiseReport.objects.all()
    serializer_class = DoctorWiseReportSerializer

class DoctorWiseReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorWiseReport.objects.all()
    serializer_class = DoctorWiseReportSerializer

class TPAReportListCreateView(generics.ListCreateAPIView):
    queryset = TPAReport.objects.all()
    serializer_class = TPAReportSerializer

class TPAReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TPAReport.objects.all()
    serializer_class = TPAReportSerializer

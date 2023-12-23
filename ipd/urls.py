# ipd/urls.py
from django.urls import path
from ipd.views.views import (
    IPDRegistrationListCreateView, IPDRegistrationRetrieveUpdateDestroyView,
    IPDDepositListCreateView, IPDDepositRetrieveUpdateDestroyView,
    IPDDischargeListCreateView, IPDDischargeRetrieveUpdateDestroyView,
    IPDAdmitReportListCreateView, IPDAdmitReportRetrieveUpdateDestroyView,
    IPDDepositReportListCreateView, IPDDepositReportRetrieveUpdateDestroyView,
    IPDDischargeReportListCreateView, IPDDischargeReportRetrieveUpdateDestroyView,
    DepartmentReportListCreateView, DepartmentReportRetrieveUpdateDestroyView,
    WardWiseReportListCreateView, WardWiseReportRetrieveUpdateDestroyView,
    DoctorWiseReportListCreateView, DoctorWiseReportRetrieveUpdateDestroyView,
    TPAReportListCreateView, TPAReportRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('ipd-registrations/', IPDRegistrationListCreateView.as_view(), name='ipd-registration-list-create'),
    path('ipd-registrations/<int:pk>/', IPDRegistrationRetrieveUpdateDestroyView.as_view(), name='ipd-registration-retrieve-update-destroy'),

    path('ipd-deposits/', IPDDepositListCreateView.as_view(), name='ipd-deposit-list-create'),
    path('ipd-deposits/<int:pk>/', IPDDepositRetrieveUpdateDestroyView.as_view(), name='ipd-deposit-retrieve-update-destroy'),

    path('ipd-discharges/', IPDDischargeListCreateView.as_view(), name='ipd-discharge-list-create'),
    path('ipd-discharges/<int:pk>/', IPDDischargeRetrieveUpdateDestroyView.as_view(), name='ipd-discharge-retrieve-update-destroy'),

    path('ipd-admit-reports/', IPDAdmitReportListCreateView.as_view(), name='ipd-admit-report-list-create'),
    path('ipd-admit-reports/<int:pk>/', IPDAdmitReportRetrieveUpdateDestroyView.as_view(), name='ipd-admit-report-retrieve-update-destroy'),

    path('ipd-deposit-reports/', IPDDepositReportListCreateView.as_view(), name='ipd-deposit-report-list-create'),
    path('ipd-deposit-reports/<int:pk>/', IPDDepositReportRetrieveUpdateDestroyView.as_view(), name='ipd-deposit-report-retrieve-update-destroy'),

    path('ipd-discharge-reports/', IPDDischargeReportListCreateView.as_view(), name='ipd-discharge-report-list-create'),
    path('ipd-discharge-reports/<int:pk>/', IPDDischargeReportRetrieveUpdateDestroyView.as_view(), name='ipd-discharge-report-retrieve-update-destroy'),

    path('department-reports/', DepartmentReportListCreateView.as_view(), name='department-report-list-create'),
    path('department-reports/<int:pk>/', DepartmentReportRetrieveUpdateDestroyView.as_view(), name='department-report-retrieve-update-destroy'),

    path('ward-wise-reports/', WardWiseReportListCreateView.as_view(), name='ward-wise-report-list-create'),
    path('ward-wise-reports/<int:pk>/', WardWiseReportRetrieveUpdateDestroyView.as_view(), name='ward-wise-report-retrieve-update-destroy'),

    path('doctor-wise-reports/', DoctorWiseReportListCreateView.as_view(), name='doctor-wise-report-list-create'),
    path('doctor-wise-reports/<int:pk>/', DoctorWiseReportRetrieveUpdateDestroyView.as_view(), name='doctor-wise-report-retrieve-update-destroy'),

    path('tpa-reports/', TPAReportListCreateView.as_view(), name='tpa-report-list-create'),
    path('tpa-reports/<int:pk>/', TPAReportRetrieveUpdateDestroyView.as_view(), name='tpa-report-retrieve-update-destroy'),
]

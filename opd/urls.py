from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from opd.views.views import (
    OPD_REGISTERViewSet,
    OPD_BillingViewSet,
    OPD_REPORTViewSet,
    OPD_PRESCRIPTIONViewSet,
    OPDTOIPDTRANSFERViewSet,
    OPDPatientSummaryViewSet,
    DepwisereportViewSet,
    RefDoctorReportViewSet,
    ConsultantDoctorReportViewSet,
)

urlpatterns = [
    path('api/opd-register/', OPD_REGISTERViewSet.as_view({'get': 'list', 'post': 'create'}), name='opd-register-list-create'),
    path('api/opd-register/<int:pk>/', OPD_REGISTERViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='opd-register-detail'),

    path('api/opd-billing/', OPD_BillingViewSet.as_view({'get': 'list', 'post': 'create'}), name='opd-billing-list-create'),
    path('api/opd-billing/<int:pk>/', OPD_BillingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='opd-billing-detail'),

    path('api/opd-report/', OPD_REPORTViewSet.as_view({'get': 'list', 'post': 'create'}), name='opd-report-list-create'),
    path('api/opd-report/<int:pk>/', OPD_REPORTViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='opd-report-detail'),

    path('api/opd-prescription/', OPD_PRESCRIPTIONViewSet.as_view({'get': 'list', 'post': 'create'}), name='opd-prescription-list-create'),
    path('api/opd-prescription/<int:pk>/', OPD_PRESCRIPTIONViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='opd-prescription-detail'),

    path('api/opdtoipdtransfer/', OPDTOIPDTRANSFERViewSet.as_view({'get': 'list', 'post': 'create'}), name='opdtoipdtransfer-list-create'),
    path('api/opdtoipdtransfer/<int:pk>/', OPDTOIPDTRANSFERViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='opdtoipdtransfer-detail'),

    path('api/opd-patient-summary/', OPDPatientSummaryViewSet.as_view({'get': 'list', 'post': 'create'}), name='opd-patient-summary-list-create'),
    path('api/opd-patient-summary/<int:pk>/', OPDPatientSummaryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='opd-patient-summary-detail'),

    path('api/depwisereport/', DepwisereportViewSet.as_view({'get': 'list', 'post': 'create'}), name='depwisereport-list-create'),
    path('api/depwisereport/<int:pk>/', DepwisereportViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='depwisereport-detail'),

    path('api/refdoctorreport/', RefDoctorReportViewSet.as_view({'get': 'list', 'post': 'create'}), name='refdoctorreport-list-create'),
    path('api/refdoctorreport/<int:pk>/', RefDoctorReportViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='refdoctorreport-detail'),

    path('api/consultantdoctorreport/', ConsultantDoctorReportViewSet.as_view({'get': 'list', 'post': 'create'}), name='consultantdoctorreport-list-create'),
    path('api/consultantdoctorreport/<int:pk>/', ConsultantDoctorReportViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='consultantdoctorreport-detail'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
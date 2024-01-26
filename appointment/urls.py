from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from appointment.views.views import AppointmentListCreateView, AppointmentRetrieveUpdateDestroyView

urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment-retrieve-update-destroy'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
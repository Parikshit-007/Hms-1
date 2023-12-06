from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', include('doctor.urls') ),
    path('patient/', include('patient.urls')),
    path('opd/', include('opd.urls')),
    path('accounts/', include('accounts.urls')),
    path('ipd/', include('ipd.urls')),
    path('staff/', include('staff.urls')),
    path('inventory/', include('inventory.urls')),
    path('emergency/', include('emergency.urls')),
    path('analytics/', include('analytics.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

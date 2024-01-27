   #path('api/patient/login/', patient_login, name='patient_login'),
from django.urls import path
from patient_dashboard.views.views import CNFTViewSet
from patient_dashboard.views.login import patient_login
from patient_dashboard.views.signup import patient_signup

urlpatterns = [

    path('api/patient/cnft/', CNFTViewSet.as_view({'get': 'list', 'post': 'create'}), name='cnft'),
    path('api/patient_dash/login/', patient_login , name='patient_login'),
    path('api/patient/signup/', patient_signup, name='patient_signup'),
    # path('api/admin/login/', admin_login, name='admin_login'),
]
from django.contrib import admin
from appointment.models.models import Appointment
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'clinic', 'date', 'time_slot', 'status')
    list_filter = ('status',)
admin.site.register(Appointment)
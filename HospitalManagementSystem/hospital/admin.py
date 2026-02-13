from django.contrib import admin
from hospital.models import Doctor,Patient,Appointment

# Register your models here.
admin.site.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','mob','special']


admin.site.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name','age','gen','mob','address','disease']


admin.site.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor','patient','date','time']
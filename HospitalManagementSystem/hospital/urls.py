from django.urls import path   
from hospital import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('doctors/',views.doctor_view,name='doctors'),
    path('patients/',views.patient_view,name='patients'),
    path('about/',views.about_view,name='about'),
    path('add-appointment/',views.add_appointment_view,name='add_appointment'),
    path('doctor/<int:id>',views.doctor_appointment_view,name='doctor_appointments'),
    path('patient/<int:id>',views.patient_appointment_view,name='patient_appointments'),
    path('add-doctor/',views.add_doctor,name='add_doctor'),
    path('add-patient/',views.add_patient,name='add_patient'),
    path('delete-doctor/<int:id>',views.delete_doctor,name='delete_doctor'),
    path('delete-patient/<int:id>',views.delete_patient,name='delete_patient'),
    path('update-doctor/<int:id>',views.update_doctor,name='update_doctor'),
    path('update-patient/<int:id>',views.update_patient,name='update_patient'),
    path('appointments/',views.appointments_view,name='appointments'),
    path('update-appointment/<int:id>',views.update_appointment,name='update_appointment'),
    path('delete-appointment/<int:id>',views.delete_appointment,name='delete_appointment'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('new_password/',views.new_password,name='new_password')

]
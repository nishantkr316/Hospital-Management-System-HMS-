from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    mob = models.IntegerField()
    special = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gen = models.CharField(max_length=10)
    disease = models.CharField(max_length=100, default='General')
    mob = models.IntegerField(null=True)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} - {self.date} {self.time}"
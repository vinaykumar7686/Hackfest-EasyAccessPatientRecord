from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class PatientProfile(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    dob = models.DateField(null=True)
    email = models.EmailField(null = False)
    password = models.TextField(null=False)

           # critical/serious
    # ---------------Foreign Keys-------------------
    # doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, null=True)
    # doctors_visiting_time = models.CharField(null=True, max_length=50, blank=True)

    def __str__(self):
        return self.patient_name

#Medical Info about the patient to be stored in this table
class MedicalInfo(models.Model):
    
    doctor_notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50)
    patient_relative_name = models.CharField(max_length=50, null=True)
    patient_relative_contact = models.CharField(max_length=15, null=True)
    resd_address = models.TextField()
    prior_ailments = models.TextField()
    height = models.CharField(max_length=5)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bloodType = models.CharField(max_length=10)
    allergy = models.CharField(max_length=100)
    alzheimer = models.BooleanField()
    asthma = models.BooleanField()
    diabetes = models.BooleanField()
    stroke = models.BooleanField()
    medical_history= models.TextField(null=False)
    # ---------------Foreign Keys-------------------
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_id)
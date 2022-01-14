from django.db import models

# Create your models here.

class PatientProfile(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=15)
    patient_relative_name = models.CharField(max_length=50, null=True)
    patient_relative_contact = models.CharField(max_length=15, null=True)
    resd_address = models.TextField()
    prior_ailments = models.TextField()
    dob = models.DateField(null=True)
    email = models.EmailField(null = False)
    password = models.TextField(max_length=50)

           # critical/serious
    # ---------------Foreign Keys-------------------

    def __str__(self):
        return str(self.patient_name)

    class Meta:
        db_table = 'PatientProfile'

    def get_patient_by_email(email):
        try:
            return PatientProfile.objects.get(email=email)
        except:
            return False

#Medical Info about the patient to be stored in this table
class MedicalInfo(models.Model):
    height = models.CharField(max_length=5)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bloodType = models.CharField(max_length=10)
    allergy = models.CharField(max_length=100)
    alzheimer = models.BooleanField()
    asthma = models.BooleanField()
    diabetes = models.BooleanField()
    stroke = models.BooleanField()
    medical_history = models.TextField()
    # ---------------Foreign Keys-------------------
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_id)

    class Meta:
        db_table = 'MedicalInfo'

from django.db import models
from patient.models import PatientProfile

# Create your models here.

# Specialization Department of Doctor
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=500)

    def __str__(self):
        return self.department_name

# Doctor's Profile
class DoctorProfile(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    # ---------------Foreign Keys-------------------
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name
    
    def get_doctor_by_email(email):
        try:
            return DoctorProfile.objects.get(email=email)
        except:
            return False


# Info of all the medicines stored here.
class Medicines(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    side_effects = models.TextField(null=True)
    description = models.TextField(null=False)
    
    def __str__(self):
        return self.name

# First enter salt then medicine which comprised of that salt
class Preparation(models.Model):
    preparation_id = models.AutoField(primary_key=True)
    substance_name = models.CharField(max_length=100)
    form = models.CharField(max_length=100) # solid/liquid
    strength_unit = models.CharField(max_length=100) # 100mg, 200mg, etc
    medicine_id = models.ForeignKey(Medicines, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.substance_name) +" inside "+str(self.medicine_id.name)

# Table to store the prescription of the patient, refers to prescribed meds
class DoctorPrescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    date = models.DateField()
    nextVisit = models.DateField(null=False)
    reason = models.CharField(max_length=100)
    doctors_notes = models.TextField(null=False)
    # ---------------Foreign Keys-------------------
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_id.patient_name)+ " is assigned to Dr. " + str(self.doctor_id.doctor_name)

# Schedule of a particular medicine to be taken by a patient
class Medication_order(models.Model):
    medication_id = models.AutoField(primary_key=True)
    medication_unit = models.CharField(max_length=100)  # quantity - 1 tab, 2 tab, etc
    prescription_id = models.ForeignKey(DoctorPrescription, on_delete=models.CASCADE)
    medicine_code = models.ForeignKey(Medicines, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.medicine_code.name) + " prescribed by Dr. " + str(self.prescription_id.doctor_id.doctor_name)

# Upto which period the patient is allowed to take medication by the doctor(for particular prescription)
class Authorisation_details(models.Model):
    authorization_id = models.AutoField(primary_key=True)
    number_of_repeats_allowed = models.IntegerField()
    validity_period = models.DateField()
    medication_id = models.ForeignKey(Medication_order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.medication_id.medicine_code.name) + " is allowed " + str(self.number_of_repeats_allowed) + " times"
        # return "Authorization of " + str(self.prescription_id.patient_id.patient_name)+"'s Prescription"

# Time at which we need to take the particular medicine
class Medication_timing(models.Model):
    medication_timing_id = models.AutoField(primary_key=True)
    morning = models.BooleanField()
    afternoon = models.BooleanField()
    evening = models.BooleanField()
    night = models.BooleanField()
    medication_id = models.ForeignKey(Medication_order, on_delete=models.CASCADE)

    def __str__(self):
        return "Timing of " + str(self.medication_id.medicine_code.name)
    

# When the patient has to take the medicine again
class Repetation(models.Model):
    repetation_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    repetation_interval = models.CharField(max_length=100) # daily, weekly, fortnightly, monthly
    medication_id = models.ForeignKey(Medication_order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.medication_id.medicine_code.name) +" medicine is continued for  " + str(self.repetation_interval) + " days"


# Precautions while taking the medicine of a particular prescription
class Medication_safety(models.Model):
    medication_safety_id = models.AutoField(primary_key=True)
    max_dose_per_period = models.IntegerField()
    override_reason = models.CharField(max_length=500)
    medication_id = models.ForeignKey(Medication_order, on_delete=models.CASCADE)

    def __str__(self):
        return "Safety with " + str(self.medication_id.medicine_code.name)

# DOCTOR PATIENT - To match between Doctor ID and Patient ID
class doctor_patient(models.Model):
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_id.patient_name)+ " assigned to Dr. " + str(self.doctor_id.doctor_name)


'''

TIPS TO RESOLVE ERROR
python manage.py migrate --run-syncdb

'''

# class Medication_order(models.Model):
#     pass

# A patient can have can have multiple prescription,
# a prescription can have multiple medicines


# Details about the hospital
# class Hospital(models.Model):
#     hospital_id = models.AutoField(primary_key=True)
#     hospital_name = models.CharField(max_length=200)
#     hospital_type = models.CharField(max_length=200) # public, private, army, etc
#     bed_capacity = models.CharField(max_length=10)
#     helpline_num = models.CharField(max_length=15)
#     road = models.CharField(max_length=200)
#     building = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)

# class Bill(models.Model):
#     bill_id = models.AutoField(primary_key=True)
#     patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
#     doctor_charge = models.CharField(max_length=10)
#     medicine_charge = models.CharField(max_length=10)
#     room_charge = models.CharField(max_length=20, null=True)
#     nursing_charge = models.CharField(max_length=20, null=True)
#     insurance_num = models.CharField(max_length=20)
#     total_bill = models.CharField(max_length=20)


# # Table to store prescribed medicines to a patient
# class PrescribedMeds(models.Model):
#     # medication_id = models.ForeignKey()
#     dose = models.CharField(max_length=4)
#     # ---------------Foreign Keys-------------------
#     medicine_code = models.ForeignKey(Medicines, on_delete=models.CASCADE)
#     prescription_id = models.ForeignKey(DoctorPrescription, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return str(self.medicine_code.name)+' '+ self.dose + " by " + str(self.prescription_id.doctor_id



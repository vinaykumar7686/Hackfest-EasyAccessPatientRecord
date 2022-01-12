from django.db import models
from patient.models import PatientProfile

# Create your models here.

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

# Specialization Department of Doctor
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=500)
    # hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name

# Doctor's Profile
class DoctorProfile(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)
    # salary = models.CharField(max_length=10) # given by hospital
    # fees = models.CharField(max_length=20)  # given by patients
    # hospital = models.CharField(max_length=50)
    # ---------------Foreign Keys-------------------
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name

# Info of all the medicines stored here.
class Medicines(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    description = models.TextField(null=False)
    side_effects = models.TextField(null=True)
    form = models.CharField(max_length=100)  # Syrup/Tablet

    # strength = models.CharField(max_length=50)   #---->> a medicine is available in multiple strength 50mg, 100mg...
    # substance_name = models.CharField(max_length=100)
    # diluent_amount = models.IntegerField()
    # diluent_unit = models.IntegerField()

    def __str__(self):
        return self.name

class Medication_safety(models.Model):
    medication_id = models.AutoField(primary_key=True)
    max_dose_per_period = models.IntegerField()
    override_reason = models.CharField(max_length=500)

    def __str__(self):
        return str(self.medication_id)

class Authorisation_details(models.Model):
    authorization_id = models.AutoField(primary_key=True)
    number_of_repeats_allowed = models.IntegerField()
    validity_period = models.DateField()

    def __str__(self):
        return str(self.authorization_id)

# class Bill(models.Model):
#     bill_id = models.AutoField(primary_key=True)
#     patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
#     doctor_charge = models.CharField(max_length=10)
#     medicine_charge = models.CharField(max_length=10)
#     room_charge = models.CharField(max_length=20, null=True)
#     nursing_charge = models.CharField(max_length=20, null=True)
#     insurance_num = models.CharField(max_length=20)
#     total_bill = models.CharField(max_length=20)

# Table to store the prescription of the patient, refers to prescribed meds
class DoctorPrescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    date = models.DateField()
    nextVisit = models.DateField(null=False)
    reason = models.CharField(max_length=100)
    doctors_notes = models.TextField(null=False)
    dosage_instructions = models.CharField(max_length=1000)
    # ---------------Foreign Keys-------------------
    # bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    # medication_id = models.ForeignKey(PrescribedMeds, on_delete=models.CASCADE)
    medication_safety = models.ForeignKey(Medication_safety, on_delete=models.CASCADE)
    authorisation_details = models.ForeignKey(Authorisation_details, on_delete=models.CASCADE)
    # dispense_directions = models.ForeignKey(Dispense_directions, on_delete=models.CASCADE)
    # order_details = models.ForeignKey(Order_details, on_delete=models.CASCADE)
    # preparation = models.ForeignKey(Preparation, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_id.patient_name)+ " ==> " + str(self.doctor_id.doctor_name)

# Table to store prescribed medicines to a patient
class PrescribedMeds(models.Model):
    # medication_id = models.ForeignKey()
    dose = models.CharField(max_length=4)
    # ---------------Foreign Keys-------------------
    medicine_code = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    prescription_id = models.ForeignKey(DoctorPrescription, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.medicine_code.name)+' '+ self.dose + " by " + str(self.prescription_id.doctor_id.doctor_name)

# DOCTOR PATIENT
class doctor_patient(models.Model):
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_id.patient_name)+ " assigned to " + str(self.doctor_id.doctor_name)

'''
TIPS TO RESOLVE ERROR
python manage.py migrate --run-syncdb
'''

class Medication_order(models.Model):
    pass

class Preparation(models.Model):
    preparation_id = models.AutoField(primary_key=True)
    substance_name = models.CharField(max_length=100)
    form = models.CharField(max_length=100) # solid/liquid
    strength_unit = models.CharField(max_length=100) # 100mg, 200mg, etc

class Dose_Direction(models.Model):
    pass

class Repetation(models.Model):
    pass

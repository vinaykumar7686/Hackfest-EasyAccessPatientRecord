from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Department)
admin.site.register(DoctorProfile)
admin.site.register(Medicines)
admin.site.register(PrescribedMeds)
admin.site.register(Medication_safety)
admin.site.register(Authorisation_details)
admin.site.register(DoctorPrescription)
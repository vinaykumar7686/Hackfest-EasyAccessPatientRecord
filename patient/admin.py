from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PatientProfile)
admin.site.register(MedicalInfo)
admin.site.register(MyUser)
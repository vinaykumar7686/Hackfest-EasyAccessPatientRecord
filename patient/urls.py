from django.urls import path
from .views import *


urlpatterns = [
    # url for patient's homepage
    path('', pat_homepage, name='pat_homepage'),
    # url for patient's registration
    path('register/', pat_register),
    # url for patient's medical form fill up
    path('medicalForm/', pat_medicalForm),
    # url for patient's personal profile
    path('info/', pat_info),
    # url for updating patient's personal medical info
    path('update/medicalinfo/', update_medicalinfo),
    # url for patient's basic info
    path('update/info/', update_patient),
]


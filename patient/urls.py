from django.urls import path
from .views import *


urlpatterns = [
    path('', pat_homepage, name='pat_homepage'),
    path('register/', pat_register),
    path('medicalForm/', pat_medicalForm),
    path('info/', pat_info),
    # path('patientdetails/<int:id>', patient_profile_details, name='patient_profile_details'),
    # path('patientdetails/', patient_details, name='patient_details'),
    # path('patientdetails/<int:id>', PatientProfileDetailsAPIView.as_view(), name='PatientProfileDetailsAPIView'),
    # path('patientdetails/', PatientDetailsAPIView.as_view(), name='PatientDetails'),
    path('patientdetails/<int:patient_id>/', GenericAPIView.as_view(), name='GenericAPIView'),
    path('patientdetails/', GenericAPIView.as_view(), name='GenericAPIView'),
    
]


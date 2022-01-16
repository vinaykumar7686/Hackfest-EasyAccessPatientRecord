from pydoc import doc
from django.urls import path

from doctor.views import doc_homepage, login

from .views import *
from patient.views import pat_info

urlpatterns = [
    path('', homepage, name='homepage'),

    path('login/', common_login, name = 'login'),
    path('logout/', common_logout, name = 'logout'),

    path('doctor/', doc_homepage, name = 'doc_homepage'),
    path('doctor/register/', doc_register, name = 'doc_register'),  
    path('doctor/info', doc_info),
    path('doctor/patientinfo/<int:id>', pat_info),
    
    path('alldoctors/',view_all_doctors),
    path('allpatients/', view_all_patients),
    path('allmedicines/',view_all_meds,name='view_all_meds'),

    path('prescription/<int:id>', view_prescription, name='view_prescription'),
    path('prescription/add/', add_prescription),
    path('prescription/add/<int:id>', add_prescription),
    
    path('medicine/<int:id>',view_one_med, name='view_meds'),
    path('doctordetails/<int:doctor_id>/', GenericAPIView.as_view(), name='GenericAPIView'),
    path('doctordetails/', GenericAPIView.as_view(), name='GenericAPIView'),
]
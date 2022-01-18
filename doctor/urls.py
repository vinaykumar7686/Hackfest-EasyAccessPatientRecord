from pydoc import doc
from django.urls import path

from doctor.views import doc_homepage, login

from .views import *
from patient.views import pat_info

urlpatterns = [
    # urls for apps homepage
    path('', homepage, name='homepage'),
    
    # urls for login and logout
    path('login/', common_login, name = 'login'),
    path('logout/', common_logout, name = 'logout'),

    # url for doctor homepage
    path('doctor/', doc_homepage, name = 'doc_homepage'),
    # url for doctor registration
    path('doctor/register/', doc_register, name = 'doc_register'),
    # url for doctors profile
    path('doctor/info', doc_info),
    # url for patient info
    path('doctor/patientinfo/<int:id>', pat_info),
    
    # url for all doctors page    
    path('alldoctors/',view_all_doctors),
    # url for all patients page
    path('allpatients/', view_all_patients),
    # url for all medicines page
    path('allmedicines/',view_all_meds,name='view_all_meds'),

    # url for viewing prescriptions
    path('prescription/<int:id>', view_prescription, name='view_prescription'),
    # url for adding prescription in general(patient can be selected)
    path('prescription/add/', add_prescription),
    # url for adding prescription to a specific patient 
    path('prescription/add/<int:id>', add_prescription),
    
    # url for viewing the details of one specific medicine    
    path('medicine/<int:id>',view_one_med, name='view_meds'),

]

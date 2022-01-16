from django.urls import path
from .views import *


urlpatterns = [
    path('', pat_homepage, name='pat_homepage'),
    path('register/', pat_register),
    path('medicalForm/', pat_medicalForm),
    path('info/', pat_info),
    path('update/medicalinfo/', update_medicalinfo)
]


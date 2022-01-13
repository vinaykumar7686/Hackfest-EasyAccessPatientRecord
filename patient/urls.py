from django.urls import path
from .views import *


urlpatterns = [
    path('', pat_homepage, name='home'),
    path('register/', pat_register),
    path('medicalForm/', pat_medicalForm)
]


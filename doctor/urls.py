from django.urls import path

from doctor.views import doc_homepage, login

from .views import *

urlpatterns = [
    path('doctor/', doc_homepage),
    path('doctor/register/', doc_register),

    path('login/', login),
    
]
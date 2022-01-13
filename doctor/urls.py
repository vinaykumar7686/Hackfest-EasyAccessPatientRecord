from django.urls import path

from doctor.views import doc_homepage, login

from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login, name = 'login'),
    path('doctor/', doc_homepage, name = 'doc_homepage'),
    path('doctor/register/', doc_register, name = 'doc_register'),

    
]
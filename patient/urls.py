from django.urls import path
from .views import *

urlpatterns = [
    path('', pat_homepage),
    path('register/', pat_register),
    
]
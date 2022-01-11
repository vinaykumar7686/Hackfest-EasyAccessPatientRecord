from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from . import views

urlpatterns = [
    
    path('',views.homePage,name = 'home'),
    path('login/',views.loginPage,name = 'login'),
    path('register/',views.registerPage,name = 'register'),
    
]

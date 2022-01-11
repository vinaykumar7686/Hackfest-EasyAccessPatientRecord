from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def loginPage(request):
    return render(request,'login.html')

def registerPage(request):
    return render(request,'register.html')

def homePage(request):
    return render(request,'home.html')

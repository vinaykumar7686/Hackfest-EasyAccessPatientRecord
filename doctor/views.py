from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request=request, template_name='login.html')

# Website Hompage
def homepage(request):
    return render(request=request, template_name='homepage.html')
    
def doc_homepage(request):
    return render(request=request, template_name='doc_home.html')

def doc_register(request):
    return render(request=request, template_name='doc_register.html')

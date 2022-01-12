from django.shortcuts import render

# Create your views here.
def pat_homepage(request):
    return render(request=request, template_name='pat_home.html')

def pat_register(request):
    return render(request=request, template_name='pat_register.html')
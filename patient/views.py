from .forms import RegForm, MedicalInfoForm
from django.shortcuts import render,redirect
from patient.models import *

# Create your views here.
def pat_homepage(request):
    return render(request=request, template_name='pat_home.html')

def pat_register(request):
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pat_homepage')
    context = {'form': form}
    return render(request, 'pat_register.html', context)


def pat_medicalForm(request):
    form = MedicalInfoForm()
    if request.method == 'POST':
        form = MedicalInfoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('pat_homepage')
    context = {'form': form}
    return render(request, 'pat_medicalForm.html', context)


def pat_info(request, id):
    patient_info = PatientProfile.objects.filter(patient_id = id)[0]
    pat_med_info = MedicalInfo.objects.filter(patient_id = id)[0]

    return render(request, 'pat_info.html', {'patient_info': patient_info, 'pat_med_info': pat_med_info})

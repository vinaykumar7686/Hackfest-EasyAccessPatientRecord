from .forms import RegForm, MedicalInfoForm
from django.shortcuts import render,redirect
from patient.models import *
from doctor.models import *

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
    prescriptions_info = DoctorPrescription.objects.filter(patient_id = id)
    print(prescriptions_info)
    data = {'prescriptions': [], 'medications' : {}}
    i = 1
    for prescription_info in prescriptions_info:

        data['prescriptions'].append(prescription_info)

        medications = Medication_order.objects.filter(prescription_id = prescription_info)
        # print(medications)

        # data1 = {'medicines':[]}
        # for medication in medications:
        #     # medicines = Medicines.objects.filter(code = )
        #     # print(medication.medicine_code)

        #     data1['medicines'].append(medication)
        
        data['medications'][f'prescription{i}'] = medications

        i+=1
    print(data)

    

    return render(request, 'pat_info.html', {'patient_info': patient_info, 'pat_med_info': pat_med_info, 'data': data})

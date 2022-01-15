from http.client import HTTPResponse
from .forms import RegForm, MedicalInfoForm
from django.shortcuts import render,redirect
from patient.models import *
from doctor.models import *
from django.contrib.auth.decorators import login_required, user_passes_test

def patient_check(user):
    return not user.is_doctor

# Create your views here.
@login_required(login_url='/login/')
@user_passes_test(patient_check, login_url='/login/')
def pat_homepage(request):
    return render(request=request, template_name='pat_home.html')


def pat_register(request):
    if request.method == 'POST':
        patient_name = request.POST.get('name')
        relative_name = request.POST.get('relative_name')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        relative_phone = request.POST.get('relative_phone')
        patient_dob = request.POST.get('pat_dob')
        patient_email = request.POST.get('patient_email')
        patient_address = request.POST.get('patient_address')
        patient_prior_ailments = request.POST.get('patient_prior_ailments')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            return redirect('/patient/register')

        patient = PatientProfile(patient_name=patient_name, relative_name=relative_name, gender=gender, phone=phone, 
        relative_phone=relative_phone,patient_dob=patient_dob, patient_email=patient_email, patient_address=patient_address, patient_prior_ailments=patient_prior_ailments)
        patient.save()
        return HTTPResponse('Patient registered successfully')
        # add message here and redirect it to login page route
    else:
        patient = PatientProfile.objects.all()
        print(patient)
        return render(request, 'pat_register.html', {'patient': patient})

@login_required(login_url='/login/')
@user_passes_test(patient_check, login_url='/login/')
def pat_medicalForm(request):
    form = MedicalInfoForm()
    if request.method == 'POST':
        form = MedicalInfoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('pat_homepage')
    context = {'form': form}
    return render(request, 'pat_medicalForm.html', context)

@login_required(login_url='/login/')
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

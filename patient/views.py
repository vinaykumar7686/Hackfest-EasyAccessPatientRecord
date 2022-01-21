from http.client import HTTPResponse
from .forms import RegForm, MedicalInfoForm
from django.shortcuts import render,redirect
from patient.models import *
from doctor.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def patient_check(user):
    '''
    Function to check if a user is patient or not.
    '''
    return not user.is_doctor

def get_userprofile_by_request(request):
    '''
    This function th=akes in the request, and returns the profile of the user signed in.
    '''
    if request.user.is_authenticated:
        try:
            email = request.user.email
            if request.user.is_doctor:
                docs = DoctorProfile.objects.filter(email = email)
                if docs is not None:
                    return docs[0]
                else:
                    None
            else:
                pats = PatientProfile.objects.filter(email = email)
                if pats is not None:
                    return pats[0]
                else:
                    None
        except:
            return None
    else:
        return None

# Create your views here.
@login_required(login_url='/login/')
@user_passes_test(patient_check, login_url='/login/')
def pat_homepage(request):
    '''
    View for patients homepage.
    '''
    userprofile = get_userprofile_by_request(request)
    return render(request, 'pat_home.html', {'username': userprofile.patient_name, 'usertype': 'patient'})


def pat_register(request):
    '''
    View to register patients homepage.
    '''
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
            
        if MyUser.objects.filter(email = patient_email):
            # User with same email already exists
            messages.error(request, "Email Already in use, Try a different one!")
            print('User with same email already exists')
            return redirect('/doctor/register')

        patient = PatientProfile(patient_name=patient_name, patient_relative_name=relative_name, gender=gender, phone_num=phone, 
        patient_relative_contact=relative_phone,dob=patient_dob, email=patient_email, resd_address=patient_address, prior_ailments=patient_prior_ailments)
        patient.save()
        # print('patientinfo saved')

        MyUser.objects.create_user( email = patient_email, is_doctor = False, password = password1)
        # print('patient account created')

        user = authenticate(request, email=patient_email, password=password1)
        login(request, user)
        # print('patient logged in')

        messages.success(request, "Registered Successfully!")
        return redirect('/patient/medicalForm')
    else:
        patient = PatientProfile.objects.all()
        print(patient)
        return render(request, 'pat_register.html', {'patient': patient})

@login_required(login_url='/login/')
@user_passes_test(patient_check, login_url='/login/')
def pat_medicalForm(request):
    '''
    View to render and save patient's medical info
    '''
    useremail = request.user.email
    patient = get_userprofile_by_request(request)
    print(useremail, patient.patient_id, patient.patient_name)

    if request.method == 'POST':
        form_data =request.POST 
        height = form_data.get('height')
        weight = form_data.get('weight')
        bloodType = form_data.get('bloodType')
        allergy = form_data.get('allergy')
        alzheimer = True if form_data.get('alzheimer') == 'on' else False
        asthma = True if form_data.get('asthma') == 'on' else False
        diabetes = True if form_data.get('diabetes') == 'on' else False
        stroke = True if form_data.get('stroke') == 'on' else False
        medical_history = form_data.get('medicalHistory')
        patientInfo = MedicalInfo(height=height, weight=weight, bloodType=bloodType, allergy=allergy, alzheimer=alzheimer,
        asthma=asthma, diabetes=diabetes, stroke=stroke, medical_history=medical_history, patient_id=patient)
        patientInfo.save()
        messages.info(request, "Welcome to Hompage")
        return redirect('/patient')
        # add message here and redirect it to patient info page route
    else:
        
        # patientInfo = MedicalInfo.objects.all()
        return render(request, 'pat_medicalForm.html', {'patient_id': patient.patient_id, 'patient_name': patient.patient_name, 'disable': True})

@login_required(login_url='/login/')
def pat_info(request, *args, **kwargs):
    '''
    View to render patient's personal, medical and prescriptions info.
    '''
    usertype = None
    username = None
    # To check whether to fetch patient id from urls or session
    if kwargs.get('id'):
        if request.user.is_doctor:
            patient = PatientProfile.objects.filter(patient_id = kwargs.get('id'))[0]
            usertype = 'doctor'
            userprofile = get_userprofile_by_request(request)
            username = userprofile.doctor_name
        else:
            # Not a doctor, trying to access patient info
            usertype = 'patient'
            userprofile = get_userprofile_by_request(request)
            username = userprofile.patient_name
            return redirect('/login')
    else:
        patient = get_userprofile_by_request(request)
        username = patient.patient_name
        usertype = 'patient'
    
    try:
        patient_info = PatientProfile.objects.filter(patient_id = patient.patient_id)[0]
    except:
        patient_info = []
    
    try:
        pat_med_info = MedicalInfo.objects.filter(patient_id = patient.patient_id)[0]
    except:
        pat_med_info = []
    

    prescriptions_info = DoctorPrescription.objects.filter(patient_id = patient.patient_id)
    # print(prescriptions_info)
    data = {'prescriptions': [], 'medications' : {}}
    i = 1
    for prescription_info in prescriptions_info:
        data['prescriptions'].append(prescription_info)
        medications = Medication_order.objects.filter(prescription_id = prescription_info)
        data['medications'][f'prescription{i}'] = medications
        i+=1
    print(data)
    return render(request, 'pat_info.html', {'patient_info': patient_info, 'pat_med_info': pat_med_info, 'data': data, 'username': username, 'usertype': usertype})


@login_required
@user_passes_test(patient_check, login_url='/login/')
def update_patient(request):
    '''
    View to update patient's basic info.
    '''
    userprofile = get_userprofile_by_request(request)

    if request.method == 'POST':
        formdata = request.POST
        patient_name = formdata.get('name')
        relative_name = formdata.get('relative_name')
        gender = formdata.get('gender')
        phone = formdata.get('phone')
        relative_phone = formdata.get('relative_phone')
        patient_dob = formdata.get('pat_dob')
        patient_address = formdata.get('patient_address')
        patient_prior_ailments = formdata.get('patient_prior_ailments')

        PatientProfile.objects.filter(email=userprofile.email).update(
            patient_name=patient_name, 
            patient_relative_name=relative_name, 
            gender=gender, 
            phone_num=phone, 
            patient_relative_contact=relative_phone,
            dob=patient_dob, 
            resd_address=patient_address, 
            prior_ailments=patient_prior_ailments)

        return redirect('/patient')
    else:
        patientinfo = PatientProfile.objects.filter(email = request.user.email)[0]
        return render(request, 'pat_update_info.html', {'patientinfo': patientinfo, 'username': userprofile.patient_name, 'usertype': 'patient'})



@login_required
@user_passes_test(patient_check, login_url='/login/')
def update_medicalinfo(request):
    '''
    View to update patient's medical info
    '''
    userprofile = get_userprofile_by_request(request)
    
    if request.method == 'POST':
        form_data =request.POST 
        height = form_data.get('height')
        weight = form_data.get('weight')
        bloodType = form_data.get('bloodType')
        allergy = form_data.get('allergy')
        alzheimer = True if form_data.get('alzheimer') == 'on' else False
        asthma = True if form_data.get('asthma') == 'on' else False
        diabetes = True if form_data.get('diabetes') == 'on' else False
        stroke = True if form_data.get('stroke') == 'on' else False
        medical_history = form_data.get('medicalHistory')

        MedicalInfo.objects.filter(patient_id = userprofile.patient_id).update(
            height=height, 
            weight=weight, 
            bloodType=bloodType, 
            allergy=allergy, 
            alzheimer=alzheimer,
            asthma=asthma, 
            diabetes=diabetes, 
            stroke=stroke, 
            medical_history=medical_history)
        
        messages.success(request, "Details updated successfully")
        return redirect('/patient')

    else:
        medicalinfo = MedicalInfo.objects.filter(patient_id = userprofile.patient_id)[0]
        return render(request, 'pat_update_medicalInfo.html', {'patient_id': userprofile.patient_id, 'patient_name': userprofile.patient_name,'medicalinfo':medicalinfo, 'username': userprofile.patient_name, 'usertype': 'patient'})

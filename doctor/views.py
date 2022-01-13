from django.shortcuts import redirect, render
from .models import DoctorProfile
from django.http import HttpResponse
from .models import Department
from patient.models import PatientProfile
from. models import *

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        doctor = DoctorProfile.get_doctor_by_email(email)

        error_message = None 

        if doctor and (password== doctor.password):
            request.session['doctor_id'] = doctor.doctor_id
            return redirect('homepage')

        else:
            patient = PatientProfile.get_patient_by_email(email)

            if patient and (password == patient.password):
                request.session['patient_id'] = patient.patient_id
                return redirect('pat_homepage')
            else:
                error_message = 'Invalid Email or Password!!'

        return render(request, 'login.html', {'error_message': error_message})

# Website Hompage
def homepage(request):
    return render(request=request, template_name='homepage.html')
    
def doc_homepage(request):
    return render(request=request, template_name='doc_home.html')

def doc_register(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('name')
        email = request.POST.get('email')
        phone_num = request.POST.get('phone')
        department = request.POST.get('department')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1!=password2:
            return redirect('/doctor/register')
        

        department_inst = Department.objects.filter(department_id = department)[0]

        doctor = DoctorProfile(doctor_name=doctor_name, email=email, phone_num=phone_num, department=department_inst, password = password1)

        doctor.save()
        return HttpResponse('doctor is registered')
        
    else:
        departments = Department.objects.all()
        print(departments)
        return render(request, 'doc_register.html', {'departments' : departments})

def add_prescription(request):

    if request.method == 'GET':

        # Adding prescription
        patient = PatientProfile.objects.filter(patient_id = 1)[0]
        doctor = DoctorProfile.objects.filter(doctor_id = 1)[0]

        new_prescription = DoctorPrescription(
            date = '1999-05-11',
            nextVisit = '1999-05-11',
            reason = "blah blah",
            doctors_notes = "mai pagal",
            patient_id = patient,
            doctor_id = doctor)
        new_prescription.save()

        #-----> Issues: multiple medication order and all below

        # +++++++++Adding Medication Order
        medicine = Medicines.objects.filter(code = 1)[0]

        medication_order = Medication_order(
        medication_unit = 10,
        prescription_id  = new_prescription,
        medicine_code = medicine
        )
        medication_order.save()

        # ++++++++++ Adding Authorisation_details
        authorization_details = Authorisation_details(
            number_of_repeats_allowed = 3,
            validity_period ='1999-05-12',
            medication_id = medication_order
        )
        authorization_details.save()

        # ++++++++++ Adding Medication_timing
        medication_timing = Medication_timing(
            morning = False,
            afternoon = True,
            evening = True,
            night = True,
            medication_id = medication_order
        )
        medication_timing.save()

        # +++++++++++ Adding Repetations
        repetation = Repetation(
            start_date = '1999-05-12',
            end_date = '1999-05-12',
            repetation_interval = '12',
            medication_id = medication_order
        )
        repetation.save()

        # +++++++++++ Adding Medication_safety
        medication_safety = Medication_safety(
            max_dose_per_period = 5,
            override_reason = 'Nothing',
            medication_id = medication_order
        )
        medication_safety.save()

        print(('Data Posted Successfully!'))
        return HttpResponse('Data Posted Successfully!') 

    else:
        return HttpResponse('This is a get Request!')

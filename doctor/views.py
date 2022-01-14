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

    if request.method == 'POST':
        
        form_data =  request.POST
        print(form_data)
        # Adding prescription
        patient = PatientProfile.objects.filter(patient_id = form_data.get('patient'))[0]
        doctor = DoctorProfile.objects.filter(doctor_id = form_data.get('doctor'))[0]

        new_prescription = DoctorPrescription(
            date = form_data.get('date'),
            nextVisit = form_data.get('nextVisit'),
            reason = form_data.get('reason'),
            doctors_notes = form_data.get('doc_notes'),
            patient_id = patient,
            doctor_id = doctor)
        new_prescription.save()

        #-----> Issues: multiple medication order and all below

        # +++++++++Adding Medication Order
        # medicines = Medicines.objects.all()[:2] #filter(code = 1)[0:2]
        no_of_medicines = int(form_data.get('medcounter'))
        for i in range(1,no_of_medicines+1):
            print(i,form_data.get(f'medicine{i}'))
            medicine = Medicines.objects.filter(name = form_data.get(f'medicine{i}'))[0]

            medication_order = Medication_order(
            medication_unit = 10,
            prescription_id  = new_prescription,
            medicine_code = medicine
            )
            medication_order.save()

            # ++++++++++ Adding Authorisation_details
            authorization_details = Authorisation_details(
                number_of_repeats_allowed = form_data.get(f'repeats_allowed{i}'),
                validity_period = form_data.get(f'validity_period{i}'),
                medication_id = medication_order
            )
            authorization_details.save()

            # ++++++++++ Adding Medication_timing
            medication_timing = Medication_timing(
                morning = True if form_data.get(f'morning{i}') == 'on' else False,
                afternoon = True if form_data.get(f'afternoon{i}') == 'on' else False,
                evening = True if form_data.get(f'evening{i}') == 'on' else False,
                night = True if form_data.get(f'night{i}') == 'on' else False,
                medication_id = medication_order
            )
            medication_timing.save()

            # +++++++++++ Adding Repetations
            repetation = Repetation(
                start_date = form_data.get(f'start_date{i}'),
                end_date = form_data.get(f'end_date{i}'),
                repetation_interval = form_data.get(f'repetation_interval{i}'),
                medication_id = medication_order
            )
            repetation.save()

            # +++++++++++ Adding Medication_safety
            medication_safety = Medication_safety(
                max_dose_per_period = form_data.get(f'max_dose_per_period{i}'),
                override_reason = form_data.get(f'override_reason{i}'),
                medication_id = medication_order
            )
            medication_safety.save()

            print((f'{medicine.name} added Successfully!'))

        print(('Data Posted Successfully!'))
        return redirect('/doctor/')

    else:
        doctors = DoctorProfile.objects.all()
        patients = PatientProfile.objects.all()
        medicines = Medicines.objects.all()
        return render(request, 'doc_add_prescription.html', {'doctors': doctors, 'patients': patients, 'medicines': medicines})


def view_prescription(request):
    prescription = DoctorPrescription.objects.all()[0]#filter(prescription_id = 4)[0]
    # print(prescription)
    # print(prescription.prescription_id)
    # print('------------')
    medication_orders = Medication_order.objects.filter(prescription_id=prescription.prescription_id)
    # print(prescription)

    prescription_data = {
        'prescription_details': prescription,
        'medication_data':[]
        }
    
    for med_order in medication_orders:
        authorization = Authorisation_details.objects.filter(medication_id=med_order.medication_id)[0]
        med_timing = Medication_timing.objects.filter(medication_id=med_order.medication_id)[0]
        repetation = Repetation.objects.filter(medication_id=med_order.medication_id)[0]
        med_safety = Medication_safety.objects.filter(medication_id=med_order.medication_id)[0]
        medicine_details = Medicines.objects.filter(name = med_order.medicine_code)[0]
        medication_data = {
            'medication_order': med_order,
            'authorization': authorization,
            'med_timing': med_timing,
            'repetation': repetation,
            'med_safety': med_safety,
            'medicine_details': medicine_details
            }
        prescription_data['medication_data'].append(medication_data)

    print(prescription_data)
    return render(request,'doc_prescription.html', prescription_data)

    
def doc_info(request):
    # dept = Department.objects.all()[0]
    # doctors = DoctorProfile.objects.filter(department = dept.department_id)
    # doctor_detail = {
    #     'dept':dept,
    #     'doctors':[]
    # }
    # print(doctors)
    # print('-----------------------')
    # for doc in doctors:
    #     docProfile = DoctorProfile.objects.filter(department=doc.department_id)[0]
    #     doctors={
    #         'docProfile':docProfile
    #     }       
    #     doctor_detail['doctors'].append(doctors)
    # return render(request, 'doc_info.html',{'doctors':doctors})
    # return HttpResponse("Done")
    doctors = DoctorProfile.objects.all()
    return render(request, 'doc_info.html', {'doctors':doctors})

def view_all_meds(request):
    meds = Medicines.objects.all()
    return render(request, 'view_all_meds.html', {'medicines':meds})

def view_one_med(request, id):
    meds = Medicines.objects.filter(code=id)[0]
    preparation = Preparation.objects.filter(medicine_id=id)[0]
    context={'meds':meds, 'prep':preparation}
    return render(request, 'view_one_med.html',context)



#========> Form Response
# {'csrfmiddlewaretoken': ['9UGllsw3J0T8pw2UUXrRMFOci3VHsYtoBA2fbn0wZIVcYql6jlNWcZtS0iUGC2fi'
#     ], 'date': ['2022-01-29'
#     ], 'nextVisit': ['2022-01-20'
#     ], 'reason': ['Reason'
#     ], 'doc_notes': [' Doctor Notes'
#     ], 'patient': ['1'
#     ], 'doctor': ['1'
#     ], 'medicine1': ['Paracetamol'
#     ], 'morning1': ['on'
#     ], 'afternoon1': ['on'
#     ], 'evening1': ['on'
#     ], 'night1': ['on'
#     ], 'start_date1': ['2022-01-27'
#     ], 'end_date1': ['2022-01-29'
#     ], 'repetation_interval1': [' Repitition Interval'
#     ], 'repeats_allowed1': ['8'
#     ], 'validity_period1': ['2022-01-28'
#     ], 'max_dose_per_period1': ['5'
#     ], 'override_reason1': ['Override Reason'
#     ], 'submit': ['Submit'
#     ]
# }

'''
    # This is the JSON response that the front end will recieve
    
    {
    'prescription_details': <DoctorPrescription: Dinesh Sharma is assigned to Dr. Vinay Kumar>,
    'medication_data': 
    [
        {
            'medication_order': <Medication_order: Paracetamol prescribed by Dr. Vinay Kumar>, 
            'authorization': <Authorisation_details: Paracetamol is allowed 3 times>, 
            'med_timing': <Medication_timing: Timing of Paracetamol>, 
            'repetation': <Repetation: Paracetamol medicine is continued for  12 days>, 
            'med_safety': <Medication_safety: Safety with Paracetamol>, 
            'medicine_details': <Medicines: Paracetamol>
        },
        {
            'medication_order': <Medication_order: aspirin prescribed by Dr. Vinay Kumar>, 
            'authorization': <Authorisation_details: aspirin is allowed 3 times>, 
            'med_timing': <Medication_timing: Timing of aspirin>, 
            'repetation': <Repetation: aspirin medicine is continued for  12 days>, 
            'med_safety': <Medication_safety: Safety with aspirin>, 
            'medicine_details': <Medicines: aspirin>
        }
    ]
}
    '''
from http.client import HTTPResponse
from .forms import RegForm, MedicalInfoForm
from django.shortcuts import render,redirect, get_object_or_404
from patient.models import *
from doctor.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .serializers import PatientSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

def patient_check(user):
    return not user.is_doctor

def get_userprofile_by_email(request):
    if request.user.is_authenticated:
        try:
            email = request.user.email
            if request.user.is_doctor:
                return DoctorProfile.objects.filter(email = email)[0]
            else:
                return PatientProfile.objects.filter(email = email)[0]
        except:
            return None
    else:
        return None

# Create your views here.
@login_required(login_url='/login/')
@user_passes_test(patient_check, login_url='/login/')
def pat_homepage(request):
    userprofile = get_userprofile_by_email(request)
    return render(request, 'pat_home.html', {'username': userprofile.patient_name, 'usertype': 'patient'})


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
            
        if MyUser.objects.filter(email = patient_email):
            # User with same email already exists
            print('User with same email already exists')
            return redirect('/doctor/register')

        patient = PatientProfile(patient_name=patient_name, patient_relative_name=relative_name, gender=gender, phone_num=phone, 
        patient_relative_contact=relative_phone,dob=patient_dob, email=patient_email, resd_address=patient_address, prior_ailments=patient_prior_ailments)
        patient.save()
        print('patientinfo saved')

        MyUser.objects.create_user( email = patient_email, is_doctor = False, password = password1)
        print('patient account created')
        # Logging into newly created account
        user = authenticate(request, email=patient_email, password=password1)
        login(request, user)
        print('patient logged in')

        return redirect('/patient/medicalForm')
        # add message here and redirect it to login page route
    else:
        patient = PatientProfile.objects.all()
        print(patient)
        return render(request, 'pat_register.html', {'patient': patient})

@login_required(login_url='/login/')
@user_passes_test(patient_check, login_url='/login/')
def pat_medicalForm(request):
    useremail = request.user.email
    patient = get_userprofile_by_email(request)
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

        return redirect('/patient')
        # add message here and redirect it to patient info page route
    else:
        
        # patientInfo = MedicalInfo.objects.all()
        return render(request, 'pat_medicalForm.html', {'patient_id': patient.patient_id, 'patient_name': patient.patient_name, 'disable': True})

@login_required(login_url='/login/')
def pat_info(request, *args, **kwargs):
    usertype = None
    # To check whether to fetch patient id from urls or session
    if kwargs.get('id'):
        if request.user.is_doctor:
            patient = PatientProfile.objects.filter(patient_id = kwargs.get('id'))[0]
            usertype = 'doctor'
            userprofile = get_userprofile_by_email(request)
            username = userprofile.doctor_name
        else:
            # Not a doctor, trying to access patient info
            return redirect('/login')
            usertype = 'patient'
            userprofile = get_userprofile_by_email(request)
            username = userprofile.patient_name
    else:
        patient = get_userprofile_by_email(request)
    
    patient_info = PatientProfile.objects.filter(patient_id = patient.patient_id)[0]
    pat_med_info = MedicalInfo.objects.filter(patient_id = patient.patient_id)[0]
    prescriptions_info = DoctorPrescription.objects.filter(patient_id = patient.patient_id)
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
    return render(request, 'pat_info.html', {'patient_info': patient_info, 'pat_med_info': pat_med_info, 'data': data, 'username': username, 'usertype': usertype})

# ---------------------------------------API---------------------------------------------- #
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, 
mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = PatientSerializer
    queryset = PatientProfile.objects.all()
    lookup_field = 'patient_id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, patient_id=None):
        if patient_id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)

    def put(self, request, patient_id=None):
        return self.update(request, patient_id)

    def delete(self, request, patient_id=None):
        return self.destroy(request, patient_id)

# class PatientDetailsAPIView(APIView):
#     def get(self, request):
#         patient = PatientProfile.objects.all()
#         serializer = PatientSerializer(patient, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PatientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PatientViewSet(viewsets.ViewSet):
#     def list(self, request):
#         patient = PatientProfile.objects.all()
#         serializer = PatientSerializer(patient, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = PatientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     def retrieve(self, request, patient_id=None):
#         queryset = PatientProfile.objects.all()
#         patient = get_object_or_404(queryset, patient_id=patient_id)
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)


# class PatientProfileDetailsAPIView(APIView):
#     def get_object(self, id):
#         try:
#             return PatientProfile.objects.get(patient_id=id)
#         except PatientSerializer.DoesNotExist:
#             return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         patient = self.get_object(id)
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)

#     def put(self, request, id):
#         patient = self.get_object(id)
#         serializer = PatientSerializer(patient, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         patient = self.get_object(id)
#         patient.delete()
#         return HTTPResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST',])
# def patient_details(request):
#     if request.method == 'GET':
#         patient = PatientProfile.objects.all()
#         serializer = PatientSerializer(patient, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PatientSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def patient_profile_details(request,id):
#     try:
#         patient = PatientProfile.objects.get(patient_id=id)
#     except PatientSerializer.DoesNotExist:
#         return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PatientSerializer(patient, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         patient.delete()
#         return HTTPResponse(status=status.HTTP_204_NO_CONTENT)
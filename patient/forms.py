from django import forms
from django.forms import ModelForm
from .models import PatientProfile, MedicalInfo


class RegForm(ModelForm):
    class Meta:
        model = PatientProfile
        fields = '__all__'


class MedicalInfoForm(ModelForm):
    class Meta:
        model = MedicalInfo
        fields = '__all__'

from .models import *
from django.db import models
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = PatientProfile
        fields="__all__"
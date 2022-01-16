from .models import *
from django.db import models
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = DoctorProfile
        fields="__all__"
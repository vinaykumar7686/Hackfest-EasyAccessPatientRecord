from email.policy import default
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from datetime import datetime
from django.utils.timezone import now

from doctor.models import *
# Create your models here.

class PatientProfile(models.Model):
    patient_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    patient_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=15)
    patient_relative_name = models.CharField(max_length=50, null=True)
    patient_relative_contact = models.CharField(max_length=15, null=True)
    resd_address = models.TextField()
    prior_ailments = models.TextField()
    dob = models.DateField(null=True)
    created_date = models.DateField(default=now)

           # critical/serious
    # ---------------Foreign Keys-------------------

    def __str__(self):
        return str(self.patient_name)

    # def get_id_by_email(email):
    #     try:
    #         return PatientProfile.objects.get(email=email)[0]['doctor_id']
    #     except:
    #         return False

    class Meta:
        db_table = 'PatientProfile'

    def get_patient_by_email(email):
        try:
            return PatientProfile.objects.get(email=email)
        except:
            return False

#Medical Info about the patient to be stored in this table
class MedicalInfo(models.Model):
    height = models.CharField(max_length=5)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bloodType = models.CharField(max_length=10)
    allergy = models.CharField(max_length=100)
    alzheimer = models.BooleanField()
    asthma = models.BooleanField()
    diabetes = models.BooleanField()
    stroke = models.BooleanField()
    medical_history = models.TextField()
    # ---------------Foreign Keys-------------------
    patient_id = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_id)

    class Meta:
        db_table = 'MedicalInfo'


class MyUserManager(BaseUserManager):
    def create_user(self, email, is_doctor, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            is_doctor=is_doctor,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, is_doctor, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        u = self.create_user(email,
                        is_doctor = is_doctor,
                        password=password
                    )
        u.is_admin = True
        u.save(using=self._db)
        return u

class MyUser(AbstractBaseUser):
    email = models.EmailField(
                        verbose_name='email address',
                        max_length=255,
                        unique=True,
                    )

    is_doctor = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_doctor']

    def get_email(self):
        # The user is identified by their email address
        return self.email
    
    def is_adoctor(self):
        return self.is_doctor

    # def get_userid(self):
    #     # print(self.get_email())
    #     if self.is_adoctor():
    #         docData = DoctorProfile.objects.filter(email = self.get_email())[0]
    #         return docData# ['doctor_id']
    #     else:
    #         patData = PatientProfile.objects.filter(email = self.get_email())[0]
    #         return patData# ['patient_id']

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    



# user = MyUser.objects.create_user( email = 'abscdef@gmail.com', is_doctor = True, password = 'wowowowow')

# useremail = request.user.email
#         patient = get_userprofile_by_email(useremail)
#         print(useremail, patient)


# def get_userprofile_by_email(email):
#     return PatientProfile.objects.filter(email = email)[0]
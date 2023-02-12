import uuid
from django.db import models
from datetime import date, datetime
from phone_field import PhoneField
from .utils import create_new_ref_number

# Create your models here.

# choice list
YES = 'Yes'
NO = 'No'
YES_NO_CHOICES = [
    (YES, 'Yes'),
    (NO, 'No'),
]


class PatientInformation(models.Model):
    registration_no = models.CharField(max_length=200, null=True, blank=True)
    recorddate = models.DateField(auto_now_add=False, blank=True, null=True, editable=True)
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True, default='')
    age = models.CharField(max_length=200, null=True, blank=True, default='')
    MALE = 'Male'
    FEMALE = 'Female'
    TRANSGENDER = 'Transgender'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (TRANSGENDER, 'Transgender')
    ]
    gender = models.CharField(max_length=100, null=True, blank=True, choices=GENDER_CHOICES, default='')
    address = models.TextField(default='', null=True, blank=True)
    phone = models.CharField(max_length=200, default='', null=True, blank=True)
    email = models.EmailField(max_length=1000, null=True, blank=True, default='')
    guardian_name = models.CharField(max_length=200, default='', null=True, blank=True)
    refferance = models.CharField(max_length=200, default='', null=True, blank=True)
    drug_allergy = models.CharField(max_length=200, choices=YES_NO_CHOICES, default='', null=True, blank=True)
    name_drug_allergy = models.CharField(max_length=2000, blank=True, null=True, default='')
    rheumatic_fever = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    valvular_diseases = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    asthma_tb = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    hypertension = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    heart_desease = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    heart_valve_pace_maker = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    peptic_ulcer = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    jaundice_liver_disease = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    diabetes = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    kidney_disease = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    epilepsy = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    bleeding_disorder = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    hepa_b_c_hiv = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    take_any_vaccine = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    vaccine_type = models.CharField(max_length=400, blank=True, null=True, default='')
    drug_history_name_if_any = models.CharField(max_length=200, blank=True, null=True, default='')
    last_dental_check_up_date = models.DateField(auto_now_add=False, blank=True, null=True, editable=True)
    last_treatment_type = models.CharField(max_length=200, blank=True, null=True, default='')
    habits_addiction_name = models.CharField(max_length=200, blank=True, null=True, default='')
    experience_tooth_extraction_anaesthesia = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    pregnancy = models.CharField(max_length=200, choices=YES_NO_CHOICES, blank=True, null=True, default='')
    month_pregnant = models.CharField(max_length=200, blank=True, null=True, default='')
    lmp_date = models.DateField(auto_now_add=False, blank=True, null=True, editable=True)
    other_information = models.TextField(blank=True, null=True, default='')
    treatment_date = models.DateField(auto_now_add=False, blank=True, null=True, editable=True)
    procedure = models.TextField(default='', null=True, blank=True)
    next_date = models.DateField(auto_now_add=False, blank=True, null=True, editable=True)

    class Meta:
        db_table = 'patientinformation'

    def __str__(self):
        return f'{self.registration_no} - {self.patient_name}'

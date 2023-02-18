from django import forms
from .models import *
from phone_field import phone_number

YES = 'Yes'
NO = 'No'
YES_NO_CHOICES = [
    (YES, 'Yes'),
    (NO, 'No')
]
MALE = 'Male'
FEMALE = 'Female'
RATHERNOTTOSAY = 'Rather not to say'
GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (RATHERNOTTOSAY, 'Rather not to say')
]


class PatientRecord(forms.ModelForm):
    registration_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    recorddate = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-autoclose': 'true'}))

    patient_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    age = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))

    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 30}))

    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    guardian_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    refferance = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    drug_allergy = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    name_drug_allergy = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    rheumatic_fever = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    valvular_diseases = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    asthma_tb = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    hypertension = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    heart_desease = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    heart_valve_pace_maker = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    peptic_ulcer = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    jaundice_liver_disease = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    diabetes = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    kidney_disease = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    epilepsy = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    bleeding_disorder = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    hepa_b_c_hiv = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    take_any_vaccine = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    vaccine_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    drug_history_name_if_any = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_dental_check_up_date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-autoclose': 'true'}))

    last_treatment_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    habits_addiction_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    experience_tooth_extraction_anaesthesia = forms.CharField(widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    pregnancy = forms.CharField(required=False, widget=forms.RadioSelect(choices=YES_NO_CHOICES))

    month_pregnant = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    lmp_date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-autoclose': 'true'}))

    other_information = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    treatment_date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-autoclose': 'true'}))

    procedure = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    next_date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-autoclose': 'true'}))

    class Meta:
        model = PatientInformation
        fields = '__all__'

    def refresh_from_db(self):
        pass



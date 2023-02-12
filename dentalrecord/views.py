from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def patientinfoadd(request):
    if request.POST:
        infoform = PatientRecord(request.POST)
        if infoform.is_valid():
            infoform_view = infoform
            infoform_view.refresh_from_db()
            infoform_view.registration_no = infoform.cleaned_data.get('registration_no')
            infoform_view.recorddate = infoform.cleaned_data.get('recorddate')
            infoform_view.patient_name = infoform.cleaned_data.get('patient_name')
            infoform_view.occupation = infoform.cleaned_data.get('occupation')
            infoform_view.age = infoform.cleaned_data.get('age')
            infoform_view.gender = infoform.cleaned_data.get('gender')
            infoform_view.address = infoform.cleaned_data.get('address')
            infoform_view.phone = infoform.cleaned_data.get('phone')
            infoform_view.email = infoform.cleaned_data.get('email')
            infoform_view.guardian_name = infoform.cleaned_data.get('guardian_name')
            infoform_view.refferance = infoform.cleaned_data.get('refferance')
            infoform_view.drug_allergy = infoform.cleaned_data.get('drug_allergy')
            infoform_view.name_drug_allergy = infoform.cleaned_data.get('name_drug_allergy')
            infoform_view.rheumatic_fever = infoform.cleaned_data.get('rheumatic_fever')
            infoform_view.valvular_diseases = infoform.cleaned_data.get('valvular_diseases')
            infoform_view.asthma_tb = infoform.cleaned_data.get('asthma_tb')
            infoform_view.hypertension = infoform.cleaned_data.get('hypertension')
            infoform_view.heart_desease = infoform.cleaned_data.get('heart_desease')
            infoform_view.heart_valve_pace_maker = infoform.cleaned_data.get('heart_valve_pace_maker')
            infoform_view.peptic_ulcer = infoform.cleaned_data.get('peptic_ulcer')
            infoform_view.jaundice_liver_disease = infoform.cleaned_data.get('jaundice_liver_disease')
            infoform_view.diabetes = infoform.cleaned_data.get('diabetes')
            infoform_view.kidney_disease = infoform.cleaned_data.get('kidney_disease')
            infoform_view.epilepsy = infoform.cleaned_data.get('epilepsy')
            infoform_view.bleeding_disorder = infoform.cleaned_data.get('bleeding_disorder')
            infoform_view.hepa_b_c_hiv = infoform.cleaned_data.get('hepa_b_c_hiv')
            infoform_view.take_any_vaccine = infoform.cleaned_data.get('take_any_vaccine')
            infoform_view.vaccine_type = infoform.cleaned_data.get('vaccine_type')
            infoform_view.drug_history_name_if_any = infoform.cleaned_data.get('drug_history_name_if_any')
            infoform_view.last_dental_check_up_date = infoform.cleaned_data.get('last_dental_check_up_date')
            infoform_view.last_treatment_type = infoform.cleaned_data.get('last_treatment_type')
            infoform_view.habits_addiction_name = infoform.cleaned_data.get('habits_addiction_name')
            infoform_view.experience_tooth_extraction_anaesthesia = infoform.cleaned_data.get(
                'experience_tooth_extraction_anaesthesia')
            infoform_view.pregnancy = infoform.cleaned_data.get('pregnancy')
            infoform_view.month_pregnant = infoform.cleaned_data.get('month_pregnant')
            infoform_view.lmp_date = infoform.cleaned_data.get('lmp_date')
            infoform_view.other_information = infoform.cleaned_data.get('other_information')
            infoform_view.treatment_date = infoform.cleaned_data.get('treatment_date')
            infoform_view.procedure = infoform.cleaned_data.get('procedure')
            infoform_view.next_date = infoform.cleaned_data.get('next_date')

            infoform_view.save()
            return redirect('dentalrecord:patientinformation')

    context = {"infoform": PatientRecord}
    return render(request, 'pages/patientinfoadd.html', context)


def patientinfoview(request):
    patientlist = PatientInformation.objects.all().order_by('-id')
    context = {
        'patientlist': patientlist
    }
    return render(request, 'pages/viewpatientinfo.html', context)


def infodetails(request, pk):
    patientdetails = get_object_or_404(PatientInformation, pk=pk)
    context = {
        'detailsinformation': patientdetails,
    }
    return render(request, 'pages/infodetails.html', context)

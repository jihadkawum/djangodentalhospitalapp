from django.shortcuts import render, redirect, get_object_or_404
from .models import PatientInformation
from .forms import PatientRecord
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.

def index(request):
    list_of_patient = PatientInformation.objects.values('patient_name')
    total_patient = PatientInformation.objects.count()
    context = {
        'list_of_patient': list_of_patient,
        'total_patient': total_patient
    }
    return render(request, 'pages/index.html', context)


def patientinfoadd(request):
    if request.method == 'POST':
        infoform = PatientRecord(request.POST)
        if infoform.is_valid():
            try:
                infoform.save()
                return redirect('dentalrecord:patientinformation')
            except:
                pass
    else:
        infoform = PatientRecord()
    context = {
        'infoform': infoform
    }
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
        'detailsinformation': patientdetails
    }
    return render(request, 'pages/infodetails.html', context)


def infoedit(request, pk):
    patientlist = get_object_or_404(PatientInformation, pk=pk)
    context = {
        'patientlist': patientlist
    }
    return render(request, 'pages/infoedit.html', context)


def infoupdate(request, pk):
    patientlist = PatientInformation.objects.get(pk=pk)
    infoform = PatientRecord(request.POST, instance=patientlist)
    context = {
        'infoform': infoform
    }
    if infoform.is_valid():
        infoform.save()
        return redirect('dentalrecord:details', pk=pk)

    return render(request, 'pages/infoedit.html', context)


def destroy(request, pk):
    patient = PatientInformation.objects.get(pk=pk)
    patient.delete()
    return redirect('dentalrecord:patientinformation')


class SearchResultsView(ListView):
    template_name = 'pages/searchresults.html'
    model = PatientInformation

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('q')
        if keyword:
            queryset = queryset.filter(
                Q(registration_no__icontains=keyword) | Q(patient_name__icontains=keyword)
            )
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        keyword = self.request.GET.get('q')
        if keyword and not context['object_list']:
            context['no_result'] = True
        return context

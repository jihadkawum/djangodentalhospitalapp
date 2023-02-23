from django.contrib import admin

# Register your models here.

from .models import *


# Register your models here.

class PatientListAdmin(admin.ModelAdmin):
    list_display = ("registration_no", "patient_name",)


admin.site.register(PatientInformation, PatientListAdmin)

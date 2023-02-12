from django.urls import path
from . import views
app_name = 'dentalrecord'
urlpatterns = [
    path('', views.index, name='home'),
    path('patientinfoadd/', views.patientinfoadd, name='patientinfoadd'),
    path('patientinformation/', views.patientinfoview, name='patientinformation'),
    path('<int:pk>', views.infodetails, name='details')
]
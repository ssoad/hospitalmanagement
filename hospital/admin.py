from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails, Hospital, Post
# Register your models here.
admin.site.register([Hospital,Doctor,Patient,Appointment,PatientDischargeDetails, Post])

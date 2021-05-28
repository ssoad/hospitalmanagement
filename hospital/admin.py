from django.contrib import admin
from .models import Doctor,Patient,DoctorAppointment,PatientDischargeDetails, Hospital, Post, HospitalPatient, HospitalReview, DoctorReview
# Register your models here.
admin.site.register([Hospital,Doctor,Patient,DoctorAppointment,PatientDischargeDetails, Post, HospitalPatient, HospitalReview, DoctorReview])

from django.db import models
from django.contrib.auth.models import User
hospital_patient_status = [('Admitted', 'Admitted'), ('Discharged', 'Discharged')]
doctor_patient_status = [('Enrolled', 'Enrolled'), ('Discharged', 'Discharged')]

class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=40)
    profile_pic = models.ImageField(upload_to='profile_pic/HospitalProfilePic/', null=True, blank=True)
    location = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{} ({})".format(self.hospital_name, self.location)


departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    approved = models.BooleanField(null=False, blank=False , default=True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class DoctorAppointment(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,null=True,on_delete=models.CASCADE)
    appointmentDate = models.DateField(auto_now=True)
    symtoms = models.CharField(max_length=50, null=False, blank=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)


class PatientDischargeDetails(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40)
    assignedDoctorName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)

    admitDate = models.DateField(null=True)
    releaseDate = models.DateField(null=True)
    daySpent = models.PositiveIntegerField(null=True)

    roomCharge = models.PositiveIntegerField(null=True)
    medicineCost = models.PositiveIntegerField(null=True)
    doctorFee = models.PositiveIntegerField(null=False)
    OtherCharge = models.PositiveIntegerField(null=True)
    total = models.PositiveIntegerField(null=False)


class Post(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE),
    text = models.CharField(max_length=1000, null=False, blank=False)


ratings = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class HospitalReview(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, default=1)
    hospital = models.ForeignKey(Hospital, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=ratings, null=False, blank=False)
    comment = models.CharField(max_length=1000)


hospital_patient_status = [('Admitted', 'Admitted'), ('Discharged', 'Discharged')]

class DoctorReview(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, default=1)
    doctor = models.ForeignKey(Doctor, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=ratings,null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True, blank= True)




class HospitalPatient(models.Model):
    patient = models.ForeignKey(Patient,null=False, blank=False,on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, null=False, blank=False,on_delete=models.CASCADE)
    symptoms = models.CharField(max_length=1000,default="")
    status = models.CharField(choices=hospital_patient_status, null=False, blank=False,max_length=100)
    is_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.hospital.hospital_name, self.patient.get_name)

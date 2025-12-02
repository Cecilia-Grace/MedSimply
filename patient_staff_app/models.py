from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    patient_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    id_number = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    patient_emergency_contact = models.CharField(max_length=15, null=True, blank=True) 
    
    def __str__(self):
        return self.patient_name
    
    class Meta:
        verbose_name = 'Patient Profile'
        
        
class HealthWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    job_title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.get_full_name()}: {self.job_title}"
        
    class Meta:
        verbose_name = 'Health Worker Profile'
        permissions = [
            ('can_view_patient_assignments', 'Can view the patients he/she is assigned to'),
        ]
        
        
class PatientAssignment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='health_worker_assigned_to')
    health_worker = models.ForeignKey('HealthWorker', on_delete=models.CASCADE, related_name='patient_assigned_to')
    start_time_date= models.DateTimeField(auto_now_add=True)
    end_time_date= models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.health_worker.user.get_full_name()} is assigned to {self.patient.patient_name}"
    
#Login history for accountability
class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    successful_login = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user} logged in at {self.login_time}"
    
    class Meta:
        verbose_name = "Login History"
        
    
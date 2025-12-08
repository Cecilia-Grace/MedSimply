from django.contrib import admin
from .models import Patient, HealthWorker, LoginHistory, PatientAssignment

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'phone_number', 'id_number', 'date_of_birth', 'gender', 'created_at', 'patient_emergency_contact')
    search_fields = ('patient_name', 'phone_number', 'date_of_birth', 'gender', 'created_at', 'patient_emergency_contact')

@admin.register(HealthWorker)
class HealthWorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'job_title')
    search_fields = ('user__full_name', 'phone_number', 'job_title')

@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'login_time', 'ip_address', 'successful_login')
    search_fields = ('user__username', 'login_time', 'ip_address', 'successful_login')
    list_filter = ('login_time',)
    
@admin.register(PatientAssignment)
class PatientAssignmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'health_worker', 'start_time_date', 'end_time_date')
    search_fields = ('patient', 'health_worker')

from django.contrib import admin
from .models import MedicationSchedule, NotificationDashboard

# Register your models here.
@admin.register(MedicationSchedule)
class MedicationScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'medication_given', 'patient_given_to', 'scheduled_time')
    search_fields = ('id', 'medication_given', 'patient_given_to', 'scheduled_time')
    

@admin.register(NotificationDashboard)
class NotificationDashboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'health_worker', 'phone_number', 'is_remainder_sent', 'remainder_response', 'remainder_message', 'is_given')
    search_fields = ('id', 'patient_name', 'health_worker', 'phone_number', 'is_remainder_sent', 'remainder_response', 'remainder_message', 'is_given')
    
    
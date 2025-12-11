from django.contrib import admin
from .models import MedicationSchedule, NotificationDashboard

# Register your models here.
@admin.register(MedicationSchedule)
class MedicationScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'medication_given', 'patient_given_to', 'scheduled_time')
    search_fields = ('id', 'medication_given', 'patient_given_to', 'scheduled_time')
    

@admin.register(NotificationDashboard)
class NotificationDashboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'schedule', 'health_worker', 'is_reminder_sent', 'reminder_response', 'reminder_message', 'is_given')
    search_fields = ('id', 'schedule', 'health_worker', 'is_reminder_sent', 'reminder_response', 'reminder_message', 'is_given')
    
    
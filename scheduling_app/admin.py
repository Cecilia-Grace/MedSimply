from django.contrib import admin
from .models import MedicationSchedule

# Register your models here.
@admin.register(MedicationSchedule)
class MedicationScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'medication_given', 'patient_given_to', 'scheduled_time')
    search_fields = ('id', 'medication_given', 'patient_given_to', 'scheduled_time')
from django.contrib import admin
from .models import Medication, PatientMedication

# Register your models here.
@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'medication_name', 'medication_form', 'expiry_date', 'dosage_unit')
    search_fields = ('medication_name', 'medication_form', 'expiry_date', 'dosage_unit')
    
@admin.register(PatientMedication)
class PatientMedication(admin.ModelAdmin):
    list_display = ('id', 'medication_name', 'patient_name', 'dosage_unit', 'quantity_per_dose', 'days_to_take_medicine', 'remaining_days', 'start_date', 'end_date')
    search_fields = ('medication_name', 'patient_name', 'dosage_unit', 'quantity_per_dose', 'days_to_take_medicine', 'remaining_days', 'start_date', 'end_date')
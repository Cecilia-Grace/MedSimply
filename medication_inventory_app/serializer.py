from rest_framework import serializers
from .models import Medication, PatientMedication

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'medication_name', 'medication_form', 'expiry_date', 'dosage_unit']
        
        
class PatientMedicationSerializer(serializers.ModelSerializer):
    medication_name_display = serializers.CharField(source='medication_name.medication_name', read_only=True)
    patient_name_display = serializers.CharField(source='patient_name.patient_name', read_only=True)
    
    class Meta:
        model = PatientMedication
        fields = ['id', 'medication_name', 'medication_name_display', 'patient_name', 'patient_name_display', 'dosage_unit', 'quantity_per_dose', 'days_to_take_medicine', 'remaining_days', 'start_date', 'end_date', 'health_worker']
        read_only_fields = ['medication_name', 'patient_name', 'days_to_take_medicine', 'remaining_days', 'start_date', 'health_worker']
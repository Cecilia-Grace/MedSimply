from rest_framework import serializers
from .models import MedicationSchedule
from django.contrib.auth.models import User

class MedicationScheduleSerializer(serializers.ModelSerializer):
    medication_given_display = serializers.CharField(source='medication_given.medication_name', read_only=True)
    patient_given_to_display = serializers.CharField(source='patient_given_to.patient_name', read_only=True)
    
    class Meta:
        model = MedicationSchedule
        fields = ('id', 'medication_given', 'medication_given_display', 'patient_given_to', 'patient_given_to_display', 'scheduled_time', 'is_given', 'given_by', 'time_given')
        read_only_fields = ('medication_given', 'patient_given_to', 'scheduled_time', 'is_given', 'given_by', 'time_given')
        
    
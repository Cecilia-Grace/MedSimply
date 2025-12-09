from rest_framework import serializers
from .models import MedicationSchedule, NotificationDashboard
from django.contrib.auth.models import User

class MedicationScheduleSerializer(serializers.ModelSerializer):
    medication_given_display = serializers.CharField(source='medication_given.medication_name', read_only=True)
    patient_given_to_display = serializers.CharField(source='patient_given_to.patient_name', read_only=True)
    
    class Meta:
        model = MedicationSchedule
        fields = ('id', 'medication_given', 'medication_given_display', 'patient_given_to', 'patient_given_to_display', 'scheduled_time')
        read_only_fields = ('medication_given', 'patient_given_to', 'scheduled_time')
        
class NotificationDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationDashboard
        fields = ('id', 'patient_name', 'health_worker', 'phone_number', 'is_remainder_sent', 'remainder_response', 'remainder_message', 'is_given')
        read_only_fields = ('id', 'patient_name', 'health_worker', 'phone_number', 'is_remainder_sent', 'remainder_response', 'remainder_message', 'is_given')
   

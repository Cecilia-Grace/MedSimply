from rest_framework import serializers
from .models import MedicationSchedule

class MedicationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSchedule
        fields = ('id', 'medication_given', 'patient_given_to', 'scheduled_time', 'is_given', 'given_by', 'time_given')
        read_only_fields = ('medication_given', 'patient_given_to', 'scheduled_time', 'is_given', 'given_by', 'time_given')
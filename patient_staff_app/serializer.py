from rest_framework import serializers
from .models import Patient, HealthWorker, PatientAssignment, LoginHistory

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'patient_name', 'phone_number', 'id_number', 'date_of_birth', 'gender', 'created_at', 'patient_emergency_contact']
        read_only_fields = ['id_number']
        
        
class HealthWorkerSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = HealthWorker
        fields =  ['id', 'full_name', 'email', 'job_title', 'phone_number']
        
        
class PatientAssignmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    health_worker = HealthWorkerSerializer(read_only=True)
    
    class Meta:
        model = PatientAssignment
        fields = ['patient', 'health_worker', 'start_time_date', 'end_time_date']
        read_only_fields = ['start_time_date']
        
        
class LoginHistorySerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    
    class Meta:
        model = LoginHistory
        fields = ['id', 'full_name', 'login_time', 'ip_address', 'successful_login']
        read_only_fields = fields
from django.shortcuts import render
from .models import PatientAssignment, Patient, HealthWorker, LoginHistory
from .serializer import PatientAssignmentSerializer, PatientSerializer, HealthWorkerSerializer, LoginHistorySerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsHealthWorker

# Create your views here.
class HealthWorkerViewSet(viewsets.ModelViewSet):
    queryset = HealthWorker.objects.all()
    serializer_class = HealthWorkerSerializer
    
    permission_classes = [IsAdminUser]
    
    
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    permission_classes = [IsHealthWorker]
    
    def get_queryset(self):
        user = self.request.user
        
        #checks if is admin/superuser
        if user.is_superuser or user.groups.filter(name='Admins').exists():
            return Patient.objects.all()
        #checks if user is health worker
        if user.groups.filter(name='HealthWorkers').exists():
            try:
                health_worker_profile = user.healthworker
                assigned_patients = Patient.objects.filter(health_worker_assigned_to__health_worker=health_worker_profile).distinct()
                return assigned_patients
            except HealthWorker.DoesNotExist:
                print("The named Health Worker does not exist")
                return Patient.objects.none()  
        else:
            Patient.objects.none()
            
            
class PatientAssignmentViewSet(viewsets.ModelViewSet):
    queryset = PatientAssignment.objects.all()
    serializer_class = PatientAssignmentSerializer
    
    def get_permissions(self):
        #Admin permitted actions
        if self.action == ['create', 'retrieve', 'update', 'destroy', 'partial update']:
            permission_classes = [IsAdminUser]
        #heath worker permitted actions
        elif self.action == ['retrieve', 'list']:
            permission_classes = [IsHealthWorker]
        else:
            permission_classes = [IsAuthenticated]
            
        return [permission() for permission in permission_classes]
    
    
class LoginHistoryViewSet(viewsets.ModelViewSet):
    queryset = LoginHistory.objects.all()
    serializer_class = LoginHistorySerializer
    
    permission_classes = [IsAdminUser]
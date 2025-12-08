from django.shortcuts import render
from .models import PatientAssignment, Patient, HealthWorker, LoginHistory
from .serializer import PatientAssignmentSerializer, PatientSerializer, HealthWorkerSerializer, LoginHistorySerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsHealthWorker, CanViewPatients

# Create your views here.
class HealthWorkerViewSet(viewsets.ModelViewSet):
    queryset = HealthWorker.objects.all()
    serializer_class = HealthWorkerSerializer
    
    permission_classes = [IsAdminUser]
    
    
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    permission_classes = [CanViewPatients]
    
            
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
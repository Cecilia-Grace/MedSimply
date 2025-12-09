from django.shortcuts import render
from .models import Medication, PatientMedication
from rest_framework import viewsets
from .serializer import MedicationSerializer, PatientMedicationSerializer 
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    
    permission_classes = [IsAdminUser]
    
    
class PatientMedicationViewSet(viewsets.ModelViewSet):
    queryset = PatientMedication.objects.all()
    serializer_class = PatientMedicationSerializer
    
    permission_classes = [IsAdminUser]
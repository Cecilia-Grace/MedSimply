from django.shortcuts import render
from .models import MedicationSchedule
from .serializer import MedicationScheduleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.utils import timezone

# Create your views here.
class MedicationScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicationSchedule.objects.all()
    serializer_class = MedicationScheduleSerializer
    
    permission_classes = [IsAdminUser]
    
    def perform_update(self, serializer):
        if 'is_given' in serializer.validated_data and serializer.validated_data['is_given']:
            assignment = serializer.instance.patient_name.health_worker_assigned_to.filter(end_time_date__isnull=True).first()
        
            serializer.save(time_given=timezone.now(), given_by=assignment)
        else:
            serializer.save()
     

            

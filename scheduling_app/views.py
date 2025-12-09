from django.shortcuts import render
from .models import MedicationSchedule
from .serializer import MedicationScheduleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.utils import timezone
from rest_framework.exceptions import PermissionDenied


# Create your views here.
class MedicationScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicationSchedule.objects.all()
    serializer_class = MedicationScheduleSerializer
    
    permission_classes = [IsAdminUser]
    
    def perform_update(self, serializer):
        """
        Automatically set time_given and given_by when marking as given,
        and ensure only the assigned health worker can do it.
        """
        instance = serializer.instance
        if serializer.validated_data.get('is_given'):
            assignment = instance.patient_given_to.health_worker_assigned_to.filter(
                end_time_date__isnull=True,
                health_worker__user=self.request.user  # logged-in user must match
            ).first()

            if assignment:
                serializer.save(
                    time_given=timezone.now(),
                    given_by=assignment
                )
            else:
                # Deny if the logged-in user is not the assigned health worker
                raise PermissionDenied("You are not assigned to this patient or dose.")
        else:
            serializer.save()  # Normal update if is_given is False
     

            

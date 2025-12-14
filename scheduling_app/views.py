from django.shortcuts import render
from .models import MedicationSchedule, NotificationDashboard
from .serializer import MedicationScheduleSerializer, NotificationDashboardSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.utils import timezone



# Create your views here.
class MedicationScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicationSchedule.objects.all()
    serializer_class = MedicationScheduleSerializer
    
    permission_classes = [IsAdminUser]
    
class NotificationDashboardViewSet(viewsets.ModelViewSet):
    queryset = NotificationDashboard.objects.all()
    serializer_class = NotificationDashboardSerializer
    
    permission_classes = [IsAdminUser]
    
    



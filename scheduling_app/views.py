from django.shortcuts import render
from .models import MedicationSchedule, NotificationDashboard
from .serializer import MedicationScheduleSerializer, NotificationDashboardSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



# Create your views here.
class MedicationScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicationSchedule.objects.all()
    serializer_class = MedicationScheduleSerializer
    
    permission_classes = [IsAdminUser]
    
class NotificationDashboardViewSet(viewsets.ModelViewSet):
    queryset = NotificationDashboard.objects.all()
    serializer_class = NotificationDashboardSerializer
    
    permission_classes = [IsAdminUser]
    
    
@csrf_exempt
def receive_sms(request):
    if request.method == "POST":
        sender = request.POST.get("from")
        text = request.POST.get("text", "").strip()

        if text.upper() == "TAKEN":
            notification = NotificationDashboard.objects.filter(
                health_worker__phone_number=sender,
                is_given=False
            ).order_by('-schedule__scheduled_time').first()

            if notification:
                notification.is_given = True
                notification.reminder_response = f"{text} at {timezone.now()}"
                notification.save()
                return JsonResponse({"status": "success", "message": "Marked as taken"})

    return JsonResponse({"status": "failed", "message": "Invalid request"})


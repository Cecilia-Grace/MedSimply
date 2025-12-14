from rest_framework.routers import DefaultRouter
from .views import MedicationScheduleViewSet, NotificationDashboardViewSet, receive_sms
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'medication_schedule', MedicationScheduleViewSet, basename='medication_schedules')
router.register(r'notification_dashboard', NotificationDashboardViewSet, basename='notifications_dashboard')

urlpatterns = router.urls



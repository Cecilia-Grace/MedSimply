from rest_framework.routers import DefaultRouter
from .views import MedicationScheduleViewSet, NotificationDashboardViewSet

router = DefaultRouter()
router.register(r'medication_schedule', MedicationScheduleViewSet, basename='medication_schedules')
router.register(r'notification_dashboard', NotificationDashboardViewSet, basename='notifications_dashboard')

urlpatterns = router.urls

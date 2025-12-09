from rest_framework.routers import DefaultRouter
from .views import MedicationScheduleViewSet

router = DefaultRouter()
router.register(r'medication_schedule', MedicationScheduleViewSet, basename='medication_schedules')

urlpatterns = router.urls

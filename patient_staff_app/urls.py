from .views import PatientAssignmentViewSet, PatientViewSet, HealthWorkerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'health-workers', HealthWorkerViewSet, basename='health-worker')
router.register(r'patient-assignments', PatientAssignmentViewSet, basename='patient-assignments')
router.register(r'login-history', HealthWorkerViewSet, basename='login-history')

urlpatterns = router.urls



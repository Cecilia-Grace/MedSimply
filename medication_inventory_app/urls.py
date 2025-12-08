from rest_framework.routers import DefaultRouter
from .views import MedicationViewSet, PatientMedicationViewSet

router = DefaultRouter()
router.register(r'medication', MedicationViewSet, basename='medications')
router.register(r'patient_medication', PatientMedicationViewSet, basename='patient-medication')

urlpatterns = router.urls

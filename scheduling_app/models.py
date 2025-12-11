from django.db import models
from django.utils import timezone
from medication_inventory_app.models import PatientMedication
from .models import PatientMedication

# Create your models here.
class MedicationSchedule(models.Model):
    medication_given = models.ForeignKey('medication_inventory_app.PatientMedication', on_delete=models.CASCADE, related_name='medication_schedule')
    patient_given_to = models.ForeignKey('patient_staff_app.Patient', on_delete=models.CASCADE, related_name='patient_medication_schedule')
    scheduled_time = models.DateTimeField(help_text="The specific date and time the dose is due.")
    
    def __str__(self):
        return f"""
                Patient Name: {self.patient_given_to}
                Medication: {self.medication_given} 
                Scheduled at: {self.scheduled_time}
                """
        
    class Meta:
        verbose_name = "Medication Schedule"
        
class NotificationDashboard(models.Model):
    patient_name = models.ForeignKey(MedicationSchedule, on_delete=models.CASCADE, related_name='patient_to_take_medication')
    health_worker = models.ForeignKey('patient_staff_app.PatientAssignment', on_delete=models.CASCADE, related_name='health_worker_to_giv_medication')
    phone_number = models.ForeignKey('patient_staff_app.HealthWorker', on_delete=models.CASCADE, related_name='health_worker_phone_number')
    is_remainder_sent = models.BooleanField(default=False)
    remainder_response = models.TextField()
    remainder_message = models.TextField(
        default=f"""
                Hello, kindly administer to: 
                    Patient Name: {patient_name},
                    Medication: {MedicationSchedule.medication_given},
                    Scheduled at: {MedicationSchedule.scheduled_time},
                    Quantity per dose: {PatientMedication.quantity_per_dose}
                """
            )
    is_given = models.BooleanField(default=False)
        
        

        
    
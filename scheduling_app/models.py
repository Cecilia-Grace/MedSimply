from django.db import models
from django.utils import timezone
from medication_inventory_app.models import PatientMedication
from patient_staff_app.models import Patient
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    schedule = models.ForeignKey(MedicationSchedule, on_delete=models.CASCADE, related_name='notifications')
    health_worker = models.ForeignKey('patient_staff_app.HealthWorker', on_delete=models.SET_NULL,  related_name='scheduled_notifications', null=True,  blank=True, help_text="The caregiver assigned to receive this reminder.")
    
    is_reminder_sent = models.BooleanField(default=False)
    reminder_response = models.TextField(blank=True, null=True)
   
    reminder_message = models.TextField(
        default=(
            "Hello, kindly administer to:\n"
            "Patient: {patient_name}\n"
            "Medication: {medication}\n"
            "Scheduled at: {scheduled_time}\n"
            "Dose: {dose_quantity} {dosage_unit}"
        )
    )
    def build_reminder_message(self):
        schedule = self.schedule # Access the related MedicationSchedule instance
        patient = schedule.patient_given_to
        patient_medication = schedule.medication_given # Access the PatientMedication instance

        return self.reminder_message.format(
            patient_name=schedule.patient_given_to.patient_name, 
            medication=patient_medication.medication_name,
            scheduled_time=schedule.scheduled_time.strftime("%Y-%m-%d %H:%M"),
            dose_quantity=patient_medication.quantity_per_dose,
            dosage_unit=patient_medication.dosage_unit
        )

    is_given = models.BooleanField(default=False)
        
        
    
        

        
    
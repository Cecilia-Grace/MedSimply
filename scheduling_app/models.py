from django.db import models
from django.utils import timezone

# Create your models here.
class MedicationSchedule(models.Model):
    medication_given = models.ForeignKey('medication_inventory_app.PatientMedication', on_delete=models.CASCADE, related_name='medication_schedule')
    patient_given_to = models.ForeignKey('patient_staff_app.Patient', on_delete=models.CASCADE, related_name='patient_medication_schedule')
    scheduled_time = models.DateTimeField(help_text="The specific date and time the dose is due.")
    is_given = models.BooleanField(default=False)
    given_by = models.ForeignKey('patient_staff_app.PatientAssignment', on_delete=models.CASCADE, null=True, blank=True, related_name='health_worker_administering_medication')
    time_given = models.DateTimeField(null=True, blank=True)
    
    def mark_as_given(self, assignment):  #acts as a button that sets all to true if given
        self.is_given = True
        self.given_by = assignment
        self.time_given = timezone.now()
        self.save()
    
    def __str__(self):
        return f"{self.patient_given_to} was administered {self.medication_given} by {self.given_by}"
        
    class Meta:
        verbose_name = "Medication Schedule"
        
    
from django.db import models
from django.utils import timezone

# Create your models here.
class Medication(models.Model):
    medication_name = models.CharField(max_length=255)
    medication_form = models.CharField(max_length=255)  #syrup, tablet
    expiry_date = models.DateField()
    dosage_unit = models.CharField(max_length=255)   #ml, mg
    
    def __str__(self):
        return self.medication_name
    
    class Meta:
        verbose_name = 'Medications'
    
    
class PatientMedication(models.Model):
    medication_name = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='medication_for_patient')
    patient_name = models.ForeignKey('patient_staff_app.Patient', on_delete=models.CASCADE, related_name='patient_medication')
    dosage_unit = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity_per_dose = models.PositiveIntegerField()
    days_to_take_medicine = models.PositiveIntegerField()
    remaining_days = models.PositiveIntegerField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.medication_name} for {self.patient_name}"
    
    
    def remaining_days(self):
        if self.end_date:
            remaining = self.end_date - timezone.now().date()
            return max(remaining.days, 0)
        return None
    
    class Meta:
        verbose_name = 'Patient Medication'
        
    
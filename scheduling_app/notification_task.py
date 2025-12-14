from django.utils import timezone
from scheduling_app.utils import send_sms
from .models import NotificationDashboard
from patient_staff_app.models import HealthWorker

def send_due_medication_reminders():
    now = timezone.now()

    reminders = NotificationDashboard.objects.select_related(
        'schedule',
        'health_worker',
        'schedule__patient_given_to',
        'schedule__medication_given'
    ).filter(
        is_reminder_sent=False,
        schedule__scheduled_time__lte=now,
        health_worker__isnull=False
    )

    for reminder in reminders:
        health_worker = reminder.health_worker
        phone = health_worker.phone_number

        message = reminder.build_reminder_message()

        response = send_sms(phone, message)

        reminder.is_reminder_sent = True
        reminder.reminder_response = str(response)
        reminder.save()

from celery import shared_task
from django.utils import timezone
from .models import NotificationDashboard
from scheduling_app.utils import send_sms  

@shared_task
def send_due_medication_reminders():
    now = timezone.now()
    print("⏰ Celery task running at:", now)

    reminders = NotificationDashboard.objects.filter(
        is_reminder_sent=False,
        schedule__scheduled_time__lte=now,
        health_worker__isnull=False
    )

    print("🔎 Reminders found:", reminders.count())

    for reminder in reminders:
        phone = str(reminder.health_worker.phone_number)
        message = reminder.build_reminder_message()

        print("📞 Sending to:", phone)
        print("✉️ Message:", message)

        response = send_sms(phone, message)

        print("📡 Africa’s Talking response:", response)

        reminder.is_reminder_sent = True
        reminder.reminder_response = str(response)
        reminder.save()

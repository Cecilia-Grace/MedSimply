import africastalking
import os

AT_USERNAME = os.getenv("AT_USERNAME")
AT_API_KEY = os.getenv("AT_API_KEY")

# Initialize Africa's Talking SDK (once)
africastalking.initialize(AT_USERNAME, AT_API_KEY)
sms = africastalking.SMS

def send_sms(to, message):
    try:
        response = sms.send(
            message=message,
            recipients=[to],
            sender_id='MedSimply Reminder'
        )
        return response
    except Exception as e:
        return f"SMS ERROR: {e}"
